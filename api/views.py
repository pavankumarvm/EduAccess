import random
import pandas as pd
import os
from eduaccess.settings import BASE_DIR

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate

from accounts.models import EduUser
from .models import Student, Subject, Question,Feedback
from .serializers import StudentSerializer, SubjectSerializer, QuestionSerializer
from accounts.serializers import EduUserSerializer
# from .forms import StuForm  

class HomePageView(TemplateView):
	template_name = 'home.html'


class SeekCollegeView(TemplateView):
	template_name = 'seekcollege.html'
	# college_list = []
	
	# GET method
	# def get(request):
	# 	pass
	
	# POST method
	def post(request):
		stream = request.POST.get('stream')
		degree = request.POST.get('degree')
		cut_off = request.POST.get('cut_off')

		college_list = []
		sql_query = """
				SELECT C.college_id, C.college_name, C.college_city, S.stream_id, S.stream_name, S.cut_off
				FROM stream as S, college as C 
				WHERE C.college_id = S.college_id and S.cut_off <= """ + cut_off + ';'
		for i in Stream.objects.raw(sql_query):
			print(i)


class AptitudeTestView(TemplateView):
	template_name = 'test.html'

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

		# test = []
		# while len(test)<10 and len(all_questions)>0:
		#     i = random.randint(0, len(all_questions)-1)
		#     test.append(all_questions[i])
		#     all_questions.remove(all_questions[i])
		# print(test)
		
		data = {'test' : all_questions}
		return render(request, 'test.html', data)


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
	