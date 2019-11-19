from mongoengine import connect
import models

connect("web_shop_bot")

for i in range(5):
    obj = models.Category(**{'title': f'root{i}',
                             'description': f'descr{i}'}).save()

    obj.add_subcategory(
        models.Category(**{'title': f'sub{i}',
                           'description': f'descr{i}'})
    )

objects = models.Category.objects(parent__ne=None)

for i in objects:
    i.add_subcategory(
        models.Category(**{'title': f'sub-sub{i}',
                           'description': f'd{i}'})
    )
