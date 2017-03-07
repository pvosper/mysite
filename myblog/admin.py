from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    exclude = ('posts',)

admin.site.register(Category, CategoryAdmin)


class CategoriesInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInline,
    ]
    fields = ('title', 'text', 'author','published_date') #, 'posts')

admin.site.register(Post, PostAdmin)