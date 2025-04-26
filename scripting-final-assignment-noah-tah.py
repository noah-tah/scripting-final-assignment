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

DestroyedComputers = {
	"jeffrey": False,
	"billy": False,
	"theodore": False
}

def main (): 
	print("Welcome to the Three Little Pigs game!")
	print("You are a wolf, and you are trying to catch the three little pigs.")
	print("Why are you trying to catch them you ask?")
	print("It is because they've been mooching off grandma wolf's Wi-Fi!")
	print("They run a very popular Minecraft server, and it lags grandma wolf's Netflix.")
	print("You're trying to show your grandma wolf that anime isn't just for kids, but the pigs keep ruining it.")

	print("Thankfully, you don't have to go far, the pigs apartment complex is just behind grandma wolf's house.")
	print("You head over to the apartment complex, it's dark outside, but you can see the glow of their computer screens through the windows.")
	print("You can see that each of them are in their own apartments, likely playing Minecraft together.")
	print("The pigs reside in the following apartments:")
	print("1. Jeffrey Pig - Apartment 43-1")
	print("2. Billy Pig - Apartment 70-1")
	print("3. Theodore Pig - Apartment 421-1")

	print("Which pig do you want to catch first?")
	print("1. Jeffrey Pig")
	print("2. Billy Pig")
	print("3. Theodore Pig")

	choice = input("Enter the number of the pig you want to catch: ")

	if choice == "1":
		jeffreyPig()
	elif choice == "2":
		billyPig()
	elif choice == "3":
		theodorePig()
	else:
		print("Invalid choice. Please enter 1, 2, or 3.")
		main()


def jeffreyPig():
	print("You head to Jeffrey Pig's apartment.")
	print("You smell a skunk nearby, and you can hear an intense amount of clicking, they must be playing Minecraft.")
	print("You knock on the door, and Jeffrey Pig opens it.")
	print("He looks at you and says, 'What do you want? I'm trying to play Minecraft here!'")
	print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
	print("My server? It's not even my server, it's Billy's server!")

	print('You say, "Are you LYING to me?"')
	print("Jeffrey Pig looks at you and says, 'No, I'm not lying! I swear!'")

	print("There is a chance that Jeffrey Pig is lying to you.")
	print("You can either:")
	print("1. Decide he's lying and destroy his computer")
	print("2. Decide he's telling the truth and go get Billy Pig")

	choice = input("Enter the number of your choice: ")
	if choice == "1":
		destroyJeffreysComputer()
	elif choice == "2":
		print("You decide that Jeffrey Pig is telling the truth.")
		billyPig()
	else:
		print("Invalid choice. Please enter 1 or 2.")
		jeffreyPig()

def destroyJeffreysComputer():
	DestroyedComputers["jeffrey"] = True

	print("You decide that Jeffrey Pig is lying to you.")
	print("You destroy his computer, and he starts crying.")
	print("You feel bad for him, but you know you have to do it so grandma can learn that anime is totally awesome.")

	print('Jeffrey Pig says, "You\'re a monster! You just destroyed my computer, and i\'m not even the one hosting the server!"')
	print('"See? Look!" he holds up his phone and shows you a livestream of Billy Pig playing Minecraft on the server.')
	print('"I told you it wasn\'t my server!"')
	print("You feel bad for Jeffery Pig, but he told everyone he ordered a new PC last week.")
	print("You head over to Billy Pig's apartment.")

	billyPig()

