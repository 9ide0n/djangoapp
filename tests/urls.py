from django.conf.urls import include,url

from . import views

app_name = 'tests'
urlpatterns = [
    url(r'app/$', views.app, name='app'),
    url(r'db/(?P<table_id>(1|2|3){1})$', views.db, name='db'),

]
