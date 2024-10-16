# This program outputs the age category for a given input age.
# It has a semantic error.  Can you find it?
# Which values of age produce the output "adult"?
# Correct the error.
# Can you simplify the code to avoid redundant conditions

age = int(input("Age? "))

print("Age:", age)

if age < 0:
    print("Invalid age")
    exit()

elif age < 13 :
    cat = "child"

elif age < 18:
       cat = "teenager"

else:
        cat = "adult"

print("Category:", cat)
