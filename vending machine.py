#Toki Pona Vending Machine
#Based on ZenOokami's code
#www.EssenceOfZen.org
#Version 1.0

start = "\033[1m" #The start and end variables are to make bold text in Python
end = "\033[0;0m"
money = 10.00 #This will be the money used to purchase the snacks
vending_machine = {"pan suwi":"0A", "telo suwi":"0B", "telo pi lape ala":"0C", "kili lili":"0D", "moku soweli":"0E", "namako 1 GBP lon poki sina":"1A", "namako 2 GBP lon poki sina":"1B", "namako 5 GBP lon poki sina":"1C", "namako 10 GBP lon poki sina":"1D", "namako 20 GBP lon poki sina":"1E", "namako mani wile lon poki sina":"1F"} #We created this hash (python calls them dictionaries) to list the items and their selection
prices = {"pan suwi":"0.75 GBP", "telo suwi":"0.50 GBP", "telo pi lape ala":"1.25 GBP", "kili lili":"0.25 GBP", "moku soweli":"0.75 GBP", "namako "+start+"1 GBP"+end+" lon poki sina":"", "namako "+start+"2 GBP"+end+" lon poki sina":"", "namako "+start+"5 GBP"+end+" lon poki sina":"", "namako "+start+"10 GBP"+end+" lon poki sina":"", "namako "+start+"20 GBP"+end+" lon poki sina":"", "namako mani wile lon poki sina":""} #We created this hash to have the same keys as the first hash, but this time having prices be their values

#==Debug Functions==================================
def set_money(amount): #This function is used to set the amount of money
	global money
	money = amount
	

#===================================================
def purchase(needed_money): #Made this for personal ease. It simply keeps track of money after checking to see if you can buy said item.
	global money
	if money >= needed_money:
		money -= needed_money
		print("ijo pana")
	else:
		print("ni li mani wile ala")

def transaction(user_input): #Function is made to take care of choosing said item, it then calls the "purchase" funciton
	global money
	if user_input == "0A":
		purchase(0.75)
	elif user_input == "0B":
		purchase(0.50)
	elif user_input == "0C":
		purchase(1.25)
	elif user_input == "0D":
		purchase(0.25)
	elif user_input == "0E":
		purchase(0.75)
	elif user_input == "1A":
		purchase(-1)
	elif user_input == "1B":
		purchase(-2)
	elif user_input == "1C":
		purchase(-5)
	elif user_input == "1D":
		purchase(-10)
	elif user_input == "1E":
		purchase(-20)
	elif user_input == "1F":
		maniWile = float(input("mani la mute seme li sina wile lon poki sina?")) #Adds a desired value to your account
		maniWile = maniWile*-1
		purchase(maniWile)
	else:
		print("sina sitelen li pakala")
	
			
#==============================================================	
		

def main(): #Main program 
	item_list = []
	switch = 1 #In case you want to add a "different person" system
	while switch == 1:
		print("toki a! ni li ilo wile.") #Welcome Messages
		print("ni li wile sina!")
		for item, selection in vending_machine.items(): #This for loop will append items to the list item_list
			item_list.append((item, selection))
		
		print(item_list[::-1]) #Print backwards so that it goes from top to the bottom.
		
		print()
		print("ni li mani esun")
		for item, price in prices.items(): #Prints the items and their prices on separate lines.
			print(item, price)
		print()
		
		user_switch = 1 #User Proof loop
		while user_switch == 1:
			print("sina jo e " + str(money) + " GBP")
			user_input = input("mi wile la o kepeken poki wile sina: ").upper()
			transaction(user_input)
			print()
			choice = 1
			while choice == 1: #User proof loop
				user_input = input("sina pini kepeken e ni anu seme?(k/a): ").lower()
				if user_input == "k" or user_input == "kepeken":
					user_switch = 0
					choice = 0
					switch = 0
				elif user_input == "a" or user_input == "ala":
					user_switch = 1
					choice = 0
				else:
					print("sina sitelen li pakala")
					choice = 1
			
		print("sina pona tawa kepeken ni ilo.")
		print("mi pali ni kepeken sitelen lawa pi jan ZenOokami")
					
				
			
		
main()
