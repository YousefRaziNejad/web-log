from django import forms

from blog.models import Post, Comment

class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'img', 'content', 'category']

class CommentCreate(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
