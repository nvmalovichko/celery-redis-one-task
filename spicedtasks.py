import functools

import redis

_PREFIX = 'creaper'


def singleton_task(timeout):
    """
    Parametrized singleton task decorator
    :param timeout: <int> redis cached lock id lifetime in seconds;
    """

    def task_exc(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            lock_id = "{0}-singleton-task-{1}".format(_PREFIX ,func.__name__)
            _execute_function(func, lock_id, timeout, *args, **kwargs)

        return wrapper

    return task_exc


def spiced_singleton_task(timeout):
    """
    Parametrized singleton task decorator with spices. Spices used when you want to create many singleton tasks
    with unique id.
    :param timeout: <int> redis cached lock id lifetime in seconds;
    """

    def task_exc(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            spices = kwargs.pop('add_spices', 'null')
            lock_id = "{0}-spiced-singleton-task-{1}-{2}".format(_PREFIX, func.__name__, spices)
            _execute_function(func, lock_id, timeout, *args, **kwargs)

        return wrapper

    return task_exc


def _execute_function(wrapped_function, id_, timeout, *args, **kwargs):
    """
    Lock id and execute decorated function. If id exists, decorated function won't be executed.
    :param wrapped_function: decorated function;
    :param id_: <str> id for locking in cache;
    :param timeout: redis cached lock id lifetime in seconds;
    """
    r = redis.StrictRedis()
    is_locked = lambda: r.exists(id_)
    acquire_lock = lambda: r.setex(id_, timeout, 'true') if not is_locked() else False
    release_lock = lambda: r.delete(id_)
    if acquire_lock():
        try:
            wrapped_function(*args, **kwargs)
        finally:
            release_lock()
