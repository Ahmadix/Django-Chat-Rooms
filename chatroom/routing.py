# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
  re_path(r'ws/chatrooms/(?P<roomname>\w+)/$', consumers.ChatConsumer),
  re_path(r'wss/chatrooms/(?P<roomname>\w+)/$', consumers.ChatConsumer),
]
