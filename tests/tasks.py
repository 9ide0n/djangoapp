# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import random
from django.db.models import Sum
from .models import T1, T2, T3

@shared_task()
def random_sort2(n):
    l = [random.random() for i in range(n)]
    l.sort()
    return "APP: Sort %i random items" % n


@shared_task()
def sum_query(table_id):
    model = eval("T%s" % table_id)
    model.objects.aggregate(Sum('n'))
    return "DB: Sum %i items for %s" % (model.objects.count(), model.__name__)