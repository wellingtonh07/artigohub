from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # Inclui as URLs do app accounts
    path("accounts/", include("django.contrib.auth.urls")),  # Inclui as URLs de login, logout, etc. do Django
    path("articles/", include("articles.urls")), 
    path("", include("pages.urls")),
]
