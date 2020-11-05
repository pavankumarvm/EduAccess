from django.db import models
import uuid

from accounts.models import EduUser
# Create your models here.

GENDER = (('Male','Male'), ('Female','Female'),('Others',('Others')))
BOARD = (('SB','SB'),('CBSE','CBSE'),('ICSE','ICSE'),('IB','IB'))

class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(EduUser, on_delete=models.CASCADE,unique=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default=None)
    birth_date = models.DateField(blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    tenth_per = models.DecimalField(decimal_places=2, max_digits=4)
    twelth_per = models.DecimalField(decimal_places=2, max_digits=4)
    tenth_brd = models.CharField(max_length=5, choices=BOARD, null=False, blank=False)
    twelth_brd = models.CharField(max_length=5, choices=BOARD, null=False, blank=False)


STD = (('10th', '10th'), ('12th', '12th'))
class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="subjects")
    std = models.CharField(max_length=4,default=None, choices=STD)
    sub_name = models.CharField(max_length=20, blank=True,null=True)
    marks = models.IntegerField(blank=True,null=True)
