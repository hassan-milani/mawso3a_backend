from rest_framework.permissions import BasePermission
from accounts.models import UserProfile

class HasRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        
        if not request.user.is_authenticated:
            return False
        
        try:
            profile = request.user.profiles.get()
        except UserProfile.DoesNotExist:
            return False
        
        required_roles = getattr(view, 'required_roles', None)

        if required_roles:
            if isinstance(required_roles, (list, tuple)):
                return any(profile.has_role(role) for role in required_roles)
            else:
                return profile.has_role(required_roles)

        return False
