from django.urls import path
from .views import lista_de_posts, detalle_post, PostCreateView, posts_by_category, posts_by_tag, search_results # NUEVA LÍNEA: Importa search_results

urlpatterns = [
    path('', lista_de_posts, name='lista_de_posts'),
    path('new/', PostCreateView.as_view(), name='post_new'), # URL para crear posts
    path('<int:post_id>/', detalle_post, name='detalle_post'),
    path('category/<slug:category_slug>/', posts_by_category, name='posts_by_category'), # URL para filtrar por categoría
    path('tag/<slug:tag_slug>/', posts_by_tag, name='posts_by_tag'), # URL para filtrar por etiqueta
    path('search/', search_results, name='search_results'), # NUEVA LÍNEA: URL para la búsqueda
]