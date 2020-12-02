import random
import pandas as pd
import os
from datetime import datetime, timezone
from eduaccess.settings import BASE_DIR

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import EduUser
from .models import Student, Subject, Question, Feedback, Test, College, Stream, Application
from .serializers import StudentSerializer, SubjectSerializer, QuestionSerializer
from .serializers import TestSerializer, CollegeSerializer, StreamSerializer, ApplicationSerializer
from accounts.serializers import EduUserSerializer
# from .forms import StuForm  

class HomePageView(TemplateView):
	template_name = 'home.html'


class SeekCollegeView(TemplateView):
	template_name = 'seekcollege.html'

	# GET method
	def get(self, request):
		queryset = Stream.objects.all()
		streams = []
		for query in queryset:
			serializer = StreamSerializer(query)
			stream = serializer.data
			streams.append(stream['stream_name'])
		streams = set(streams)
		# print(streams)
		data = {
			'streams' : streams,
		}
		if request.method =="POST":
			return streams
		return render(request, template_name="seekcollege.html", context=data)

	# POST method
	def post(self,request):
		user = request.user
		student = Student.objects.get(user=user)
		stream = request.POST.get('stream')
		degree = request.POST.get('degree')
		cut_off = request.POST.get('cut_off')
		if cut_off == '':
			cut_off = 100

		stream_list = []
		queryset = Stream.objects.filter(main_stream=stream, stream_name=degree)
		for query in queryset:
			serializer = StreamSerializer(query)
			stream_list.append({**serializer.data})
		# print(stream_list)
		colleges = []
		for stream in stream_list:
			if float(stream['cut_off']) <= int(cut_off):
				college_obj = College.objects.get(college_id = stream['college_id'])
				college = CollegeSerializer(college_obj)
				college = {**college.data, **stream}
				applied = Application.objects.filter(student=student, college=college_obj, stream_name=degree)
				# print(applied)
				college['applied'] = bool(applied)
				colleges.append(college)
		# print(colleges)
		data = {
			'colleges' : colleges,
		}
		data['streams'] = self.get(request)
		return render(request, template_name='seekcollege.html', context=data)


def addQuestions():
	path = os.path.join(BASE_DIR , 'questions.xlsx')
	# print(path)
	df = pd.read_excel(path)
	# print(df)
	for i in range(len(df)):
		row = df.loc[i,:]
		# print(row)
		_, created = Question.objects.get_or_create(
				category= row['category'],
				question= row['question'],
				option_A= row['option_A'],
				option_B= row['option_B'],
				option_C= row['option_C'],
				option_D= row['option_D'],
				answer= row['answer'],
				explanation= row['explanation'],
			)
	

class AptitudeTestView(TemplateView):
	template_name = 'test.html'
	test = []

	def get(self, request):
		# Question.objects.all().delete()
		if Question.objects.count() == 0:
			addQuestions()
		queryset = Question.objects.all()
		all_questions = []
		for query in queryset:
			serializer = QuestionSerializer(query)
			all_questions.append({**serializer.data})
		# print(all_questions)

		student = Student.objects.get(user=request.user)
		test_obj = None
		for test in Test.objects.filter(student_id=student):
			if (datetime.now(timezone.utc) - test.date_appeared).total_seconds() < 1800:
				test_obj = test
		if test_obj== None:
			test_obj = Test.objects.create(student_id=student)
		test_id = test_obj.test_id
		# Test.objects.all().delete()

		while len(self.test)<30 and len(all_questions)>0:
		    i = random.randint(0, len(all_questions)-1)
		    self.test.append(all_questions[i])
		    all_questions.remove(all_questions[i])
		# print(self.test)
		
		data = {'test' : self.test,
				'test_id' : test_id,
				}
		return render(request, 'test.html', data)

	def post(self, request):
		result = 0
		test_id = request.POST.get('test_id')
		for question in self.test:
			answered = request.POST.get(question['question_id'])
			correct_answer = str(question['answer']).upper()
			# print(answered, correct_answer)
			if answered == correct_answer:
				result += 1
		test_obj = Test.objects.get(test_id=test_id)
		test_obj.result = result
		test_obj.save()
		# print(result)

		return redirect('/results/')


class ResultsView(TemplateView):
	template_name = 'results.html'

	def get(self, request):
		student = Student.objects.get(user=request.user)
		data = {
			'appeared' : False,
		}
		tests = []
		if Test.objects.filter(student_id=student):
			data['appeared'] = True
			queryset = Test.objects.filter(student_id=student)
			for test in queryset:
				serializer = TestSerializer(test)
				test_data = serializer.data
				if test_data['result'] == None:
					test_obj = Test.objects.get(test_id=test_data['test_id'])
					test_obj.delete()
				else:
					dt = test.date_appeared
					test_data['date'] = dt.date()
					test_data['time'] = dt.timetz()
					tests.append({**test_data})
		data['tests'] = tests
		return render(request, 'results.html', data)


