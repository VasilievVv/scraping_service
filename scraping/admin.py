from django.contrib import admin

from scraping.models import City, Specialization, Vacancy


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'specialization',
                    'company', 'timestamp')
