v1 = 10
v2 = 20

# v1 = d/t1
# v2 = d/t2
# v1*t1 = v2*t2
# t = t1+t2
# t = d/v1 + d/v2
# vm = d/(d/v1 + d/v2)
# vm = d/(d*(1/v1 + 1/v2))
# vm = 1/(1/v1 + 1/v2)
# vm = 1/((v1+v2)/(v1*v2))
# vm = v1*v2/(v1+v2)

vm = v1*v2/(v1+v2)

print(vm)