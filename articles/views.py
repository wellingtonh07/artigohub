# Importações necessárias para as views, mixins e outras funcionalidades
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Mixins de autenticação e permissão de acesso
from django.views.generic import ListView, DetailView, FormView  # Atualizado com FormView
from django.views.generic.detail import SingleObjectMixin  # Usado para pegar o objeto da view
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # Views para criar, editar e excluir
from django.urls import reverse_lazy, reverse  # Funções para redirecionar e gerar URLs
from .forms import CommentForm  # Formulário de comentários
from .models import Article  # Modelo de artigos
from django.shortcuts import render, redirect  # Funções auxiliares de renderização e redirecionamento
from django.views import View  # Classe base para views

# --- Views para o artigo ---

class ArticleListView(LoginRequiredMixin, ListView):
    # Exibe a lista de artigos
    model = Article  # O modelo usado será o 'Article'
    template_name = "article_list.html"  # Template associado a esta view

    # LoginRequiredMixin: Garante que o usuário precise estar autenticado para acessar essa view.

class ArticleDetailView(LoginRequiredMixin, DetailView):
    # Exibe os detalhes de um artigo
    model = Article  # O modelo usado será o 'Article'
    template_name = "article_detail.html"  # Template associado a esta view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Adiciona o formulário de comentário ao contexto da página
        return context  # Retorna o contexto com o formulário

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Permite editar um artigo
    model = Article  # O modelo usado será o 'Article'
    fields = ("title", "body")  # Os campos do formulário para editar o artigo
    template_name = "article_edit.html"  # Template associado a esta view

    def test_func(self):
        # Verifica se o usuário é o autor do artigo
        obj = self.get_object()  # Obtém o objeto (artigo)
        return obj.author == self.request.user  # O usuário precisa ser o autor do artigo para editar

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Permite excluir um artigo
    model = Article  # O modelo usado será o 'Article'
    template_name = "article_delete.html"  # Template associado a esta view
    success_url = reverse_lazy("article_list")  # Redireciona para a lista de artigos após a exclusão

    def test_func(self):
        # Verifica se o usuário é o autor do artigo
        obj = self.get_object()  # Obtém o objeto (artigo)
        return obj.author == self.request.user  # O usuário precisa ser o autor do artigo para excluir

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")  # Os campos que o usuário pode preencher

    def form_valid(self, form):
        # Preenche o campo 'author' com o usuário logado antes de salvar
        form.instance.author = self.request.user  # Associando o autor ao artigo
        return super().form_valid(form)  # Salva o formulário e chama o método form_valid da superclasse

    def get_success_url(self):
        # Redireciona para a lista de artigos após a criação do artigo
        return reverse("article_list")
# --- Views para os comentários ---

class CommentPost(SingleObjectMixin, FormView):
    # View para processar o envio de um comentário
    model = Article  # O modelo usado será o 'Article'
    form_class = CommentForm  # O formulário utilizado para os comentários
    template_name = "article_detail.html"  # Template que exibe os detalhes do artigo e o formulário de comentário

    def post(self, request, *args, **kwargs):
        # Processa o envio de um comentário
        self.object = self.get_object()  # Obtém o artigo para associar o comentário
        return super().post(request, *args, **kwargs)  # Processa o formulário do comentário

    def form_valid(self, form):
        # Salva o comentário, associando ao artigo e ao usuário
        comment = form.save(commit=False)  # Cria o objeto de comentário sem salvar ainda
        comment.article = self.object  # Associa o comentário ao artigo
        comment.author = self.request.user  # Associa o comentário ao usuário logado
        comment.save()  # Salva o comentário
        return super().form_valid(form)  # Processa o formulário e retorna a resposta

    def get_success_url(self):
        # Redireciona para a página de detalhes do artigo após o comentário ser postado
        article = self.get_object()  # Obtém o artigo
        return reverse("article_detail", kwargs={"pk": article.pk})  # Redireciona para o detalhe do artigo

# --- A view que lida com as requisições GET e POST para um artigo com comentários ---

class ArticleDetailWithCommentsView(LoginRequiredMixin, View):
    # Combina GET e POST para exibir o artigo e processar os comentários
    def get(self, request, *args, **kwargs):
        # Exibe o artigo e o formulário de comentário
        article = Article.objects.get(pk=kwargs['pk'])  # Obtém o artigo
        form = CommentForm()  # Cria o formulário de comentário
        context = {
            'article': article,  # Passa o artigo para o contexto
            'form': form  # Passa o formulário de comentário para o contexto
        }
        return render(request, "article_detail.html", context)  # Renderiza o template com o contexto

    def post(self, request, *args, **kwargs):
        # Processa o envio de um comentário
        return CommentPost.as_view()(request, *args, **kwargs)  # Chama a view de postagem de comentário
