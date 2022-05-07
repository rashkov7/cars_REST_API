import datetime

from rest_framework import serializers

from cars_REST_API.cars_app.models import CarBrand, CarModel, UserCar


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('brand_name', )

    def create(self, validated_data):
        return CarBrand.objects.create(brand_name=validated_data['brand_name'])


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        exclude = ('is_deleted', "deleted")

    def create(self, validated_data):
        return CarModel.objects.create(**validated_data)


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = '__all__'

    def create(self, validated_data):
        return UserCar.objects.create(**validated_data)
