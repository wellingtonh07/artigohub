# Importa os caminhos necessários do Django e as views da aplicação.
from django.urls import path
from .views import (
    ArticleListView,  # View para listar todos os artigos.
    ArticleDetailView,  # View para exibir os detalhes de um artigo.
    ArticleUpdateView,  # View para editar um artigo existente.
    ArticleDeleteView,  # View para excluir um artigo existente.
    ArticleCreateView,  # View para criar um novo artigo.
)

# Define as URLs que serão acessadas na aplicação, associando-as às views correspondentes.
urlpatterns = [
    # URL para visualizar os detalhes de um artigo, usando seu ID (pk) na URL.
    path(
        "<int:pk>/",  # Captura o ID do artigo da URL (pk).
        ArticleDetailView.as_view(),  # Chama a view de detalhes do artigo.
        name="article_detail",  # Nomeia essa URL para ser referenciada como 'article_detail'.
    ),  # new

    # URL para editar um artigo, usando seu ID (pk) na URL.
    path(
        "<int:pk>/edit/",  # Captura o ID do artigo e o adiciona ao caminho '/edit/'.
        ArticleUpdateView.as_view(),  # Chama a view para editar o artigo.
        name="article_edit",  # Nomeia essa URL para ser referenciada como 'article_edit'.
    ),  # new

    # URL para excluir um artigo, usando seu ID (pk) na URL.
    path(
        "<int:pk>/delete/",  # Captura o ID do artigo e o adiciona ao caminho '/delete/'.
        ArticleDeleteView.as_view(),  # Chama a view para excluir o artigo.
        name="article_delete",  # Nomeia essa URL para ser referenciada como 'article_delete'.
    ),  # new

    # URL para listar todos os artigos, sem necessidade de um ID (sem 'pk').
    path(
        "",  # Caminho raiz para a listagem de artigos (não inclui nenhum ID na URL).
        ArticleListView.as_view(),  # Chama a view para listar os artigos.
        name="article_list",  # Nomeia essa URL para ser referenciada como 'article_list'.
    ),

    # URL para criar um novo artigo, acessível através do caminho '/new/'.
    path(
        "new/",  # Caminho para a criação de um novo artigo.
        ArticleCreateView.as_view(),  # Chama a view para criar um novo artigo.
        name="article_new",  # Nomeia essa URL para ser referenciada como 'article_new'.
    ),
]
