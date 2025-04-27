'''
Noah Tah
4/25/2025
Scripting Final Assignment
Programming II
Evan Vaverka
Northwestern Oklahoma State University
Assignment Description:
	Three Little Pigs

	Stolen Wi-Fi – The pigs have been mooching off the wolf's Wi-Fi, and he's sick of their Minecraft server lagging his Netflix.
'''
import os
import time

DestroyedComputers = {
	"jeffrey": False,
	"billy": False,
	"theodore": False
}

def clearScreen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

def waitForInput():
    # Wait for the user to press Enter to continue
    input("\nPress Enter to continue...")
    clearScreen()

def main (): 
    clearScreen()
    print("Welcome to the Three Little Pigs game!")
    print("You are a wolf, and you are trying to catch the three little pigs.")
    print("\nWhy are you trying to catch them you ask?")
    print("\nIt is because they've been mooching off grandma wolf's Wi-Fi!")
    print("They run a very popular Minecraft server, and it lags grandma wolf's Netflix.")
    print("You're trying to show your grandma wolf that anime isn't just for kids, but the pigs keep ruining it.")

    print("\nThankfully, you don't have to go far, the pigs apartment complex is just behind grandma wolf's house.")
    print("You head over to the apartment complex, it's dark outside.")
    print("You can see the glow of their computer screens and RGB lights through the windows.")
    print("You can see that each of them are in their own apartments, likely playing Minecraft together.")


    print("\nWhich pig do you want to catch first?")
    print("1. Jeffrey Pig - Apartment 43-1")
    print("2. Billy Pig - Apartment 70-1")
    print("3. Theodore Pig - Apartment 421-1")

    choice = input("\nEnter the number of the pig you want to catch: ")
    print("You chose: " + choice)
    waitForInput()
    
    if choice == "1":
        jeffreyPig()
    elif choice == "2":
        billyPig()
    elif choice == "3":
        theodorePig()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        waitForInput()
        main()


