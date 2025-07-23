from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q # NUEVA LÍNEA: Importa Q para búsquedas complejas
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment, Category, Tag
from .forms import CommentForm, PostForm, AuthorPostForm # Importamos AuthorPostForm

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    form_class = AuthorPostForm # Usamos nuestro AuthorPostForm
    template_name = 'html/post_form.html'
    permission_required = 'posts.can_post'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detalle_post', kwargs={'post_id': self.object.pk})


def lista_de_posts(request):
    all_posts = Post.objects.all().order_by('-fecha_creacion')
    
    # Lógica de paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 5) # Muestra 5 posts por página
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Datos para la barra lateral
    recent_posts = Post.objects.all().order_by('-fecha_creacion')[:5]
    pinned_posts = Post.objects.filter(is_pinned=True).order_by('-fecha_creacion')[:3]
    popular_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count', '-fecha_creacion')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    contexto = {
        'posts': posts,
        'recent_posts': recent_posts,
        'pinned_posts': pinned_posts,
        'popular_posts': popular_posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'html/lista_de_posts.html', contexto)

def detalle_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    # Obtener solo los comentarios aprobados para mostrar
    comments = post.comments.filter(approved_comment=True)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detalle_post', post_id=post.id)
    else:
        form = CommentForm()

    # Datos para la barra lateral
    recent_posts = Post.objects.all().order_by('-fecha_creacion')[:5]
    pinned_posts = Post.objects.filter(is_pinned=True).order_by('-fecha_creacion')[:3]
    popular_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count', '-fecha_creacion')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    contexto = {
        'post': post,
        'comments': comments,
        'form': form,
        'recent_posts': recent_posts,
        'pinned_posts': pinned_posts,
        'popular_posts': popular_posts,
        'categories': categories,
        'tags': tags,
    }
    
    return render(request, 'html/detalle_post.html', contexto)

def posts_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    all_posts = Post.objects.filter(category=category).order_by('-fecha_creacion')

    # Lógica de paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 5) # Muestra 5 posts por página
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Datos para la barra lateral
    recent_posts = Post.objects.all().order_by('-fecha_creacion')[:5]
    pinned_posts = Post.objects.filter(is_pinned=True).order_by('-fecha_creacion')[:3]
    popular_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count', '-fecha_creacion')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    contexto = {
        'category': category,
        'posts': posts,
        'recent_posts': recent_posts,
        'pinned_posts': pinned_posts,
        'popular_posts': popular_posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'html/lista_de_posts.html', contexto)

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    all_posts = Post.objects.filter(tags=tag).order_by('-fecha_creacion')

    # Lógica de paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 5) # Muestra 5 posts por página
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Datos para la barra lateral
    recent_posts = Post.objects.all().order_by('-fecha_creacion')[:5]
    pinned_posts = Post.objects.filter(is_pinned=True).order_by('-fecha_creacion')[:3]
    popular_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count', '-fecha_creacion')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    contexto = {
        'tag': tag,
        'posts': posts,
        'recent_posts': recent_posts,
        'pinned_posts': pinned_posts,
        'popular_posts': popular_posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'html/lista_de_posts.html', contexto)

def search_results(request):
    query = request.GET.get('q')
    if query:
        # Filtra posts por título o contenido que contengan la consulta
        all_posts = Post.objects.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query)).order_by('-fecha_creacion')
    else:
        all_posts = Post.objects.none() # Si no hay consulta, no hay resultados

    # Lógica de paginación (reutilizada de otras vistas)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 5) # Muestra 5 posts por página
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # Datos para la barra lateral (reutilizados)
    recent_posts = Post.objects.all().order_by('-fecha_creacion')[:5]
    pinned_posts = Post.objects.filter(is_pinned=True).order_by('-fecha_creacion')[:3]
    popular_posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count', '-fecha_creacion')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    contexto = {
        'query': query,
        'posts': posts,
        'recent_posts': recent_posts,
        'pinned_posts': pinned_posts,
        'popular_posts': popular_posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'html/lista_de_posts.html', contexto) # Reutiliza la plantilla de lista de posts