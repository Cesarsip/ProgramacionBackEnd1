from rest_framework.permissions import SAFE_METHODS, BasePermission


class ReadOnlyOrAuthenticated(BasePermission):
    """Permite GET/HEAD/OPTIONS públicos y exige JWT para modificar datos."""

    def has_permission(self, request, view):
        # SAFE_METHODS no cambia datos. Las demás operaciones requieren un
        # usuario autenticado; si se elimina esta condición cualquiera podría
        # crear, editar o borrar asignaciones.
        return request.method in SAFE_METHODS or bool(request.user and request.user.is_authenticated)