def jeffreyPig():
    clearScreen()
    print("You head to Jeffrey Pig's apartment.")
    print("\nYou hear an intense amount of clicking and keyboard smashing. It sounds like he's really into the game.")
    print("You knock on the door, and Jeffrey Pig opens it quickly, nearly yanking the door off the hinges.")

    print("\nHe looks at you and says, 'What do you want? I'm trying to play Minecraft here!'")

    print('\nYou say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
    print("\nMy server? It's not even my server, it's Billy's server!")

    print('\nYou say, "Are you LYING to me?"')
    print("\nJeffrey Pig looks at you and says, 'No, I'm not lying! I swear!'")

    print("\nThere is a chance that Jeffrey Pig is lying to you.")
    print("You can either:")
    print("1. Decide he's lying and destroy his computer")
    print("2. Decide he's telling the truth and go get Billy Pig")

    choice = input("\nEnter the number of your choice: ")
    print("You chose: " + choice)
    waitForInput()
    
    if choice == "1":
        print("You decide that Jeffrey Pig is lying to you.")
        waitForInput()
        destroyJeffreysComputer()
    elif choice == "2":
        print("You decide that Jeffrey Pig is telling the truth.")
        waitForInput()
        billyPig()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        waitForInput()
        jeffreyPig()

def destroyJeffreysComputer():
    clearScreen()
    DestroyedComputers["jeffrey"] = True

    print("You take his life-sized replica of the Minecraft Diamond Sword and smash his computer with it.")

    print("\nYou feel bad for him, but you know you have to do it.")
    print("This is for grandma wolf and anime, and you know she would want yout to do this.")

    print('\nJeffrey Pig yells, "You\'re a monster! You just destroyed my computer!"')
    print("I am not even the one hosting the server!")
    print('"See? Look!" he holds up his phone and shows you a livestream of Billy Pig playing Minecraft on the server.')
    print('"I told you it wasn\'t my server!"')
    print("\nYou feel bad for Jeffery Pig, but he told everyone he ordered a new PC last week.")
    print("He needs a break from Minecraft anyways, and you know he will be fine.")
    print("\nYou leave his apartment, carrying the life-sized replica of the Minecraft Diamond Sword.")
    waitForInput()
    billyPig()

def billyPig():
    clearScreen()
    if DestroyedComputers["jeffrey"]:
        print("You head to Billy Pig\'s apartment, carrying the life-sized replica of the Minecraft Diamond Sword.")
        print("You knock with the Minecraft Diamond Sword, and Billy Pig opens it.")
        print("You see that Billy Pig has Minecraft running on his computer.")
        print("You can also see that he has a new computer, and it looks like he just got it.")
        print('Billy Pig says, "Have you heard from Jeffrey Pig? He suddenly stopped playing Minecraft."')
        print('"We were in a diamond mining competition, and I was about to win!"')
        print('"Wait... why do you have a life-sized replica of the Minecraft Diamond Sword?"')
    else: 
        print("You head over to Billy Pig\'s apartment.")
        print("You knock on the door, and Billy Pig opens it.")
        print("He says, 'What do you want? I'm trying to play Minecraft here!'")

    print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
    print('"It\'s really important I prove to grandma wolf that anime is full of important life lessons!"')
    print('"She needs to see that anime is a serious art form! It\'s not just for kids or weirdos!"')
    print('"It\'s not just for kids or weirdos", you yell at a high pitch."')
    print("Billy Pig replies, 'I don't care about your grandma, or anime! I'm trying to play Minecraft here!'")
    print('"Also, it\'s not even my server! It\'s Theodore\'s server!"')
    print('"It\'s Theodore\'s server!"')
    print('"He\'s the only one who knew how to set it up!"')
    print('"I just play on it and post about it on TikTok!", he says')
    print('You say, "Are you LYING to me?", you take a few steps closer to his computer.')
    print("Billy Pig looks at you and says, 'No, I'm not lying! I swear!'")

    print("There is a chance that Billy Pig is lying to you.")
    print("You can either:")
    print("1. Decide he's lying and destroy his computer")
    print("2. Decide he's telling the truth and go get Theodore Pig")

    choice = input("Enter the number of your choice: ")
    print("You chose: " + choice)
    waitForInput()
    if choice == "1":
        destroyBillysComputer()
    elif choice == "2":
        theodorePig()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        waitForInput()
        billyPig()

def destroyBillysComputer():
    clearScreen()
    DestroyedComputers["billy"] = True
    if DestroyedComputers["jeffrey"]:
        print("You decide that Billy Pig is lying to you.")
        print("You take the replica of the Minecraft Diamond Sword and smash his computer with it.")
        print('"Boy this sword is great for smashing computers!", you say maniacally.')
    else:
        print("You decide that Billy Pig is lying to you.")
        print("You notice he has a shrine dedicated to his time on the high school baseball team.")
        print("You notice that included in the shrine is a baseball bat, and it looks like it has been signed by the entire team.")
        print("With the baseball bat, you smash his computer, starting with the peripherals, ending with the tower.")

    print("After smashing the computer, the room goes dark from the sudden lack of RGB lights.")
    print('Billy pig is shocked and horrified, and he stands there hands spread to his sides yelling, "NOOOOOO!", Darth Vader style.')
    print("You feel bad for him, but you know you have to do it so grandma can learn that anime can be enjoyed by all ages.")

    print('Billy Pig says, "You\'re a monster! You just destroyed my computer, and I\'m not even the one hosting the server!"')
    print('"See? Look!" he holds up his phone and shows you a livestream of Theodore Pig playing Minecraft on the server.')
    print('"I told you it wasn\'t my server!"')
    print("You feel bad for Billy Pig, but you know his parents are loaded anyways.")
    print('"You can thank Jeffrey Pig for this, he\'s the one who told me to come here in an effort to save the server, hope it was worth it."')

    theodorePig()

def theodorePig():

    clearScreen()
    if DestroyedComputers["jeffrey"] and DestroyedComputers["billy"]:
        print("You head over to Theodore Pig's apartment, carrying the life-sized replica of the Minecraft Diamond Sword.")
        print("You knock on the door with the sword, and Theodore Pig opens it, it smells strongly as he opens the door.")
        print("You can see that Theodore Pig is playing Minecraft on the server.")
        print('Theodore Pig looks at you and says, "Have you heard from Jeffrey Pig or Billy Pig? They suddenly stopped playing Minecraft!')
        print('"We were in a diamond mining competition, and I was about to knock them into the lava... ", he stops and looks at the sword.')
        print('"Wait, why do you have Jeffrey Pig\'s life-sized replica of the Minecraft Diamond Sword?"')
        print('"Both of their computers have been destroyed defending this server, and it\'s time to end this!", you exclaim to Theodore Pig.')
    elif DestroyedComputers["jeffrey"] or DestroyedComputers["billy"]:
        destroyedPig = ""
        if DestroyedComputers["jeffrey"]:
            destroyedPig = "Jeffrey Pig"
        else:  # Must be Billy's computer that was destroyed
            destroyedPig = "Billy Pig"
        print("You head over to Theodore Pig\'s apartment.")
        print("You knock on the door, and Theodore Pig opens it. It smells strongly as he opens the door.")
        print("You can see that Theodore Pig is playing Minecraft on the server.")
        print(f'Theodore Pig looks at you and says, "Have you heard from {destroyedPig}? They suddenly stopped playing Minecraft."')
        print('"We were in a diamond mining competition, and I was about to knock them into the lava!"')
        if destroyedPig == "Jeffrey Pig":
            print('"Wait, why do you have a life-sized replica of the Minecraft Diamond Sword?"')
        elif destroyedPig == "Billy Pig":
            print('"Wait, why do you have Billy Pig\'s baseball bat? He never lets anyone touch it!", Theodore Pig says nervously.')
        else:
            print("You head over to Theodore Pig\'s apartment, and you knock on the door.")
            print("Theodore Pig opens it, and as the door opens, it smells strongly inside.")
            print("You can see that Theodore Pig is playing Minecraft on the server.")
            print('Theodore Pig looks at you and says, "What do you want? I\'m trying to play Minecraft here!"')

    print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
    print('"It\'s really important that I prove to grandma wolf that anime is not just for kids or weirdos!"')
    print('She needs to know that Naruto is not cringe, and that Attack on Titan isn\'t overrated!, you yell at a high pitch."')

    print('Theodore Pig looks at you and says, "Dude, calm down. I forgot to pay my internet bill, but you don\'t understand! This server HAS to stay up!"' )
    print('I run the most popular roleplay server on Minecraft, and I need it so we can play Minecraft Dungeons and Dragons!"')
    print('"I was going to be a grey dwarf bard, and I was going to howl sweet melodies into the night!')
    print('"How about you and grandma wolf come play with us? We can roleplay Sword Art Online, and you can be Kirito!')

    print("Theodore Pig has presented us with a interesting choice, Kirito is a pretty cool character.")

    print("You can either:")
    print("1. Decide you don't care, and destroy his computer for ruining you and grandma wolf's anime time")
    print("2. Decide to let him keep his computer, and go play Minecraft with him and grandma wolf")

    choice = input("Enter the number of your choice: ")
    print("You chose: " + choice)
    waitForInput()
    if choice == "1":
        destroyTheodoresComputer()
    elif choice == "2":
        rolePlayWithTheodore()

def destroyTheodoresComputer():
    clearScreen()
    DestroyedComputers["theodore"] = True
    if DestroyedComputers["jeffrey"] and DestroyedComputers["billy"]:
        print("You decide that Theodore Pig is lying to you.")
        print("You take the life-sized replica of the Minecraft Diamond Sword and smash his computer with it.")
        print('"You think you can just run a server on my grandma\'s Wi-Fi and get away with it?"')
        print('Theodore Pig looks at you and cries out, "We could have worked this out! You\'re a monster!"')
    elif DestroyedComputers["jeffrey"] or DestroyedComputers["billy"]:
        destroyedPig = ""
        if DestroyedComputers["jeffrey"]:
            destroyedPig = "Jeffrey Pig"
        else:  # Must be Billy's computer that was destroyed
            destroyedPig = "Billy Pig"
        if destroyedPig == "Billy Pig":
            print("You decide that Theodore Pig is lying to you.")
            print("You take the baseball bat and smash his computer with it.")
            print('"You think you can just run a server on my grandma\'s Wi-Fi and get away with it?"')
            print('Theodore Pig looks at you and cries out, "We could have worked this out! You\'re a monster!"')
        else:
            print("You decide that Theodore Pig is lying to you.")
            print("You find a nearby replica of the Master Sword from the Legend of Zelda, and you smash his computer with it.")
            print('"You think you can just run a server on my grandma\'s Wi-Fi and get away with it?"')
            print('Theodore Pig looks at you and cries out, "We could have worked this out! You\'re a monster!"')
    print("You feel bad for Theodore Pig, but you know you and grandma wolf will have a great time watching anime together now.")
    print("You head back to grandma wolf's house, and you can see that she is really happy.")
    print("You sit down with her and start watching anime together.")
    print("You can see that she is really enjoying herself, and you know that you made the right choice.")

    # For the ending, you might want to just wait before clearing
    print("The End")
    print("Thanks for playing!")
    input("\nPress Enter to exit...")

def rolePlayWithTheodore():
    clearScreen()
    print("You decide to let Theodore Pig keep his computer.")
    print("You head inside and start playing Minecraft with him and grandma wolf.")
    print("You all have a great time, and you can see that grandma wolf is really enjoying herself.")
    print("You all play Minecraft for hours, and you can see that grandma wolf is really happy.")
    print("You feel good about yourself, and you know that you made the right choice.")

    # For the ending, you might want to just wait before clearing
    print("The End")
    print("Thanks for playing!")
    input("\nPress Enter to exit...")


main()