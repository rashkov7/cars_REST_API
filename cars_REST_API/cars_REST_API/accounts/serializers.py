from rest_framework import serializers

from cars_REST_API.accounts.models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileModel
        exclude = ('user',)