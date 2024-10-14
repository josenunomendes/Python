temp_cels = input("Temperature in Celsius: ")

try:
    temp_cels = float(temp_cels)
except ValueError:
    print("Error")
    exit()

temp_fahr = (1.8 * temp_cels) + 32

print("{:.2f} ºC = {: .2f} ºF".format(temp_cels, temp_fahr))