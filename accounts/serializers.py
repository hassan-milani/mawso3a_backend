from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, UserProfile

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions']
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    roles = RoleSerializer(many=True, read_only=True)
    

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'name', 'roles', 'info']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_id = self.context['user_id'] 
        user = User.objects.get(pk=user_id)
        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile
