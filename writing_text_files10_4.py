import os  # for use with last example
# open the file
# write text to file one line at a time
# close the file

output_file = open("departments2.txt", "w")
output_file.write("Psychology")
output_file.write("History")
output_file.write("Sociology")
output_file.close()
# to write new line for each input a new line character between them
# second argument 'a' appends document instead of overwriting it
output_file = open("departments2.txt", "a")
output_file.write("\n")
output_file.write("Psychology")
output_file.write("\n")
output_file.write("History")
output_file.write("\n")
output_file.write("Sociology")
output_file.write("\n")
output_file.close()
# to append use 'a'
output_file = open("departments2.txt", "a")
output_file.write("Computer Programming")
output_file.write("\n")
output_file.close()
# Let's try using a loop from a list
output_file = open("departments3.txt", "a")
course_list = ["Psychology", "History", "Sociology", "Computer Programming",
               "Data Science", "Game Development", "Networking", "Web Development"]

for c in course_list:
    course_name = c
    output_file.write(c)
    output_file.write("\n")
output_file.close()
# open file, process, write file
input_file = open("scores.txt", "r")
output_file = open("scores_grades.txt", "w")

for line in input_file:
    score = float(line)
    if 100 >= score >= 90:
        grade = "A"
    elif 90 > score >= 80:
        grade = "B"
    elif 80 > score >= 70:
        grade = "C"
    elif 70 > score >= 60:
        grade = "D"
    elif 60 > score >= 0:
        grade = "F"
    output_string = str(score) + " " + grade + "\n"
    output_file.write(output_string)

input_file.close()
output_file.close()
print()
# to delete input file after finishing with it

input_file = open("scores.txt", "r")
output_file = open("scores_grades2.txt", "w")

for line in input_file:
    score = float(line)
    if 100 >= score >= 90:
        grade = "A"
    elif 90 > score >= 80:
        grade = "B"
    elif 80 > score >= 70:
        grade = "C"
    elif 70 > score >= 60:
        grade = "D"
    elif 60 > score >= 0:
        grade = "F"
    output_string = str(score) + " " + grade + "\n"
    output_file.write(output_string)

input_file.close()
output_file.close()
os.remove("scores.txt")  # deletes input file
