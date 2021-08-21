import string

letters = " " + string.ascii_lowercase

user = input("Enter a phrase: ").lower()
user_shift = int(input("How much steps: "))

new_string = ""

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

print(new_string)