from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyAuthorEditNote(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # если хотим читать, то всё ок
            return True

        return request.user == obj.author