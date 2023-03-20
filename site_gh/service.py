import json
import requests
from django.conf import settings
from django.core.cache import cache


def get_starred_repositories(request):
    extra_user_data = request.user.social_auth.get(provider='github').extra_data
    url = f'https://api.github.com/users/{extra_user_data["login"]}/starred'
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': f'Bearer {extra_user_data["access_token"]}'
    }
    cache_key = f'starred_repos_{request.user.username}'
    repos = cache.get(cache_key)
    if repos is not None:
        return repos

    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    # Извлекаем нужные поля и кэшируем ответ на 5 минут
    repos = [{'name': repo['name'], 'url': repo['html_url'], 'fullname': repo['full_name']} for repo in
             response.json()]
    cache.set(cache_key, repos, settings.CACHE_TTL)

    return repos


def get_issues(repo_name, request, tag=None):
    # Проверяем есть ли ответ в кэше
    if tag:
        cache_key = f'issues_{repo_name}_{tag}'
    else:
        cache_key = f'issues_{repo_name}'
    issues = cache.get(cache_key)
    if issues is not None:
        return issues

    extra_user_data = request.user.social_auth.get(provider='github').extra_data
    # Если ответа в кэше нет, получаем его из Github API
    if tag:
        url = f'https://api.github.com/search/issues?q=repo:{repo_name}+state:open+label:{tag}&per_page=100'
    else:
        url = f'https://api.github.com/search/issues?q=repo:{repo_name}+state:open&per_page=100'
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': f'Bearer {extra_user_data["access_token"]}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open('data1.json', 'w') as f:
        json.dump(response.json(), f)
    # Извлекаем нужные поля и кэшируем ответ на 5 минут
    issues = [
        {
            'title': issue['title'],
            'url': issue['html_url'],
            'labels': [item['name'] for item in issue['labels']]}
        for issue in response.json()['items']
    ]
    cache.set(cache_key, issues, settings.CACHE_TTL)

    return issues
