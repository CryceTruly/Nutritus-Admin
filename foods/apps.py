from django.apps import AppConfig


class FoodsConfig(AppConfig):
    name = 'foods'

    def ready(self):
        import users.signals
