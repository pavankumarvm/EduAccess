from django.urls import path

from .views import HomePageView, StudentProfileView
from .views import AptitudeTestView, SeekCollegeView
from .views import ResultsView
from .views import CollegeProfileView
from .views import QuestionView
from .views import AddStreamView
from .views import ApplicationsView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/<str:username>/', StudentProfileView.as_view() , name="dashboard"),
    path('test/', AptitudeTestView.as_view(), name="aptitude_test"),
    path('results/', ResultsView.as_view(), name="results"),
    path('seekcollege/', SeekCollegeView.as_view(), name="stream"),
    path('college/<str:username>/', CollegeProfileView.as_view(), name="college"),
    path('suggest_question/', QuestionView.as_view(), name="suggest_question"),
    path('add_stream/', AddStreamView.as_view(), name="add_stream"),
    path('apply/<str:stream>/<str:id>/', views.apply , name="apply"),
    path('feedback/', views.feedbackView, name="feedback"),
    path('view_students/', ApplicationsView.as_view(), name="view_students"),
]