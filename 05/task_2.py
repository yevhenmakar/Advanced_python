from threading import Thread
import urllib.request
import time

list_of_urls = ['http://wingware.com/images/screenshots/wing7-screenshot-dark.png',
                'https://wingware.com/images/news/2019-02-08/dracula.png',
                'https://cdn0.capterra-static.com/screenshots/2127621/140420.png',
                'https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2019/08/August19-jupyterdebug.gif',
                'https://code.visualstudio.com/assets/docs/python/jupyter/interactive-window-intellisense.gif']


def decorator(name, is_daemon):
    def outer(func):
        def wrapper(*args):
            t = Thread(target=func, name=name, args=args, daemon=is_daemon)
            print(f'{t.name} starts')
            start = time.time()
            t.start()
            print(f'{t.name} finished')
            print(f'Execution time of {t.name} is: ', time.time() - start)
        return wrapper
    return outer


@decorator(name='', is_daemon=False)
def some_func(url, name):
    print('Start downloading')
    urllib.request.urlretrieve(url, name)
    print('Downloading completed')


for i in list_of_urls:
    file_name = i.split('/')[-1]
    some_func(i, file_name)
