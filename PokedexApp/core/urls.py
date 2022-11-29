from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.indexview, name="home"),
    path("add/", views.addview, name="add"),
    path("delete/<int:pk>/", views.deleteview, name="delete"),
    path("all/", views.allview, name="all"),
]
