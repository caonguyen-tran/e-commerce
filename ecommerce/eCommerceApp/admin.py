from .models import User, Shop, CartDetail, Order, OrderDetail, Comment, Rating, Product, ReviewShop, \
    ReviewProduct, Category, Pay
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib import admin


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'STATISTIC VIEW'

    def get_urls(self):
        return [
                   path('stats-views/', self.stats_view)
               ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html', {
            'stats': "Test"
        })


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'date_joined', 'is_active']
    search_fields = ['first_name', 'last_name']
    list_filter = ['id', 'first_name']


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_created', 'logo', 'confirm_status', 'user']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'price', 'shop']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date', 'updated_date', 'active', 'content', 'parent_cmt', 'user']


class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date', 'updated_date', 'active', 'rate']
    list_filter = ['id']


class ReviewShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'rating', 'shop']


class ReviewProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'rating', 'product']


class CartDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'total_price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_date', 'address', 'total_price']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity', 'total_price']


class PayAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']


admin_site = CourseAppAdminSite(name='eCommerceApp')

admin_site.register(User, UserAdmin)
admin_site.register(Shop, ShopAdmin)
admin_site.register(Product, ProductAdmin)
admin_site.register(Comment, CommentAdmin)
admin_site.register(Rating, RateAdmin)
admin_site.register(ReviewShop, ReviewShopAdmin)
admin_site.register(CartDetail, CartDetailAdmin)
admin_site.register(Order, OrderAdmin)
admin_site.register(OrderDetail, OrderDetailAdmin)
admin_site.register(ReviewProduct, ReviewProductAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Pay, PayAdmin)
