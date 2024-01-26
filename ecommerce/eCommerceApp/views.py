from rest_framework import viewsets, generics, permissions, decorators, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializer
from .models import Category, Product, User, Shop
from .perms import StaffPermissions, AdminPermissions, OwnerPermissions


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer


class ProductViewSet(viewsets.ViewSet, generics.ListAPIView, generics.DestroyAPIView, generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializer.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action in ['current-user', 'create-shop']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_name='current-user', url_path='current-user')
    def current_user(self, request):
        return Response(serializer.UserSerializer(request.user).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_name='create-shop', url_path='create-shop')
    def create_shop(self, request, pk):
        try:
            shop = Shop.objects.create(name=request.data.get('name'), logo=request.data.get('logo'), user_id=pk)
            shop.save()
            return Response(serializer.ShopSerializer(shop).data, status=status.HTTP_201_CREATED)
        except Shop.DoesNotExist:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


class ShopViewSet(viewsets.ViewSet, generics.ListAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = serializer.ShopSerializer

    def get_permissions(self):
        if self.action in ['confirm']:
            return [StaffPermissions()]

        elif self.action in ['add-product']:
            return [OwnerPermissions()]

        return [permissions.AllowAny()]

    @action(methods=['put'], url_path='confirm', detail=True)
    def confirm(self, request, pk):
        try:
            shop = Shop.objects.get(pk=pk)
            shop.confirm_status = True
            shop.save()
            return Response(serializer.ShopSerializer(shop).data)
        except Shop.DoesNotExist:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['post'], detail=True, url_path='add-product', url_name='add-product')
    def add_product(self, request, pk):
        try:
            p = Product.objects.create(name=request.data.get('name'), price=request.data.get('price'),
                                       description=request.data.get('description'), image=request.data.get('image'),
                                       category_id=request.data.get('category'), shop_id=pk)
            p.save()
            return Response(serializer.ProductSerializer(p).data, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
