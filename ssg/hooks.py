_callbacks = {}


def register(hook, order=0):
    def register_callback(func):
        """
        responsible for adding default key value pairs to the _callbacks
        dictionary.
        """
        _callbacks.setdefault(hook, {}).setdefault(order, []).append(func)
        return func
    return register_callback


def event(hook, *args):
    """Fires an event."""
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            func(*args)


def filter(hook, value, *args):
    """Capture the result of the callback."""
    for order in sorted(_callbacks.get(hook, {})):
        for func in _callbacks[hook][order]:
            value = func(value, *args)
    return value
