from django.urls import path
from .views import ShopView,ShopDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView
urlpatterns = [
    path("", ShopView.as_view(), name="shop"),
    path("<int:id>/", ShopDetailView.as_view(), name="shop-detail"),
    path("create/", ProductCreateView.as_view(), name="shop-create"),
    path("update/<int:id>/", ProductUpdateView.as_view(), name="shop-update"),
    path("delete/<int:id>/", ProductDeleteView.as_view(), name="shop-delete"),
]
