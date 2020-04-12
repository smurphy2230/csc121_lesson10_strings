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
