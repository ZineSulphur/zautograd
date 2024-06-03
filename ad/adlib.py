# the Lib base autograd functions

def ADadd(x, dx, y, dy, z, dz):
    # x + y -> z
    z = x + y
    dz = dx + dy

def ADsub(x, dx, y, dy, z, dz):
    # x - y -> z
    ADadd(x, dx, -y, -dy, z, dz)

def ADmul(x, dx, y, dy, z, dz):
    # x * y -> z
    z = x * y
    dz = dx * y + x * dy

def ADdiv(x, dx, y, dy, z, dz):
    # x / y -> z
    z = x / y
    dz = dx /y + (x / (y * y)) * dy

def ADpow(x, dx, y, z, dz):
    # x ** y -> z
    z = x ** y
    dz = y * x ** (y - 1) * dx