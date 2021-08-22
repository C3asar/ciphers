import random, string

def seperation_encrypte(user_input, rows):
	first = 0
	second = rows
	result = []

	while first <= len(user_input):
		if len(user_input[first : second]) == rows:
			result.append(user_input[first : second])
		else:
			# Result len last line - rows 
			rest = rows - len(user_input[first : second])
			# Get random alphabets equal to rest and join them as they're a list
			
			fill = "".join(random.choices(string.ascii_lowercase, k=rest))
			result.append(user_input[first : second] +  fill)

		# Add same row number to both [first + row : second + row]
		first += rows
		second += rows

	return result

def split(result):

	for word in result:
		print(" | ".join([char for char in word]))

def view(result):

	new = []
	string = ""
	for col in range(len(result[0])):
		for row in range(len(result)):
			string += result[row][col]
		new.append(string)
		string = ""
	return new

def seperation_decrypte(user_input, rows):
	first = 0
	second = rows
	list_ = []
	while second <= len(user_input):
		list_.append(user_input[first : second])
		first += rows
		second += rows
	return list_

choice = ""
user = ""
row_number = ""

while True:
	choice = input('''
1.Encrypte text using Transpose Cipher
2.Display text on the Traspose table
3.Decrypte text using Transpose Cipher
4.Exit
Your choice: ''')

	
	if choice == "4":
		quit()
	else:
		user = input("Enter the phrase: ").lower().replace(" ", "") 
		# Ask for rows' number 
		row_number =  int(input("Enter number of rows: "))
		print()
		if choice == "1":
			print("The Encrypted text: " + "".join(view(seperation_encrypte(user, row_number))))
		elif choice == "2":
			split(seperation_encrypte(user, row_number))
		elif choice == "3":
			print("The Decrypted text: " + "".join(view(seperation_decrypte(user, row_number))))
		else:
			print("Please enter a correct input.")
		print()


