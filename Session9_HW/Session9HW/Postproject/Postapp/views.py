from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )

        return redirect ('detail_page', new_post.pk)
    return render(request, 'create_post.html')

def detail_page(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail_page.html', {"post": post})

def edit_post(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    if request.method == 'POST':
        post.update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect ('detail_page', post_pk)
    return render(request, 'edit_post.html', {'post': post[0]})


def delete_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')
    pass