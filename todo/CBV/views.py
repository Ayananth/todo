from django.views.generic import ListView
from core.models import Task
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect, get_object_or_404


class TaskListView(ListView):
    print("Hello")
    model = Task
    template_name = 'CBV/list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title']  # Automatically builds form for 'title'
    template_name = 'CBV/add.html'
    success_url = reverse_lazy('task_list')


class TaskCompleteView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.completed = True
        task.save()
        return redirect('CBVtask_list')
    
class TaskDeleteDirectView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('task_list')

