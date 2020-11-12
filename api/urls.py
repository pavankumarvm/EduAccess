from django.urls import path

from .views import HomePageView, StudentProfileView, AptitudeTestView, SeekCollegeView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/<str:username>/', StudentProfileView.as_view() , name="dashboard"),
    path('test/', AptitudeTestView.as_view(), name="aptitude_test"),
    path('feedback/', views.feedbackView, name="feedback"),
    path('seekcollege/', SeekCollegeView.as_view(), name="stream"),
    #  path('college/', views.college, name="college"),
    #  path('manageclg/', views.manageclg, name="manageclg"),
    #  path('training/', views.training, name="training"),
    #  path('viewstd/', views.viewstd, name="viewstd"),
    #  path('questions/', views.questions, name="questions"),
]