from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from instagram.models import Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']




class PostSerializer(ModelSerializer):
    # username = serializers.ReadOnlyField(source='author.username')
    # author_email = serializers.ReadOnlyField(source='author.email')
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            'pk',
            'author',
            # 'username',
            # 'author_email',
            'message',
            'created_at',
            'update_at',
        ]
