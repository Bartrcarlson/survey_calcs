""" Bart's V curve homework """
from sympy import symbols, Eq, solve


def rate(g2,g1,dist) -> float:
    return (g2-g1)*10000 /dist
    
def vcurve_elev(x,bvc,dist,g2,g1) -> float:
    """takes x location along vcurve and returns elevation in ft
    where x is dist in feet. bvc is elev in ft. dist is the length of curve
    in ft. g2 is grade leaving curve in decimal. g1 grade entering cruve in decimal"""
    return bvc + g1*x + (rate(g2,g1,dist) / 2) * (x/100)**2
    
def vcurve_max_min(g2,g1,dist) -> float:
    """finds the max or min of the curve and returns the x position aka the horizontal distance
    from begining of vertical curvature"""
    return -g1/rate(g2,g1,dist*10000)
    

### problem 1 ###
#################
starting_sta = 5050
starting_elev = 975.50
sta_bvc = 5050 - 1000/2
sta_evc = 5050 + 1000/2
elev_bvc = starting_elev - 500*.0275
dist = 1000
opt = vcurve_max_min(-.0225,.0275,dist)
stas = [4550,4600,4700,4800,4900,5000,5100,5200,5300,5400,5500,5550, sta_bvc + opt]

for i in stas:
    sta = i - sta_bvc
    elev = vcurve_elev(sta,elev_bvc,dist,-.0225,.0275)
    # print(f"station {(sta + sta_bvc)/100}  elevation {round(elev,2)}")
"""
station 45+5  elevation 961.75
station 46+0  elevation 963.06
station 47+0  elevation 965.31
station 48+0  elevation 967.06
station 49+0  elevation 968.31
station 50+0  elevation 969.06
station 51+0  elevation 969.31
station 52+0  elevation 969.06
station 53+0  elevation 968.31
station 54+0  elevation 967.06
station 55+0  elevation 965.31
station 55+5  elevation 964.25
station 51+0  elevation 969.31 maximum
"""

### problem 2 ###
#################

starting_sta = 8930
starting_elev = 130
dist = 550
sta_bvc = starting_sta - dist/2
sta_evc = starting_sta + dist/2
elev_bvc = starting_elev - dist*.5*-.029
opt = vcurve_max_min(.0125,-.029,dist)
stas = [8655.0,8700,8750,8800,8850,8900,8950,9000,9050,9100,9150,9200,9205, sta_bvc + opt]

for i in stas:
    sta = i - sta_bvc
    elev = vcurve_elev(sta,elev_bvc,dist,.0125,-.029)
    # print(f"station {(sta + sta_bvc)/100}  elevation {round(elev,2)}")
"""
station 86+55  elevation 137.97
station 87+0  elevation 136.75
station 87+5  elevation 135.56
station 88+0  elevation 134.56
station 88+5  elevation 133.75
station 89+0  elevation 133.13
station 89+5  elevation 132.7
station 90+0  elevation 132.46
station 90+5  elevation 132.41
station 91+0  elevation 132.54
station 91+5  elevation 132.86
station 92+0  elevation 133.38
station 92+05  elevation 133.44
station 90+39  elevation 132.4 minimum
"""

#### 23-8 #####
###############
"""find PVI"""
starting_sta = 3600
starting_elev = 622.80 
end_sta = 5200
end_elev = 623.4
g1 = .04
g2 = -.05
dist = end_sta - starting_sta
 
x = symbols('x')
eq1 = Eq(starting_elev+g1*x,end_elev-g2*(dist - x))
sol = solve(eq1)
x = sol[0]

# print(x+starting_sta)
y = g1 * x + starting_elev
# print(y)
"""
44+95.6 sta
658.6' elev
"""

###### 23-18 ########
#####################
g1 = -.024
g2 = .032
int_sta = 10300
int_elev = 153.25
dist = 1200
find=[9900,10400]

starting_sta = int_sta - dist/2 
starting_elev = int_elev - g1*dist/2
# print(starting_sta)
# print(starting_elev)

for i in find:
    elev = vcurve_elev(i-starting_sta,starting_elev,dist,g2,g1)
    # print(elev)
"""
99+00    163.78333333333333
104+00   162.28333333333333
"""

###### 23-21 ##########
#######################

def op(x,step) -> list:
    results =[]
    for d in np.arange(x-2,x+2,step):
        eq = (120+2*d)+-4*(d/2+1)+((3+4)/d)/2*(d/2+1)**2
        results.append([d,eq,eq])  
    return [results[min(range(len(results)), key = lambda i: abs(results[i][1]-x))][0],step]


# import decimal

# def newton(x,step):
#     op(x,step)
#     while abs(x.as_tuple().exponent) < 3:
#         newton
#     else:
#         return newton()


# test = 3.14
# print(test.as_tuple().exponent)

d = symbols('d')
eq = Eq((120+2*d)+-4*(d/2+1)+((3+4)/d)/2*(d/2+1)**2,128)
sol = solve(eq)
print(sol)