import random, string


user = input("Enter the phrase: ").lower().replace(" ", "") 

# Ask for rows' number 
row_number =  int(input("Enter number of rows: "))



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


# split(seperation(user, row_number))
# 

def view(result):

	for index, row in enumerate(result):
		for col in range(len(row)):
			print(result[index][col])






view(seperation(user, row_number))