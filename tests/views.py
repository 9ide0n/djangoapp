from django.http import HttpResponse
from django.shortcuts import render

from .tasks import random_sort2, sum_query
from .models import Task
from celery.result import AsyncResult

def app(request):
    result = random_sort2.delay(5000000)
    t = Task(id=result.task_id)
    t.save()
    return mock(request)


def db(request, table_id):
    result = sum_query.delay(table_id)
    t = Task(id=result.task_id)
    t.save()
    return mock(request)


def clear(request):
    Task.objects.all().delete()
    return mock(request)


def index(request):
    return mock(request)


def mock(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'navigation.html', context)


def task(request, task_id):
    # t = Task.objects.get(pk=task_id)
    ar = AsyncResult(task_id)
    context = {'ar': ar}
    return render(request, 'tests/tasks.html', context)