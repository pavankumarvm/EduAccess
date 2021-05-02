from rest_framework import serializers

from .models import Student, Subject, Question, Test, College, Stream, Application

class StudentSerializer(serializers.ModelSerializer):
    """
        Serialize the Student Data
    """
    class Meta:
        model = Student
        fields = ['student_id', 'full_name', 'gender', 'birth_date', 'phone_no', 'tenth_per', 'tenth_brd' ,'twelth_brd', 'twelth_per', 'twelth_stream']
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


class QuestionSerializer(serializers.ModelSerializer):
    """
        Serialize the data
    """
    class Meta:
        model = Question
        fields = ['question_id', 'question', 'option_A', 'option_B', 'option_C', 'option_D', 'answer', 'explanation', 'given_by']
        read_only_fields = ['given_by']
    
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

class TestSerializer(serializers.ModelSerializer):
    """
        Serialize the data
    """
    class Meta:
        model = Test
        fields = ['test_id', 'student_id', 'result', 'date_appeared']
        read_only_fields = ['test_id', 'student_id']

    def create(self, validated_data):
        return Test.objects.create(**validated_data)

class CollegeSerializer(serializers.ModelSerializer):
    """
        Serialize the college data
    """
    class Meta:
        model = College
        fields = ['college_id', 'user', 'college_name', 'college_address', 'college_city']

    def create(self, validated_data):
        return College.objects.create(**validated_data)


class StreamSerializer(serializers.ModelSerializer):
    """
        Serialize the stream data
    """
    class Meta:
        model = Stream
        fields = ['stream_id', 'college_id', 'stream_name', 'main_stream', 'cut_off']

    def create(self, validated_data):
        return Stream.objects.create(**validated_data)


class ApplicationSerializer(serializers.ModelSerializer):
    """
        Serialize the application data
    """
    class Meta:
        model = Application
        fields = ['application_id', 'student', 'college', 'stream_name', 'date_applied', 'status']

    def create(self, validated_data):
        return Application.objects.create(**validated_data)

