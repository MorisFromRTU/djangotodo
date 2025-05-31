from django.shortcuts import render, redirect
from .models import Task
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

@require_http_methods(["POST"])
def add_task(request):
    title = request.POST.get('title')
    Task.objects.create(title=title)
    return redirect('index')

@require_http_methods(["POST"])
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

@require_http_methods(["POST"])
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')