from django.db import models
import uuid

from django.db.models.fields import NullBooleanField
from accounts.models import EduUser
from django import forms
# Create your models here.

GENDER = (('Male','Male'), ('Female','Female'),('Others',('Others')))
BOARD = (('SB','SB'),('CBSE','CBSE'),('ICSE','ICSE'),('IB','IB'))


class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(EduUser, on_delete=models.CASCADE,unique=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default=None, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    tenth_per = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    twelth_per = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    tenth_brd = models.CharField(max_length=5, choices=BOARD, null=True, blank=False)
    twelth_brd = models.CharField(max_length=5, choices=BOARD, null=True, blank=False)
    twelth_stream = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'student'

class College(models.Model):
    college_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(EduUser, on_delete=models.CASCADE,unique=True)
    college_name = models.CharField(max_length=100, blank=False, null=False)
    college_address = models.CharField(max_length=100, blank=True, null=True)
    college_city = models.CharField(max_length=25, blank=False, null=False)

    
    class Meta:
        db_table = 'college'


class Stream(models.Model):
    stream_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE, related_name="streams")
    stream_name = models.CharField(max_length=50, blank=False, null=False)
    main_stream = models.CharField(max_length=20, blank=False, null=False)
    cut_off = models.DecimalField(decimal_places=2, max_digits=4)

    class Meta:
        db_table = 'stream'


class Application(models.Model):
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    college = models.ForeignKey(College, related_name='applied_to', on_delete=models.CASCADE, null=True)
    stream_name = models.CharField(max_length=50, blank=True, null=True)
    date_applied = models.DateField(auto_now_add=True)
    # For status it can hold three following values
    # A - Accepted
    # N - None
    # U - Unavailable
    status = models.CharField(max_length=1, blank=False, null=False, default="N")


    class Meta:
        db_table = 'application'


STD = (('10th', '10th'), ('12th', '12th'))
class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="subjects")
    std = models.CharField(max_length=4,default=None, choices=STD)
    sub_name = models.CharField(max_length=20, blank=True,null=True)
    marks = models.IntegerField(blank=True,null=True)

    
    class Meta:
        db_table = 'subject'


ANSWER = (('a','A'), ('b','B'), ('c','C'), ('d','D'))
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

    class Meta:
        db_table = 'question'


class Test(models.Model):
    test_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    result = models.IntegerField(null=False, blank=False, default=0)
    date_appeared = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'test'


RATING = (('Bad','Bad'),('Average','Average'),('Good','Good'),('Excellent','Excellent'))
class Feedback(models.Model):
    sno= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField()
    rating = models.CharField(max_length=20, choices=RATING, null=True, blank=True)

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return 'Message from ' + self.comment
