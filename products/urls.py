
from django.urls import path
from . import views

urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.details, name="delete"),
    path('confirmdelete/', views.confirmed, name="confirmed"),
    path('createRecord/', views.createRecord, name="createRecord"),

    ]
