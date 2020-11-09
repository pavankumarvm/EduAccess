from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Feedback
from django.contrib import messages
from datetime import datetime
# from .forms import StuForm  

class HomePageView(TemplateView):
    template_name = 'home.html'

class StudentProfileView(TemplateView):
    template_name = 'dashboard.html'

class StreamDetailsView(TemplateView):
    template_name = 'StreamDetails.html'
    
class AptitudeDetailsView(TemplateView):
    template_name = 'AptitudeQuestions.html'

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
<<<<<<< HEAD
    return render(request, template_name = 'feedback.html')    
=======

    return render(request, 'feedback.html')    

# def tryinView(request):  
#     stu = StuForm()  
#     return render(request,"tryin.html",{'form':stu})  

# def stream_user(request):
#     return render(request,
#                     'StreamDetails.html',
#                 )

# def college_user(request):
#     return render(request,
#                     'clgdetails.html',
#                 )                

# def manageclg_user(request):
#     return render(request,
#                     'ManageClg.html',
#                 )                

# def training_user(request):
#     return render(request,
#                     'TrainingData.html',
#                 )   

# def viewstd_user(request):
#     return render(request,
#                     'ViewStudents.html',
#                 )                              

# def questions_user(request):
#     return render(request,
#                     'Questions.html',
#                 )        
>>>>>>> be5ea6c7a3c14d3f275571f8a8a20bcd81d97eac
