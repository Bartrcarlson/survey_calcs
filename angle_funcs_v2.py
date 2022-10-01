
def dd_to_dms(dd):

    dms = []
    dms.append(int(dd))
    m = (dd % 1) * 60
    dms.append(int(m))
    s = (m % 1) * 60
    dms.append(round(s)) 
 
    if dms[1] >= 60:
        dms[0] = dms[0] + int(dms[1]/60)
        dms[1] = dms[1] - int(dms[1]/60) * 60
    
    if dms[2] >= 60:
        dms[1] = dms[1] + int(dms[2]/60)
        dms[2] = dms[2] - int(dms[2]/60) * 60

    return dms



def dms_to_dd(dms):
    return dms[0] + dms[1]/60 + dms[2]/3600


def az_to_bearing(az,type):

    bearing =[None]*3
    if az < 0 or az>360:
        raise ValueError('value must be between 0 and 360')

    if az >=270 or az<=90:
        bearing[0] = "N"
    else:
        bearing[0] = "S"

    if az >= 0 and az <= 180:
        bearing[2] = "E"
    else:
        bearing[2] = "w"

    if az <= 90:
        bearing[1] = az
    elif az >= 270:
        bearing[1] = 360 - az
    elif az > 90 and az < 180:
        bearing[1] = 180 - az
    elif az >= 180 and az < 270:
        bearing[1] = az - 180
    if type == 'dd':
        return bearing
    else:
        dd_to_dms(bearing[1])
        return [bearing[0],dd_to_dms(bearing[1]), bearing[2]]



def bearing_to_az(bearing, type):

    if bearing[1] <0 or bearing[1]>90:
        raise ValueError('value must be between 0 and 90')

    if bearing[0] == "N" and bearing[2] == "E":
        az = bearing[1]

    elif bearing[0] == "S" and bearing[2] == "E":
        az = 180 - bearing[1]
        
    elif bearing[0] == "S" and bearing[2] == "W":
        az = 180 + bearing[1]

    elif bearing[0] == "N" and bearing[2] == "W":
        az = 360 - bearing[1]

    if type == 'dd':
        return az
    else:
        return dd_to_dms(az) 


def internal_angles(sides):
    angles = []
    for i in range(len(sides)):
   
        x = sides[i] - sides[i-1]
        if x < 0:
            angles.append(abs(180 + x))
        else:
            angles.append(abs(180 - x))
    return angles

def deflection_angles(sides):
    angles = []
    for i in range(len(sides)):
   
        x = sides[i] - sides[i-1]
        if x < 0:
            angles.append(abs(x))
        else:
            angles.append(abs(x))
    return angles

def side_ex_ang(int_angle,prev_side):
    run = (180-int_angle) + prev_side

    if run < 0:
        return run + 360
    elif run > 360:
        return run -360
    else:
        return run


