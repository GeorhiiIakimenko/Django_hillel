# Імпортуємо необхідні бібліотеки для API
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from django.db.models import Count
from django.http import JsonResponse
from django.db.models.functions import TruncDate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


# Функція для отримання статистики по лайкам
def likes_analytics(request):
    likes_by_day = (Post.objects.annotate(date=TruncDate('timestamp'))
                    .values('date')
                    .annotate(total_likes=Count('likes__id'))
                    .order_by('date'))

    results = [{'date': item['date'], 'total_likes': item['total_likes']} for item in likes_by_day]

    return JsonResponse({'analytics': results})


# Налаштування API для користувачів
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Налаштування API для постів
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Функція для лайку поста
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post.likes.add(user)
        return Response({'message': 'Liked'})

    # Функція для видалення лайка
    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post.likes.remove(user)
        return Response({'message': 'Unliked'})


# Налаштування реєстрації користувача
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=201)
        else:
            return Response(serializer.errors, status=400)
