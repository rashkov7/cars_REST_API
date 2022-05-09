from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver
from rest_framework.generics import get_object_or_404

from cars_REST_API.accounts.models import ProfileModel

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(
            first_name="Anonymous",
            last_name="Anonymous",
            age=0,
            user=instance,
        )
