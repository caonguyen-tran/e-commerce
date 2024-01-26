from django.urls import path, include
from . import views
from .admin import admin_site

from rest_framework import routers

router = routers.DefaultRouter()

router.register('categories', views.CategoryViewSet, basename='categories')
router.register('product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls)
]
