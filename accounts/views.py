from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Post

from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect("blog:post_list")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("accounts:login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.published.filter(author=author)
    return render(
        request,
        "accounts/profile.html",
        {"author": author, "posts": posts},
    )
