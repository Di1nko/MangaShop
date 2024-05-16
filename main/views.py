from django.shortcuts import render
from .models import Manga_news


def index(request):
    query = request.GET.get('q')
    if query:
        manga_news = Manga_news.objects.filter(title__icontains=query)
    else:
        manga_news = Manga_news.objects.all()
    context = {
        'title': 'Главная страница',
        # 'values': ['Some','Hello','123'],
        'manga_news': manga_news
    }

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html', )
