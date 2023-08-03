from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    available_permissions = {'criar_metas': True, 'ver_metas': True}


class Vendedor(AbstractUserRole):
    available_permissions = {'acessar_produtos': True, 'ver_metas': True}
    