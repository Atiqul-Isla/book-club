from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/socket-server/(?P<pk>\w+)/$', consumers.ChatConsumer.as_asgi())
]