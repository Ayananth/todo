from django.shortcuts import render, redirect, get_object_or_404
from core.models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'core/list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'core/add.html')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
