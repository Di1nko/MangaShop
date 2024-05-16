from django.db import models

class Manga_table(models.Model):
    title = models.CharField('Название',max_length=100)
    author = models.CharField('Автор', max_length=100)
    genre = models.CharField('Жанр', max_length=100)
    quantity = models.IntegerField('Количество на складе')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'