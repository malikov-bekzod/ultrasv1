from rest_framework import serializers

from django.contrib.auth.models import User
from blog.models import Blog
from review.models import Review
from shop.models import Category,Brands,Product,Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"] 


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "text", "author", "image", "topic", "created_date"]


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    blog = BlogSerializer(read_only=True) 

    class Meta:
        model = Review
        fields = ["id", "author", "blog", "text", "created_date"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_date"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "color",
            "size",
            "price",
            "category",
            "brand",
            "count",
            "types",
            "image",
            "gender",
            "viewed",
            "created_date",
        ]


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ["id", "product", "user", "created_date"]
