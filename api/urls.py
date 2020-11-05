from django.urls import path

from .views import HomePageView, StudentProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', StudentProfileView.as_view(), name="dashboard")
    # path('feedback/', views.feedback, name="feedback"),
    # path('stream/', views.stream, name="stream"),
    # path('college/', views.college, name="college"),
    # path('manageclg/', views.manageclg, name="manageclg"),
    # path('training/', views.training, name="training"),
    # path('viewstd/', views.viewstd, name="viewstd"),
    # path('questions/', views.questions, name="questions"),
]