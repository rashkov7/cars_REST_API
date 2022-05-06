from django.db import models


class CarBrand(models.Model):
    brand_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class CarModel(models.Model):
    model_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)


class UserCar(models.Model):
    first_registration = models.DateTimeField(auto_now_add=True)
    odometer = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)