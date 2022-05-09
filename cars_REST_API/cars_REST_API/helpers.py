from rest_framework import serializers


def validate_confirm_password(pass1, pass2):
    if pass1 == pass2:
        return
    raise serializers.ValidationError({"password": "Confirm password error"})
