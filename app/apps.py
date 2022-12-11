from django.apps import AppConfig


class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'

class ChatConfig(AppConfig):
    name = 'chat'
    
class appConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

