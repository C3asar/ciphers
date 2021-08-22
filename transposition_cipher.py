import random, string

def seperation(user_input, rows):
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



def encrypte(result):

	new = []
	string = ""
	for col in range(len(result[0])):
		for row in range(len(result)):
			string += result[row][col]
		new.append(string)
		string = ""
	return new


choice = ""
user = ""
row_number = ""

while choice != "3":
	choice = input("1.Encrypte text using Transpose cipher\n2.Display text on the Traspose table\n3.Exit\nYour choice: ")

	user = input("Enter the phrase: ").lower().replace(" ", "") 
	# Ask for rows' number 
	row_number =  int(input("Enter number of rows: "))
	print()
	if choice == "1":
		print("The encrypted text: " + "".join(encrypte(seperation(user, row_number))))
	elif choice == "2":
		split(seperation(user, row_number))
	else:
		print("Please enter a correct input.")
	print()


