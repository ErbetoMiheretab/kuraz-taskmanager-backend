from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/tasks/", views.list_tasks, name="list-tasks"),
    path("api/tasks/create/", views.create_task, name="create-task"),
    path("api/tasks/<int:pk>/", views.get_task, name="get-task"),
    path("api/tasks/<int:pk>/update/", views.update_task, name="update-task"),
    path("api/tasks/<int:pk>/delete/", views.delete_task, name="delete-task"),
]
