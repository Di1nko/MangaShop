from django.db import models


class Manga_news(models.Model):
    title = models.CharField('Название',max_length=100)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости по манге'
        verbose_name_plural = 'Новости по манге'
