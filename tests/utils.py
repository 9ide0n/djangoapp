from django.shortcuts import render
from time import time
from .models import Task


def all_tasks_render(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'navigation.html', context)


def create_task_and_render(request, result):
    t = Task(id=result.task_id)
    t.start_time = time()
    t.save()
    return all_tasks_render(request)