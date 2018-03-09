from django.apps import AppConfig


class MylinksConfig(AppConfig):
    name = 'mylinks'

    def ready(self):
        import mylinks.signals