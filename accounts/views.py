from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import EduUserSerializer
from .models import EduUser
from django.views.generic import TemplateView
# Create your views here.

# class RegisterView(TemplateView):
#     template_name = 'register.html'

# class EduUserViewSet(viewsets.ModelViewSet):
#     queryset = EduUser.objects.all()
#     serializer_class = EduUserSerializer

#     """
#         This view will return all data about user
#     """

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             EduUser.objects.create_user(**serializer.validated_data)

#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

#         return Response({
#             'status' : 'Bad Request',
#             'message' : 'Account could not be created with received data.'
#         }, status=status.HTTP_400_BAD_REQUEST)


#     def get(self,request):
#         # method: GET
#         # Return about EduUsers

#         queryset = EduUser.objects.all()
#         serializer = EduUserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         # method: POST
#         # Add Details about EduUsers

#         serializer = EduUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, username):
#         # Method: GET
#         # Return data about prticular EduUser

#         queryset = self.get_detail(username)
#         serializer = EduUserSerializer(queryset)
#         return Response(serializer.data)

#     def update(self, request, username):
#         # Method : PUT
#         # Update a particular EduUser detail

#         queryset = self.get_detail(username)
#         serializer = EduUserSerializer(queryset, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, username):
#         # Method: DELETE
#         # Delete a record

#         queryset = self.get_detail(username)
#         queryset.delete()
#         return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

#     def get_detail(self, user_username):
#         try:
#             print(user_username)
#             return EduUser.objects.get(username=user_username)
#         except EduUser.DoesNotExist:
#             raise Http404


# @api_view(['POST'])
# @permission_classes(AllowAny)
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (username and first_name and last_name and email and password):
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
                user = EduUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                # token = Token.objects.get_or_create(user=user)
                # print(token)
                data = {
                    # 'token' : token.key,
                    'error' : 'false',
                    'message' : 'User registerd successfully.'
                }
                return redirect("/")
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

# @api_view(['POST'])
# @permission_classes([AllowAny])
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        if Token.objects.filter(user=user):
            token = Token.objects.get(user=user)
            token.delete()

        token = Token.objects.create(user=user)

        data = {
            'token': token.key,
            'error': 'false',
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }

    else:
        data = {
            'token': 'empty',
            'error': 'true',
            'message': 'User not found',
        }
    return redirect("/")