from django.core.exceptions import PermissionDenied


class CreatedByCurrentUserMixin:
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.created_by == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
