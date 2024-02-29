from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to="category/",blank=True)
    descriptions = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class meta:
        db_table = "categories"
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):

        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="post/%Y/%m/%d", blank=True, null=True)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    objects = models.Manager()
    PostManager = PostManager()

    class meta:
        ordering = ['created_time']
        db_table = "Posts"
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)


    class Meta:
        ordering = ['created_time']
        db_table = "comments"
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.name}: برای پست {self.post.title}: نظر داد."