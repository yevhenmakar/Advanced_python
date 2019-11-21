from threading import Thread


def decorator(func):
    def wrapper(name, is_daemon):
        t = Thread(target=func, name=name, daemon=is_daemon)
        t.start()
    return wrapper
