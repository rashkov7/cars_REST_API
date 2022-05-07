from django.contrib import admin

# Register your models here.
from cars_REST_API.cars_app.models import CarBrand, CarModel, UserCar


@admin.register(CarBrand)
class AdminCarBrand(admin.ModelAdmin):
    pass


@admin.register(CarModel)
class AdminCarBrand(admin.ModelAdmin):
    pass


@admin.register(UserCar)
class AdminCarBrand(admin.ModelAdmin):
    pass
