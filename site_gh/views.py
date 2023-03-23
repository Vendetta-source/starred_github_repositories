from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .service import get_starred_repositories, get_issues


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated and not request.user.is_staff:
        username = request.GET.get('username')
        repos = get_starred_repositories(request, username=username)
        tag = request.GET.get('tag')
        len_issues = 0
        for repo in repos:
            repo['issues'] = get_issues(repo['fullname'], request, tag)
            if repo['issues'] is not None:
                len_issues += len(repo['issues'])
        return render(request, 'home.html', {
            'repos': repos,
            'tag': tag,
            'len_repos': len(repos),
            'len_issues': len_issues,
        })
    logout(request)
    return redirect('login')

