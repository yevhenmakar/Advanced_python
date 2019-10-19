import time


def decorator(number_of_repeats=0):
    def outer(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(number_of_repeats):
                start = time.time()
                result = func(*args, **kwargs)
                print('Execution time is: ', time.time() - start)
                results.append(result)
            return results, func.__name__
        return wrapper
    return outer


@decorator(10)
def say_hello(name):
    greetings = f'Hello, {name}'
    return greetings


some_func = say_hello('Alex')

print(f'Function name "{some_func[1]}"')
