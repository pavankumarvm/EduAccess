from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from .models import Student, Subject, College, Question, Stream
from .models import Feedback

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


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question)
admin.site.register(Feedback)