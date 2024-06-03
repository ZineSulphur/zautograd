# the Lib base autograd functions
import math

def ADlib():

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

    def ADexp(x, dx, z, dz):
        # z = e ** x
        z = math.exp(x)
        dz = math.exp(x) * dx
    
    def ADlog(x, dx, z, dz):
        # z = log(x)
        z = math.log(x)
        dz = 1.0 / x * dx

    def ADsin(x, dx, z, dz):
        # z = sin(X)
        z = math.sin(x)
        dz = math.cos(x) * dx

    def ADcos(x, dx, z, dz):
        # z = cos(X)
        z = math.cos(x)
        dz = -1 * math.sin(x) * dx