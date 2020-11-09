from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Feedback
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'home.html'

class StudentProfileView(TemplateView):
    template_name = 'dashboard.html'

class StreamDetailsView(TemplateView):
    template_name = 'StreamDetails.html'
    
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
