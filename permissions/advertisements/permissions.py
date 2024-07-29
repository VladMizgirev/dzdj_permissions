from rest_framework.permissions import BasePermission


class IsOvnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'Get':
            return True
        return request.user == obj.user
