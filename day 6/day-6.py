# while loops, recap quiz

# quiz

# while loops - infinite loops, foundation of apps that allow the user to run it
# multiple times

while True:
    print("hi")
    break

# most cases will use True or something similar

# how to end it
# SENTINEL

sentinel = "stop"

while True:
    name = input("What is your name? ")
    if name == sentinel:
        break

    print("Hello", name)


# use functions for repeatability

def collect_names():
    sentinel = "end"
    names = []
    while True:
        name = input("Enter a name (or 'end' to stop): ")
        if name == sentinel:
            break
        names.append(name)
    return names

print("Names:", collect_names())

# TEACH += etc

# quiz
#activity: calculator