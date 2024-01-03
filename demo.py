import asyncio
import functools
import time
from goroutine.app import go


# A normal func
def task_1(n=2):
    time.sleep(n)
    print('Task_1_done')
    return 'Result_1'

# A coroutinefunction
async def task_2(n=1):
    await asyncio.sleep(n)
    print('Task_2_done')
    return 'Result_2'

# callback func
def callback(future, arg=None):
    '''
    At least ONE Parameter "future" is required.
    This future is a concurrent.futures.Future.
    Use functools.partial() to give arguments for your callback func.
    '''
    print(future.result(),arg)


if __name__ == '__main__':
    go(task_1)
    go(task_2)
    go(task_1, 4, callback=callback)
    go(task_2, 3, callback=functools.partial(callback,arg='a'))
    print('END')
