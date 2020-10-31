from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate
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
 
        if not (username and first_name and last_name and email and password1):
            data = {
                'token': 'empty',
                'error': 'true',
                'message': 'Fill the Empty Fields.', 
            }
        else:
            if EduUser.objects.filter(username=username) or EduUser.objects.filter(email=email):
                data = {
                    'token': 'empty',
                    'error': 'true',
                    'message': 'Username or email already exists.Try another.', 
                }
            else:
                user = EduUser.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                # token,created = Token.objects.get_or_create(user=user)
                data = {
                    # 'token' : token.key,
                    'error' : 'false',
                    'message' : 'User registerd successfully.'
                }
                return redirect("/")
        return render(request, 'register.html', context=data)
    else:
        return render(request, 
                    template_name='register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # if Token.objects.filter(user=user):
            #     token = Token.objects.get(user=user)
            #     token.delete()

            # token = Token.objects.create(user=user)

            # data = {
            #     'token': token.key,
            #     'error': 'false',
            #     'username': user.username,
            #     'first_name': user.first_name,
            #     'last_name': user.last_name,
            #     'email': user.email,
            # }
            return redirect('/')
        else:
            data = {
                'token': 'empty',
                'error': 'true',
                'message': 'User not found',
            }
    else:
        return render(request,
                    template_name='login.html',
                )