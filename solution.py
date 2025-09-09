import numpy as np

def calculate_step(p1, p2, p3, v1, v2, v3, m1, m2, m3, dt, G):

    rAB = p2 - p1
    rAC = p3 - p1
    rBC = p3 - p2

    FAB = -G*m1*m2*(rAB /np.linalg.norm(rAB)) / np.linalg.norm(rAB)**2
    FAC = -G*m1*m3*(rAC /np.linalg.norm(rAC)) / np.linalg.norm(rAC)**2
    FBC = -G*m2*m3*(rBC /np.linalg.norm(rBC)) / np.linalg.norm(rBC)**2

    v1 = (v1 * m1 + (-FAB -FAC)*dt) / m1
    v2 = (v2 * m2 + (FAB - FBC)*dt) / m2
    v3 = (v3 * m3 + (FAC + FBC)*dt) / m3
    

    p1 = p1 + v1*m1*dt/m1
    p2 = p2 + v2*m2*dt/m2
    p3 = p3 + v3*m3*dt/m3

    return p1, p2, p3, v1, v2, v3