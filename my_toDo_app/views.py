from django.shortcuts import render
from django.http import HttpResponse


def todo(request):
    return render(request, 'base.html')


def add_item(request):
    return render(request, 'my_toDo_app/add_item.html')

