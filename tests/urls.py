from django.conf.urls import include,url

from . import views

app_name = 'tests'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'app/$', views.app, name='app'),
    url(r'clear/$', views.clear, name='clear'),
    url(r'task/(?P<task_id>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$', views.task, name='task'),
    url(r'db/(?P<table_id>(1|2|3){1})$', views.db, name='db'),

]
