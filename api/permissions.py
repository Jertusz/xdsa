from rest_framework import permissions


class StaffReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS and request.user.groups.filter(name='staff').exists():
            return True
        return False


class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='staff').exists():
            return True
        return False


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='user').exists() and request.user.id == obj.id:
            return True
        return False


class StaffOrUserReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='user').exists() and request.user.id == obj.user.id or request.user.groups.filter(name='staff').exists():
            if request.method in permissions.SAFE_METHODS:
                return True
        return False


class UserOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='user').exists() and request.user.id == obj.id and request.method in permissions.SAFE_METHODS:
            print('here')
            return True
        return False


class IsAdminOrUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='user').exists() and request.user.id == obj.id or request.user.is_superuser:
            print('here')
            return True
        print('there')
        return False

    def has_permission(self, request, view):
        if request.user.groups.filter(name='staff').exists():
            return False

        return True


class IsNotUserAdminStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='staff').exists or request.user.groups.filter(name='user').exists or request.user.is_superuser:
            return False
        return True
