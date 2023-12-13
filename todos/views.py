from django.shortcuts import render,  get_object_or_404
from todos.models import TodoList, TodoItem

# Create your views here.

def todo_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list" : todos,
    }

    return render(request, "todos/list.html", context)

def detail_list(request, id):
    todo =  get_object_or_404(TodoList, id=id)
    context = {
        "todo_item" : todo
    }

    return render(request, "todos/detail.html", context)

