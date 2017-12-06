from django.conf.urls import include,url

from . import views

app_name = 'tests'
urlpatterns = [
    url(r'app/$', views.app, name='app'),
    # url(r't1/$', views.t1, name='t1'),
    # url(r't2/$', views.t2, name='t2'),
    # url(r't3/$', views.t3, name='t3'),
    url(r'db/(?P<table_id>(1|2|3){1})$', views.db, name='db'),

]
