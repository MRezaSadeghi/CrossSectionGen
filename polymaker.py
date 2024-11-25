import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt

import logging

class PolyAnalysis():
    
    def __init__(self) -> None:
        # Initialize the logger
        self.logger = logging.getLogger('poly_logger')
        self.logger.setLevel(logging.DEBUG)
        
        # Format
        formatter = logging.Formatter('[%(funcName)s:%(lineno)d] %(levelname)s => %(message)s')

        # Handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        # Add the handler to the logger
        if not self.logger.hasHandlers():
            self.logger.addHandler(ch)
    
    def random_polar_generator(self, n, method="fully_random"):
        
        if method == "band_random":
            band_theta = 2*np.pi/n
            theta = np.random.rand(n)*band_theta
            theta = theta + band_theta*np.arange(n)
            
        elif method == "fully_random":
            theta = np.random.rand(n)*2*np.pi
            theta = np.sort(theta)
            
        
        r0 = 0.1
        r1 = 0.5
        r = r0 + np.random.rand(n)*(r1 - r0)
        
        self.logger.debug(f"theta: {theta*180/np.pi}")
        self.logger.debug(f"theta: {r}")
        
        x = r*np.sin(theta)
        y = r*np.cos(theta)
        
        return x, y
    
    def regular_generator(self, n):
        r = 0.5
        theta = np.linspace(0, 2*np.pi, n+1)
        theta = theta[:-1]
        
        x = r*np.sin(theta)
        y = r*np.cos(theta)
        
        return x, y
        
    def rotate_2d(self, x, y, theta):
        # counter clock wise
        rotation = R.from_euler('z', theta, degrees=False)
        A = rotation.apply(np.vstack((x, y, x*0)).T)
        x_rotated = A[:, 0]
        y_rotated = A[:, 1]
        return x_rotated, y_rotated
    
    def get_area(self, x, y):
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        A = np.dot(x[:-1], y[1:]) - np.dot(y[:-1], x[1:])
        A /= -2
        return A
    def get_centroid(self, x, y):
        area = self.get_area(x, y)
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        n = len(x)
        
        Cx, Cy = 0, 0
        for i in range(n-1):
            xi, yi = x[i], y[i]
            xip, yip = x[i+1], y[i+1]
            
            A = xi*yip - xip*yi
            Cx += (xi + xip)*A
            Cy += (yi + yip)*A
            
        Cx, Cy = -Cx/(6*area), -Cy/(6*area)
        return Cx, Cy
        
    def get_moment2(self, x, y):
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        n = len(x)
        
        Ix, Iy, Ixy = 0, 0, 0
        for i in range(n-1):
            xi, yi = x[i], y[i]
            xip, yip = x[i+1], y[i+1]
            
            A = xi*yip - xip*yi
            Iy += A*(xi**2 + xip*xi + xip**2)
            Ix += A*(yi**2 + yip*yi + yip**2)
            Ixy += A*(xi*yip + xip*yi + 2*xi*yi + 2*xip*yip)
        
        Ix, Iy, Ixy = -Ix/12, -Iy/12, -Ixy/12
        Jz = Ix + Iy #polar moment x
        return Ix, Iy, Ixy, Jz
    
    def ploy_draw_ax(self, x, y):
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        v = (x, y, "k")
        ax.plot(*v)
        plt.show()
        
        return None
    