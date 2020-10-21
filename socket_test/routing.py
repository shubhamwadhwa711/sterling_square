from django.urls import re_path

from socket_test import consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumer.ChatConsumer),
]