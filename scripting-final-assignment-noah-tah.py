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

def main (void): 
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
		billyPig()
	else:
		print("Invalid choice. Please enter 1 or 2.")
		jeffreyPig()

def destroyJeffreysComputer():
	print("You decide that Jeffrey Pig is lying to you.")
	print("You destroy his computer, and he starts crying.")
	print("You feel bad for him, but you know you have to do it so grandma can learn that anime is totally awesome.")

	print('Jeffrey Pig says, "You\'re a monster! You didn\'t even stop the server, you just destroyed my computer!"')
	print('"See? Look!" he holds up his phone and shows you a livestream of Billy Pig playing Minecraft on the server.')
	print('"I told you it wasn\'t my server!"')
	print("You feel bad for Jeffery Pig, but you know his parents are loaded anyways.")
	print("You head over to Billy Pig's apartment.")

	billyPig()

def billyPig():
	print("You head over to Billy Pig's apartment.")
	print("You knock on the door, and Billy Pig opens it.")
	print("He looks at you and says, 'What do you want? I'm trying to play Minecraft here!'")
	print('You say, "Your minecraft server is lagging grandma wolf\'s Netflix and we can\'t watch anime!"')
	print("My server? It's not even my server, it's Theodore's server!")

	print('You say, "Are you LYING to me?"')
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

	


main()