from django.apps import AppConfig
from django.db import OperationalError


class AdvisingAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "advising_app"

    def ready(self):
        import advising_app.signals