import angle_funcs_v2 as af
import classy_program as survey


ab = ['N',[50,37,48],'E']
B = [100,37,0]
C = [110,46,0]
D = [98,24,0]
E = [122,37,0]
ang_lst = [B,C,D,E]
ab_az = af.bearing_to_az([ab[0],af.dms_to_dd(ab[1]),ab[2]],'dd')

##problem 1.1
sum_of_angles = 0
for i in ang_lst:
    i_dd = af.dms_to_dd(i)
    sum_of_angles = sum_of_angles + i_dd

A = (180*(5-2)) - sum_of_angles
# print(af.dd_to_dms(A))

##problem 1.1 answer
"""
A = [107, 36, 0]
"""


## problem 1.2
line_direction = ab_az
for i in ang_lst:
    i_dd = af.dms_to_dd(i)

    deflection = 180 - i_dd

    line_direction = line_direction + deflection
    if line_direction >= 360:
        line_direction = line_direction- 360
    # print(af.dd_to_dms(line_direction), af.az_to_bearing(line_direction,'dms'))


## problem 1.2 answer
"""
BC  [130, 0, 48]     ['S', [49, 59, 12], 'E']
CD  [199, 14, 48]    ['S', [19, 14, 48], 'w']
DE  [280, 50, 48]    ['N', [79, 9, 12], 'w']
EA  [338, 13, 48]    ['N', [21, 46, 12], 'w']
"""


## problem 2

# AB = ['N',[8,17,0],'E',404.03]
# BC = ['N', [87,2,0],'E',662.13]
# CD = ['S',[14,47,0],'W',653.1]
# DA = ['N',[68,43,0],'W',550.9

AB = survey.Line(survey.Angle(['N',[8,17,0],'E']), 404.03, [0,0])
BC = survey.Line(survey.Angle(['N',[87,2,0],'E']),662.13)
CD = survey.Line(survey.Angle(['S',[14,47,0],'W']),653.16)
DA = survey.Line(survey.Angle(['N',[68,43,0],'W']),550.94)
lst = [AB,BC,CD,DA]

print(AB.dep)


