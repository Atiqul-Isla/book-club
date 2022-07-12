"""
ASGI config for board project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
## Importing the ProtocolTypeRouter function
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import backend.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'board.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            backend.routing.websocket_urlpatterns
        )
    )
})
