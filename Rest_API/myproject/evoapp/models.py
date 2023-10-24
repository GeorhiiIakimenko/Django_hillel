# Імпортуємо моделі з Django
from django.db import models


# Модель користувача
class User(models.Model):
    username = models.CharField(max_length=150)  # Ім'я користувача
    password = models.CharField(max_length=100)  # Пароль
    last_activity = models.DateTimeField(null=True, blank=True)  # Остання активність


# Модель поста
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор поста
    content = models.TextField()  # Зміст поста
    likes = models.ManyToManyField(User, related_name='liked_posts')  # Лайки
    timestamp = models.DateField(auto_now_add=True)  # Час створення