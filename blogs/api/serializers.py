from rest_framework import serializers
from blogs.models import BlogPost


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"