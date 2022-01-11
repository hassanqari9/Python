print('''
                888                888        888                   
                888                888        888                   
                888                888        888                   
 .d8888b 8888b. 888 .d8888b888  888888 8888b. 888888 .d88b. 888d888 
d88P"       "88b888d88P"   888  888888    "88b888   d88""88b888P"   
888     .d888888888888     888  888888.d888888888   888  888888     
Y88b.   888  888888Y88b.   Y88b 888888888  888Y88b. Y88..88P888     
 "Y8888P"Y888888888 "Y8888P "Y88888888"Y888888 "Y888 "Y88P" 888     
                                                                         
      ''')
print('''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      
      ''')
def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mult(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mult,
  "/" : div,
}

def func():
  stop = False
  n1 = int(input("First num: "))
  while stop is False:
    operation = input("Operation? ")
    n2 = int(input("Second num: "))
    cal = operations[operation]
    ans = cal(n1,n2)
    print(f"Ans={ans}")
    ask = input("do u want to continue calculating this no? if yes then type y if not then type n\n")
    if ask == "y":
      n1 = ans
    elif ask == "n":
      stop = True
      func()
func()
    
