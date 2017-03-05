from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

# admin.site.register(Post)
# admin.site.register(Category)

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

class CategoryAdmin(admin.ModelAdmin):
    #exclude Post field
    fields = ('name', 'description')
    exclude = ('posts',)

admin.site.register(Category, CategoryAdmin)


class CategoriesInline(admin.TabularInline):
    model = Category.name.through


class PostAdmin(admin.ModelAdmin):
    # Add Category.name
    # 'created_date' 'modified_date' are non-editable fields
    # <class 'myblog.admin.CategoriesInline'>: (admin.E202) 'myblog.Category' has no ForeignKey to 'myblog.Post'.
    inlines = [
        CategoriesInline,
    ]
    fields = ('title', 'text', 'author','published_date', 'name')

admin.site.register(Post, PostAdmin)