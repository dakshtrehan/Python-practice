import math
def catAndMouse(x, y, z):
    print(math.fabs(x-z))
    print(math.fabs(y-z))
    if math.fabs(x-z)>math.fabs(y-z):
        return ("Cat A")
    elif math.fabs(x-z)<math.fabs(y-z):
        return ("Cat B")
    elif math.fabs(x-z)==math.fabs(y-z):
        return ("Mouse C")

catAndMouse(1,2,3)