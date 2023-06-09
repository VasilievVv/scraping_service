from django.db import models
from django.db.models import CharField


class City(models.Model):
    name = models.CharField('Название города',
                            max_length=50,
                            unique=True)
    slug = models.SlugField('ссылка', blank=True, unique=True)

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Названия городов'

    def __str__(self) -> CharField:
        return self.name


class Specialization(models.Model):
    name = models.CharField('Специализация',
                            max_length=50,
                            unique=True)
    slug = models.SlugField('ссылка', blank=True, unique=True)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self) -> CharField:
        return self.name


class Vacancy(models.Model):
    city = models.ForeignKey(
        City,
        verbose_name='город',
        on_delete=models.CASCADE,
    )
    specialization = models.ForeignKey(
        Specialization,
        verbose_name='специализация',
        on_delete=models.CASCADE,
    )
    url = models.URLField('ссылка', unique=True)
    title = models.CharField('Заголовок ваканасии', max_length=250)
    company = models.CharField('компания', max_length=250)
    description = models.TextField('описание вакансии')
    timestamp = models.DateField('создана', auto_now_add=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    def __str__(self) -> CharField:
        return self.title
