from djangochannelsrestframework.consumers import view_as_consumer
from django.urls import re_path,path
from .consumers import AnotherCOnsumer, LiveConsumer


websocket_urlpatterns = [
    path("ws/", LiveConsumer.as_asgi()),
]