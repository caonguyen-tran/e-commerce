from rest_framework.permissions import IsAuthenticated


class ShopConfirmPermissions(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and \
               (request.user.id == obj.user.id) and request.user.is_seller and obj.confirm_status


class UserPermissions(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and request.user.id == obj.user.id


class OwnerPermissions(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and request.user == obj.user


class AdminPermissions(IsAuthenticated):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_admin


class StaffPermissions(IsAuthenticated):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_employee


class ProductOwnerPermissions(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and request.user.id == obj.shop.user.id
