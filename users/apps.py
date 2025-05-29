from django.apps import AppConfig


class UsersConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
        # This ensures that the signals are imported when the app is ready.
        # The signals module contains the logic for creating and saving user profiles.
        # This is necessary to ensure that the Profile model is created when a User instance is created.
        # The import is done here to avoid circular imports.        
