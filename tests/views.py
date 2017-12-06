from django.http import HttpResponse
from .helpers import random_sort2, sum_query

from .models import T1, T2, T3


def app(request):
    return HttpResponse(random_sort2(4000000))


def db(request, table_id):
    return HttpResponse(sum_query(eval("T%s" % table_id)))

# def t3(request):
#     return HttpResponse(sum_query(T3))
#
#
# def t2(request):
#     return HttpResponse(sum_query(T2))
#
#
# def t1(request):
#     return HttpResponse(sum_query(T1))


