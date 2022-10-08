from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     profile=prof()
#     class Meta:
#         model = User
#         depth = 1
#         fields = ['profile',"id"]

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password',"email")
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['password'])
        return user
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")