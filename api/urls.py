from django.urls import path

from .views import HomePageView, StudentProfileView
from .views import AptitudeTestView, SeekCollegeView
from .views import ResultsView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/<str:username>/', StudentProfileView.as_view() , name="dashboard"),
    path('test/', AptitudeTestView.as_view(), name="aptitude_test"),
    path('results/', ResultsView.as_view(), name="results"),
    path('feedback/', views.feedbackView, name="feedback"),
    path('seekcollege/', SeekCollegeView.as_view(), name="stream"),
    #  path('college/', views.college, name="college"),
    #  path('manageclg/', views.manageclg, name="manageclg"),
    #  path('training/', views.training, name="training"),
    #  path('viewstd/', views.viewstd, name="viewstd"),
    #  path('questions/', views.questions, name="questions"),
]