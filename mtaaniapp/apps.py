from django.apps import AppConfig


class MtaaniappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mtaaniapp'

    def ready(self):
        import mtaaniapp.signals