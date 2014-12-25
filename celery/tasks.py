"""
celery -A tasks worker -l info
"""
from celery import Celery

app = Celery('tasks', broker='redis://localhost')

app.conf.update(
    BROKER_URL='redis://localhost',
    CELERY_RESULT_BACKEND='redis://localhost',
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_TASK_RESULT_EXPIRES=10,
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
