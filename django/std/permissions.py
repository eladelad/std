from rest_framework import permissions
from views.core import isPermittedToEdit

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

class IsTheUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

class IsVerified(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.isVerify

class IsOwnerOrNullObj(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if obj.user is None:
           return True
        return obj.user == request.user or request.user.is_staff

class IsNullObj(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if obj.user is None:
           return True

class IsSharedWithUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        if obj.user is None:
            return True
        if obj.board.permittedUsers is not None:
            permittedUsers = obj.board.permittedUsers.split()
            if unicode(request.user.id) in permittedUsers:
                return True
        return request.user.is_staff

class IsEditOK(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return isPermittedToEdit(obj.board, request.user)