[English](https://github.com/purplegrapeZz/goroutine-py/blob/master/README.md) | 中文

### goroutine-py

🚀 基于Asyncio的Python并发库.

​	在Python中像goroutine一样使用线程和协程.

# 介绍

您可以通过  ``goroutine.app.go`` 异步地使用线程和协程.

主函数 ___go___ :

#####  go _(obj: callable, *args, callback: callable = None, lock: bool = False)_

​	___obj:___ 接受协程方法或普通方法.

​	___*args:___ 任务方法需要的参数.

​	___callback:___ 任务结束后的回调函数.

​	___lock:___ 线程安全参数, 只在线程(传入普通函数)中有效.



# 开始
## 支持

	Python 3.7 / 3.8 / 3.9 / 3.10 / 3.11 / 3.12

## 安装

安装 goroutine-py :

```
pip install goroutine-py
```

## 教程

goroutine-py 的主要函数是 ``goroutine.app.go``.
简单两步学会使用goroutine-py:

首先, 定义你的任务函数:

```
import asyncio
import functools
import time
from goroutine.app import go

# 普通函数
def task_1(n=2):
    time.sleep(n)
    print('Task_1_done')
    return 'Result_1'
```

```
# 协程函数
async def task_2(n=1):
    await asyncio.sleep(n)
    print('Task_2_done')
    return 'Result_2'
```

```
# 回调函数
def callback(future, arg=None):
    '''
    至少需要声明一个 "future" 参数.
    future 是 concurrent.futures.Future.
    使用 functools.partial() 为回调函数传递参数.
    '''
    print(future.result(),arg)
```
go分配你的任务 :

```
go(task_1)
go(task_2)
go(task_1, 4, callback=callback)
go(task_2, 2, callback=functools.partial(callback,arg='a'))
print('END')
```

输出 :

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

# 执照

使用 MIT License - 详情参见 `LICENSE` 文件.
