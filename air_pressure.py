import math


def air_pressure_at_heights(h):
    p0 = 101325     #reference pressure level
    M = 0.02896968  # MOLAR mass if dry air
    g = 9.80665     #gravity
    R0 = 8.314462618 #gas constant
    T = 273         #temperature in kelvin

    ratio = -(g*h*M)/(R0*T)
    p_h = p0 * math.exp(ratio)
    return p_h

 #list of elevation to run
h_list =range (0, 1000, 100)
for height in h_list:
    p_h = air_pressure_at_heights(height)
    print (p_h)
