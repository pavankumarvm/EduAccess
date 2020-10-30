from django.urls import path

# from .views import EduUserViewSet,RegisterView
from . import views

urlpatterns = [
    path('register/', views.register_user, name="register_user"),
    path('login/', views.login_user, name="login_user"),
    # path('',RegisterView.as_view(), name="register"),
    # path('get-user/', EduUserViewSet.as_view({
    #     'get': 'get',
    #     'post' : 'post',
    # })),
    # path('get-user/<str:username>/', EduUserViewSet.as_view({
    #     'get': 'retrieve',
    #     'post': 'update',
    #     'delete': 'destroy',
    # }))
]