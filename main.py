print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

movement1 = input("Where do you want to go? Left or Right?").lower()

if movement1 == "left":
    print('''
                 |
          _,  iO_|
         /_ \_|  /
           )     '-,
          | ._.-: (`;
           \|   //
       _.-'```"""``"-._
    /"`                '.
    `':.,_               "._
         \`'-._             `'-._
          \    `:._              `'-._          _
          |      \ `:_                `"--"--"``
          |       \   `:_
          |      :|    \ '.
          |       |     |  `:_
          |       |:    |     `:_
          |:      |     |
          |       |
          |
  ''')
    movement2 = input("You come to an edge of cliff. Wild animals are behind you? Jump or wait? ").lower()
    if movement2 == "jump":
        print("You manage to escape and grab a tree. Small injuries but you okay.")
        print('''
     ______________
    |\ ___________ /|
    | |  _ _ _ _  | |
    | | | | | | | | |
    | | |-+-+-+-| | |
    | | |-+-+=+%| | |
    | | |_|_|_|_| | |
    | |    ___    | |
    | |   [___] ()| |

    | |         ||| |
    | |         ()| |
    | |           | |
    | |           | |
    | |           | |
    |_|___________|_| 
    ''')
        movement3 = input("You come across a golden door. Will you open it? Yes or No?").lower()
        if movement3 == "yes":
            print('''
      ______________
    |\ ___________ /|
    | |  /|,| |   | |
    | | |,x,| |   | |
    | | |,x,' |   | |
    | | |,x   ,   | |
    | | |/    |%==| |
    | |    /] ,   | |
    | |   [/ ()   | |
    | |       |   | |
    | |       |   | |
    | |       |   | |
    | |      ,'   | |
    | |   ,'      | |
    |_|,'_________|_|
      ''')
            print("Right before your eyes, there is a golden chest. You did it! You found the chest!")
        elif movement3 == "no":
            print('''
        ____
        \___\_.:::::::.___
        /___/ '::::::: 

      You stood so long in front of golden door. You got poisoned by traps and now you are dead. Game over.''')
    elif movement2 == "wait":
        print('''
                      ___
                    ,'---`.
                  /\l^L^j/\\n
                  f---\-/---Y
              ,--`---j"l---'--.
              f , _, -. ,- ._ ` Y
              |f /l    Y    j\,|
              l (  \-"-^-"-/  ) j
              `.`. Y`-^-'f .','
                l_)|`-^-'|(_j   _____
                  ,'` -^- '`.,-'",  < "`-.
                f`--------'|> <  > , > ' `-.      _.,-----.
                l`--------'l < ' ,--.  < >  `---"',  '_,--.`-.._,
                  \`--------'`-.,'    `.  , '< > ,  ,'"     "`--'
                  `._______.-'"        `-._____.,-'   

    I guess, wild animals will have a nice dinner this night. You are inveted... as main food. Game over.''')
elif movement1 == "right":
    print('''
    )       )     
    ) \    ) \     
  / ) (   / ) (   
  \(_)/   \(_)/   

  You directly fell into a trap. You died by burning. Game over.''')