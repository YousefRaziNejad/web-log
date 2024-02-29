from django.contrib import admin

from blog.models import Category, Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'content', 'is_active')
    list_filter = ('is_active',)
    search_fields = ("title", 'content')
    list_editable = ('is_active',)

    inlines = [CommentInline]


admin.site.register(Category)