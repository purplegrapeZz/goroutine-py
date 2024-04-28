# Copyright 2022 ZIHAN MA. All Rights Reserved.

'''
🚀 An Asyncio-based concurrency library for Python.
   Easy concurrency in Python. Just like goroutine.
'''

__author__ = 'ZIHAN MA (xudesoft@126.com)'

import asyncio
from threading import Thread
import functools
from asyncio.futures import Future


def _run() -> None:
    '''
    Start loop.
    '''
    _goroutine_loop.run_forever()


def _iscorfunc(obj: callable) -> bool:
    '''
    Check if obj a coroutinefunction.
    Return:
        True or Fale.
    '''
    return asyncio.iscoroutinefunction(obj)


async def _wrap_as_cor(obj: callable, *args) -> Future:
    '''
    Wrap a func as a coroutine.
    Return:
        A coroutine.
    '''
    res = await asyncio.to_thread(obj, *args)
    return res


async def _wrap_as_cor_withlock(obj: callable, *args) -> Future:
    '''
    Wrap a func as a coroutine with lock. Means thread safe.
    Return:
        A coroutine.
    '''
    async with _goroutine_loop_lock:
        res = await asyncio.to_thread(obj, *args)
        return res


def _wrap_as_func(obj: callable, future: Future) -> None:
    '''
    For callback func is given as a coroutine.
    '''
    asyncio.run_coroutine_threadsafe(obj(future), _goroutine_loop)


def _finish(future: Future, callback: callable) -> None:
    '''
    Do the callback.
    '''
    if callable(callback):
        if not _iscorfunc(callback):
            # Check if callback a func.
            future.add_done_callback(callback)
        else:
            future.add_done_callback(
                functools.partial(
                    _wrap_as_func, callback))
    else:
        raise TypeError(
            'A callable func or coroutinefunction object is required for callback.')


def go(obj: callable, *args, callback: callable = None, lock: bool = False) -> None:
    '''
    Run a coroutine or a func asynchronously.
    Easy concurrency in Python.
    Args:
        obj: Takes both callable coroutinefunction and func as object.
             Coroutinefunction runs as coroutine.
             Normal function runs as thread.
        *args: Arguments for your obj.
               You can also use functools.partial() for your func.
        callback: Attaches a callable that will be called when the future finishes.
                  Use functools.partial() to your callback func.
        lock: Thread safe if True. It can slow your program.
              This argument only work for "func" not "coroutinefunction".
    Return:
        None
    '''
    if callable(obj):
        '''
        Check if the given obeject callable.
        '''
        if _iscorfunc(obj):
            # If a coroutinefunction run this.
            future = asyncio.run_coroutine_threadsafe(obj(*args), _goroutine_loop)
            if callback:
                # Add callback func.
                _finish(future, callback)
        else:
            # Normal func runs as a thread.
            if lock:
                # Thread safe. Only for a normal func.
                cor = _wrap_as_cor_withlock(obj, *args)
            else:
                # Thread without lock.
                cor = _wrap_as_cor(obj, *args)
            future = asyncio.run_coroutine_threadsafe(cor, _goroutine_loop)
            if callback:
                _finish(future, callback)
    else:
        raise TypeError(
            'A callable func or coroutinefunction object is required')


# An asyncio-lock.
_goroutine_loop_lock = asyncio.Lock()

# Getting loop.
_goroutine_loop = asyncio.new_event_loop()

# Run the loop in a thread.
T = Thread(target=_run, daemon=True)
T.start()
