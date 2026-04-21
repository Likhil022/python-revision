# functions
#argument - args are the things which we pass to function while calling
#parameters - variables used in function definition

def func():
    print("likhil kosuru")
func()



def my_function(name = "likhil"): #by default it will print likhil if we didn't mentioned any argument
    print(name)
my_function()

def my_fun(name, job):
    print(name,job)
my_fun(name = "likhil", job= "AI Engineer") 

#can also be passed as key : value pair as argumnets


# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple containing all the passed arguments


#when no of arguments are not known *placeholder will become a tuple and stores the arguments - *keys
def arguments(*test):
    print(test)
arguments("likhil","kosuru", "AI Engineer")


def hybrid_argumnets(first, *rest):
    print(first)
    print(rest)
hybrid_argumnets("first", "second", "third", "fourth")



# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

# This way, the function will receive a dictionary of arguments and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "likhil", lname = "kosuru")

#unpacking
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")