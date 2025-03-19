# Importa as configurações do Django (para acessar o modelo de usuário) e os módulos necessários.
from django.conf import settings
from django.db import models
from django.urls import reverse

# Define o modelo Article, que representa um artigo no blog ou site.
class Article(models.Model):
    # O título do artigo, limitado a 255 caracteres.
    title = models.CharField(max_length=255)
    
    # O corpo do artigo, que pode ter texto de qualquer tamanho.
    body = models.TextField()
    
    # A data de criação do artigo, que é automaticamente preenchida com a data e hora atual.
    date = models.DateTimeField(auto_now_add=True)
    
    # O autor do artigo, que é uma chave estrangeira para o modelo de usuário (AUTH_USER_MODEL).
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usa o modelo de usuário configurado no settings (pode ser CustomUser).
        on_delete=models.CASCADE,  # Caso o usuário seja excluído, todos os artigos dele também são excluídos.
    )

    # Método que retorna o título do artigo quando o objeto é convertido para string.
    def __str__(self):
        return self.title

    # Método que retorna a URL absoluta para visualizar o artigo. Usado no `get_absolute_url()`.
    def get_absolute_url(self):
        # Retorna a URL de detalhes do artigo com base no seu ID (pk).
        return reverse("article_detail", kwargs={"pk": self.pk})
    

# Define o modelo Comment, que representa um comentário feito em um artigo.
class Comment(models.Model):  # novo
    # O artigo ao qual o comentário pertence (chave estrangeira para Article).
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    # O texto do comentário, com limite de 140 caracteres.
    comment = models.CharField(max_length=140)
    
    # O autor do comentário, que é uma chave estrangeira para o modelo de usuário (AUTH_USER_MODEL).
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usa o modelo de usuário configurado no settings (pode ser CustomUser).
        on_delete=models.CASCADE,  # Caso o usuário seja excluído, todos os comentários dele também são excluídos.
    )

    # Método que retorna o comentário quando o objeto é convertido para string.
    def __str__(self):
        return self.comment

    # Método que retorna a URL absoluta para a lista de artigos. Usado no `get_absolute_url()`.
    def get_absolute_url(self):
        # Retorna a URL de listagem de artigos.
        return reverse("article_list")
