English | [中文](https://github.com/purplegrapeZz/goroutine-py/blob/master/README-CN.md)

### goroutine-py

🚀 An Asyncio-based concurrency library for Python.

​	Easy concurrency just like goroutine without worry about thread and coroutine in Python.

# Introduction

Withing  ``goroutine.app.go`` you can run a coroutine or a func asynchronously.

Main function ___go___ :

#####  go _(obj: callable, *args, callback: callable = None, lock: bool = False)_

​	___obj:___ Takes both callable coroutinefunction and func as object.

​	___*args:___ Arguments for your obj.

​	___callback:___ Attaches a callable that will be called when the future finishes.

​	___lock:___ Thread safe if True. It can slow your program.

​		 This argument only work for "func" not "coroutinefunction".

# Getting Started

## Installation

First you have to install goroutine-py like this:

```
pip install goroutine-py
```

## Quick Tutorial

The primary entity of goroutine-py is ``goroutine.app.go``.
You can simply start using goroutine-py like this:

First, define your tasks:

```
import asyncio
import functools
import time
from goroutine.app import go

# A normal func
def task_1(n=2):
    time.sleep(n)
    print('Task_1_done')
    return 'Result_1'
```

```
# A coroutinefunction
async def task_2(n=1):
    await asyncio.sleep(n)
    print('Task_2_done')
    return 'Result_2'
```

```
# Callback func
def callback(future, arg=None):
    '''
    At least ONE Parameter "future" is required.
    This future is a concurrent.futures.Future.
    Use functools.partial() to give arguments for your callback func.
    '''
    print(future.result(),arg)
```
After you defined all your tasks and callback, you can go like this:

```
go(task_1)
go(task_2)
go(task_1, 4, callback=callback)
go(task_2, 2, callback=functools.partial(callback,arg='a'))
print('END')
```

Output :

```
>>>
END
Task_2_done
Task_1_done
Task_2_done
Result_2 a
Task_1_done
Result_1 None
```

# License

This project is licensed under the MIT License - see the `LICENSE` file for details.
