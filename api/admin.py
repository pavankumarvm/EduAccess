from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from .models import Student, Subject, College, Question, Stream
from .models import Feedback, Test, Application

class StudentAdmin(ModelAdmin):

    ordering = ('user',)
    list_display = ('user', 'full_name', 'phone_no',)
    search_fields = ('user', 'phone_no',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None,{'fields': ('user', 'full_name',)}),
        ('Personal Information',{'fields' : ('gender', 'birth_date', 'phone_no',)}),
        ('Academic Information',{'fields' : ('tenth_brd', 'tenth_per', 'twelth_brd', 'twelth_per',)}),
    )


class SubjectAdmin(ModelAdmin):
    ordering = ('subject_id',)
    fieldsets = (
        (None,{'fields': ('subject_id', 'student_id', 'std', 'sub_name', 'marks')}),
    )

class QuestionAdmin(ModelAdmin):
    ordering = ('category','question_id',)
    list_display = ('category', 'question', 'answer', 'given_by')
    fieldsets = (
        (None,{'fields': ('category','question_id', 'question', 'option_A', 'option_B', 'option_C', 'option_D', 'answer', 'explanation', 'given_by')}),
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Test)
admin.site.register(Application)
admin.site.register(Feedback)