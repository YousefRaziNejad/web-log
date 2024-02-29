from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from blog.models import Category, Post, Comment
from blog.forms import PostCreate, CommentCreate

def post_list(request):
    posts = Post.PostManager.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    try:
        post = Post.objects.select_related('user', 'category').get(id=id)
    except Post.DoesNotExist:
        return HttpResponse("post does not exist")
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post-list")
    else:
        form = PostCreate()
        return render(request, 'blog/post_create.html', {'form': form})

@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("post-list")
    else:
        form = PostCreate(instance=post)
        return render(request, 'blog/post_create.html', {'form': form})

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    post.delete()
    return redirect("post-list")

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse("category does not exist")
    return render(request, "blog/category_detail.html", {'category': category})

def post_search(request):
    search = request.GET.get("q")

    posts = Post.objects.filter(is_active=True).filter(Q(title__icontains=search) | Q(content__icontains=search))
    return render(request, "blog/post_search.html", {'posts': posts})


def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentCreate(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect("post-detail", id=id)
    else:
        form = CommentCreate()
        return render(request, 'blog/comment.html', {'form': form})