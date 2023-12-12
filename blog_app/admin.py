from .models import PostCategory
from .models import Post
from .models import Category
from django.contrib import admin
from .models import Comment


admin.site.register(PostCategory)

admin.site.register(Comment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color', 'slug')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    fieldsets = (
        ('Category', {
            'fields': ('name', 'description', 'color', 'slug')
        }),
    )


class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',
                    'created_at', 'updated_at', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    ordering = ('title',)
    inlines = [PostCategoryInLine,]
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Post', {
            'fields': ('title', 'content', 'slug', 'author',
                       'created_at', 'updated_at', 'status')
        }),
    )
