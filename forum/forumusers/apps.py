from django.apps import AppConfig


class ForumusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forumusers'

    def ready(self):
        import forumusers.signals 