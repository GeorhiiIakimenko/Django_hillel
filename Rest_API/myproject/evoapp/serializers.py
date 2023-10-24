# Імпортуємо необхідні бібліотеки для серіалізатора
from rest_framework import serializers
from .models import User, Post


# Серіалізатор для користувача
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_activity']


# Серіалізатор для поста
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'likes']
