dict_of_countries = {'Ukraine': 'Kyiv', 'England': 'London', 'France': 'Paris'}
list_of_countries = ['Ukraine', 'Germany', 'France']

for i in list_of_countries:
    if i in dict_of_countries:
        print(dict_of_countries[i])
