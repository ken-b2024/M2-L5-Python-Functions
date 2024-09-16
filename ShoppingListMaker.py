shopping_items = ['milk', 'bread']

def add_item():
        action = input("Please add your item: ")
        shopping_items.append(action)
        print(*shopping_items, sep='\n')
def remove_item():
        action = input("What items would you like to remove? ")
        shopping_items.remove(action)
        print(shopping_items)
def view_list():
        print('Shopping Items:', *shopping_items, sep='\n- ')

while True:
    user_input = input("Would you like to add an item to the list? (yes/no) ")
    if user_input == 'yes':
          add_item()
    user_input = input("Would you like to remove any items? (yes/no) ")
    if user_input == 'yes':
        remove_item()
    user_input = input("Would you like to view your shopping list? (yes/no) ")
    if user_input == 'yes':
        view_list()