class StudentProfileView(TemplateView):
	template_name = 'dashboard.html'
	success_url = '/dashboard/'

	# GET method
	def get(self, request, username):
		if EduUser.objects.filter(username=username):
			User = EduUser.objects.get(username = username)
			serializer = EduUserSerializer(User)
			user = serializer.data

			if not Student.objects.filter(user=User):
				student = Student.objects.create(user=User)
				student.save()
			else:
				student = Student.objects.get(user=User)
			serializer = StudentSerializer(student)
			user = {**user, **serializer.data}
			# print(user)

			queryset = Subject.objects.filter(student_id = user['student_id'])
			subjects = []
			for sub in queryset:
				serializer = SubjectSerializer(sub)
				subjects.append({**serializer.data})
			# print(subjects)

			user['subjects'] = subjects
			# print(user)

			return render(request, 'dashboard.html', context=user)
		else:
			messages.error("You have not logged in.")
			return redirect('/accounts/login/')
	
	# POST method
	def post(self,request):
		if 'update_username' in request.POST:
			# Using this form
			# User can update username
			user = request.user
			username = user.username
			new_username = request.POST.get('new_username')
			if username != new_username:
				if not EduUser.objects.filter(username=new_username):
					user = EduUser.objects.get(username=username)
					user.username = new_username
					user.save()
					messages.success(request, 'Username updated successfully.')
				else:
					messages.error(request, 'Username already taken.')
			else:
				messages.success(request, 'Username updated successfully.')

		elif 'update_email' in request.POST:
			# Using this form
			# User can update Email
			email = request.POST.get('email')
			new_email = request.POST.get('new_email')
			if email != new_email:
				if not EduUser.objects.filter(email=new_email):
					user = EduUser.objects.get(email=email)
					user.email = new_email
					user.save()
					messages.success(request, 'Email updated successfully.')
				else:
					messages.error(request, 'Email already taken.')
			else:
				messages.success(request, 'Email updated successfully.')

		elif 'change_password' in request.POST:
			# Using this form
			# User can change his/her password from dashboard itself
			
			user = request.user
			old_password = request.POST.get('old_password')
			new_password = request.POST.get('new_password')
			confirm_password = request.POSt.get('confirm_password')
			user = EduUser.objects.get(user_id = user.user_id)
			user.authenticate(username=user.username, password=old_password)
			if user is not None:
				if new_password == confirm_password:
					user.password = new_password
					user.save()
					messages.success(request, 'Password changed Successfully.')
				else:
					messages.error(request, " New Password doesn't match.")
			else:
				messages.error(request, "Password doesn't match.")
			
		elif 'update_personal' in request.POST:
			# Using this form
			# User can update personal details

			user = request.user
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			full_name = request.POST.get('full_name')
			gender = request.POST.get('gender')
			birth_date = request.POST.get('birth_date')
			phone_no = request.POSt.get('phone_no')
			
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			
			student = Student.objects.get(user=user)
			student.full_name = full_name
			student.gender = gender
			student.birth_date = birth_date
			student.phone_no = phone_no
			student.save()
			messages.success(request, "Details updated Successfully.")

		elif 'update_academic' in request.POST:
			# Using this form
			# Student can update his/her acdemic details

			tenth_brd = request.POST.get('tenth_brd')
			tenth_per = request.POST.get('tenth_per')
			twelth_brd = request.POST.get('twelth_brd')
			twelth_per = request.POST.get('twelth_per')
			twelth_stream = request.POST.get('twelth_stream')

			user = request.user
			student = Student.objects.get(user=user)
			student.tenth_brd = tenth_brd
			student.tenth_per = tenth_per
			student.twelth_brd = twelth_brd
			student.twelth_per = twelth_per
			student.twelth_stream = twelth_stream
			student.save()

		elif 'add_subject' in request.POST:
			# Using this form
			# Student can add various subjects and it's marks.

			user = request.user
			sub_name = str(request.POST.get('sub_name')).lower()
			std = request.POST.get('std')
			marks = request.POST.get('marks')

			student = Student.objects.get(user=user)
			subject, created = Subject.objects.get_or_create(
				student_id= student.student_id,
				std = std,
				sub_name= sub_name,
			)
			subject.marks = marks
			subject.save()

		elif 'remove_subject' in request.POST:
			# Using this form
			# Student can remove the subjects

			subject_id = request.POST.get('subject_id')
			subject = Subject.objects.get(subject_id=subject_id)
			subject.delete()


