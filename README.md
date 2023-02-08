# Cash Register

## Description
This is a cash register with a database stored in a file. We have the possibility to:

Shopping cart:
- Add items to the shopping cart,
- Remove items from the shopping cart,
- Show the shopping cart,

Database:
- Add objects to the database
- Remove objects from the database
- Show the database

Recipt:
- Show the receipt
- Resizing the receipt

Application:
- Stop the application


## Imports
```python
import os
import pprint
import sys
```

## DataBase class
```python
class Db():
    def __init__(self):
        self.directory = os.path.dirname(os.path.realpath(__file__))+'\\lista.txt'
        self.food_list = {}
        with open(self.directory) as file:
            for lines in file:
                try:
                    self.object = lines.split()
                    self.food_list.setdefault(self.object[0], dict(Quantity=self.object[1],Unit=self.object[2],Price=self.object[3]))
                except:
                    pass
                
    def add(self,item):
        if item[0].strip(' ')!='' and item[1].strip(' ')!='' and item[2].strip(' ')!='' and item[3].strip(' ')!='':
            with open(self.directory, 'a') as file:
                if item[0] not in self.food_list:
                    file.write(' '.join(item)+'\n')
                    self.food_list.setdefault(item[0], dict(Quantity=item[1],Unit=item[2],Price=item[3]))
                else:
                    print('This object is already in the database')
        else:
            print('\nThe name you entered has a wrong format\n')
            
    def remove(self, item):
        if item in Shopping_cart().shopping_cart:
            Shopping_cart().remove(item.title())
            
        if  item.strip(' ')!='':
            with open(self.directory, "r") as f:
                lines = f.readlines()
            with open(self.directory, "w") as f:
                for line in lines:
                    if not str(item+" ") in line:
                        f.write(line)
                    else:
                        print(f'Object "{item}" has been removed from the database')
                        self.food_list.pop(item)
        else:
            print('The name you entered has a wrong format')
            main()


```

## Recipt class
```python
class Recipt:
    def __init__(self):
        self.width = 45
        self.price_width = 10
        self.item_width = self.width - self.price_width
        self.total_price = 0
        
    def show(self,shopping_cart,db_food_list):
        self.format_name_price= '{{:{}}}{{:>{}}} '.format(self.item_width,self.price_width)
        self.format_quantity = '{{:^{}}} {{:<{}}} X {{:<{}.2f}}'.format(3,1,1)
        print(u'\u2704'+'-'*(self.width-2),'\n')
        print('{name:^{space}}'.format(space=self.width, name='STORE'),'\n')
        print('-'*self.width,'\n')
        print('{name:^{space}}'.format(space=self.width, name='STORE Angro SRL'))
        print('{name:^{space}}'.format(space=self.width, name='Country Timis, Timisoara'))
        print('{name:^{space}}'.format(space=self.width, name='Street, number'))
        print('{name:^{space}}'.format(space=self.width, name='Fiscal identification code: RO12345678 \n'))
        print('-'*self.width)
        print(self.format_name_price.format('Items','Price(Lei)'))
        print('-'*self.width,'\n')
        for items in shopping_cart:
            self.price_right = float(db_food_list[items.title()]['Price']) * shopping_cart[items] / float(db_food_list[items.title()]['Quantity']) 
            print(self.format_name_price.format(items.title() , '{:.2f}'.format(self.price_right)))
            print(self.format_quantity.format(shopping_cart[items],db_food_list[items.title()]['Unit'], float(db_food_list[items.title()]['Price'])))
            print()
            self.total_price +=self.price_right
        print('-'*self.width)
        print(self.format_name_price.format('Total', '{:.2f} Lei'.format(self.total_price)))
        print('-'*self.width,'\n')
        print('{name:^{space}}'.format(space=self.width, name='Thank you for buying from us'.upper()),'\n')
        print('{name:^{space}}'.format(space=self.width, name='receipt'.title())+'\n'+u'\u2704'+'-'*(self.width-2),'\n')

    def resize(self, width=45, price_width=10):
        self.width = width
        self.price_width = price_width
        self.item_width = self.width - self.price_width

```

## Shopping cart class
```python
    def __init__(self):
        self.shopping_cart = {}
        
    def add(self, item, db_food_list):
        if item[0].title() in db_food_list.keys():
            if item[0] in self.shopping_cart:
                self.shopping_cart[item[0]]+=item[1]
            else:
                self.shopping_cart.setdefault(item[0].title(),item[1])
        else:
            print('The object you wanted to add to the shopping cart does not exist in the database')
            
    def remove(self, item):
        if item in self.shopping_cart:
            self.shopping_cart.pop(item)
        else:
            print('The object is not in the shopping cart')
        
    def show(self):
        print('Shopping cart: \n',self.shopping_cart)

```

## Main function
```python
def main():
    db = Db()
    recipt = Recipt()
    shopping_cart = Shopping_cart()
    width = 45
    
    def again(number):
        again = int(input('Do you want to repeat this action one more time?\n1: for yes\n2: for no '))
        if again == 1:
            menu_action(number)
        else:
            menu_show()
            
    def menu_action(number):
        if number == 1:
            nume_obiect = input('Give the name of the object you want to add to the shopping cart: ')
            quantity_obiect = float(input('Enter the quantity of the item you want to add to the shopping cart: '))
            shopping_cart.add((nume_obiect.title(),quantity_obiect), db.food_list)
            again(1)
            
        elif number == 2:
            name = input('Give the name of the object you want to remove from the shopping cart: ')
            shopping_cart.remove(name.title())
            again(2)
            
        elif number == 3:
            shopping_cart.show()
            menu_show()
            
        elif number == 4:
            name = input('Give the name of the object: ')
            quantity = input('Give the quantity of the object: ')
            unit = input('Give the unit of measure of the object: ')
            price = input('Give the price of the object: ')
            db.add([name.title(), quantity, unit, price])
            again(4)
            
        elif number == 5:
            name = input('Give the name of the object you want to remove from the database: ')
            db.remove(name.title())
            again(5)
            
        elif number == 6:
            print('\nDatabase: ')
            pprint.pprint(db.food_list)
            menu_show()
            
        elif number == 7:
            recipt.show(shopping_cart.shopping_cart , db.food_list)
            menu_show()
            
        elif number == 8:
            size = int(input('Enter the size you want to resize: '))
            recipt.resize(size)
            menu_show()
            
        elif number == 9:
            sys.exit()
            
    def menu_show():
        print('\nTo navigate the menu, you must select one of the options and write the corresponding number\n')
        print('-'*width)
        print('1 : Add items to the shopping cart')
        print('2 : Remove items from the shopping cart')
        print('3 : Show the shopping cart')
        print('-'*width)
        print('4 : Add objects to the database')
        print('5 : Remove objects from the database')
        print('6 : Show the database')
        print('-'*width)
        print('7 : Show the receipt')
        print('8 : Resize the recipt')
        print('-'*width)
        print('9 : Exit')
        print('-'*width+'\n')
        try:
            answer = int(input('Give the number corresponding to the desired option: '))
            assert 0 < answer < 10
            menu_action(answer)
        except Exception as exception:
            menu_show()
            print(exception)
    menu_show()
```

## Main 
```python
main()
```


