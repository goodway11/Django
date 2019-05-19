
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #----?? part of syntax...?
from django.conf.urls import include # taking import paths to include another url(url patterns we used before)
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    ]
urlpatterns += staticfiles_urlpatterns()#function