class CollegeProfileView(TemplateView):
	# In this view manage get and post for college_dashboard.html
	template_name = 'college_dashboard.html'

	# GET method
	def get(self, request, username):
		user = EduUser.objects.get(username=username)
		data = {
			'created' : True
		}
		if user.is_college_admin:
			college,created = College.objects.get_or_create(user=user)
			serializer = CollegeSerializer(college)
			data['college'] = {**serializer.data}
			streams = []
			if created == False:
				queryset = Stream.objects.filter(college_id=college.college_id)
				for query in queryset:
					serializer = StreamSerializer(query)
					streams.append({**serializer.data})
				data['streams'] = streams
				data['created'] = False
			return render(request, 'college_dashboard.html', data)
		else:
			return redirect('/dashboard/' + user.username)

	# POST method
	def post(self, request,username):
		college_name = request.POST.get('college_name')
		college_city = request.POST.get('college_city')
		college_address = request.POST.get('college_address')
		user = request.user
		college = College.objects.get(user=user)
		college.college_name = college_name
		college.college_address = college_address
		college.college_city = college_city
		college.save()
		messages.success(request, 'College Details Updated Successfully.')
		return redirect('/college/' + username)


class QuestionView(TemplateView):
	# this view is for question page
	# on which college admin can suggest questions
	template_name="questions.html"

	def post(self, request):
		category = request.POST.get('category')
		category = str(category).lower()
		question = request.POST.get('question')
		option_A = request.POST.get('option_A')
		option_B = request.POST.get('option_B')
		option_C = request.POST.get('option_C')
		option_D = request.POST.get('option_D')
		answer = request.POST.get('answer')
		answer = str(answer).lower()
		explanation = request.POST.get('explanation')
		user = request.user

		question_obj = Question.objects.create(
					category=category,
					question=question,
					option_A=option_A,
					option_B=option_B,
					option_C=option_C,
					option_D=option_D,
					answer=answer,
					explanation=explanation,
					given_by= user,
					)
		question_obj.save()
		messages.success(request, "Question added successfully.")
		return render(request, template_name = 'questions.html')


class AddStreamView(TemplateView):
	template_name = "addstream.html"

	# GET method
	def get(self, request):
		queryset = Stream.objects.all()
		streams = []
		for query in queryset:
			serializer = StreamSerializer(query)
			stream = serializer.data
			streams.append(stream['stream_name'])
		streams = set(streams)
		data = {
			'streams' : streams,
		}
		return render(request, template_name="addstream.html", context=data)

	def post(self, request):
		user = request.user
		college = College.objects.get(user=user)
		main_stream = request.POST.get('main_stream')
		stream = request.POST.get('stream')
		if stream == "others":
			stream = request.POST.get('others')
		cut_off = request.POST.get('cut_off')
		stream_obj,created = Stream.objects.get_or_create(
			college_id=college,
			main_stream=main_stream,
			stream_name=stream,
			cut_off=cut_off,
		)
		stream_obj.save()
		messages.success(request, "Stream added Successfully.")
		return redirect('/college/' + user.username + '/')


class ApplicationsView(TemplateView):
	template_name = "view_students.html"

	# GET method
	def get(self, request):
		user = request.user
		college = College.objects.get(user=user)
		queryset = Application.objects.filter(college=college)
		applications = []
		for query in queryset:
			serializer = ApplicationSerializer(query)
			application = {**serializer.data}
			student = Student.objects.get(student_id=application['student'])
			serializer = StudentSerializer(student)
			application = {**application, **serializer.data}
			tests = Test.objects.filter(student_id=application['student'])
			results = [0]
			for test_obj in tests:
				test = TestSerializer(test_obj)
				print(test.data)
				results.append(test.data['result'])
			application['result'] = max(results)
			applications.append(application)
		print(applications)
		data = {
			'applications' : applications
		}
		return render(request, template_name='view_students.html', context=data)

	# POST method
	def post(self,request):
		pass

def apply(request,stream, id):
	user = request.user
	student = Student.objects.get(user=user)
	college = College.objects.get(college_id=id)
	_, created = Application.objects.get_or_create(
			student = student,
			college = college,
			stream_name=stream
		)
	messages.success(request, "Application submitted")
	return redirect('/seekcollege/')

def feedbackView(request):
	if request.method == 'POST':
		comment = request.POST.get('comment')
		rating = request.POST.get('rating')
		
		if len(comment)<4:
			messages.error(request, 'Please give your feedback. It helps us to grow.')
		else:
			feedback = Feedback(comment = comment, rating = rating)
			feedback.save()
			messages.success(request, 'Successfully submitted')   
	return render(request, template_name = 'feedback.html')    

