from django.http import HttpResponse
from .tasks import random_sort2, sum_query




def app(request):
    result=random_sort2.delay(5000000)
    return HttpResponse(result.task_id)


def db(request, table_id):
    result=sum_query.delay(table_id)
    return HttpResponse(result.task_id)

