"""
celery -A tasks worker -l info --concurrency=10 -B
"""
from datetime import timedelta

from celery import Celery, Task
from celery.exceptions import Ignore
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost')

app.conf.update(
    BROKER_URL='redis://localhost',
    CELERY_RESULT_BACKEND='redis://localhost',
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    # CELERY_IGNORE_RESULT=True,
    CELERY_TASK_RESULT_EXPIRES=10,
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERYBEAT_SCHEDULE={
        'add-every-5-seconds': {
            'task': 'tasks.add',
            'schedule': timedelta(seconds=5),
            'args': (16, 16)
        },
        'add-every-minute': {
            'task': 'tasks.add',
            'schedule': crontab(minute='*'),
            'args': (14, 30),
        }
    },
)


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


class AddJob(Task):

    def run(self, *args):
        return sum(args)


class IgnoreJob(Task):

    def run(self, *args):
        raise Ignore()
