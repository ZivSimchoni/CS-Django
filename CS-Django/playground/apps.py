from django.apps import AppConfig

# class name must be the same as the app name
# configures the app
class PlaygroundConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "playground"
