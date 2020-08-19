from django_redis import get_redis_connection

def tearDown(self):
    get_redis_connection("default").flushall()
from django.core.cache import cache
cache.set("foo", "value", timeout=25)
cache.ttl("foo")