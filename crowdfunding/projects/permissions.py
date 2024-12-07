from rest_framework import permissions
#from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(permissions.BasePermission):
   def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
           return True
       return obj.owner == request.user
   

class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for any user
        #if request.method in permissions.SAFE_METHODS:
            #return True
        # Only the pledge supporter can modify or delete the pledge
        #return obj.supporter == request.user
    
         # Allow read-only access for everyone
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Write access is allowed only for the supporter
        return obj.supporter == request.user