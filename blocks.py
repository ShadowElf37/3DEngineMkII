from draw_voxel import Block

class Dirt(Block):
    def __init__(self, x, y, z):
        super(Dirt, self).__init__(x, y, z, 'dirt')