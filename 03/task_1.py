import time


def decorator(num_of_repeats=1):

    def actual_decorator(func):

        def wrapper(*args, **kwargs):

            results = []
            for i in range(num_of_repeats):
                execution_time = time.time()
                result = func(*args, **kwargs)
                print(execution_time)
                results.append(result)
                final_time = execution_time - time.time()
            return results, func.__name__, final_time
        return wrapper
    return actual_decorator


@decorator(10)
def say_hello(name):
    pass


some_func = say_hello('Alex')

print(f'Execution time {some_func[2]}')
print(f'Function name "{some_func[1]}"')