def billyPig():
	print("You head over to Billy Pig's apartment.")
	print("You knock on the door, and Billy Pig opens it.")
	print("You can see that Billy Pig is playing Minecraft on the server.")
	print("You can also see that he has a new computer, and it looks like he just got it.")

	if DestroyedComputers["jeffrey"]:
		print('Billy Pig looks at you and says, "Have you heard from Jeffrey Pig? He suddenly stopped playing Minecraft."')
		print('"We were in a diamond mining competition, and I was about to win!"')
	else: 
		print("He looks at you and says, 'What do you want? I'm trying to play Minecraft here!'")

	print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
	print('"It\'s really important that I prove to grandma wolf that anime is not just for kids!"')
	print('"She needs to see that anime is a serious art form!"')
	print("Billy Pig looks at you and says, 'I don't care about your grandma, or anime! I'm trying to play Minecraft here!'")
	print('"Also, it\'s not even my server! It\'s Theodors\'s server!"')
	print('"He\'s the only one who knew how to set it up, and I just play on it!", he says.')

	print('You say, "Are you LYING to me?", you take a few steps closer to his computer.')
	print("Billy Pig looks at you and says, 'No, I'm not lying! I swear!'")

	print("There is a chance that Billy Pig is lying to you.")
	print("You can either:")
	print("1. Decide he's lying and destroy his computer")
	print("2. Decide he's telling the truth and go get Theodore Pig")

	choice = input("Enter the number of your choice: ")
	if choice == "1":
		destroyBillysComputer()
	elif choice == "2":
		theodorePig()
	else:
		print("Invalid choice. Please enter 1 or 2.")
		billyPig()

def destroyBillysComputer():
	DestroyedComputers["billy"] = True

	print("You decide that Billy Pig is lying to you.")
	print("You notice he has a shrine dedicated to his time on the high school baseball team, and it has a bat.")
	print("You grab the bat and smash his computer, the room going dark from the sudden lack of RGB lights.")
	print("Billy Pig starts crying, and you can see that he is really upset.")
	print("You feel bad for him, but you know you have to do it so grandma can learn that anime is totally awesome.")

	print('Billy Pig says, "You\'re a monster! You just destroyed my computer, and I\'m not even the one hosting the server!"')
	print('"See? Look!" he holds up his phone and shows you a livestream of Theodore Pig playing Minecraft on the server.')
	print('"I told you it wasn\'t my server!"')
	print("You feel bad for Billy Pig, but you know his parents are loaded anyways.")
	print("You head over to Theodore Pig's apartment.")

	theodorePig()

def theodorePig():
	print("You head over to Theodore Pig's apartment.")
	print("You knock on the door, and Theodore Pig opens it.")
	print("You can see that Theodore Pig is playing Minecraft on the server.")

	if DestroyedComputers["jeffrey"] and DestroyedComputers["billy"]:
		print('Theodore Pig looks at you and says, "Have you heard from Jeffrey Pig or Billy Pig? They suddenly stopped playing Minecraft."')
		print('"We were in a diamond mining competition, and I was about to knock them into the lava!"')
		print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
		print('"Both of their computer have been destroyed defending this server, and it\'s time to end this!')
	elif DestroyedComputers["jeffrey"] or DestroyedComputers["billy"]:
		destroyedPig = ""
		if DestroyedComputers["jeffrey"]:
			destroyedPig = "Jeffrey Pig"
		else:  # Must be Billy's computer that was destroyed
			destroyedPig = "Billy Pig"
		print(f'Theodore Pig looks at you and says, "Have you heard from {destroyedPig}? They suddenly stopped playing Minecraft."')
		print('"We were in a diamond mining competition, and I was about to knock them into the lava!"')
		print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
		print('"It\'s really important that I prove to grandma wolf that anime is not just for kids or weirdos!"')
		print('She needs to know that Naruto is not cringe, and that Attack on Titan isn\'t overrated!, you yell at a high pitch."')
	else:
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
	if choice == "1":
		destroyTheodoresComputer()
	elif choice == "2":
		rolePlayWithTheodore()

def destroyTheodoresComputer():
	DestroyedComputers["theodore"] = True
	print("You decide that you don't care about Theodore Pig's roleplay server. Grandma wolf and anime is more important.")
	print("You destroy his computer with a nearby life sized replica of the Master Sword.")
	print('Theodore screams "NOOOOOO!" and falls to his knees, crying.')
	print("You feel bad for him, but you know you have to do it so grandma and you can watch anime.")
	print("You head back to grandma wolf's house, and you can see that she\'s been waiting for you.")

def rolePlayWithTheodore():
	print("You decide to let Theodore Pig keep his computer.")
	print("You head inside and start playing Minecraft with him and grandma wolf.")
	print("You all have a great time, and you can see that grandma wolf is really enjoying herself.")
	print("You all play Minecraft for hours, and you can see that grandma wolf is really happy.")
	print("You feel good about yourself, and you know that you made the right choice.")

	print("The End")
	print("Thanks for playing!")


main()