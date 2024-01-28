from django.urls import path, include
from . import views
from .admin import admin_site

from rest_framework import routers

router = routers.DefaultRouter()

router.register('categories', views.CategoryViewSet, basename='categories')
router.register('product', views.ProductViewSet, basename='product')
router.register('user', views.UserViewSet, basename='user')
router.register('shop', views.ShopViewSet, basename='shop')
router.register('cart', views.CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls)
]
