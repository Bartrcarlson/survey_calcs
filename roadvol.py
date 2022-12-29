import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial


def sta_cumi_vol(sta_area: list) -> float:
    """takes a list of locations with crosectional area in ft^2 [[feet,ft^2],etc] returns yds"""
    total = 0
    for i in range(len(sta_area)):
        if i-1 > 0:
            dist = sta_area[i][0] - sta_area[i-1][0]
            avgA = (sta_area[i][1] + sta_area[i-1][1])/2
            total = total + (dist*avgA)/27
    return total


def doublearea(coord_lst: list) -> float:
    """takes a list of coordinates with the shape [[x1,y1],[x2,y2],etc]
    and returns the area using the double area method"""
    down_diag = []
    up_diag = []
    for i in range(len(coord_lst)):
        # print(coord_lst[i])
        down_diag.append(coord_lst[i][0] * coord_lst[i-1][1])
        up_diag.append(coord_lst[i-1][0] * coord_lst[i][1])
    return abs(sum(down_diag)-sum(up_diag)) / 2 
assert(doublearea([[0,0],[0,1],[1,1],[1,0]]) == 1)


def trapezoidal_area(xyz):
    """Calculate volume under a surface defined by irregularly spaced points
    using delaunay triangulation. "x,y,z" is a <numpoints x 3> shaped ndarray.
    https://stackoverflow.com/questions/8792551/volume-under-plane-defined-by-data-points-python
    """
    d = scipy.spatial.Delaunay(xyz[:,:2])
    tri = xyz[d.vertices]

    a = tri[:,0,:2] - tri[:,1,:2]
    b = tri[:,0,:2] - tri[:,2,:2]
    vol = np.cross(a, b) @ tri[:,:,2]
    return vol.sum() / 6.0


def trap_coords(base_width,centerhgt,horiz) -> list:
    """func works on the assumption of a trapazoid crosssection
    with a horizontal bottom and road with no cross slope takes total 
    width of prism and height along with the horiz portion of bank slope"""
    lst =[]
    inset = abs(centerhgt) * horiz
    if centerhgt >0 :
        lst.append([(inset-base_width/2),0]) ## rd left @ grade
        lst.append([(-inset +base_width/2),0]) ## rd right @ grade
        lst.append([(base_width/2),-centerhgt]) ## rd right @ base
        lst.append([(-base_width/2),-centerhgt]) ## rd left @ base
        
    else:    
        lst.append([(base_width/2-inset),0]) ## rd right @ grade
        lst.append([(base_width/2),-centerhgt]) ## rd right @ base
        lst.append([(-base_width/2),-centerhgt]) ## rd left @ base
        lst.append([(-base_width/2+inset),0]) ## rd left @ grade
    return lst


def plot_sections(sections: list):
    """take a list of coordinates shaped [[x1,y1],[x2,y2],etc]
    and uses matplotlib to graph them """
    for section in sections:
        section.append(section[0])
        xs, ys = zip(*section)
        plt.plot(xs,ys)
    # plt.figure()
    plt.axis('equal')
    plt.show()



####  question 1  ########
##########################

### 1Aa
base = 40
h = 6.7
top = base - h *2/1 *2
# print(((base + top)/2) * h)       ## 178.22000000000003 ft^2
base = 40
h = 8.3
top = base - h *2/1 *2
# print(((base + top)/2) * h)       ## 194.22 ft^2

### 1Ab
a = trap_coords(40,-6.7,2)
b = trap_coords(40,-8.3,2)
# print(doublearea(a),doublearea(b))        ## 178.22, 194.22 ft^2
# plot_sections([a,b])

### 1B
dist = 100
# print(dist * ((doublearea(a)*doublearea(b))/2)/27)      ## 64099.79 yds

#### question 2 #######
#######################
"""question 2 is unsolvable the fill height combined
with the road base width and slope bank does not work. 
The specified bank slopes are to layed back for the specified
fill height more base width is needed"""

#### question 3#########
########################

### 3A
"""the end volumes are 265ft^2 and 210ft^2"""
s3640 = [[-19.2,(-5.9+4.8)],[0,0],[22.2,(6.8-5.9)],[12,-5.9],[-12,-5.9]]
# plot_sections([s3640])
# print(doublearea(s3640))        ## 191.73 ft^2

### 3B
volume = ((265 + 4*210 +191.73)/6) * 40/27
# print(volume)       ## 320 yds


###### question 4 ##########
############################
s5200 = [[-12.8,(-3+2.4)],[0,0],[15.4,.7],[8,-3],[-8,-3]]
s5300 = [[-14.2,-.7],[0,0],[16.2,.3],[8,-3.8],[-8,-3.8]]

print(doublearea(s5200))        ## 66.7 ft^2
print(doublearea(s5300))        ## 86.5 ft^2

## 4B
volume = ((doublearea(s5200)+doublearea(s5300))/2)*(100/27)
print(volume)       ## 283.8 yds

##### question 5 ########
#########################
"""the cost of excavation is different than the cost of filling and compacting
there is also issues of soil density"""

##### question 6 ########
#########################
cuts = [[1000,0],[1100,158],[1200,403],[1300,560],[1400,426],[1460,0]]
fills = [[1460,0],[1500,124],[1600,283],[1700,350],[1800,356],[1900,183],[2000,126]]


print(sta_cumi_vol(cuts))               ## 5121 yds cut
print(sta_cumi_vol(fills) * 1.25)      ## 6004.6 yds fill



##### question 20-3 #####
#########################
array = np.array([[0,0,3.4],[40,0,3.6],[80,0,4.5],
                    [0,-40,4.2],[40,-40,4.3],[80,-40,5.5], [100,-40,4.9],
                    [0,-70,6.2],[40,-70,7.4],[80,-70,6.4],[110,-70,6.2],
                    [-30,-110,2.3],[0,-110,4.1],[40,-110,4.8],[80,-110,4.4],[120,-110,5.8]])
x=array[:,0]
y=array[:,1]
z=array[:,2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_trisurf(x, y, z, cmap = 'winter', linewidth=0)
fig.colorbar(surf)
fig.tight_layout()
plt.show()


print(trapezoidal_area(array)/27)       ## 2440 yds
