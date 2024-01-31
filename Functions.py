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
