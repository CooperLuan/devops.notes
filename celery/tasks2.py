"""
celery -A tasks worker -l info --autoreload
"""
import logging
logging.basicConfig(level=logging.INFO)
from celery import Celery, Task
from celery.utils.log import get_task_logger
log = get_task_logger(__name__)

app = Celery('tasks2', broker='redis://localhost')

app.conf.update(
    BROKER_URL='redis://localhost',
    CELERY_RESULT_BACKEND='redis://localhost',
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    # CELERY_IGNORE_RESULT=True,
    CELERY_TASK_RESULT_EXPIRES=10,
    CELERY_DISABLE_RATE_LIMITS=True,
)


@app.task()
def fetch_page(url):
    log.info('fetch page from %s' % url)
    return {'title': 'Hello Tank'}


@app.task()
def parse_page(html):
    log.info('parse page %s' % html)
    return {'data': html, 'url': 'url'}


@app.task(ignore_result=True)
def store_page(data):
    log.info('store data %s' % data)
