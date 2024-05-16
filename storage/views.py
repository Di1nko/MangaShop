from django.shortcuts import render
from .models import Manga_table


def manga_list(request):
    query = request.GET.get('q')
    if query:
        manga = Manga_table.objects.filter(title__icontains=query)
    else:
        manga = Manga_table.objects.all()
    return render(request, 'storage/manga_list.html', {'manga': manga})