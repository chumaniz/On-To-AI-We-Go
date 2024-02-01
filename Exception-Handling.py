# In python, errors are a normal part of lif
# Right now we aere finding ways to be able to curb them

try:

    math_meme = 10/0 
    name = "Zuma"

    number = int(name)  
    print(number)
except ValueError:
    print("You cannot perform this action")
except ZeroDivisionError:
    print("Such an action is ridiculous...do better")

try: 
    print(10/0)
except ZeroDivisionError:
    print("Disgrace to all human kind") 
finally:
    print("Useless")

