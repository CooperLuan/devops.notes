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
celery multi start 3 -A tasks -l info
celery multi stop 3 -A tasks -l info
```
