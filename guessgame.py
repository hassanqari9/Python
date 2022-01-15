import random 
print("""
          _.----.                          
       .-"       \-.                       
      /           ; \                      
     :           /:  \                     
     ;         .'  ;  ;                    
     ;      .-"    :  :                    
    :   _.+(   .-- :  :                    
    ;  ;   ' :  :                    
    ;  :           ;  ;                    
    :   ;    -    :  :                     
     )  '   .-.   '  :                     
    (    '. `"' .'   ;                     
     "-._.:`---':-"-.'+'                   
          ;     ;    "                     
   _..__.-. -. (:                          
 ,'   .:(o);     "-._                      
 :    _: 0 ;        \`.                    
 ;  .'/.\-/-.        `:                    
:  : :  -U--:"-.  \    ;                   
;  ; :  ----;   "-.L.-" \                  
'. '  \ ---(      ;O:    ;                 
  \ '. '-;-'      :-:    :                 
   `. ""/         ; :    ;                 
     ""T      .-":  :`. /                  
       :  --""   :   ; Y                   
        ;        ;   : :                   
        :       :     ; ;                  
         ;      :   ; : :                  
         :      ;   :  ; \                 
          ;    :    ;  :  \_               
          :    :        \  \"-.            
          ;    ;         \  `. "-.         
         :    :     c     \   `./"-._      
         ;    :            \    \    "-.   
        :     ;             `.   ;-.  -.`. 
        :    :       __..--"" \  :  `.\.`.\
        ;    :_..--"";  ;  _.-'\  ;   ")))T
       :     ;      _L.-'""     ; :    '-='
       ;    :_..--""            :  ;       
      /     ;                   ;; :       
    .'     /                    ;: J       
    `.    /                     ;'"        
      :-.'         /\           ;          
      ;           /  ;          :          
     :           /   :          :          
     ;          /     ;         :          
    :          /      ;         :          
    ;         /       :         :          
   :         /        :         :    
WELCOME TO GUESSING GAME😋
      """)
level = input("Choose difficulty level\nEasy or Hard: ").lower()

random_number = random.randint(1,100)

if level == "easy":
  life = 10
  print(f"Life:{life}")
elif level == "hard":
  life = 5
  print(f"Life:{life}")
else:
  print("Only Choose between Easy or Hard")
print("Guess a number between 1-100")
while(life > 0):
    guess = int(input("Guess the number: "))
    if guess < random_number:
      print("Guess higher")
      life -= 1
      print(f"Life:{life}")
      
    elif guess > random_number:
      print("Guess lower")
      life -= 1
      print(f"Life:{life}")
      
    elif guess == random_number:
      print("You won 🎉")
      life = -1

if life == 0:
  print("You lost 🔫")
