while True:
    pD = input(float("enetr pD"))
    fV = input(float("enetr fV"))
    dV = input(float("enetr dV"))
    R = pD*fV/dV
    print("Reynolds number=",R)
    if R < 2000:
        print("laminar flow region")
    elif R <=3000:
        print("transition flow region")
    else:
        print("turbulent flow region")
    agine = input("Another REynolds number to calculate? y/n")
    if agine.lower() == "n":
        break
    