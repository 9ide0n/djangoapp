from django.db import models


class T(models.Model):
    n = models.IntegerField(default=0)

    class Meta:
        abstract = True


class T1(T):
    pass


class T2(T):
    pass


class T3(T):
    pass

