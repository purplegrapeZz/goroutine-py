import asyncio
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

# Callback func
def callback(result):
    '''
    Parameter "result" is the return from task.
    Use functools.partial() to give arguments if you need more args at the beginning.
    '''
    print('-* callback *-')
    print(result)


if __name__ == '__main__':
    go(task_1)
    go(task_2)

    # The "callback" parameter must be specified separately.
    go(task_1, 5, callback = callback)
    go(task_2, 3, callback = callback)
    print('END')

    # Forever runing to show results.
    while 1:
        time.sleep(5)
        
