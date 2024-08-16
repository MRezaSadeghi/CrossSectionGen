import numpy as np
import matplotlib.pyplot as plt
import logging

class PolyGenerator():
    
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
            theta = np.random.rand(n)*2*np.p
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
        
    
    
    def ploy_draw_ax(self, x, y):
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        v = (x, y, "k")
        ax.plot(*v)
        plt.show()
        
        return None
    