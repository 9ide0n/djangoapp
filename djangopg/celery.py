from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangopg.settings')

#run this to allow using models in signal handlers
import django
django.setup()

app = Celery('djangopg')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

#signal handlers must be in the module where Celery app is defined

from time import time
from celery.signals import task_prerun, task_postrun
from tests.models import Task

@task_postrun.connect()
def task_postrun_handler(task_id, task, *args, **kwargs):

    try:
        t = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        t = Task(pk=task_id)
    t.end_time = time()
    t.save()

