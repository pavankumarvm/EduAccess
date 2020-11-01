from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_user, name="register_user"),
    path('login/', views.login_user, name="login_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path('feedback/', views.feedback_user, name="feedback_user"),
    path('stream/', views.stream_user, name="stream_user"),
    path('college/', views.college_user, name="college_user"),
    path('manageclg/', views.manageclg_user, name="manageclg_user"),
    path('training/', views.training_user, name="training_user"),
    path('viewstd/', views.viewstd_user, name="viewstd_user"),
    path('questions/', views.questions_user, name="questions_user"),
    path('forgotpass/', views.forgotpass_user, name="forgotpass_user"),
]