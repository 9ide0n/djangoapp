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
    # APP = 0
    # DB = 1
    # WORK_TYPE = (
    #     (APP, 'app'),
    #     (DB, 'db'),
    # )
    # type = models.IntegerField(
    #     choices=WORK_TYPE,
    #     default=APP,
    # )
    id = models.CharField(max_length=40, primary_key=True)
    start_time = models.FloatField(default=0)
    end_time = models.FloatField(default=0)

    def duration(self):
        return self.end_time - self.start_time
    # def get_work_type(self):
    #     return self.WORK_TYPE[self.type][1]