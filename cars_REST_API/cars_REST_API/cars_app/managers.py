from django.db.models import Manager

# from cars_REST_API.cars_app.models import CarModel


class SoftDeleteManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class CarModelsManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(brand__is_deleted=False)