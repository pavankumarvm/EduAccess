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
    
    def post(self,request):
        if 'update_username' in request.POST:
            # Using this form
            # User can update username
            username = request.POST.get('username')
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

        elif 'change_password' in request.POST:
            # Using this form
            # User can change his/her password from dashboard itself
            
            username = request.POST.get('username')
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POSt.get('confirm_password')
            user = EduUser.objects.get(username=username)
            user.authenticate(username=username, password=old_password)
            if user is not None:
                if new_password == confirm_password:
                    user.password = new_password
                    user.save()
                    messages.success(request, 'Password changed Successfully.')
                else:
                    messages.error(request, " New Password doesn't match.")
            else:
                messages.error(request, "Password doesn't match.")
            
        else:
            pass
        

def feedbackView(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        # experience = request.POST.get('experience')
        FeedbackView = Feedback(comment = comment, rating = rating)
        FeedbackView.save()
        
        if len(comment)<4:
            messages.error(request, 'Please give your feedback. It helps us to grow.')
        else:
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
    