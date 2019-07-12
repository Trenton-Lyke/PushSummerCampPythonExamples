#don't worry about this stuff at the top it just randomly sets the condition to
#True or False
import random
def adjustCondition():
    return random.randint(0,10) != 1

condition = True

while condition:
    print("condition is True")
    condition = adjustCondition()
    
