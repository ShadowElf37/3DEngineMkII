import mapping
from math import sqrt

class Camera:
    def __init__(self, x, y, z, thetaX, thetaY, thetaZ):
        self.x, self.y, self.z = x, y, z
        self.vx, self.vy, self.vz = 0, 0, 0
        self.mcap, self.macc = 0.05, 0.0025
        self.thetaX, self.thetaY, self.thetaZ = thetaX, thetaY, thetaZ
        self.vxr, self.vyr, self.vzr = 0, 0, 0
        self.rcap, self.racc = 5, 1
        self.inair = False
        self.origin = self.x, self.y, self.z
        self.ux, self.uy, self.uz = self.x, self.y, self.z
    def update(self, keys): # keys is a boolean list of [xup, xdown, yup, ydown, zup, zdown, tleft, tright, tup, tdown]
        # x-motion
        if keys[0]:
            if self.vx < self.mcap:
                self.vx += self.macc
        elif keys[1]:
            if self.vx > -self.mcap:
                self.vx -= self.macc
        else:
            if self.vx >= self.macc:
                self.vx -= self.macc
            elif self.vx <= -self.macc:
                self.vx += self.macc
            else:
                self.vx = 0
        
        # y-motion
        if keys[2]:
            if self.vy < self.mcap:
                self.vy += self.macc
        elif keys[3]:
            if self.vy > -self.mcap:
                self.vy -= self.macc
        else:
            if self.vy >= self.macc:
                self.vy -= self.macc
            elif self.vy <= -self.macc:
                self.vy += self.macc
            else:
                self.vy = 0
        
        # z-motion
        if keys[4]:
            if self.vz < self.mcap:
                self.vz += self.macc
        elif keys[5]:
            if self.vz > -self.mcap:
                self.vz -= self.macc
        else:
            if self.vz >= self.macc:
                self.vz -= self.macc
            elif self.vz <= -self.macc:
                self.vz += self.macc
            else:
                self.vz = 0
        
        # LR-rotation:
        if keys[6]:
            if self.vyr < self.rcap:
                self.vyr += self.racc
        elif keys[7]:
            if self.vyr > -self.rcap:
                self.vyr -= self.racc
        else:
            if self.vyr >= self.racc:
                self.vyr -= self.racc
            elif self.vyr <= -self.racc:
                self.vyr += self.racc
            else:
                self.vyr = 0
        
        # UD-rotation:
        if keys[8]:
            if self.vxr < self.rcap:
                self.vxr += self.racc
        elif keys[9]:
            if self.vxr > -self.rcap:
                self.vxr -= self.racc
        else:
            if self.vxr >= self.racc:
                self.vxr -= self.racc
            elif self.vxr <= -self.racc:
                self.vxr += self.racc
            else:
                self.vxr = 0
        
        # finally update the actual variables
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        if(abs(self.thetaX + self.vxr - 90) < 90):
            self.thetaX += self.vxr
        self.thetaY += self.vyr
        self.thetaZ += self.vzr
        self.persp_rot()

    def persp_rot(self):
        self.ux, self.uy, self.uz = self.x, self.y, self.z#mapping.rotate([self.x, self.y, self.z], self.thetaZ, 2, origin=self.origin)
    def pointdist(self, point):
        try:
            return (self.x - point[0]) * (self.x - point[0]) + (self.y - point[1]) * (self.y - point[1]) + (self.z - point[2]) * (self.z - point[2]) # apparently * much faster than ** for small exps
        except ValueError:
            return 0
