from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class StudentProfileView(TemplateView):
    template_name = 'dashboard.html'
    

# def feedback_user(request):
#     return render(request,
#                     'feedback.html',
#                 )

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