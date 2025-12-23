# File handling

# 2. with :

# Open a file
# file = open("path of the file",mode)
# mode : r - read , w - write , a - append , x - create

# Read a file
# 1. read() - reads the whole file
# 2. readline() - reads a single line
# 3. readlines() - reads all the lines and returns a list of lines

# file = open("D:/VS Code/SRU/Day3/text.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("D:/VS Code/SRU/Day3/text.txt", "r")
# content = file.readlines()
# print(type(content))
# print(len(content))
# print(content[2])
# file.close()

# file = open("D:/VS Code/SRU/Day3/text.txt", "r")
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)
# file.close()


# Opening a file using with
# with open("D:/VS Code/SRU/Day3/text.txt", "r") as file:
#     content = file.read()
#     print(content)
# No need to close the file, it is automatically closed after the with block

# Write to a file
# with open("D:/VS Code/SRU/Day3/text.txt", "w") as file:
#     file.write("SR University, a premier educational institution, nestled in the picturesque town of Hasanparthy, Telangana, offers a transformative learning experience.\nWith a rich legacy of over 50 years, SR University aims to redefine education by nurturing inquisitive minds and fostering creativity.\nIts innovative curriculum empowers students to think critically, apply theoretical knowledge to real-world scenarios, and contribute meaningfully to the progress of Telangana and India.\n With a focus on experiential learning, SR University is committed to producing graduates who are sought after for their ability to solve complex problems and drive positive change.")

# Append to a file
# with open("D:/VS Code/SRU/Day3/text.txt", "a") as file:
#     file.write("\nI like the Campus and the environment of SR University.")


# task_number        task_description               task_owner    task_status
#     1       Implement file read functionality       Alice       Assigned
#     2       Implement file write functionality      Bob         In Progress
#     3       Implement file read functionality       Alice       Completed
#     4       Implement file append functionality     Charlie     Assigned
