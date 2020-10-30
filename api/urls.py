from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('register/', RegisterView.as_view(), name='register'),
]