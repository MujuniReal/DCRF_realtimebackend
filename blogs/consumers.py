from .models import BlogPost
from .api.serializers import *
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework import mixins

#from asgiref.sync import async_to_sync

class BlogConsumer(mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.PatchModelMixin,
        mixins.UpdateModelMixin,
        mixins.CreateModelMixin,
        mixins.DeleteModelMixin,
        GenericAsyncAPIConsumer,):
        
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.AllowAny,)