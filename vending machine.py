#Python 3.3 Vending Machine
#By ZenOokami
#www.EssenceOfZen.org
#Version 1.0

money = 10.00 #This will be the money used to purchase the snacks
vending_machine = {"Chips":"0A", "Soda":"0B", "Chocolate":"0C", "Fruit Snacks":"0D"} #We created this hash (python calls them dictionaries) to list the items and their selection
prices = {"Chips":"$0.75", "Soda":"$0.50", "Chocolate":"$1.25", "Fruit Snacks":"$.25"} #We created this hash to have the same keys as the first hash, but this time having prices be their values


#==Debug Functions==================================
def set_money(amount): #This function is used to set the amount of money
	global money
	money = amount
	


#===================================================
#==Normal Functions=================================
def get_stock(): #Old Function -- do not use. It functioned when I was keep track of number of stocks
	stock = vending_machine.values()
	i = 0
	for amount in stock:
		i += amount
	print(i)
	
def purchase(needed_money): #Made this for personal ease. It simply keeps track of money after checking to see if you can buy said item.
	global money
	if money >= needed_money:
		money -= needed_money
		print("Item Vended.")
	else:
		print("Not enough money.")

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
	else:
		print("Invalid Input")
	
			
#==============================================================	
		

def main(): #Main program 
	item_list = []
	switch = 1 #Incase you want to add a "different person" system
	while switch == 1:
		print("Welcome to the Vending Machine program.") #Welcome Messages
		print("Here are your selections!")
		for item, selection in vending_machine.items(): #This for loop will append items to the list item_list
			item_list.append((item, selection))
		
		print(item_list[::-1]) #Print backwards so that it goes from top to the bottom.
		
		print()
		print("Here are the prices")
		for item, price in prices.items(): #Prints the items and their prices on separate lines.
			print(item, price)
		print()	
		
		user_switch = 1 #User Proof loop
		while user_switch == 1:
			print("You currently have $" + str(money))
			user_input = input("Please input your selction: ").upper()
			transaction(user_input)
			print()
			choice = 1
			while choice == 1: #User proof loop
				user_input = input("Are you finished with the vending?(y/n): ").lower()
				if user_input == "y":
					user_switch = 0
					choice = 0
					switch = 0
				elif user_input == "n":
					user_switch = 1
					choice = 0
				else:
					print("Invalid command")
					choice = 1
			
		print("Thank you for using this program to either learn or for practice.")
		print("If you have any quesitons, please visit the forums over at www.EssenceOfZen.org/")
		print("-ZenOokami")
					
				
			
			
			
			
			
		
main()
		
