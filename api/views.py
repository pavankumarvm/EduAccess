from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from accounts.models import EduUser
from .models import Student, Subject, Feedback
from .serializers import StudentSerializer, SubjectSerializer
from accounts.serializers import EduUserSerializer
# from .forms import StuForm  

class HomePageView(TemplateView):
    template_name = 'home.html'

class StreamuserView(TemplateView):
    template_name = 'Streamuser.html'
    
class AptitudeuserView(TemplateView):
    template_name = 'AptitudeQuestions.html'

class StudentProfileView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, username):
        if EduUser.objects.filter(username=username):
            queryset = EduUser.objects.get(username = username)
            serializer = EduUserSerializer(queryset)
            user = serializer.data

            queryset = Student.objects.get(user=username)
            serializer = StudentSerializer(queryset)
            user = {**user, **serializer.data}
            # print(user)

            queryset = Subject.objects.filter(student_id = user['student_id'])
            subjects = []
            for sub in queryset:
                serializer = SubjectSerializer(sub)
                subjects.append({**serializer.data})
            # print(subjects)

            user['subjects'] = subjects
            print(user)

            return render(request, 'dashboard.html', context=user)
        else:
            messages.error("You have not logged in.")
            return redirect('/accounts/login/')
    
    def post(self,request,username):
        pass

def feedbackView(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        # experience = request.POST.get('experience')
        FeedbackView = Feedback(comment = comment)
        FeedbackView.save()
        

        if len(comment)<4:
            messages.error(request, 'Please give your feedback. It helps us to grow.')
        else:
            messages.success(request, 'Successfully submitted')   
    return render(request, template_name = 'feedback.html')    
