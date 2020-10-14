#!/usr/bin/env python3

"""
Project Statement
The application shown has five errors. Find and fix the four errors so
that the program allows the user to input as many items and their
costs as desired and outputs a subtotal of the items and a total
cost including 6% sales tax.

#Kate Blunt
#Debugging Program

Fill in a description of the errors you found and how you fixed them below:
1. There was no colon after goodbye() and goodbye method was not called. 
2. In the while loop, the (and repeat.lower() = "n") should not be there. Repeat
can not equal yes and no at the same time.
3. Sub needs to be declared in the get_item method.
4. The value for tax should be .06, not .6. 
5. get_tax needs to return sub.
"""

def display_welcome():
    print("This program will create a wish list for the user.")
    print("Enter as many items as you like, with their costs")
    print("and the program will calculate your total, before and")
    print("after 6% tax.")

def get_item():
    sub = 0
    repeat = "y"
    while repeat.lower() == "y": # and repeat.lower() == "n":
        print("Enter an item? y/n ")
        repeat = input()
        if repeat.lower() == "y":
            print("Enter the name of your item: ")
            item_name = input()
            print("Enter the cost of this item: ")
            item_cost = float(input())
            item_cost = validate(item_cost)
            print("Item: ", item_name, " for $ ", round(item_cost, 2))
            sub = sub + item_cost
        else:
            
            print("Your subtotal is $", round(sub, 2))
            get_tax(sub)
            
            break      
                   
def validate(item_cost):
    while item_cost <= 0:
        print("Enter a valid cost for this item: ")
        item_cost = float(input())
    return item_cost

def get_tax(sub):
    tax = sub * .06
    total_cost = sub + tax
    print("Your total cost, including 6% tax, is $", round(total_cost,2))
    return sub
    goodbye()

def goodbye():
    print("Hope you get everything you wish for in 2020!")
    print("Goodbye!")

def main():
    display_welcome()
    get_item()
    print()
    goodbye() #this was not here 
    
# if started as the main module, call the main function
if __name__ == "__main__":
    main()

