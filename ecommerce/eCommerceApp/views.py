from rest_framework import viewsets, generics, permissions, decorators, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializer
from .models import Category, Product, User, Shop, CartDetail
from .perms import StaffPermissions, AdminPermissions, OwnerPermissions, UserPermissions
from .utils import confirm_status_update, user_update


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

    @action(methods=['post'], detail=True, url_path='add-cart', url_name='add-cart')
    def add_cart(self, request, pk):
        user = request.user
        product = Product.objects.get(pk=pk)
        cart = user.carts.filter(product_id=pk).first()
        if cart:
            cart.quantity += 1
            cart.total_price = int(cart.quantity * cart.product.price)
            cart.save()
        else:
            new_cart = CartDetail(quantity=1, total_price=product.price, user=request.user,
                                  product=product)
            new_cart.save()

        list_product = user.carts.all()
        return Response(serializer.CartDetailSerializer(list_product, many=True).data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializer.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action in ['current_user', 'create_shop']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_name='current-user', url_path='current-user')
    def current_user(self, request):
        return Response(serializer.UserSerializer(request.user).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_name='create-shop', url_path='create-shop')
    def create_shop(self, request):
        try:
            shop = Shop.objects.create(name=request.data.get('name'), logo=request.data.get('logo'),
                                       user_id=request.user.id)
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
        elif self.action in ['add_product']:
            return [UserPermissions()]

        return [permissions.AllowAny()]

    @action(methods=['put'], url_path='confirm', detail=True)
    def confirm(self, request, pk):
        try:
            shop = Shop.objects.get(pk=pk)
            user_update(shop.user)
            shop_update = confirm_status_update(shop)
            return Response(serializer.ShopSerializer(shop_update).data)
        except Shop.DoesNotExist:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['post'], detail=True, url_path='add-product', url_name='add-product')
    def add_product(self, request, pk):
        try:
            p = Product.objects.create(name=request.data.get('name'), price=request.data.get('price'),
                                       description=request.data.get('description'), image=request.data.get('image'),
                                       category_id=request.data.get('category_id'), shop_id=self.get_object().id)
            print(request.user)
            p.save()
            return Response(serializer.ProductSerializer(p).data, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


