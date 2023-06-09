# Generated by Django 3.2.19 on 2023-06-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Название города', 'verbose_name_plural': 'Названия городов'},
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='ссылка'),
        ),
    ]
