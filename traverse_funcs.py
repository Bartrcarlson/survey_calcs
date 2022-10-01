import re
import angle_funcs_v2 as af
import math

"""    0     1        2    3   4 5    6     7
p1 = ['N/S',[d,m,s],'E/W',dist,e,n,[proj_e],[proj_n]]

need to be able to compute forward and backwards
need to have a system of averaging ties with respect to distance
bearings work on assumption of clockwise traverse 
ignoring issues of grid vs ground dist
"""
def lat_dep(az,dist):
    e_dep = math.sin(math.radians(az)) * dist
    n_dep = math.cos(math.radians(az)) * dist
    return(e_dep, n_dep)

l26r = ['N',[9,47,24],'W', 435.89, 6094751, 1840802]
l27r = ['S',[82,21,39],'W', 2033, 6094685,1841227]
lst = [l26r, l27r]


for i in lst:
    i[1]=af.bearing_to_az([i[0],af.dms_to_dd(i[1]),i[2]],'dd')

for i in range(len(lst)):
    diffs = lat_dep(lst[i][1],lst[i][3])

    lst[i-1].append(lst[i][4]+ diffs[0])
    lst[i-1].append(lst[i][5]+ diffs[1])

print(lst)
