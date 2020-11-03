from pygame import Color
import texture
from statistics import mean

# Note: x is right, y is back, z is down

modes = [
    lambda c, v: v.parent.z > c.z,  # top
    lambda c, v: v.parent.z < c.z,  # bottom
    lambda c, v: v.parent.y < c.y,  # back
    lambda c, v: v.parent.y > c.y,  # front
    lambda c, v: v.parent.x > c.x,  # right
    lambda c, v: v.parent.x < c.x,  # left
] # NOTE: as is, the backface culling system will not be able to support non-cube blocks - so????

class Block:
    def __init__(self, x, y, z, texture_path):
        self.tex = texture.load_tex(texture_path) # 2D list of hex vals
        self.x = x
        self.y = y
        self.z = z
        self.flists = {}
        self.faces = [ # Because of the way this works, adding faces would be somewhat difficult, though not impossible
            # PLEASE NOTE that these are likely VERY wrong and probably will ONLY WORK for a cube at 0,0,0
               lambda x,y: ((x,     y,     self.z),
                            (x + 1, y,     self.z),
                            (x + 1, y + 1, self.z),
                            (x,     y + 1, self.z)),
               lambda x,y: ((x,     y,     self.z - self.tex.w),
                            (x + 1, y,     self.z - self.tex.w),
                            (x + 1, y + 1, self.z - self.tex.w),
                            (x,     y + 1, self.z - self.tex.w)),
               lambda x,y: ((x,     self.z, y - self.tex.w),
                            (x + 1, self.z, y - self.tex.w),
                            (x + 1, self.z, y - self.tex.w + 1),
                            (x,     self.z, y - self.tex.w + 1)),
               lambda x,y: ((x,     self.z + self.tex.w, y - self.tex.w),
                            (x + 1, self.z + self.tex.w, y - self.tex.w),
                            (x + 1, self.z + self.tex.w, y - self.tex.w + 1),
                            (x,     self.z + self.tex.w, y - self.tex.w + 1)),
               lambda x,y: ((self.z, x,     y - self.tex.w),
                            (self.z, x + 1, y - self.tex.w),
                            (self.z, x + 1, y - self.tex.w + 1),
                            (self.z, x,     y - self.tex.w + 1)),
               lambda x,y: ((self.z + self.tex.w, x,     y - self.tex.w),
                            (self.z + self.tex.w, x + 1, y - self.tex.w),
                            (self.z + self.tex.w, x + 1, y - self.tex.w + 1),
                            (self.z + self.tex.w, x,     y - self.tex.w + 1))
        ]
        self.face_centers = [
            (self.x, self.y, self.z + self.tex.w / 2),  # bottom
            (self.x, self.y, self.z - self.tex.w / 2),  # top
            (self.x, self.y - self.tex.h / 2, self.z),  # back
            (self.x, self.y + self.tex.h / 2, self.z),  # front
            (self.x + self.tex.w / 2, self.y, self.z),  # right
            (self.x - self.tex.w / 2, self.y, self.z),  # left
        ]
    def get_face(self, face):
        if not self.flists.get(face):
            self.flists[face] = list([Tile(self, self.tex.w, face, self.faces[face](x,y), self.tex.data[y][x]) for x in range(self.tex.w) for y in range(self.tex.h)])
        return self.flists[face]
    def get_faces(self, *indices):
        if not indices:
            return [*self.get_face(0), *self.get_face(1), *self.get_face(2), *self.get_face(3), *self.get_face(4), *self.get_face(5)]
        else:
            l = []
            for i in indices:
                l += self.get_face(i)
            return l

class Tile: #square/pixel of voxel texture
    def __init__(self, parent, size, face, coords, color_cls):
        self.parent = parent
        self.last = False
        self.face = face
        self.w = self.h = size
        self.color = color_cls
        self.seen = True
        self.cmp_mode = modes[face]
        self.coords = coords # note this will be a 2D array of tuples
        self.center = [mean([coords[i][j] for i in range(len(coords))]) for j in range(3)]
