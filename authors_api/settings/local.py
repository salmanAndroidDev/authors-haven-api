from email.policy import default
from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="ASDFHGRTYSDFGK2SD32FK23GSDL5FKG23LK5SDFG2KLK3SD3F3G3")
ALLOWED_HOSTS = ["localhost", '0.0.0.0', '127.0.0.1']
