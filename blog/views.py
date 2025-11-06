from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = Post.objects.filter(status=1)
    post = get_object_or_404(post, pk=pid)
    context = {'post' : post}
    return render(request, 'blog/blog-single.html', context)

# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1,category__name=cat_name)
#     context = {'posts' : posts}
#     return render(request, 'blog/blog-home.html', context)
