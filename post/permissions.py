from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request,obj):
        return obj.author == request.user or request.user.is_staff

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request,obj):
        return obj.author == request.user

