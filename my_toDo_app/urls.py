from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo, name='base'),
    path('add_item', views.add_item, name='add_item'),
]
