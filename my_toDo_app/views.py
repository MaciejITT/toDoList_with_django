from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo


def todo(request):
    latest_items_list = Todo.objects.all().order_by('-added_date')
    items = {
        'latest_items_list': latest_items_list,
    }
    return render(request, 'my_toDo_app/add_item.html', items)


def add_item(request):
    current_date = timezone.now()
    item_todo = request.POST["item_todo"]
    to_database = Todo.objects.create(added_date=current_date, item_todo=item_todo)

    return HttpResponseRedirect("/")


def delete_item(request, todo_id):
    print(todo_id)
    item_to_delete = Todo.objects.get(pk=todo_id)
    item_to_delete.delete()

    return HttpResponseRedirect("/")


