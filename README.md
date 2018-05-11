# CROIT: celery redis one instance task
This module provides utils for creating one instance tasks with celery (using Redis).

## Examples
- Simple one instance task.

  (`60*15` - redis cached lock id maximum lifetime in seconds. When task is ended, lock will be deleted automatically.)
```
@shared_task(name='Task name')
@singleton_task(60 * 15)
def mytask():
    print('task execution')
```

- Parameterized one instance task. Look at `kwargs={'add_spices': number)`.

  (`60*15` - redis cached lock id maximum lifetime in seconds. When task is ended, lock will be deleted automatically.)
```
@shared_task(name='Task name')
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
@spiced_singleton_task(60 * 15)
def mytask():
    print('subtask execution')
```
