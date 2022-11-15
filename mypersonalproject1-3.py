# add some product names
#CREATE products list
products = ['Fanta', 'Sprite', 'Coke', 'Rubella']
#CREATE orders list
orders = [{
 "customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334",
 "courier": 2,
 "status": "preparing"
}, { 
 "customer_name": "Peter",
 "customer_address": "Unit 1, 15 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789557314",
 "courier": 31,
 "status": "preparing"
}]

order_status_list = ['preparing', 'on the way', 'delivered']
#PRINT main menu options
user_input = ""
while user_input != "0":
	print("=====================")
	print("MAIN MENU")
	print("0: Exit")
	print("1: Product Menu")
	print("2:Order Menu")
	#GET user input for main menu option
	user_input = input("Enter option: ")

	if user_input == "0":
		# quit
		print("\nThank you! Goodbye!\n")
	elif user_input == "1":
		# product menu
		product_user_input = ""
	
		while product_user_input != "0":
			print("\nPRODUCT MENU")
			print("0: Return to main menu")
			print("1: Display products")
			print("2: Add new product")
			print("3: Update product")
			print("4: Delete product")
			product_user_input = input("Enter option: ")
	
			if product_user_input == "0":
				# return to main menu
				print("\nReturning to main menu\n")
			elif product_user_input == "1":
				# display
				print("\nProduct List:")
				for product in products:
					print(product)
				input("Press ENTER to return to menu.")
			elif product_user_input == "2":
				# create
				new_product = input("Please, enter a new product name: ")
				print("Adding", new_product, "to database.")
				products.append(new_product)
			elif product_user_input == "3":
				# update
				print("\nProduct List:")
				for idx, product in enumerate(products):
					print("\t", idx, product)
				product_number = input("Which product would you like to update? ")
				# TODO: Validate number is in range
				product_number = int(product_number)
				existing_name = products[product_number]

				new_name = input(f"Enter a new name for {existing_name}: ")
				products[product_number] = new_name

				#DELETE PRODUCT
			elif product_user_input == "4":
				print("\nProduct List:")
				for idx, product in enumerate(products):
					print("\t", idx, product)
				product_number = input("Which product would you like to delete? ")
			
				#TODO: Validate number is in range
				product_number = int(product_number)
				existing_name = products[product_number]
				print(existing_name)
				del products[product_number]
				
			else:

				print("\nUnknown option. Press 0 to 4.")

	elif  user_input == "2":
    				# order menu
			order_user_input = ""
			while order_user_input != "0":
				print("=====================")
				print("ORDER MENU")
				print("0: Return to Main Menu")
				print("1: Print Order List")
				print("2: Create New Order")
				print("3: Update Existing Order")
				print("4: Delete Order")
				#GET user input for order menu option
				order_user_input = input("Enter option: ")
				if order_user_input == "0":
					# return to main menu
					print("\nReturning to Main Menu\n")
				elif order_user_input == "1":
					# print order list
					print("\nOrder List:")
					for order in orders:
						print(order)
					input("Press ENTER to return to menu.")

				elif order_user_input == "2":
					# create new order
					print("Add New Order")
					new_name = input("Enter customer name: ")
					new_address = input("Enter customer address: ")
					new_phone = input("Enter customer phone: ")
					new_courier = input("Enter courier number: ")
					new_status = input("Enter order status: ")
					new_order = {"customer_name": new_name, 
					"customer_address": new_address, 
					"customer_phone": new_phone}
					print("Adding", new_order, "to database.")
					orders.append(new_order)

				elif order_user_input == "3":
    			# update existing order
					print("\nOrder List:")
				for idx, order in enumerate(orders):
					print("\t", idx, order)
					order_number = input("Which order would you like to update? ")
					order_number = int(order_number)
					existing_name = orders[order_number]
					new_name = input(f"Enter a new name for {existing_name}: ")
					orders[order_number] = new_name   #WHYYYYYY NOTHING'S HAPPENING/something wrong with update loops works not as expected
