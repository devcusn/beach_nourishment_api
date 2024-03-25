
A = 0.4


def get_closure_depth(h_s, t_m):
    res = 2.28 * h_s - 68.5*((h_s**2)/(9.81 * t_m ** 2))
    return res


def get_water_depth(A, y):
    h = A * y**(2/3)
    return h


def get_closure_depth_x(closure_depth, A):
    return (closure_depth / A)**(3/2)


cd = get_closure_depth(2.5, 8)
print(cd)

x = get_closure_depth_x(cd, A)
print(x)

depth = get_water_depth(A, x)

print(depth)
