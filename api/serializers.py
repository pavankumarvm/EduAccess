from rest_framework import serializers

from .models import Student, Subject

class StudentSerializer(serializers.ModelSerializer):
    """
        Serialize the Student Data
    """
    class Meta:
        model = Student
        fields = ['student_id', 'full_name', 'gender', 'birth_date', 'phone_no', 'tenth_per', 'tenth_brd' ,'twelth_brd', 'twelth_per', ]
        read_only_fields = ['student_id', 'user']

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

class SubjectSerializer(serializers.ModelSerializer):
    """
        Serialize the data
    """
    class Meta:
        model = Subject
        fields = ['subject_id', 'std', 'sub_name', 'marks']
        read_only_fields = ['student_id']

    
    def create(self, validated_data):
        return Subject.objects.create(**validated_data)