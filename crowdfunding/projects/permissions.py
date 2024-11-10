from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
   def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
           return True
       return obj.owner == request.user
   

class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the pledge supporter can modify or delete the pledge
        return obj.supporter == request.user