from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .service import get_starred_repositories, get_issues


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated and not request.user.is_staff:
        repos = get_starred_repositories(request)
        tag = request.GET.get('tag')
        for repo in repos:
            repo['issues'] = get_issues(repo['fullname'], request, tag)
        return render(request, 'home.html', {'repos': repos, 'tag': tag})
    logout(request)
    return redirect('login')

