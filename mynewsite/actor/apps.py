from django.apps import AppConfig


class ActorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'actor'
    verbose_name = 'Актеры'

    def ready(self) -> None:
        import actor.signals
