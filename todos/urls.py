from django.urls import path
from todos.views import todo_list, detail_list

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", detail_list, name="todo_list_detail"),
]
