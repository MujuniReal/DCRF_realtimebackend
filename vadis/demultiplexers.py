from channelsmultiplexer import AsyncJsonWebsocketDemultiplexer
from .consumers import LiveConsumer,AnotherCOnsumer
from blogs.consumers import BlogConsumer
class EchoDemultiplexerAsyncJson(AsyncJsonWebsocketDemultiplexer):
    applications = {
        'vadisliveconsumer': LiveConsumer.as_asgi(),
        'blogconsume' : BlogConsumer.as_asgi(),
        'anotherblog' : AnotherCOnsumer.as_asgi(),
        # "echostream": EchoTestConsumer.as_asgi(),
        # "altechostream": AltEchoTestConsumer.as_asgi(),
        # "closeafterfirst": EchoCloseAfterFirstTestConsumer.as_asgi(),
        # "neveraccept": NeverAcceptTestConsumer.as_asgi()
    }