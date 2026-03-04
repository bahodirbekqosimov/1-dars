from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.core.handlers.wsgi import WSGIRequest


class CustomPermissons(BasePermission):
    def has_permission(self, request:WSGIRequest, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user.is_authenticated
    

class AllowStaff(BasePermission):
    def has_permission(self, request:WSGIRequest, view):
        if request.user.is_authenticated and request.user.is_staff:
            return True
        return False
            