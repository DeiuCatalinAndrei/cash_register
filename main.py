import os
import pprint
import sys

class Db():
    def __init__(self):
        self.directory = os.path.dirname(os.path.realpath(__file__))+'\\lista.txt'
        self.food_list = {}
        with open(self.directory) as file:
            for lines in file:
                try:
                    self.object = lines.split()
                    self.food_list.setdefault(self.object[0], dict(Price=self.object[3],quantity=self.object[1],Unit=self.object[2]))
                except:
                    pass
                
    def add(self,item):
        with open(self.directory, 'a') as file:
            if item[0] not in self.food_list:
                file.write(' '.join(item)+'\n')
                self.food_list.setdefault(item[0], dict(Price=item[3],quantity=item[1],Unit=item[2]))
            else:
                print('This object is already in the database')
    
    def remove(self, item):
        if item.strip()!= "":
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
class Recipt:
    def __init__(self):
        self.width = 45
        self.price_width = 10
        self.item_width =self.width - self.price_width
        self.Total_price = 0
        
    def show(self,shopping_cart,db_food_list):
        self.format_name_price= '{{:{}}}{{:>{}}} '.format(self.item_width,self.price_width)
        self.format_quantity = '{{:^{}}} {{:<{}}} X {{:<{}.2f}}'.format(3,1,1)
        self.db_food_list = db_food_list
        self.shopping_cart = shopping_cart
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
        for items in self.shopping_cart:
            self.Price1 = float(self.db_food_list[items.title()]['Price']) * self.shopping_cart[items] / float(self.db_food_list[items.title()]['quantity']) 
            print(self.format_name_price.format(items.title() , '{:.2f}'.format(self.Price1)))
            print(self.format_quantity.format(self.shopping_cart[items], self.db_food_list[items.title()]['Unit'], float(self.db_food_list[items.title()]['Price'])))
            print()
            self.Total_price+=self.Price1
        print('-'*self.width)
        print(self.format_name_price.format('Total', '{:.2f} Lei'.format(self.Total_price)))
        print('-'*self.width,'\n')
        print('{name:^{space}}'.format(space=self.width, name='Thank you for buying from us'.upper()),'\n')
        print('{name:^{space}}'.format(space=self.width, name='receipt'.title())+'\n\n'+u'\u2704'+'-'*(self.width-2),'\n')

    def resize(self, width=45, price_width=10):
        self.width = width
        self.price_width = price_width
        self.item_width =self.width - self.price_width

db = Db()
class Shopping_cart():
    def __init__(self):
        self.shopping_cart = {}
        
    def add(self, item, db_food_list = db.food_list):
        if item[0].title() in db_food_list.keys():
            if item[0] in self.shopping_cart:
                self.shopping_cart[item[0]] +=item[1]
            else:
                self.shopping_cart.setdefault(item[0],item[1])
        else:
            print('The object you wanted to add to the shopping cart does not exist in the database')
            
    def remove(self, item):
        if item in self.shopping_cart:
            self.shopping_cart.pop(item)
        else:
            print('The object is not in the shopping cart')
        
    def show(self):
        print(self.shopping_cart)

def main():
    shopping_cart = Shopping_cart()
    recipt = Recipt()
    width = 45
    def again(number):
        try:
            again = int(input('Do you want to repeat this action one more time? 1: for yes, 2: for no '))
            if again == 1:
                menu(number)
            else:
                menu_show()
        except:
            menu_show()
    def menu(number):
        if number == 1:
            try:
                nume_obiect = input('Give the name of the object you want to add to the shopping cart: ')
                quantity_obiect = int(input('Enter the quantity of the item you want to add to the shopping cart: '))
                shopping_cart.add((nume_obiect.title(),quantity_obiect))
                again(1)
            except:
                pass
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
            pprint.pprint(db.food_list)
            menu_show()
        elif number == 7:
            recipt.show(shopping_cart.shopping_cart , db.food_list)
            menu_show()
        elif number == 8:
            try:
                size = int(input('Enter the size you want to resize: '))
                recipt.resize(size)
                menu_show()
            except:
                pass
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
            assert 0 <answer < 10
            menu(answer)
        except:
            menu_show()
    menu_show()

main()

