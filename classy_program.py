import math
import angle_funcs_v2 as af


class Angle:
    def __init__(self,ang=None):
        if type(ang) == list: 
            if type(ang[0]) == int:
                self.ang = af.dms_to_dd(ang)
                self.dms = ang
            else:
                self.ang = af.bearing_to_az([ang[0],af.dms_to_dd(ang[1]),ang[2]],'dd')
                self.dms = af.bearing_to_az([ang[0],af.dms_to_dd(ang[1]),ang[2]],'dms')
        elif type(ang) == int or type(ang) == float:
            self.ang = ang
            self.dms = af.dd_to_dms(ang)
        elif type == None:
            pass
        else:
            raise(ValueError('type must be \'dd\' or \'dms\' or None'))
    def __float__(self):
        return self.ang


class Line():
    def __init__(self, ang=None, length=None, start_p=None):
        self.length = length
        self.dep = [math.sin(math.radians(ang)) * length]
        self.dep.append(math.cos(math.radians(ang)) * length)
        self.start_p = start_p






