# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.
def restaurant_helper():
 menu_list=["Burger","Fries","Wrap","noodles","chickenwings","friedrice"]
 print(menu_list)
#AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

 customer_selected_items=input("Select the items from the menu: ").split()
 return customer_selected_items
 # As a user, I want to have my order read back to me in formated way so I know what I ordered.

print("order :" ,restaurant_helper())