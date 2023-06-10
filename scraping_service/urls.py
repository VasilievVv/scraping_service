from django.contrib import admin
from django.urls import path

import scraping.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', scraping.views.home_view)
]
