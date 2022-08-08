from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import BookPost, BookComment, MoviePost, MovieComment, DramaPost, DramaComment
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

def book(request):
    return render(request, "book.html")

def movie(request):
    return render(request, "movie.html")

def drama(request):
    return render(request, "drama.html")

def bookpost(request):
    bookpost = BookPost.objects.all()

    return render(request, "book.html", {"bookposts": bookposts})

def moviepost(request):
    moviepost = MoviePost.objects.all()

    return render(request, "movie.html", {"movieposts": movieposts})


def dramapost(request):
    dramapost = DramaPost.objects.all()

    return render(request, "drama.html", {"dramaposts": dramaposts})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("home")
    return render(request, "registration/signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
                )
            return redirect(request.GET.get("next", "/"))
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, "registration/login.html", {"error": error})

    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)

    return redirect("home")