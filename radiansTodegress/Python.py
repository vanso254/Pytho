from numpy import pi as pi


def convertRadians(degrees):
    radians=degrees*(pi/180)
    return radians


def convertDegrees(radians):
    degrees=radians*(180/pi)
    return degrees