# EXERCISE- 1 
# Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

shopping_list=[]
def create_list(entered_items):
    shopping_list.append(entered_items)

def main():
    while True:
        
        user_choice = input ('Select an action for your shopping list (add/delete/show/quit): ')
        if user_choice == 'add' :
            entered_items = input ( 'Enter an item to your shopping list: ')
            create_list(entered_items)
        elif user_choice == 'delete':
            deleted_item = input ('What do you want to remove from your shopping list? ')
            print(f'{deleted_item} had been deleted from your shopping list.')
            shopping_list.remove(deleted_item)    
        elif user_choice == 'show':
            print(shopping_list)
        elif user_choice == 'quit':
            break
           
    #return(shopping_list) 
    print(f'This is your updated shopping list: {shopping_list}')
main()