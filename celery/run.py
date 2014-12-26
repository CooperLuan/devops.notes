import logging
logging.basicConfig(level=logging.INFO)
from datetime import timedelta

from celery import group, chain, chord
from celery.utils.log import get_task_logger
from tasks import add, mul, xsum, AddJob, IgnoreJob
from tasks import app

log = get_task_logger(__name__)
log.setLevel(logging.INFO)


def test_delay():
    result = add.delay(2, 2).get()
    log.info('add.delay 2, 2) = %s' % result)

    result = add.s(2, 2).delay().get()
    log.info('add.s(2, 2).delay().get() = %s' % result)

    result = add.s(2).delay(12).get()
    print(result)


def test_async():
    result = add.apply_async((2, 2)).get()
    log.info('add.apply_async(2, 2) = %s' % result)


def test_grouping():
    result = group(add.s(i, i) for i in range(10, 20))().get()
    print(result)

    result = chain(add.s(2, 2) | mul.s((4)))().get()
    print(result)

    result = chord((mul.s(i, i) for i in range(10)), xsum.s())().get()
    print(result)

    result = (group(mul.s(i, i) for i in range(10)) | xsum.s())().get()
    print(result)


def test_task_class():
    result = AddJob().delay(123, 456).get(timeout=1)
    print(result)


def test_ignore():
    result = IgnoreJob().delay()
    print(result)


def test_linking():
    result = add.apply_async((2, 2), link=mul.s(5))
    print(result.get())
    print(list(result.collect()))


def test_group_results():
    job = group([
        add.s(2, 4),
        mul.s(4, 9),
        xsum.s([2, 3, 5]),
    ])
    result = job.apply_async()
    print(result.ready())
    print(result.successful())
    print(result.join())
    print(result.get())


def test_complex_chord():
    result = chord(mul.s(i, i) for i in range(100))(xsum.s()).get()
    print(result)


def test_map():
    result = ~xsum.map([range(10), range(1000)])
    print(result)

    result = xsum.map([range(10), range(1000)]).apply_async().get()
    print(result)

    result = ~mul.starmap(zip(range(10), range(10, 20)))
    print(result)

    result = mul.starmap(zip(range(10), range(10, 20))).apply_async().get()
    print(result)


def tesst_thunks():
    # split tasks to every 5 items
    n = 5
    result = mul.chunks(zip(range(100), range(100)), n).apply_async().get()
    print(result)

    result = ~mul.chunks(zip(range(100), range(100, 200)), n)
    print(result)


if __name__ == '__main__':
    test_delay()
    test_async()
    test_task_class()
    test_ignore()
    test_linking()
    test_group_results()
    test_complex_chord()
    test_map()
    tesst_thunks()
