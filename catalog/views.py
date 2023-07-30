from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TagSerializer, GoodsSerializer, CategorySerializer
from .models import Tag, Goods, Category
from rest_framework.permissions import IsAuthenticated


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



