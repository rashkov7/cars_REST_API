from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.views import APIView

from cars_REST_API.accounts.models import ProfileModel
from cars_REST_API.helpers import validate_confirm_password

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=3,
        max_length=30,
        write_only=True,
        style={"input_type": "password"}
    )

    password2 = serializers.CharField(
        min_length=3,
        max_length=30,
        write_only=True,
        style={"input_type": "password"}
    )

    def validate(self, attrs):
        pass1 = attrs['password']
        pass2 = attrs['password2']
        validate_confirm_password(pass1, pass2)
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return UserModel.objects.create_user(**validated_data)

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password', 'password2')


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=3,
        max_length=30,
        write_only=True,
        style={"input_type": "password"}
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password', 'token')
        read_only_fields = ['token']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileModel
        exclude = ('user',)