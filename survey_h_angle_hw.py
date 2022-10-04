from  angle_funcs_v2 import *
### 9-3 Three lines have the following north azimuths: 146° 18', 227°36' and 332°48'. What are their bearings

            # d  m  s
dms_list = [[146,18,0],
            [227,36,0],
            [332,48,0]]
dd_list =[]
for i in dms_list:
    dd_list.append(dms_to_dd(i))

bearing_list=[]
for i in dd_list:
    bearing_list.append(az_to_bearing(i,'bearing'))

# print(bearing_list)

### 9-3 answer
### the 59" issue is due to bianry float aproximation and rounding down
"""
[['S', [33, 41, 59], 'E'], 
 ['S', [47, 35, 59], 'w'], 
 ['N', [27, 11, 59], 'w']]

    """

### 9-5 Calculate the north azimuth for sides OA, OB, OC, and OD in the accompanying figure.

##            ln   n/s  d  m s    e/w  
dms_list = [['OA','N',[19,33,52],'E'],
            ['OB','S',[74,46,6],'E'],
            ['OC','S',[9,16,57],'W'],
            ['OD','N',[73,22,26],'W']]

for i in dms_list:
    i[2] = dms_to_dd(i[2])

result = []
for i in dms_list:
    del i[0]
    result.append(bearing_to_az(i,'dms'))
# print result

### 9-5 answer
"""
###    d    m   s
['OA',[ 19, 33, 51]],
['OB',[105, 13, 54]],
['OC',[189, 16, 56]],
['OD',[286, 37, 34]]
"""

###9-7. Compute the bearings of sides BC and CD in the accompanying figure.

AB = ['N', [70,42,0], 'E']
AB[1] = dms_to_dd(AB[1])
AB_az = bearing_to_az(AB,'dd')

B = [97,18,0]
C = [88,26,00]
B_dd = dms_to_dd(B)
C_dd = dms_to_dd(C)
BC = az_to_bearing((AB_az + (180-B_dd)),'dms')
CD = az_to_bearing((AB_az + 180 - B_dd + 180 - C_dd),'dms')
# print([BC,CD])

### 9-7 answer
""" 
  ln  n/s   d   m   s    e/w
[[BC, 'S', [26, 35, 59], 'E'], 
 [CD, 'S', [64, 57, 59], 'w']]
"""

### 9-9. Determine the angles AOB, BOC, and DOA for the figure of Problem 9-5.

#ln   n/s  d  m s    e/w  
OA = ['N',[19,33,52],'E']
OB = ['S',[74,46,6],'E']
OC = ['S',[9,16,57],'W']
OD = ['N',[73,22,26],'W']
ls = [OA, OB, OC, OD]

for i in ls:
    i[1] = dms_to_dd(i[1])
    i.append(bearing_to_az(i,'dd'))


AOB = dd_to_dms(OB[3] - OA[3])
BOC = dd_to_dms(OC[3] - OB[3])
DOA = dd_to_dms(360 + OA[3] - OD[3])
# print([AOB,BOC,DOA])


###9-9 answer
"""    d    m  s
AOB = [85, 40, 1]
BOC = [84,  3, 2]
DOA = [92, 56, 17]
"""

### In Problems 9-11  compute all of the interior angles for each of the figures shown. 

AB = ['N', [81,56,0], 'E']
BC = ['S', [11,52,0], 'E']
CA = ['N', [72,27,0], 'W']
ls = [AB,BC,CA]

az_ls =[]
for i in ls:
    i[1] = dms_to_dd(i[1])
    az_ls.append(bearing_to_az(i,'dd'))

int_angles = internal_angles(az_ls)
int_angles_dms =  [dd_to_dms(i) for i in int_angles]
# print(int_angles_dms)


### 9-11 answer
"""
##    d    m   s
A = [25, 37, 0]
B = [93, 48, 0]
C = [60, 34, 59]
"""

### In Problems 9-13  compute all of the interior angles for each of the figures shown. 
AB = ['N', [73,38,10], 'E']
BC = ['S', [22,16,59], 'E']
CD = ['N', [89,27,36], 'W']
DA = ['N', [20,6,8], 'W']

ls = [AB,BC,CD,DA]

az_ls =[]
for i in ls:
    i[1] = dms_to_dd(i[1])
    az_ls.append(bearing_to_az(i,'dd'))

int_angles = internal_angles(az_ls)
int_angles_dms =  [dd_to_dms(i) for i in int_angles]
# print(int_angles_dms)

### 9-13 answer angle D is funny
##   d    m   s
A = [86, 15, 41],
B = [95, 55, 9],
C = [67, 10, 37],
D = [110, 38, 31],

