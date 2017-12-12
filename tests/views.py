from django.shortcuts import render

from .tasks import random_sort2, sum_query
from .models import Task
from .utils import all_tasks_render, create_task_and_render
from celery.result import AsyncResult


def app(request):
    result = random_sort2.delay(5000000)
    return create_task_and_render(request, result)


def db(request, table_id):
    result = sum_query.delay(table_id)
    return create_task_and_render(request, result)


def clear(request):
    Task.objects.all().delete()
    return all_tasks_render(request)


def index(request):
    return all_tasks_render(request)


def task(request, task_id):
    t = Task.objects.get(pk=task_id)
    ar = AsyncResult(task_id)
    context = {'ar': ar, 't': t}
    return render(request, 'tests/tasks.html', context)