from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, filters, pagination
from rest_framework.decorators import action
from django.contrib.auth.models import User
from blog.models import Blog
from review.models import Review
from shop.models import Category, Brands, Product, Order
from .serializers import (
    UserSerializer,
    BlogSerializer,
    ReviewSerializer,
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    OrderSerializer,
)

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["username"]
    pagination_class = LimitOffsetPagination


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "text"]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["get"])
    def recent_posts(self, request, pk=None):
        blog = self.get_object()
        recent_posts = blog.posts.order_by("-created_date")[:5]
        serializer = self.get_serializer(recent_posts, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["text"]
    pagination_class = LimitOffsetPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]
    pagination_class = LimitOffsetPagination


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["product__name", "user__username"]
    pagination_class = LimitOffsetPagination
