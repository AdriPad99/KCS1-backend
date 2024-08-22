from django.urls import path
from . import views

urlpatterns = [
    path("", views.TasksLC.as_view(), name="tasks-list-make"),
    path("<int:pk>/", views.TasksRUDAPIView.as_view(), name="book-edit"),
]