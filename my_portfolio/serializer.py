from rest_framework import serializers
from .models import ContactModel, Post

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactModel
        fields= '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
