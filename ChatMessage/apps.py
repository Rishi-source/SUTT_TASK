from django.apps import AppConfig


class ChatmessageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ChatMessage'

    def ready(self):
        import ChatMessage.signals  
class MyAppConfig(AppConfig):

     default_app_config = 'myapp.apps.MyAppConfig' 
