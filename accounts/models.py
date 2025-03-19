# Importa o modelo AbstractUser do Django, que fornece funcionalidades básicas para autenticação
from django.contrib.auth.models import AbstractUser
# Importa a classe models do Django, que é usada para definir campos e modelos de banco de dados
from django.db import models

# Define um modelo CustomUser que herda de AbstractUser
class CustomUser(AbstractUser):
    # Adiciona um campo personalizado para armazenar a idade do usuário
    age = models.PositiveIntegerField(null=True, blank=True)
    # 'PositiveIntegerField' garante que a idade seja um número inteiro positivo
    # 'null=True' permite que o campo seja nulo no banco de dados
    # 'blank=True' permite que o campo fique em branco ao preencher o formulário (não obrigatório)
