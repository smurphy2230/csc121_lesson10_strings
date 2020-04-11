# opens txt file to be read (may need file path in first  string argument)
input_file = open("instructors.txt", "r")
whole_file = input_file.read()
print(whole_file)
# remember to close file after reading
input_file.close()
print("---while loop-----")
input_file2 = open("instructors.txt", "r")
line = input_file2.readline()
while line != "":  # while loop to print each line of text document
    print(line)
    line = input_file2.readline()
input_file2.close()
print("--------------")
input_file3 = open("instructors.txt", "r")
line = input_file3.readline()
while line != "":
    line = line.strip("\n")  # this strips away the hidden new line character
    print(line)
    line = input_file3.readline()
input_file3.close()
print("-----for loop----")
# using a for loop to read and display one line at a time
input_file4 = open("instructors.txt", "r")
for line in input_file4:
    line = line.strip("\n")
    print(line)
input_file4.close()
# open and automatically close file using with statement
print("----with statement----")
with open("instructors.txt", "r") as input_file5:
    for line in input_file5:
        line = line.strip("\n")
        print(line)
# numerical values in text files
print("------converting numerical values-----")
input_file5 = open("scores.txt", "r")
total = 0

for line in input_file5:
    score = float(line)
    print(score)
    total = total + score

input_file5.close()
print("Total score is: ", total)
