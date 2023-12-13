from django.urls import path
from todos.views import todo_list, detail_list, create_list, edit_list

urlpatterns = [
    path("<int:id>/edit/", edit_list, name="todo_list_update"),
    path("create/", create_list, name="todo_list_create"),
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", detail_list, name="todo_list_detail"),
]
