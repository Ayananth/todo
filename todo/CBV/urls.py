from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskCompleteView,
    TaskDeleteDirectView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='CBVtask_list'),
    path('add/', TaskCreateView.as_view(), name='CBVadd_task'),
    path('complete/<int:task_id>/', TaskCompleteView.as_view(), name='complete_task'),
    path('delete/<int:pk>/', TaskDeleteDirectView.as_view(), name='delete_task'),  # uses `pk` by default
]
