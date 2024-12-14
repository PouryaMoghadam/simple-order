from functools import wraps


def async_view(view_func):
    """
    Decorator to mark a view as asynchronous.
    """
    @wraps(view_func)
    async def _wrapped_view(*args, **kwargs):
        return await view_func(*args, **kwargs)
    return _wrapped_view