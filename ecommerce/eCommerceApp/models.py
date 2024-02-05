from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='user/%Y/%m', default="user/2024/02/avatardefault.jpg")
    is_admin = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)


class Shop(models.Model):
    name = models.CharField(max_length=200, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, null=True)
    logo = models.ImageField(upload_to="shop_logo/%Y/%m", default="shop_logo/2024/02/shoplogo1.jpg")
    confirm_status = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name='shop')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to="product/%Y/%m")
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")

    def __str__(self):
        return self.name


class Interaction(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True


class Comment(Interaction):
    content = models.TextField()
    parent_cmt = models.ForeignKey("Comment", null=True, blank=True, related_name="replies", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " " + self.content


class Rating(Interaction):
    rate = models.SmallIntegerField(default=5)

    def __str__(self):
        return self.rate


class ReviewShop(models.Model):
    shop = models.ForeignKey(Shop, null=False, on_delete=models.CASCADE)
    comment = models.OneToOneField(Comment, null=True, on_delete=models.CASCADE, blank=True)
    rating = models.OneToOneField('Rating', null=False, on_delete=models.CASCADE)


class ReviewProduct(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    comment = models.OneToOneField(Comment, null=True, on_delete=models.CASCADE, blank=True)
    rating = models.OneToOneField('Rating', null=False, on_delete=models.CASCADE)


class CartDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='carts')


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    total_price = models.IntegerField()
    pay = models.ForeignKey('Pay', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')

    class Meta:
        ordering = ['id']


class OrderDetail(models.Model):
    quantity = models.IntegerField(default=0)
    total_price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['order']


class Pay(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to="pay/%Y/%m", default="pay/2024/02/pay_default.jpg", null=False)
