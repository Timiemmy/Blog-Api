from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # This permission will only give the authenticated person to see the api list
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Here, others can still see and Get the details of API
        if request.method in permissions.SAFE_METHODS:
            return True

        # Here only author can update or post an api
        return obj.author == request.user