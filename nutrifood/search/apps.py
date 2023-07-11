from django.apps import AppConfig


class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'
    
    def ready(self):
        from .management.commands import maj_bdd_opfofa
