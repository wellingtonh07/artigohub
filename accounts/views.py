# Importa a função reverse_lazy, que resolve URLs de maneira preguiçosa (não executa até ser realmente necessário)
from django.urls import reverse_lazy
# Importa a classe CreateView, que é uma view baseada em classe para criar objetos no banco de dados
from django.views.generic import CreateView
# Importa o formulário CustomUserCreationForm, que é utilizado para a criação de usuários personalizados
from .forms import CustomUserCreationForm

# Define a view para o cadastro de novos usuários
class SignUpView(CreateView):
    # Define o formulário que será usado para criar o novo usuário
    form_class = CustomUserCreationForm
    # Define a URL para onde o usuário será redirecionado após um cadastro bem-sucedido
    success_url = reverse_lazy('login')
    # Define o template que será usado para renderizar a página de cadastro
    template_name = "registration/signup.html"
