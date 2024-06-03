# the Lib base autograd functions
import math

class ADlib():

    @staticmethod
    def ADadd(x, dx, y, dy):
        # x + y -> z
        z = x + y
        dz = dx + dy
        return z, dz
    
    @staticmethod
    def ADsub(x, dx, y, dy):
        # x - y -> z
        return ADlib.ADadd(x, dx, -y, -dy)

    @staticmethod
    def ADmul(x, dx, y, dy):
        # x * y -> z
        z = x * y
        dz = dx * y + x * dy
        return z, dz

    @staticmethod
    def ADdiv(x, dx, y, dy):
        # x / y -> z
        z = x / y
        dz = dx /y + (x / (y * y)) * dy
        return z, dz

    @staticmethod
    def ADpow(x, dx, y):
        # x ** y -> z
        z = x ** y
        dz = y * x ** (y - 1) * dx
        return z, dz

    @staticmethod
    def ADexp(x, dx):
        # z = e ** x
        z = math.exp(x)
        dz = math.exp(x) * dx
        return z, dz
    
    @staticmethod
    def ADlog(x, dx):
        # z = log(x)
        z = math.log(x)
        dz = 1.0 / x * dx
        return z, dz

    @staticmethod
    def ADsin(x, dx):
        # z = sin(X)
        z = math.sin(x)
        dz = math.cos(x) * dx
        return z, dz

    @staticmethod
    def ADcos(x, dx):
        # z = cos(X)
        z = math.cos(x)
        dz = -1 * math.sin(x) * dx
        return z, dz