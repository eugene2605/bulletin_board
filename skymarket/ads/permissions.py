from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsAdmin(BasePermission):
    message = "Вы не являетесь администратором"

    def has_permission(self, request, view):
        return request.user.role == 'admin'
