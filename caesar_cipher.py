import string

letters = " " + string.ascii_lowercase

choice = ""


while True:
	# Ask for a user's choice
	# 
	choice = input("1. Encrypte\n2. Decrypte (You know steps)\n3. BruteForce\n4. Exit\n* Enter a number : ")

	if choice != "4":
		user = input("\nEnter a phrase: ").lower()

		if choice == "1" or choice == "2":
			user_shift = int(input("\nHow much steps: "))
			new_string = ""

			if choice == "1":
				for alpha in user:
					# Indexing the user Alphabetic
					# Adding the steps to the index
					# 
					if alpha == " ":
						continue
					else:
						index = letters.index(alpha) + user_shift

					# If index total > 26 then we modulo on 26:len(alpha)
					if index > 26:

						# len(letters) - 1) So we ignore the space at first
						index = (letters.index(alpha) + user_shift) % (len(letters) - 1)

					# Finding the coresponding letter and adding it
					new_string += letters[index : index + 1]


			elif choice == "2":
				for alpha in user:
					# (user_shift + 1) to ignore the 0
					index = letters.index(alpha) - user_shift
					# Finding the coresponding letter and adding it
					
					if index <= 0:
						# e.g ((index(B:2) - steps(5) = -3) - 1) = -4:W
						new_string += letters[index - 1 : index - 2 : -1]
					else:
						new_string += letters[index : index + 1]

				
			# Print the result
			print(new_string)

		elif choice == "3":
			for user_shift in range(1, 27):
				new_string = ""
				for alpha in user:
					# (user_shift + 1) to ignore the 0
					index = letters.index(alpha) - user_shift
					# Finding the coresponding letter and adding it
					
					if index <= 0:
						# e.g ((index(B:2) - steps(5) = -3) - 1) = -4:W
						new_string += letters[index - 1 : index - 2 : -1]
					else:
						new_string += letters[index : index + 1]
				print(new_string)

		else:
			print("Please enter a corret input!")
	else:
		quit()