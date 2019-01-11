from rest_framework import serializers
from account.models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class UserProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'phone_number', 'date_of_birth')