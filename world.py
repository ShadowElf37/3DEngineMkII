class World:
    def __init__(self):
        self.world = {}
    def add_block(self, block):
        self.world[(block.x, block.y, block.z)] = block
    def remove_block(self, x, y, z):
        self.world[(x, y, z)] = None
    def get_block(self, x, y, z):
        return self.world[(x, y, z)]
    def get_world(self):
        return self.world.values()