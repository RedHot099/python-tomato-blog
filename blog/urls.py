from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pomidory-paprykowe.html', views.papryka),
    path('pomidory-czekoladowe.html', views.czekolada),
    path('czarne-pomidory.html', views.czarne),
    path('pomidory-tygrysie.html', views.tygrysie),
    path('', views.index)
]

urlpatterns += staticfiles_urlpatterns()