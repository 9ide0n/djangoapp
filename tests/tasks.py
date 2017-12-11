# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


import random
from django.db.models import Sum
from .models import T1, T2, T3

from time import time
from celery.signals import task_prerun, task_postrun
from .models import Task

#
@task_prerun.connect()
def task_prerun_handler(task_id, task, *args, **kwargs):

    try:
        t = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        t = Task(pk=task_id)
    t.start_time = time()
    t.save()


@task_postrun.connect()
def task_postrun_handler(task_id, task, *args, **kwargs):

    try:
        t = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        t = Task(pk=task_id)
    t.end_time = time()
    t.save()

@shared_task
def random_sort2(n):
    l = [random.random() for i in range(n)]
    l.sort()
    return "Sort %i random items" % n

@shared_task
def sum_query(table_id):
    model = eval("T%s" % table_id)
    model.objects.aggregate(Sum('n'))
    return "Sum %i items for %s" % (model.objects.count(), model.__name__)