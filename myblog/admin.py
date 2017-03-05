from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

admin.site.register(Post)
admin.site.register(Category)

"""
For your homework this week, we’ll fix one glaring problem with our blog admin.

As you created new categories and posts, and related them to each-other, how
    did you feel about that work?

Although from a data perspective, the category model is the right place for
    the ManytoMany relationship to posts, this leads to awkward usage in the
    admin.

It would be much easier if we could designate a category for a post from the
    Post admin.

- Read the documentation about the Django admin.

- You’ll need to create a customized ModelAdmin class for the Post and Category
    models.

- And you’ll need to create an InlineModelAdmin to represent Categories on the
    Post admin view.

- Finally, you’ll need to exclude the ‘posts’ field from the form in your
    Category admin.
"""


class PostAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    #exclude Post field
    pass

# admin.site.register(Category, PostAdmin)

class CategoriesInline(admin.TabularInline):
    model = Post

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInline,
    ]