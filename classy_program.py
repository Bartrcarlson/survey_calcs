import math
from optparse import Values
import angle_funcs_v2 as af


class Angle:
    def __init__(self,ang=None):
        if type(ang) == list: 
            self.ang = af.dms_to_dd(ang)
            self.dms = ang
        elif type(ang) == int or type(ang) == float:
            self.ang = ang
            self.dms = af.dd_to_dms(ang)
        elif type == None:
            pass
        else:
            raise(ValueError('type must be \'dd\' or \'dms\' or None'))
    def __float__(self):
        return self.ang

class Coord():
    def __init__(self,easting=None,northing=None):
        self.easting = easting
        self.northing = northing
        self.both_coords = [easting,northing]

class Point(Angle, Coord):
    def __init__(self, ang, easting, northing):
        super().__init__(ang)
        self.coords = [easting,northing]

class Line():
    def __init__(self, ang=None, length=None, start_p=None, end_p=None,proj_start=None,proj_end=None):
        self.length = length
        # self.e_dep = math.sin(math.radians(ang)) * length
        # self.n_dep = math.cos(math.radians(ang)) * length
        self.start_p = start_p
        self.end_p = end_p
        self.proj_start = proj_start
        self.proj_end = proj_end

    def add_point(self,new_point):
        lst = self.position
        return lst.append(new_point)



p1 = Point(Angle([1,0,0]).ang,5000,5000)
p2 = Point(Angle([1,0,0]).ang,5001,5000)
l1 = Line(ang=None, length=20,start_p=[5000,5000])
l1.proj_start_p = [[5000,5000],[6000,6000]]
l1.proj_start.add_point([7000,7000])


print(l1.proj_start_p)




