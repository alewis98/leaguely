from rest_framework import serializers
from account.models import UserProfile
from api.models import *
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


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'
        

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'