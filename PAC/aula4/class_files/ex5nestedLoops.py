# Example: loops inside loops


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
def doSomething():
    for c in letters:
        for d in letters:
            print(c+d)

# What does this print? How many lines?
doSomething()

