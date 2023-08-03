from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.permissions import revoke_permission, grant_permission
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

# has_role_decorator  # Permite acesso pela função
# @has_permission_decorator('ver_metas')  # Permite acesso pela permissão
def home(request):

    # revoke_permission(request.user, 'ver_metas')  # Revoga permissão
    # grant_permission(request.user, 'ver_metas')  # Dá permissão
    # print(get_user_roles(request.user))  # Mostra a lista de categorias que o usuário possui.

    # return HttpResponse('Estou na home!')

    return render(request, 'home.html')


def criar_usuario(request):
    user = User.objects.create_user(username="caio", password="1234")
    user.save()
    assign_role(user, 'gerente')
    return HttpResponse('Usuário salvo com sucesso!')
