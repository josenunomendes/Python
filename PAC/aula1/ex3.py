name = input("Como te chamas? ")
age = input("Em que ano nasceste? ")

try:
    age = int(age)
except:
    print("Error")
    exit()

age = 2025 - age

print("{}, em 2025 farás {} anos".format(name, age))