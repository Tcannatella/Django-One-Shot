from django.shortcuts import render,  get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm

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



def edit_list(request, id):
    items = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=items)
        if form.is_valid():
            items = form.save()
            return redirect("todo_list_detail", id=items.id)
    else:
        form = TodoListForm(instance=items)

    context = {
        "todo_item" : items,
        "form": form,
    }
    return render(request, "todos/edit.html", context)

def delete_list(request,id):
  items = TodoList.objects.get(id=id)
  if request.method == "POST":
    items.delete()
    return redirect("todo_list_list")

  return render(request, "todos/delete.html")


def create_item(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            items = form.save()
        return redirect("todo_list_detail", id=items.id)
    else:
        form = TodoItemForm()

    context = {
        "form": form,
    }
    return render(request,"todos/itemscreate.html", context)
