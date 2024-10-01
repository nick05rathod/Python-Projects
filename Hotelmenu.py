#menu of restaurant
menu={'Pizza':50,
      'Pasta':80,
      'Burger':60,
      'Coffee':50}
print(menu)

print("Welcome to Cafeteria")
print("Pizza:Rs50\nPasta:Rs80\nBurger:Rs60\nCoffee:Rs50")
 

order_cost=0
item_1=input("What do you want to order: ")
if item_1 in menu:
  print("You ordered:",(item_1))
  order1_cost=order_cost+menu[item_1]
  print(order1_cost)
else:
  print("We do not have",(item_1))
another_item=input("Do you want to add another item?(yes/no)")
if another_item=='yes':
  item_2=input("What do you want to order next: ")
  if item_2 in menu:
    print("You ordered:",(item_2))
    order2_cost=order1_cost+menu[item_2]
    print(order2_cost)
    print("your total order_cost:",(order2_cost))
  else:
    print("We do not have",(item_1))
else:
    print(order1_cost)
