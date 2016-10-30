from celery import shared_task

from project.celery import app
from project.decorators import decorator1, decorator2
from spicedtasks import (
    singleton_task,
    spiced_singleton_task,
)


@shared_task(name='Task name')
@decorator1
@singleton_task(60 * 15)
def decorated_function_main():
    for number in range(25):
        arg1 = number ** 2
        arg2 = number * 3 - 1
        app.send_task('Subtask name',
                      args=[arg1, arg2],
                      kwargs={'add_spices': number},
                      countdown=10,
                      expires=180,
                      queue='priority_mid')


@shared_task(name='Subtask name')
@decorator2
@spiced_singleton_task(60 * 15)
def decorated_function_sub(arg1, arg2):
    print('subtask is executed')
