# Importa o módulo de formulários do Django e o modelo Comment da aplicação.
from django import forms
from .models import Comment

# Define um formulário para o modelo Comment usando ModelForm.
class CommentForm(forms.ModelForm):
    # A classe Meta é usada para fornecer informações sobre o modelo e os campos do formulário.
    class Meta:
        # Especifica que o modelo utilizado é o Comment.
        model = Comment
        # Define quais campos do modelo Comment serão incluídos no formulário.
        fields = ("comment", "author")  # 'comment' e 'author' são os campos do modelo que aparecerão no formulário.
