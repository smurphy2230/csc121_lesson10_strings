# s.count(char) returns the number of occurrences of char in string:
college = "Wake Tech"
num_e = college.count("e")
print("The number of e's in college:", num_e)
# checking every character in a string using methods isalpha, isdigit,
# isupper, islower
# card_num = input("Please enter your 16-digit card number: ")
# while not card_num.isdigit():
#     print("Invalid card number.")
#     card_num = input("Please enter your 16-digit card number:")
# print("Card number entered: ", card_num)
print()
postal_code = input("Please enter a 5 digit zip code: ")
while not postal_code.isdigit():
    print("Invalid zip code")
    postal_code = input("Please enter a 5 digit zip code: ")
print("Zip code entered: ", postal_code)
print()
city = input("Please enter a city: ")
if city.isalpha():
    print("City name: ", city)
else:
    print("City name can only contain letters.")
print()
# the find method returns the starting index of a target substring. If no
# occurrence is found a -1 is returned
state = "Mississippi"
print(state)
first_s = state.find("s")
print("Index of first 's': ", first_s)
first_k = state.find("k")
print("Index of first 'k': ", first_k)
first_iss = state.find("iss")
print("Index of first 'iss': ", first_iss)
print()
# the replace method produces a new string with every occurrence of a given
# substring replaced
word = "common"
print("original word: ", word)
word2 = word.replace("m", "t")
print("All 'm' replaced with 't': ", word2)
print()
# the split method separated the original string into substrings and stores
# them as separate elements in the list
my_string = "one two three four five"
word_list = my_string.split()
print(word_list)
print()
date_string = "04/22/1970"
date_list = date_string.split("/")
print("Month: ", date_list[0])
print("Day: ", date_list[1])
print("Year: ", date_list[2])
