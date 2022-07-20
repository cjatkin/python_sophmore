#lab 7 calculations

ay = 3.4*10**14
dy = 0.05
dx =0.175
v0 = 1.45*10**(7)

bd = 0.003

e = 1.6*10**(-19)
m = 9.109*10**(-31)

#e_m = e/m
e_m = 1.76*10**11

#e_m = ay/((vd/dy)-v0Bd)
vd = (v0*dy*bd) + (ay*dy)/(e_m)

print(v0*dy*bd)
print(ay*dy/e_m)
print(vd)

