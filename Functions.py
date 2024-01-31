# This is a function

def hello():
    print("Hello World!")

hello()

# The purpose of a function is to help create reusable and automatory code...helps with space and repeating oneself
# Now we add parameters 

def message(string1 , string2):
    print(string1 + string2)
  
message("Hello ", "world!")

def message2(question, name, mark):
    print(question + name + mark)

message2("Are you going to help out in the kitchen ", "Jason", "?")

# Parameters make our function more faceted, you can do more with it
# Let's see what we can do mathematically 

def calculation(number1, number2):
    # For the sake of good practice, I'm going to just add commas simply because you never know...
    print(number1+number2),
    print(number1-number2),
    print(number1/number2),
    print(number1*number2),
    print(number1%number2),

calculation(8,4)

# Alright a return statement...used for storing information

def calculation(number1, number2):
    return(number1+number2)


number = calculation(8, 4)

print(calculation(8,4))

# Practising default parameters. Basically if you don't change anything, the text by default will show.

def sms(text="Hello, we would like to notify you about your outstanding warranty"):
    print(text)

sms()


# What if we just want to set variable parameters...a placeholder function?

def sms(*text):
    Bank_account = int(input())
    if Bank_account <= 100:
        text = "You're broke"
        print(text)
    else:
        text = "All is good, keep it up"
        print(text)
sms()

# Scopes, important because one must define a local or global variable 

number = 100000

def nomber():
    print(number)

nomber()

def nomber2():
    number2 = 100
    
#print(number2) # This will not work because I'm accessing a variable from outside
                # You can access a global variable because it is outside and global, but a local variable is like Apple software, only people on the inside can access it.

# But there is a trick..adding global next to the local variable and making it accessible from outside too
number3 = 10
def nomber3():
  global number3 






print(number3)
