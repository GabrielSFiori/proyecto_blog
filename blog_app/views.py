from django.shortcuts import render
from .models import Post, Category, PostCategory, Comment
from .forms.form_blog import PostForm
from .forms.comment_form import CommentForm
from django.utils import timezone
from django.shortcuts import redirect
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST


def posts(request):
    posts = Post.objects.all()  # Obtener todos los posts
    return render(request, 'post/post_list.html', {'posts': posts})


def posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_in_category = Post.objects.filter(categories=category)
    return render(request, 'post/post_list.html', {'posts': posts_in_category})


def post_detail(request, slug):
    # Usar get_object_or_404 para manejar mejor los casos en que el post no exista
    post = get_object_or_404(Post, slug=slug)

    # Incrementar el conteo de vistas
    post.views_count += 1
    post.save(update_fields=['views_count'])

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = post
            comment.save()
            # Actualizar el conteo de comentarios
            post.comments_count = post.comments.all().count()
            post.save(update_fields=['comments_count'])
            # Redirigir al post para ver el comentario publicado
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'post/post_detail.html', {'post': post, 'form': form})


@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes_count += 1
    post.save(update_fields=['likes_count'])
    return redirect('post_detail', slug=post.slug)


@require_POST
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes_count += 1
    comment.save(update_fields=['likes_count'])
    # Redirecciona de nuevo al post
    return redirect('post_detail', slug=comment.comment_post.slug)


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        # Obtener las categorías seleccionadas
        categories = request.POST.getlist('categories')

        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.save()

            for category_id in categories:
                PostCategory.objects.create(
                    post=new_post, category_id=category_id)

            return redirect('posts')

    else:
        post_form = PostForm()
        categories = Category.objects.all()

    context = {
        'post_form': post_form,
        'categories': categories
    }
    return render(request, 'post/post_form.html', context)