### 9-15. Compute the deflection angles for the traverse of Problem 9-12.
AB = ['N', [13,27,56], 'E']
BC = ['S', [21,18,28], 'E']
CA = ['S', [40,36,8], 'W']
ls = [AB,BC,CA]

az_ls =[]
for i in ls:
    i[1] = dms_to_dd(i[1])
    az_ls.append(bearing_to_az(i,'dd'))

deff_angles = deflection_angles(az_ls)
deff_angles_dms =  [dd_to_dms(i) for i in deff_angles]
# print(deff_angles_dms)

## 9-15 answer 
"""
##   D    M   S
A = [207, 8, 11],
B = [145, 13, 35], 
C = [61, 54, 35]
"""

## 9-17 From the data given, compute the missing bearings.
## find one_two & two_three & four_one

##given
one = [51,16,0]
two = [36,22,0]
four = [221,37,56]
ang_ls = [one,two, four]

Three_four = ['N',[8,10,0],'W']
side_ls = [Three_four]

##comps
ang_ls = [dms_to_dd(i) for i in ang_ls]
Three_four = [bearing_to_az([i[0], dms_to_dd(i[1]), i[2]], 'dd') for i in side_ls]

four_one = side_ex_ang(ang_ls[2], Three_four[0])
one_two = side_ex_ang(ang_ls[0],four_one)
two_three = side_ex_ang(ang_ls[1], one_two)
results = [four_one, one_two,two_three]

# print([az_to_bearing(i,'dms') for i in results])

### 9-17 answer
"""
four_one = ['N', [49, 47, 55], 'w']
one_two =  ['N', [78, 56, 4], 'E']
two_three= ['S', [42, 34, 4], 'w']
"""

### 9-19 For the accompanying figure, compute the following:
## Deflection angle at B. 
## Interior angle at B.
## Bearing of the line CD. 
## North azimuth of DA.

### given
AB = ['N', [42,36,0], 'E']
BC = ['S',[64,56,0], 'E']
DA = ['N', [70,42,0],'W']
side_ls = [AB,BC,DA]
C_def = [38,16,0]

### calcs
C_def = dms_to_dd(C_def)

side_ls_az =[]
for i in side_ls:
   side_ls_az.append(bearing_to_az([i[0],dms_to_dd(i[1]),i[2]],'dd'))

side_ls_az.append(C_def + side_ls_az[1])

B_deff = deflection_angles([side_ls_az[0],side_ls_az[1]])[0]
# print(dd_to_dms(B_deff))

B_int = internal_angles([side_ls_az[0],side_ls_az[1]])[0]
# print(dd_to_dms(B_int))

# print(az_to_bearing(side_ls_az[3],'dms')) ##bearing cd

# print(bearing_to_az([DA[0], dms_to_dd(DA[1]),DA[2]],'dms'))

### 9-19 answers 
"""
a  [72, 28, 0]
b  [107, 31, 59]
c  ['S', [26, 40, 0], 'E']
d  [289, 18, 0]
"""

### 9-21. For the figure shown, compute the following:
## a Deflection angle at B.
## b Bearing of CD.
## c North azimuth of DE.
## d Interior angle at E.
## e Exterior angle at E

### given
BC = ['S', [46,37,0], 'E'] #0
DE = ['S', [20,6,0], 'E'] #1
EF = ['N', [78,18,0],'W'] #2
FA = ['N', [13,52,0],'W'] #3
AB = ['N', [36,58,0],'E'] #4
side_ls = [BC,DE,EF,FA,AB]
C = [72,33,0]

### calcs
side_ls_az =[]
for i in side_ls:
   side_ls_az.append(bearing_to_az([i[0],dms_to_dd(i[1]),i[2]],'dd'))

print(dd_to_dms(deflection_angles([side_ls_az[4],side_ls_az[0]])[0])) ## a
print(az_to_bearing(side_ex_ang(dms_to_dd(C),side_ls_az[0]),'dms')) ## b
print(bearing_to_az([DE[0],dms_to_dd(DE[1]),DE[2]],'dms')) ## c
print(dd_to_dms(internal_angles([side_ls_az[1], side_ls_az[2]])[0])) ## d
print(dd_to_dms(360 - internal_angles([side_ls_az[2], side_ls_az[3]])[0])) ## e

### 9-21 answer 
"""
a   [96, 24, 59]
b   ['S', [60, 49, 59], 'w']
c   [159, 54, 0]
d   [58, 12, 0]
e   [244, 26, 0]
"""