from django.urls import path, include
from . import views


urlpatterns = [
    path('task/', views.TaskListView.as_view()),
    path('task/<int:pk>/', views.TaskDetailView.as_view()),
    path('task-tracker/', views.TaskTrackerListView.as_view()),
]