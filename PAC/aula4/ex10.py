n = int(input("Enter a number: "))
nsum = 0
for i in range(1, n):
    if n % i == 0:
        nsum += i
        print(i)

if nsum == n:
    print("The number is perfect.")
elif nsum > n:
    print("The number is abundant.")
else:
    print("The number is deficient.")