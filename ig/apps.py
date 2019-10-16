from django.apps import AppConfig


class IgConfig(AppConfig):
    name = 'ig'
    def ready(self):
        print('signal is ready')
        import ig.signals
