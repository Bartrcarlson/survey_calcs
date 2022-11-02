def rate(g2,g1,dist) -> float:
    return (g2-g1)/dist
    
def vcurve_elev(x,bvc,dist,g2,g1) -> float:
    """takes x location along vcurve and returns elevation in ft
    where x is dist in feet. bvc is elev in ft. dist is the length of curve
    in ft. g2 is grade leaving curve in decimal. g1 grade entering cruve in decimal"""
    return bvc + g1*x + (rate(g2,g1,dist) / 2) * (x**2)
    
def vcurve_max_min(g2,g1,dist) -> float:
    """finds the max or min of the curve and returns the x position aka the horizontal distance
    from begining of vertical curvature"""
    return -g1/rate(g2,g1,dist)
    
