# Copyright 2022 ZIHAN MA. All Rights Reserved.

'''
🚀 An Asyncio-based concurrency library for Python.
   Easy concurrency in Python. Just like goroutine.
'''

__author__ = 'ZIHAN MA (xudesoft@126.com)'

import asyncio
from threading import Thread
from typing import Any

def _run() -> None:
    '''
    Start loop.
    '''
    _goroutine_loop.run_forever()


def _iscor(obj: callable) -> bool:
    '''
    Check if obj a coroutinefunction.
    Return:
        True or Fale.
    '''
    return asyncio.iscoroutinefunction(obj)


async def _wrap_cor(_cor, *args, callback = None) -> None:
    '''
    Handle the obj.
    And will put this wrapper to the loop.
    Return:
        None.
    '''
    res = await _cor

    # Handle the callback func from user.
    if callable(callback):
        if _iscor(callback):
            await callback(res) if res else callback()
        else:
            await _wrap_func(callback, res) if res else _wrap_func(callback)


async def _wrap_func(func: callable, *args) -> Any:
    '''
    For normal func, run as a thread.
    Return:
        Result of func.
    '''
    res = await asyncio.to_thread(func, *args)
    return res


def go(obj: callable, *args, callback: callable = None) -> None:
    '''
    Run a coroutine or a func asynchronously.
    Easy concurrency in Python.
    Args:
        obj: Takes both callable coroutinefunction and func as object.
             Coroutinefunction runs as coroutine.
             Normal function runs as thread.
        *args: Arguments for your obj.
               You can also use functools.partial() for your func.
        callback: Attaches a callable that will be called when the cor finishes.
    Return:
        None
    '''
    if callable(obj):
        # Check if the given obeject callable.
        if _iscor(obj):
            # If a coroutinefunction run this.
            future = asyncio.run_coroutine_threadsafe(_wrap_cor(obj(*args), callback=callback),  _goroutine_loop)
        else:
            # If normal func, runs as a thread.
            future = asyncio.run_coroutine_threadsafe(_wrap_cor(_wrap_func(obj, *args), callback=callback), _goroutine_loop)
    else:
        raise TypeError(
            'A callable func or coroutinefunction object is required')


# Getting loop.
_goroutine_loop = asyncio.new_event_loop()

# Run the loop in a thread.
T = Thread(target=_run, daemon=True)
T.start()
