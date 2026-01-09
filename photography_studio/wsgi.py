"""
WSGI config for photography_studio project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photography_studio.settings')

application = get_wsgi_application()
