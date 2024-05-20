from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    BlogViewSet,
    ReviewViewSet,
    CategoryViewSet,
    BrandViewSet,
    ProductViewSet,
    OrderViewSet,
)

router = DefaultRouter()
router.register(prefix="users", viewset=UserViewSet, basename="users")
router.register(prefix="blogs", viewset=BlogViewSet, basename="blogs")
router.register(prefix="reviews", viewset=ReviewViewSet, basename="reviews")
router.register(prefix="categories", viewset=CategoryViewSet, basename="categories")
router.register(prefix="brands", viewset=BrandViewSet, basename="brands")
router.register(prefix="products", viewset=ProductViewSet, basename="products")
router.register(prefix="orders", viewset=OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
]
