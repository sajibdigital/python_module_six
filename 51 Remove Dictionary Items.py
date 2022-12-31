car = {
    'brand':'Ford',
    'model':'Mustang',
    'year':'2010',
    'color':'Black'
}

# print(car.get('brand'))
# car.update({'color':'Blue'})

car.pop('color')
car.pop('year')
car.pop('model')
car.pop('brand')

print(car)