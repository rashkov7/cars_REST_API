from django.db.models import Manager


class SoftDeleteManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteFKManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(brand__is_deleted=False)