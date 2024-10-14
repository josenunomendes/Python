width = input("width\n")
height = input("height\n")

try: 
    width = float(width)
    height = float(height)
except ValueError:
    print("Error")
    exit()

area = width*2 + height*2

print(area)