from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy


from .serializers import EduUserSerializer
from .models import EduUser


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
 
        if not (username and first_name and last_name and email and password1 and password2):
            data = {
                'error': 'true',
                'message': 'Fill the Empty Fields.', 
            }
        elif password1 == password2:
            if EduUser.objects.filter(username=username):
                data = {
                    'error': 'true',
                    'message': 'Username already exists.Try another.', 
                }
                return render(request, 'register.html', context=data)
            elif EduUser.objects.filter(email=email):
                data = {
                    'error': 'true',
                    'message': 'Email Address already exists.Try another.', 
                }
                return render(request, 'register.html', context=data)
            else:
                user = EduUser.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                data = {
                    'error' : 'false',
                    'message' : 'User registered successfully.'
                }
                return redirect("/accounts/login/")
        else:
            data = {
                'error': 'true',
                'message': "Passwords doesn't match", 
            }
            return render(request, 'register.html', context=data)
    else:
        return render(request, 
                    template_name='register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            data = {
                'error': 'false',
                'message': 'Login Successfull.',
            }
            return redirect('/')
        else:
            data = {
                'error': 'true',
                'message': 'Wrong username or password.',
            }
            return render(request,
                    template_name='login.html',
                    context=data,
                    )
    else:
        return render(request,
                    template_name='login.html',
                )

def logout_user(request):
    logout(request)
    return redirect('/')

def feedback_user(request):
    return render(request,
                    'feedback.html',
                )