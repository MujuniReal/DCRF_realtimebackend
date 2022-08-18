"""
ASGI config for channelsProj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import vadis.routing
from django.conf.urls import url
from vadis.consumers import LiveConsumer,AnotherCOnsumer
from blogs.consumers import BlogConsumer
from vadis.demultiplexers import AsyncJsonWebsocketDemultiplexer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelsProj.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": 
        URLRouter([
            url(r'ws/$', AsyncJsonWebsocketDemultiplexer.as_asgi(
                vadisliveconsumer = LiveConsumer.as_asgi(),
                blogconsume = BlogConsumer.as_asgi(),
                anotherblog = AnotherCOnsumer.as_asgi(),
            )),
        ]),
    
})
