'''Plan:
You wake up in a cold stone cell. There are 2 doors, 1 is a staircase downwards and 1 is a hallway. both are lit
DOWN or UP
    DOWN
    you descend further into the tunnel, turning a corner or two as you go.
    it gets colder and there aren't any lights. Do you RETURN or CONTINUE?
        RETURN
        you are now in a different room with a staircase leading up.
        as you head up the the staircase the air grows warmer around you
        at the top you meet a man who's entirely engulfed in flame. He asks why you're here, do you FIGHT or REASON
            FIGHT
            you died.

            REASON
            the man is very understanding, helps warm your hands, and shows you the exit. You step out into the warm spring air and 
            feel as if a heavy burden has lifted off your shoulders.

        CONTINUE
        you descend deeper and after a bend you see a light up ahead. 
        upon reaching the light you find a room with food and a candle.
        there is another path continuing through the room though. EXPLORE or STAY?
            STAY
            you are warm, you are happy, and you fall asleep to the delicious scent of bread baking never to wake again.

            EXPLORE
            you push bravely forwards into the next hallway. It twists and turns but you keep your hand on the wall so as to not get lost. 
            hours later the ever-increasing cold and mind-bending passageways bring you to your knees, then to the ground. So cold...
            so cold...
    UP
    you pass a few other empty rooms like yours, none with windows. Eventually you reach a hall in which there's a great feast being held. 
    you are invited to stay and eat by many jolly strangers, begging you to enjoy the feast. STAY or LEAVE?
        STAY
        there are only 3 foods in the entire banquet hall, even though hundreds are dining. Huge platters full of chicken and ornate goblets of wine, 
        as well as periodic small bowls of carefully cleaned pomegranate. "The fruit is delicious! Come, eat!"
        do you eat FRUIT or CHICKEN?
            FRUIT
            oh it's very good, so sweet and luscious and bursting with flavor. You may as well stay for a while and have some more.
            Leave? You can't leave now! It's too delicious, too enticing. You can leave later.
            Or not. Why leave at all? Nobody is going anywhere. You'll be happier here anyway...

            CHICKEN
            You politely take some chicken, which is pretty tasty, before heading for the door.
            As the door cracks open you feel wind and smell springtime in the air. A warm gust announces 
            the door's complete opening and you step out into the midday sunlight. Free at last! 
        LEAVE
        You walk past the beckoning crowd and push open the large front door of the hall.
        As the door cracks open you feel wind and smell springtime in the air. A warm gust announces 
        the door's opening and you step out into the midday sunlight. Free at last!

'''

print("Welcome to the adventure game!")
print("You wake up in a cold stone cell. \nThere are 2 doors, 1 is a staircase downwards and 1 is a hallway. Both are lit. \nDo you go DOWN or STRAIGHT?")
dec1 = input("").lower()
if dec1 == "down":
    print("You descend further into the tunnel, turning a corner or two as you go. \nIt gets colder and there aren't any more lights. Do you RETURN or CONTINUE?")
    dec2 = input("").lower()
    if dec2 == "continue":
        print("You descend deeper and after one last bend you see a light up ahead.") 
        print("Upon reaching the light you find a room with some food, a candle and a bed.")
        print("There is another path continuing through the room. EXPLORE or STAY?")
        dec3 = input("").lower()
        if dec3 == "explore":
            print("You bravely push forwards into the next hallway. It twists and turns but you keep your hand on the wall to avoid getting lost.") 
            print("Hours later the ever-increasing cold and mind-bending passageways bring you to your knees, then to the ground. So cold...")
            print("So cold...")
        elif dec3 == "stay":
            print("You are warm, you are happy, and you fall asleep ")
            print("to the delicious scent of bread baking. Never to wake again.")
        else:
            print("Crippled by indecision, your consciousness fades away...")
    elif dec2 == "return":
        print("You return to find that you are now in a different room with only a staircase leading up.")
        print("As you head up the the staircase the air grows warmer around you.")
        print("At the top you meet a man who's entirely engulfed in flame. He asks why you're here. Do you FIGHT or REASON?")
        dec3 = input("").lower()
        if dec3 == "fight":
            print("YOU DIED\n")
        elif dec3 == "reason":
            print("The man is very understanding. He helps warm your hands and shows you the exit.") 
            print("You step out into the warm spring air and feel as if a heavy burden has lifted off your shoulders.")
        else:
            print("Crippled by indecision, your consciousness fades away...")
    else:
            print("Crippled by indecision, your consciousness fades away...")
elif dec1== "straight":
    print("You pass a few other empty rooms like yours, none with windows.") 
    print("Eventually you reach a hall in which there's a great feast being held.") 
    print("You are invited to stay and eat by many jolly strangers, begging you to enjoy the feast. STAY or LEAVE?")
    dec2 = input("").lower()
    if dec2 == "stay":
        print("There are only a few different foods in the banquet hall, even though hundreds are dining.") 
        print("Huge platters full of chicken and ornate goblets of wine, as well as periodic small bowls of carefully cleaned pomegranate.") 
        print('"The fruit is delicious! Come, eat!" Do you eat FRUIT or CHICKEN?')
        dec3 = input("").lower()
        if dec3 == "fruit":
            print("Oh it's very good. Sweet and luscious and bursting with flavor. You may as well stay for a while and have some more.")
            print("Leave? You can't leave now! It's too delicious, too enticing. You can leave later.")
            print("Or not. Why leave at all? Nobody is going anywhere. You'll be happier here anyway...")
        elif dec3 == "chicken":
            print("You politely take some chicken, which is pretty tasty, before heading for the door.")
            print("As the door cracks open you feel wind and smell springtime in the air. A warm gust complements") 
            print("the door's complete opening and you step out into the midday sunlight. Free at last!")
        else:
            print("Crippled by indecision, your consciousness fades away...")
    elif dec2 == "leave":
        print("You walk past the beckoning crowd and push open the large front door of the hall.")
        print("As the door cracks open you feel wind and smell springtime in the air. A warm gust complements") 
        print("the door's opening and you step out into the midday sunlight. Free at last!")
    else:
            print("Crippled by indecision, your consciousness fades away...")
else:
            print("Crippled by indecision, your consciousness fades away...")

print("THE END")
