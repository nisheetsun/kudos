from rest_framework import permissions

def can_access_blog(request, obj):
    for author in obj.author.all():
        if author.parent_user.id == request.user.id:
            return True
    return False

class BlogPermission(permissions.BasePermission):
    message = "You don't have permission"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if view.action == "list":
            if request.query_params.get('filter') == 'draft' or request.query_params.get('filter') == 'waiting':
                return request.user.is_authenticated
            return True
        if view.action == "publish":
            return request.user.is_staff
        if view.action == "create_blog":
            return request.user.is_authenticated
        if request.method in permissions.SAFE_METHODS or view.action == "give_kudos":
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if view.action == "partial_update" or view.action == "edit_post" or view.action == "destroy" or view.action == "unpublish":
            return can_access_blog(request, obj)
        if view.action == "publish":
            return not obj.is_private

        return True