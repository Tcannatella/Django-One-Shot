from django.shortcuts import render,  get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm

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

def create_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            items = form.save()
            return redirect("todo_list_detail", id=items.id)
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }
    return render(request,"todos/create.html", context)
