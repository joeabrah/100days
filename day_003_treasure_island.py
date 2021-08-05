print('''
                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `)
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `|
//
''')
print("Welcome to Treasure Island!")
print('Your mission is to find the hidden treasure.')

enter = input('You\'re at the door to the castle with the treasure inside, will you enter? Type "yes" or "no": ').lower()
if enter == "yes":
    direction = input('You enter the castle, and can go left or right only. Which direction do you choose? Type "left" or "right": ').lower()
    if direction == "left":
        guard = input('You go left, and run into a castle guard along the way. Type "fight" to fight the guard, or "leave" to leave the castle and give up: ')
        if guard == "fight":
            new_direction = input('You fought the guard and won! Type "left" to go left after the guard, and "straight" to continue on down the hallway: ')
            if new_direction == "straight":
                print('You eventually get to the end of the hallway, and buried under the floor is the treasure! Congratulations!!!')
            else:
                print('You got lost in the castle and eventually made your way to the mess hall. There, you were captured by the King\'s loyal knights')
        else:
            print('The guard chased you down and arrested you. No treasure for you!')
    else:
        print('You fled the castle, and gave up your treasure :(')
else:
    print('It looks like you turned around, and fell into the moat.')

