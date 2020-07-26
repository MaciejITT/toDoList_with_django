from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo, name='base'),
    path('add_item/', views.add_item, name='add_item'),
    path('delete_item/<int:todo_id>/', views.delete_item, name='delete_item'),
]
