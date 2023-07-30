from rest_framework import serializers
from .models import Tag, Goods, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name', 'uuid']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id','name', 'description', 'company', 'price', 'active', 'review', 'sale', 'category', 'tags',]


class CategorySerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id','name', 'description','goods']

