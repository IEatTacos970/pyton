# lists, for loops

# why lists are useful: store multiple things in one variable, saves space; allows us to iterate (repeat) over the list

# syntax - almst the same as a variable

fruits = ["apple", "banana", "orange"]

randomItems = ["fds", 9434, True, 0.34, "r"]

# accessing list items: indexed from 0 - end

print(fruits[0])

# quiz



# why loops are useful: to repeat code without typing a giant wall of the same code over and over again

# for loops: repeat something for a specified amount of times, or until a list ends

# syntax -- indentation is now CRUITIAL

# all of these can be variables

for i in range(3):  # set number
    print(i)

#iterate over list

for thing in randomItems:
    print(thing)

for char in "hello":  # character in text, treats it like a list
    print(char)

# break, and continue

# break: breaks the loop, it stops it 

# contnue: coninues the loop, skips the rest of the code after the "continue" for the current cycle

for char in "abcde":
    if i == "d":
        break

for thing in randomItems:
    if thing == True:
        continue
    print(thing)


# quiz