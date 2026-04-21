from rest_framework import permissions


class Authoor(permissions.BasePermission):
    def premissionn(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user