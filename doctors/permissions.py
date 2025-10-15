from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    '''
    Permiso personalizado para verificar si el usuario es un doctor.
    * Métodos:
        - has_permission: Verifica si el usuario tiene permiso para acceder a la vista.
    '''

    def has_permission(self, request, view) -> bool:
        '''
        Verifica si el usuario tiene permiso para acceder a la vista.
        * Parámetros:
        -   request: Objeto de solicitud HTTP.
        -   view: Vista a la que se intenta acceder.
        * Retorna:
        -   bool: True si el usuario es un doctor, False en caso contrario.
        '''
        # Permitir acceso solo a usuarios autenticados que sean doctores
        return request.user.groups.filter(name='doctors').exists()