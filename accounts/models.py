from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import EduUserManager
# Create your models here.

class EduUser(AbstractBaseUser, PermissionsMixin):

    # Creates User

    username = models.CharField(max_length=35, primary_key=True, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_college_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = EduUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

class Otp(models.Model):
    user = models.OneToOneField(EduUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    otp_valid_time = models.DateTimeField(auto_now_add=True)
    no_of_attempts = models.IntegerField(default = 5)