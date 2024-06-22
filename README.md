English | 中文

goroutine-py

🚀 An Asyncio-based concurrency library for Python.

	Easy concurrency just like goroutine without worry about thread and coroutine in Python.



Introduction

Withing  goroutine.app.go you can run a coroutine or a func asynchronously.

Main function go :

go (obj: callable, *args, callback: callable = None, lock: bool = False)

	obj: Takes both callable coroutinefunction and func as object.

	*args: Arguments for your obj.

	callback: Attaches a callable that will be called when the future finishes.



Getting Started

Support:

    Python 3.7 / 3.8 / 3.9 / 3.10 / 3.11 / 3.12

Installation

First you have to install goroutine-py like this:

    pip install goroutine-py

Quick Tutorial

The primary entity of goroutine-py is goroutine.app.go.

You can simply start using goroutine-py like this:

First, define your tasks:

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

After you defined all your tasks and callback, you can go like this:

    go(task_1)
    go(task_2)
    
    # The "callback" parameter must be specified separately.
    go(task_1, 5, callback = callback)
    go(task_2, 3, callback = callback)
    print('END')
    
    # Forever runing to show results.
    while 1:
        time.sleep(5)

Output :

    >>>
    END
    Task_2_done
    Task_1_done
    Task_2_done
    -* callback *-
    Result_2
    Task_1_done
    -* callback *-
    Result_1

License

This project is licensed under the MIT License - see the LICENSE file for details.
