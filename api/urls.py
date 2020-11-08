from django.urls import path

from .views import FeedbackView, HomePageView, StreamDetailsView, StudentProfileView, AptitudeDetailsView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', StudentProfileView.as_view(), name="dashboard"),
    path('stream/', StreamDetailsView.as_view(), name="stream"),
    path('AptitudeQuestions/', AptitudeDetailsView.as_view(), name="AptitudeQuestions"),
    path('feedback/', views.FeedbackView, name="feedback"),
    # path('tryin/', views.tryinView, name="tryin"),
    #  path('college/', views.college, name="college"),
    #  path('manageclg/', views.manageclg, name="manageclg"),
    #  path('training/', views.training, name="training"),
    #  path('viewstd/', views.viewstd, name="viewstd"),
    #  path('questions/', views.questions, name="questions"),
]