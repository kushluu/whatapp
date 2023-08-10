from django.urls import path
from . import consumers

websockets_urlpatterns = [
    path('ws/sc/', consumers.MySysncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsysncConsumer.as_asgi()),
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]

# routing.py

# from django.urls import path
# from .consumers import MyWebSocketConsumer

# websocket_urlpatterns = [
#     path('ws/some_endpoint/', MyWebSocketConsumer.as_asgi()),
# ]
