"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Run migrations automatically
try:
    call_command('migrate', interactive=False)
    call_command('collectstatic', interactive=False, clear=True)
except Exception as e:
    print("Auto-deploy migration/static error:", e)


application = get_wsgi_application()
