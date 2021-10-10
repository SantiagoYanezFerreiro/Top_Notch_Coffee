"""
WSGI config for top_notch_coffee project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'top_notch_coffee.settings')

application = get_wsgi_application()
