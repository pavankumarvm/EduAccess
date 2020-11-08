from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Feedback
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime

# from .models import Person
from .forms import SimpleForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class StudentProfileView(TemplateView):
    template_name = 'dashboard.html'

# class FeedbackView(TemplateView):
#     template_name = 'feedback.html'

class StreamDetailsView(TemplateView):
    template_name = 'StreamDetails.html'
    
class AptitudeDetailsView(TemplateView):
    template_name = 'AptitudeQuestions.html'

def FeedbackView(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        # form = SimpleForm(request.POST)
        # experience = request.POST.get('experience')
        FeedbackView = Feedback(comment = comment)
        FeedbackView.save()
        
        # if form.is_valid():
        #     form.save()
        #     form=SimpleForm()

        # context={
        #     'form': form
        # }    

        if len(comment)<4:
            messages.error(request, 'Please give your feedback. It helps us to grow.')
        else:
            messages.success(request, 'Successfully submitted')   
            form = SimpleForm()

    return render(request, 'feedback.html')    



# def home(request):
#   # if this is a POST request we need to process the form data
#   if request.method == 'POST':
#     # create a form instance and populate it with data from the request:
#     form = SubscribeForm(request.POST)
#     # check whether it's valid:
#     if form.is_valid():
#         # process the data in form.cleaned_data as required
#         p = form.save()
#         '''
#         name = form.cleaned_data['name']
#         number = form.cleaned_date['phone_number']
#         p = Person(name=name, phone_number=number, date_subscribed=datetime.now(), messages_recieved=0)
#         p.save()
#         '''
#         # redirect to a new URL:
#         return HttpResponseRedirect('/success/')
#   # if a GET (or any other method) we'll create a blank form    
#   else: 
#     form = SubscribeForm()

#   return render(request, 'texting/index.html', {'form': form})

# def index2(request):
#     if request.method == 'POST':
#         form = PictureForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             Picture.objects.create(like=cd['like'], name=cd['name'], email=cd['email'], message=cd['message'])
#             return HttpResponseRedirect ('/thanks/')
#     else:
#         form = PictureForm()
#     return render_to_response('index2.html', {'form':form},)


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