"""
ASGI config for photography_studio project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photography_studio.settings')

application = get_asgi_application()
