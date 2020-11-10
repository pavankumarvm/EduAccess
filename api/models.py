from django.db import models
import uuid

from django.db.models.fields import NullBooleanField
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

class College(models.Model):
    college_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(EduUser, on_delete=models.CASCADE,unique=True)
    college_name = models.CharField(max_length=100, blank=False, null=False)
    college_address = models.CharField(max_length=100, blank=True, null=True)
    college_city = models.CharField(max_length=25, blank=False, null=False)


class Stream(models.Model):
    stream_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    stream_name = models.CharField(max_length=20, blank=False, null=False)
    cut_off = models.DecimalField(decimal_places=2, max_digits=4)


STD = (('10th', '10th'), ('12th', '12th'))
class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="subjects")
    std = models.CharField(max_length=4,default=None, choices=STD)
    sub_name = models.CharField(max_length=20, blank=True,null=True)
    marks = models.IntegerField(blank=True,null=True)


ANSWER = (('A','A'), ('B','B'), ('C','C'), ('D','D'))
class Question(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category = models.CharField(max_length=50, null=True, blank=True)
    question = models.CharField(max_length=250, null=False, blank=False)
    option_A = models.CharField(max_length=250, null=True, blank=True)
    option_B = models.CharField(max_length=250, null=True, blank=True)
    option_C = models.CharField(max_length=250, null=True, blank=True)
    option_D = models.CharField(max_length=250, null=True, blank=True)
    answer = models.CharField(max_length=1, choices=ANSWER, null=True, blank=True)
    explanation = models.CharField(max_length=250, null=True, blank=True)
    given_by = models.ForeignKey(EduUser, on_delete=models.SET_NULL, related_name='author',null=True)


CHOICES = (('Bad','Bad'),('Average','Average'),('Good','Good'),('Excellent','Excellent'))
class Feedback(models.Model):
    sno= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField()
    # experience = models.CharField(max_length=10, choices=CHOICES, default=None)
    # print(experience, comment)

    def __str__(self):
        return 'Message from ' + self.comment
    
# class Student(models.Model):  
#     first_name = models.CharField(max_length=20)  
#     last_name  = models.CharField(max_length=30)  
#     class Meta:  
#         db_table = "student"  
