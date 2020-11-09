from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EduUserSerializer(serializers.ModelSerializer):
    """
        Serialize the User Data
    """

    password = serializers.CharField(write_only=True, required= False)
    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_college_admin' ,'is_active']
        read_only_fields = ['date_joined', 'last_login']

    def create(self, validated_data):
        return EduUser.objects.create(**validated_data)