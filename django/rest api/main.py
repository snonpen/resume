from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

@csrf_exempt
def task_list(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        tasks = Task.objects.filter(user=user)
        tasks_json = [t.to_json() for t in tasks]
        return JsonResponse(tasks_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        task = Task(user=user, task_name=data['task_name'])
        task.save()
        return JsonResponse(task.to_json())

@csrf_exempt
def task_detail(request, username, pk):
    user = get_object_or_404(User, username=username)
    task = get_object_or_404(Task, pk=pk, user=user)
    if request.method == 'GET':
        return JsonResponse(task.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        task.task_name = data.get('task_name', task.task_name)
        task.completed = data.get('completed', task.completed)
        task.save()
        return JsonResponse(task.to_json())
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'deleted': True})