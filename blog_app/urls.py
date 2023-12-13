from django.contrib import admin
from django.urls import path
from .views import posts, create_post, post_detail, like_post, like_comment, posts_by_category
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", posts, name="posts"),
    path("create_post/", create_post, name="create_post"),
    path("posts/<slug:slug>/", post_detail, name="post_detail"),
    path("category/<slug:slug>/", posts_by_category, name="category"),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
    path('like_comment/<int:comment_id>/', like_comment, name='like_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
