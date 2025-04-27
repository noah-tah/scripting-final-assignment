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
    waitForInput()
    print("Why are you trying to catch them you ask?")
    print("\nIt is because they've been mooching off grandma wolf's Wi-Fi!")
    print("They run a very popular Minecraft server, and it lags grandma wolf's Netflix.")
    waitForInput()
    print("You're trying to show your grandma wolf that anime isn't just for kids, but the pigs keep ruining it.")

    print("The pigs apartment complex is just behind grandma wolf's house, so you decided to head over there.")
    waitForInput()
    print("You head over to the apartment complex, it's dark outside.")
    print("You can see that each of them are in their own apartments, likely playing Minecraft together.")
    print("\nYou can see the glow of their computer screens and RGB lights through the windows.")
    waitForInput()


    print("Which pig do you want to catch first?")
    print("1. Jeffrey Pig - Apartment 43-1")
    print("2. Billy Pig - Apartment 70-1")
    print("3. Theodore Pig - Apartment 421-1")

    choice = input("\nEnter the number of the pig you want to catch: ")
    print("You chose: " + choice)
    waitForInput()

    if choice == "1":
        print("You head over to Jeffrey Pig's apartment.")
        waitForInput()
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
    print("You hear an intense amount of clicking and keyboard smashing. It sounds like he's really into the game.")

    print("\nYou knock on the door, and Jeffrey Pig opens it quickly, nearly yanking the door off the hinges.")
    print("He looks at you and says, 'What do you want? I'm trying to play Minecraft here!'")

    print('\nYou say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
    print("\nMy server? It's not even my server, it's Billy's server!")
    waitForInput()

    print('You say, "Are you LYING to me?"')
    print("\nJeffrey Pig looks at you and says, 'No, I'm not lying! I swear!'")

    print("\nThere is a chance that Jeffrey Pig is lying to you.")
    print("\nYou can either:")
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
    waitForInput()

    print('Jeffrey Pig yells, "You\'re a monster! You just destroyed my computer!"')
    print("I am not even the one hosting the server!")
    print('\n"See? Look!" he holds up his phone and shows you a livestream of Billy Pig playing Minecraft on the server.')
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
        print("\nYou see that Billy Pig has Minecraft running on his computer.")
        print("You can also see that he has a new computer, and it looks like he just got it.")
        waitForInput()
        print('Billy Pig says, "Have you heard from Jeffrey Pig? He suddenly stopped playing Minecraft."')
        print('"We were in a diamond mining competition, and I was about to win!"')
        print('\n"Wait... why do you have a life-sized replica of the Minecraft Diamond Sword?"')
        waitForInput()
    else: 
        print("You head over to Billy Pig\'s apartment.")
        print("You knock on the door, and Billy Pig opens it.")
        print("\nHe says, 'What do you want? I'm trying to play Minecraft here!'")
        waitForInput()
    print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
    print('\n"I must prove to grandma wolf that anime teaches life lessons!"')
    print('\n"Anime is a serious art form!"')
    waitForInput()
    print("\nBilly Pig replies, 'I don't care about your grandma, or anime! I'm trying to play Minecraft here!'")
    print('"Also, it\'s not even my server!"')
    print('"\nIt\'s Theodore\'s server!"')
    print('"He\'s the only one who knew how to set it up!"')
    print('\n"I just play on it and post about it on TikTok!", he says')
    waitForInput()
    print('You say, "Are you LYING to me?", you take a few steps closer to his computer.')
    print("\nBilly Pig looks at you and says, 'No, I'm not lying! I swear!'")

    print("There is a chance that Billy Pig is lying to you.")
    print("\nYou can either:")
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
    waitForInput()

    print("After smashing the computer, the room goes dark from the sudden lack of RGB lights.")
    print('\nBilly pig is shocked and horrified, and he stands there hands spread to his sides yelling, "NOOOOOO!", Darth Vader style.')
    print("\nYou feel bad for him, but you know you have to do it so grandma can learn that anime can be enjoyed by all ages.")
    waitForInput()

    print('Billy Pig says, "You\'re a monster! You just destroyed my computer, and I\'m not even the one hosting the server!"')
    print('\n"See? Look!" he holds up his phone and shows you a livestream of Theodore Pig playing Minecraft on the server.')
    print('"I told you it wasn\'t my server!"')
    waitForInput()

    print("You feel bad for Billy Pig, but you know his parents are loaded anyways.")
    print('\n"You can thank Jeffrey Pig for this, he\'s the one who told me to come here in an effort to save the server, hope it was worth it."')
    waitForInput()
    
    theodorePig()

def theodorePig():
    clearScreen()
    if DestroyedComputers["jeffrey"] and DestroyedComputers["billy"]:
        print("You head over to Theodore Pig's apartment, carrying the life-sized replica of the Minecraft Diamond Sword.")
        print("You knock on the door with the sword, and Theodore Pig opens it, it smells strongly as he opens the door.")
        print("\nYou can see that Theodore Pig is playing Minecraft on the server.")
        waitForInput()
        
        print('Theodore Pig looks at you and says, "Have you heard from Jeffrey Pig or Billy Pig? They suddenly stopped playing Minecraft!')
        print('"We were in a diamond mining competition, and I was about to knock them into the lava... ", he stops and looks at the sword.')
        print('\n"Wait, why do you have Jeffrey Pig\'s life-sized replica of the Minecraft Diamond Sword?"')
        waitForInput()
        
        print('"Both of their computers have been destroyed defending this server, and it\'s time to end this!", you exclaim to Theodore Pig.')
        waitForInput()
    elif DestroyedComputers["jeffrey"] or DestroyedComputers["billy"]:
        destroyedPig = ""
        if DestroyedComputers["jeffrey"]:
            destroyedPig = "Jeffrey Pig"
        else:  # Must be Billy's computer that was destroyed
            destroyedPig = "Billy Pig"
            
        print("You head over to Theodore Pig\'s apartment.")
        print("You knock on the door, and Theodore Pig opens it. It smells strongly as he opens the door.")
        print("\nYou can see that Theodore Pig is playing Minecraft on the server.")
        waitForInput()
        
        print(f'Theodore Pig looks at you and says, "Have you heard from {destroyedPig}? They suddenly stopped playing Minecraft."')
        print('"We were in a diamond mining competition, and I was about to knock them into the lava!"')
        waitForInput()
        
        if destroyedPig == "Jeffrey Pig":
            print('"Wait, why do you have a life-sized replica of the Minecraft Diamond Sword?"')
        elif destroyedPig == "Billy Pig":
            print('"Wait, why do you have Billy Pig\'s baseball bat? He never lets anyone touch it!", Theodore Pig says nervously.')
        waitForInput()
    else:
        print("You head over to Theodore Pig\'s apartment, and you knock on the door.")
        print("Theodore Pig opens it, and as the door opens, it smells strongly inside.")
        print("\nYou can see that Theodore Pig is playing Minecraft on the server.")
        print('Theodore Pig looks at you and says, "What do you want? I\'m trying to play Minecraft here!"')
        waitForInput()

    print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
    print('"It\'s really important that I prove to grandma wolf that anime is not just for kids or weirdos!"')
    print('\nShe needs to know that Naruto is not cringe, and that Attack on Titan isn\'t overrated!", you yell at a high pitch.')
    waitForInput()

    print('Theodore Pig looks at you and says, "Dude, calm down. I forgot to pay my internet bill, but you don\'t understand! This server HAS to stay up!"')
    print('\nI run the most popular roleplay server on Minecraft, and I need it so we can play Minecraft Dungeons and Dragons!"')
    print('"I was going to be a grey dwarf bard, and I was going to howl sweet melodies into the night!')
    waitForInput()
    
    print('"How about you and grandma wolf come play with us? We can roleplay Sword Art Online, and you can be Kirito!')
    print("\nTheodore Pig has presented us with an interesting choice, Kirito is a pretty cool character.")
    waitForInput()

    print("You can either:")
    print("1. Decide you don't care, and destroy his computer for ruining you and grandma wolf's anime time")
    print("2. Decide to let him keep his computer, and go play Minecraft with him and grandma wolf")

    choice = input("\nEnter the number of your choice: ")
    print("You chose: " + choice)
    waitForInput()
    
    if choice == "1":
        destroyTheodoresComputer()
    elif choice == "2":
        rolePlayWithTheodore()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        waitForInput()
        theodorePig()

def destroyTheodoresComputer():
    clearScreen()
    DestroyedComputers["theodore"] = True
    
    if DestroyedComputers["jeffrey"] and DestroyedComputers["billy"]:
        print("You decide that Theodore Pig is lying to you.")
        print("You take the life-sized replica of the Minecraft Diamond Sword and smash his computer with it.")
        print('\n"You think you can just run a server on my grandma\'s Wi-Fi and get away with it?"')
        print('\nTheodore Pig looks at you and cries out, "We could have worked this out! You\'re a monster!"')
    elif DestroyedComputers["jeffrey"] or DestroyedComputers["billy"]:
        destroyedPig = ""
        if DestroyedComputers["jeffrey"]:
            destroyedPig = "Jeffrey Pig"
        else:  # Must be Billy's computer that was destroyed
            destroyedPig = "Billy Pig"
            
        if destroyedPig == "Billy Pig":
            print("You decide that Theodore Pig is lying to you.")
            print("You take the baseball bat and smash his computer with it.")
            print('\n"You think you can just run a server on my grandma\'s Wi-Fi and get away with it?"')
            print('\nTheodore Pig looks at you and cries out, "We could have worked this out! You\'re a monster!"')
        else:
            print("You decide that Theodore Pig is lying to you.")
            print("You find a nearby replica of the Master Sword from the Legend of Zelda, and you smash his computer with it.")
            print('\n"You think you can just run a server on my grandma\'s Wi-Fi and get away with it?"')
            print('\nTheodore Pig looks at you and cries out, "We could have worked this out! You\'re a monster!"')
    waitForInput()
    
    print("You feel bad for Theodore Pig, but you know you and grandma wolf will have a great time watching anime together now.")
    print("\nYou head back to grandma wolf's house, and you can see that she is really happy.")
    waitForInput()
    
    print("You sit down with her and start watching anime together.")
    print("\nYou can see that she is really enjoying herself, and you know that you made the right choice.")
    waitForInput()

    print("The End")
    print("Thanks for playing!")
    input("\nPress Enter to exit...")

def rolePlayWithTheodore():
    clearScreen()
    print("You decide to let Theodore Pig keep his computer.")
    print("\nYou head inside and start playing Minecraft with him and grandma wolf.")
    waitForInput()
    
    print("You all have a great time, and you can see that grandma wolf is really enjoying herself.")
    print("\nYou all play Minecraft for hours, and you can see that grandma wolf is really happy.")
    waitForInput()
    
    print("You feel good about yourself, and you know that you made the right choice.")
    waitForInput()

    print("The End")
    print("Thanks for playing!")
    input("\nPress Enter to exit...")


main()