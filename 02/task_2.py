class Shop:

    OVERALL_NUMBER_OF_SALES = 0

    def __init__(self, name, sales=0):
        self._name = name
        self._number_of_sales = sales

    def set_sales(self):
        self._number_of_sales += 1
        Shop.OVERALL_NUMBER_OF_SALES += 1

    def get_sales(self):
        return self._number_of_sales

    def get_shop_name(self):
        return self._name


class Shop1(Shop):

    def __init__(self, name, sales=0):
        super().__init__(name, sales)


class Shop2(Shop):

    def __init__(self, name, sales=0):
        super().__init__(name, sales)


shop_1 = Shop1('ATB')
shop_2 = Shop2('EKO')

print(f'Name of first shop "{shop_1.get_shop_name()}"')
print(f'Name of second shop "{shop_2.get_shop_name()}"')

print(f'Overall sales from every shops {Shop.OVERALL_NUMBER_OF_SALES}')

print(f'Initial sales from first shop {shop_1.get_sales()}')
print(f'Initial sales from second shop {shop_2.get_sales()}')

shop_1.set_sales()
shop_2.set_sales()

print(f'Sales in first shop {shop_1.get_sales()}')
print(f'Sales in second shop {shop_2.get_sales()}')
print(f'Overall sales from every shops {Shop.OVERALL_NUMBER_OF_SALES}')