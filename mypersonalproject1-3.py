# add some product names
#CREATE products list
products = ['Fanta', 'Sprite', 'Coke', 'Rubella']
#PRINT main menu options
user_input = ""
while user_input != "0":
	print("MAIN MENU")
	print("0: Exit")
	print("1: Product Menu")
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
		
		#ADDING NEW CUSTOMER (DICTIONARY)
	{#add a new customer: 
	#"customer_name": "John",
	#update customer details:
	 #"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
	#customer phone number:
	 #"customer_phone": "0780166991",
	#add a new order:
	 #"status": "preparing"
	#update order details: 
	#"status": "dispatched"
	#delete order: 
	#"status": "cancelled"
	}

    #view all products or orders
    #STRETCH I want to be able to update or delete a product or order
