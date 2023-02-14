from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        task = Task(user=request.user)
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:
        return redirect('task_list')
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:
        return redirect('task_list')
    task.delete()
    return redirect('task_list')
