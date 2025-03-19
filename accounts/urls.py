# Importa o módulo 'path' para definir rotas de URL no Django
from django.urls import path
# Importa a view 'SignUpView' que será usada para a página de cadastro de novos usuários
from .views import SignUpView
# Importa views de autenticação padrão do Django, como Login, Logout, etc.
from django.contrib.auth import views as auth_views

# Define as URLs da aplicação
urlpatterns = [
    # URL para a página de cadastro, que usa a view SignUpView
    path("signup/", SignUpView.as_view(), name="signup"),
    # URL para fazer logout do usuário, usando a view padrão LogoutView do Django
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # URL para logout
]
