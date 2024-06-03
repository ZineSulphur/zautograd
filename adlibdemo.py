# compute gread of function z = (x ** 2 + 4) * y - x / y
# dz = 2 * x * y * dx + (x ** 2 + 4) * dy - dx /y + (x / (y * y)) * dy
from ad.adlib import ADlib

x = 101.0
y = 12.0
dx = 1.0
dy = 1.0

t1, dt1 = ADlib.ADpow(x, dx, 2)
t2, dt2 = ADlib.ADadd(t1, dt1, 4, 1)
t3, dt3 = ADlib.ADmul(t2, dt2, y, dy)
t4, dt4 = ADlib.ADdiv(x, dx, y, dy)
z1, dz1 = ADlib.ADsub(t3, dt3, t4, dt4)
z2 = (x ** 2 + 4) * y - x / y
dz2 = 2 * x * y * dx + (x ** 2 + 4) * dy - dx /y + (x / (y * y)) * dy
print("function is z = (x ** 2 + 4) * y - x / y")
print("autograd result:")
print("z = {}".format(z1))
print("dz = {}".format(dz1))
print("formula result:")
print("z = {}".format(z2))
print("dz = {}".format(dz2))