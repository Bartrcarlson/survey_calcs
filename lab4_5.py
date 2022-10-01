import angle_funcs_v2 as af


### LAB 4
#  
## DATA 
rw_df = [95,31,30]
df_pi = [343,12,10]
pi_rw = [281,14,5]
lst = [rw_df,df_pi,pi_rw]

##calcs
for i in lst:
    i.append(af.dms_to_dd(i))
    del i[0:3]
        
total = 0
for i in lst:
    for j in i:
        total = total + j/2

error = af.dd_to_dms(360 - total)
# print(f"the error of closure is{error}")

##                          d  m  s
## the error of closure is [0, 1, 8]


### LAB 5
#  
## DATA 
rw_df = [70,41,30]
df_pi = [185,49,30]
pi_rw = [103,41,40]
lst = [rw_df,df_pi,pi_rw]

##calcs
for i in lst:
    i.append(af.dms_to_dd(i))
    del i[0:3]
        
total = 0
for i in lst:
    for j in i:
        total = total + j/2
print(total)
error = af.dd_to_dms(180 - total)
print(f"the error of closure is{error}")

##                         d   m   s
## the error of closure is[0, 53, 40]
