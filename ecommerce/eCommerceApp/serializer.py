import cloudinary.api
from rest_framework import serializers
from .models import Category, Product, Shop, User
from cloudinary import CloudinaryResource


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ShopSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, obj):
        return "{}{}".format("https://res.cloudinary.com/dndakokcz/", obj.logo)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'date_created', 'logo', 'confirm_status', 'user']


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = CategorySerializer()

    def get_image(self, obj):
        return "{}{}".format("https://res.cloudinary.com/dndakokcz/", obj.image)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'shop', 'category']


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        if obj.avatar:
            return "{}{}".format("https://res.cloudinary.com/dndakokcz/", obj.avatar)

    class Meta:
        model = User
        fields = ["__all__"]
