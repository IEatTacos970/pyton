# functions & params & math

# what are functions used for: to eliminate the same code being in two different places, kinda like a variable but for code 
# instead of datatypes

# already know how to call a function

def welcomer():
    print("hello from the fucntion")

welcomer()



# parameters are extra data we can add to functions to make them more useful.

def welcomer(msg):
    print(msg)

welcomer("Hello form the fucntion parameter!")


# you can add as many or as little parameters you want

def multiAdder(a,b,c,d,e):
    print(a+b+c+d+e)

multiAdder(1, 2, 3, 4, 5)


# what if you dont want to print?

def returnNumber(a, b):
    return a + b

print(returnNumber(1, 3))

#