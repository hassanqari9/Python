print("""
________._________
|      | \   -   /
|  ||  |  \  -  /
|  ||  |___\___/
|  ||  |     X
|      |    
|      |   
|______| 
| ____ | 
||coffee__________
||____|           |
|_________________|    
      
      """)

MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash" : 0,
}
cash = 0
def casher(sum,coffee):
  if sum > MENU[coffee]["cost"]:
    change = sum - MENU[coffee]["cost"]
    print(f"Here is ur {coffee} ☕️")
    print(f"Your change:${change} 🪙")
    global cash
    cash += MENU[coffee]["cost"]
    resources["cash"] = cash
  else:
    print("Error:insufficient balance")

def repeat():
  coffee = input("What would u like to have?(expresso/latte/cappuccino/report): ")
  if coffee == "report":
    print(resources)
    repeat()
  print("Plz insert coins: ")
  quarters = float(input("Quarters: "))*0.25
  dimes =float(input("Dimes: "))*0.10
  nickles = float(input("Nickles: "))*0.05
  pennies = float(input("Pennies: "))*0.01
  sum = quarters+dimes+nickles+pennies
  

  if resources["water"]>=MENU[coffee]["ingredients"]["water"] and resources["milk"]>=MENU[coffee]["ingredients"]["milk"] and resources["coffee"]>=MENU[coffee]["ingredients"]["coffee"]:
    
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    casher(sum,coffee)
  else:
    print("Not enough resources. Money has been refunded")
  repeat()
repeat()  
  
