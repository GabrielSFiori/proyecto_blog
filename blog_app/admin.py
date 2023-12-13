from django.contrib import admin

from .models import Post, Category, Comment, PostCategory

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'color')
    list_filter = ('name', 'color')
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'color')


admin.site.register(Comment)
admin.site.register(PostCategory)


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_at', 'update_at', 'status')
    list_filter = ('status', 'create_at', 'update_at')
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'create_at'
    ordering = ('create_at',)
    inlines = [PostCategoryInline,]
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Post', {
            'fields': ('title', 'author', 'content', 'slug', 'status', 'image')
        }),
    )
