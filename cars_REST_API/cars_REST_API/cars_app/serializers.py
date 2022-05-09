from rest_framework import serializers

from cars_REST_API.cars_app.models import CarBrand, CarModel, UserCar


class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarBrand
        fields = ('brand_name', )

    def create(self, validated_data):
        return CarBrand.objects.create(brand_name=validated_data['brand_name'])


class CarModelSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField()

    class Meta:
        model = CarModel
        exclude = ('is_deleted', "deleted")


class UserCarSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField()
    model = serializers.StringRelatedField()

    class Meta:
        model = UserCar
        exclude = ('is_deleted', 'deleted')

