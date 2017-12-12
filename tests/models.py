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


class Task(models.Model):

    id = models.CharField(max_length=40, primary_key=True)
    start_time = models.FloatField(default=0)
    end_time = models.FloatField(default=0)

    def duration(self):
        result = self.end_time - self.start_time
        if result < 0:
            result = 0
        return result
