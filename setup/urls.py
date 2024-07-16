from django.contrib import admin
from django.urls import path

from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todos", TodoListView.as_view(), name="todo_list"),
    path("todo", TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:pk>/delete", TodoDeleteView.as_view(), name="todo_delete"),
    path("todo/<int:pk>/complete", TodoCompleteView.as_view(), name="todo_complete"),
]
