from django.urls import path
from .views import NoticiaListCreateView, NoticiaDetailView, NoticiaRestaurarView

urlpatterns = [
    path('noticias/', NoticiaListCreateView.as_view(), name='listar_criar_noticias'),
    path('noticias/<int:id>/', NoticiaDetailView.as_view(), name='detalhar_atualizar_remover_noticia'),
    path('noticias/<int:id>/restaurar/', NoticiaRestaurarView.as_view(), name='restaurar_noticia'),
]
