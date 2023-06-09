# Generated by Django 3.2.19 on 2023-06-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20230609_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Специализация')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название города'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='ссылка'),
        ),
    ]
