from django.urls import path

from .views import feedbackView, HomePageView, StreamDetailsView, StudentProfileView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', StudentProfileView.as_view(), name="dashboard"),
    path('stream/', StreamDetailsView.as_view(), name="stream"),
    path('feedback/', views.feedbackView, name="feedback"),
    #  path('college/', views.college, name="college"),
    #  path('manageclg/', views.manageclg, name="manageclg"),
    #  path('training/', views.training, name="training"),
    #  path('viewstd/', views.viewstd, name="viewstd"),
    #  path('questions/', views.questions, name="questions"),
]