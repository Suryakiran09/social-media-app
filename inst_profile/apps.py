from django.apps import AppConfig


class InstProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inst_profile'
    
    def ready(self):
        import inst_profile.signals