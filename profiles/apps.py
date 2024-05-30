from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles app.
    This class represents the configuration for the profiles app,
    specifying the default auto field and the name of the app.
    Attr:
        default_auto_field (str): The name of the default auto field for models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

