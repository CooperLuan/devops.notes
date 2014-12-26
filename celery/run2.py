import logging
logging.basicConfig(level=logging.INFO)

from celery import group, chain, chord
from celery.utils.log import get_task_logger
from tasks2 import fetch_page, parse_page, store_page, chain_fetch_parse_store

log = get_task_logger(__name__)
log.setLevel(logging.INFO)


def test_chain():
    url = 'http://google.com.hk'
    ch = fetch_page.s(url) | parse_page.s() | store_page.s()
    print(ch())

    result = chain_fetch_parse_store.apply_async((url, ))
    print(result)


if __name__ == '__main__':
    test_chain()
