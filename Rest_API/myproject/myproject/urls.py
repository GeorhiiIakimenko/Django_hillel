# Налаштування маршрутізації
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from evoapp.views import UserViewSet, PostViewSet, SignupView, likes_analytics

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("analytics/", likes_analytics, name='likes-analytics'),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', obtain_auth_token, name='login'),
]