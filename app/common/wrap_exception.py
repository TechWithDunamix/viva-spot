import functools
import asyncio
from nexios.http import Response, Request

def wrap_exception(exception, handler):
    def decorator(func):
        @functools.wraps(func)
        async def async_wrapper(req :Request, res :Response):
            try:
                return await func(req, res)
            except exception as e:
                return handler(req, res, e)

        def sync_wrapper(req :Request, res :Response):
            try:
                return func(req, res)
            except exception as e:
                return handler(req, res, e)

        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper

    return decorator
