pD = 0.1
fV = 12
dV = 0.00015
R= pD*fV/dV
print("Reynolds number=",R)
if R < 2000:
    print("laminar flow region")
elif R <=3000:
    print("transition flow region")
else:
    print("turbulent flow region")