from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.users'
    verbose_name = _('Users')