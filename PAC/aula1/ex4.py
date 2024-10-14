sec = input("Segundos: ")

try:
    sec = int(sec)
except:
    print("Error")
    exit()

h = sec//3600
m = (sec%3600)//60
s = (sec%3600)%60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))