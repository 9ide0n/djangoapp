import time
import random

from django.db.models import Sum


def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        return "job: %s <br>elapsed time: %f" % (retval, end_ts - beg_ts)

    return wrapper


@time_usage
def random_sort2(n):
    l = [random.random() for i in range(n)]
    l.sort()
    return "Sort %i random items" % n


@time_usage
def sum_query(model):
    model.objects.aggregate(Sum('n'))
    return "Sum %i items for %s" % (model.objects.count(), model.__name__)