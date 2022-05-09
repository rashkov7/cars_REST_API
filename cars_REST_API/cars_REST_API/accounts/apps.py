from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars_REST_API.accounts'

    def ready(self):
        from . import signals
