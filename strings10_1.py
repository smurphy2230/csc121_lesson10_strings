first_name = "John"
print("Print first name: ", first_name)
print("Print first character: ", first_name[0])
last_name = "Doe"
full_name = first_name + last_name
print("Concatenation: ", full_name)
substring = full_name[1:4]
print("Slicing:", substring)
print()
# you cannot use an assignment statement to change
# characters in a string. this results in an error:
# --------------------------------------
# my_string = "common"
# my_string[2] = 't'
# print()
# --------------------------------------
# to change a character, use concatenation and slicing
my_string = "common"
my_string = my_string[:2] + 't' + my_string[3:]
print("Changing first m to a t: ", my_string)
print()
# to concatenate a string with a numerical value, use the
# 'str' function to convert num to str
# this will fail:
# --------------------------------------
# string1 = "The price is $"
# price = 17.99
# combined_string = string1 + price  # price is not a string
# print(combined_string)
# --------------------------------------
string1 = "The price is $"
price = 17.99
combined_string = string1 + str(price)
print(combined_string)
print()
# len function
college = "Wake Tech"
length = len(college)
print("Length of string (college): ", length)
# the in operator
college2 = "Wake Tech Community College"
if "e" in college2:
    print("The letter e in found in college2")
else:
    print("The letter e is not found in college2")
print()
# using a for loop to iterate through a string
college3 = "Wake Tech"
for char in college3:
    print(char)
print()
book = "Introduction to Computer Science"
num_spaces = 0
for chr in book:
    if chr == ' ':
        num_spaces = num_spaces + 1
print("Number of spaces in book: ", num_spaces)
