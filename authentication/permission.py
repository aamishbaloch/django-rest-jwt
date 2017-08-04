from rest_framework import permissions


class UserAccessPermission(permissions.BasePermission):
    message = 'No permission for accessing this view.'

    def has_permission(self, request, view):
        return request.user.is_active