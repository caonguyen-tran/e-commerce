from rest_framework.permissions import IsAuthenticated


# class OwnerShopPermissions(IsAuthenticated):
#
#     def has_object_permission(self, request, view, obj):
#         return self.has_permission(request, view) and request.user == obj.user

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
