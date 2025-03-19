# Importa as classes padrão de criação e alteração de usuário do Django
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Importa o modelo CustomUser que foi criado no projeto
from .models import CustomUser


# Define um formulário para criar um novo usuário personalizado
class CustomUserCreationForm(UserCreationForm):
    # Configura o modelo e os campos que serão usados no formulário
    class Meta(UserCreationForm):
        # Define que o modelo utilizado será o CustomUser (modelo personalizado)
        model = CustomUser
        # Define os campos que serão incluídos no formulário de criação de usuário
        fields = (
            "username",  # Nome de usuário
            "email",     # Email do usuário
            "age",       # Idade do usuário (campo adicional personalizado)
        )


# Define um formulário para alterar os dados de um usuário personalizado
class CustomUserChangeForm(UserChangeForm):
    # Configura o modelo e os campos que serão usados no formulário
    class Meta:
        # Define que o modelo utilizado será o CustomUser (modelo personalizado)
        model = CustomUser
        # Define os campos que serão incluídos no formulário de alteração de usuário
        fields = (
            "username",  # Nome de usuário
            "email",     # Email do usuário
            "age",       # Idade do usuário (campo adicional personalizado)
        )
