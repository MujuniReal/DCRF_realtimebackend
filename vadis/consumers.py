from django.contrib.auth.models import User
from .models import Vadis
from .api.serializers import *
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
#from asgiref.sync import async_to_sync

class LiveConsumer(mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.PatchModelMixin,
        mixins.UpdateModelMixin,
        mixins.CreateModelMixin,
        mixins.DeleteModelMixin,
        GenericAsyncAPIConsumer,):
        
    queryset = Vadis.objects.all()
    serializer_class = VadisSerializer
    permission_classes = (permissions.AllowAny,)


    @model_observer(Vadis)
    async def vadis_activity(self, message, observer=None, subscribing_request_ids=[], **kwargs):
        print(kwargs)
        #for co in dir(observer): print(co)
        for request_id in subscribing_request_ids:
            await self.send_json({"message": message, "request_id": request_id})

    @vadis_activity.serializer
    def vadis_activity(self, instance: Vadis, action, **kwargs):
        return VadisSerializer(instance).data

    @action()
    async def subscribe_to_vadis_activity(self, request_id, **kwargs):
        await self.vadis_activity.subscribe(request_id=request_id)

class AnotherCOnsumer(AsyncAPIConsumer):

    @model_observer(Vadis)
    async def model_activity_handler(
        self,
        message,
        observer=None,
        action=None,
        subscribing_request_ids=[],
        **kwargs
    ):
        for request_id in subscribing_request_ids:
            await self.send_json(dict(body=message, action=action, request_id=request_id))

#    def connect(self,):
#        self.room_group_name = 'test'


#        async_to_sync(self.channel_layer.group_add)(
#            self.room_group_name,
#            self.channel_name
#        )

#        self.accept()

    
    @action()
    async def an_async_action(self, some=None, **kwargs):
        # do something async
        return {'response_with': 'some message'}, 200