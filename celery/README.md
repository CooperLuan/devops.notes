# Celery

## Introduction

- Task Queue
- version 3.1
- a client send a message to broker/queue, broker delivers to a worker
- concurrency
    + multiprocessing
    + gevent/eventlet
- moitoring
    + inspect
    + flower
    + events
- autoreloading
- workflows
    + grouping
    + chaining
    + chunking
    + callbacks
    + map
- scheduling
    + specify `datetime`
    + PeriodicTask
    + crontab
- autoscaling

## Run Celery

```sh
celery -A tasks worker -l info
celery -A tasks worker -l info -c 10
celery -A tasks worker -l info -c 10 -B
celery multi start 3 -A tasks -l info
celery multi stop 3 -A tasks -l info
# use eventlet
celery -A tasks worker -l info -c 100 -P eventlet
```

## Periodic tasks

define periodic task by

```python
from datetime import timedelta
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'add-every-30-seconds': {
            'task': 'tasks.add',
            'schedule': timedelta(seconds=30),
            'args': (16, 16),
        },
    }
)
```

[more schedule detail](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules)

then activate schedule by adding `-B` option to celery worker

```sh
celery -A proj worker -B
```

## [Routing tasks](http://docs.celeryproject.org/en/latest/userguide/routing.html#routing-tasks)

didn't understand

## Monitoring and Management Guide

### Workers

- inspect
- flower
- celery events

### Munin

## Security

## Optimizing

## Concurrency

```sh
pip install eventlet
celery -A tasks worker -l info -c 1000 -P eventlet
```

## Signals

### Task signals

- `before_task_publish`
- `after_task_publish`
- `task_prerun`
- `task_postrun`
- `task_retry`
- `task_success`
- `task_failure`

### App signals

### Worker signals

### Beat signals

### Eventlet signals

### Logging signals

### Command signals
