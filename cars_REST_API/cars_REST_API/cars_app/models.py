import datetime

from django.db import models
from django.db.models import Manager

from cars_REST_API.cars_app.managers import SoftDeleteManager, CarModelsManager


class SoftDelete(models.Model):

    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = Manager()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted = datetime.datetime.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted = None
        self.save()

    class Meta:
        abstract = True


class SoftDeleteCarModelUserCar(SoftDelete):

    class Meta:
        abstract = True


class CreatedAndDeletedFields(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class CarBrand(CreatedAndDeletedFields, SoftDelete):


    brand_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.brand_name}'


class CarModel(CreatedAndDeletedFields, SoftDeleteCarModelUserCar):

    model_name = models.CharField(max_length=30)

    objects = CarModelsManager()
    all_objects = Manager()

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model_name}'


class UserCar(CreatedAndDeletedFields, SoftDeleteCarModelUserCar):

    first_registration = models.DateTimeField(auto_now_add=True)
    odometer = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    objects = CarModelsManager()
    all_objects = Manager()

    def __str__(self):
        return f'{self.brand} - {self.model}'
