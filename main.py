#!/usr/bin/env python3
import engine, camera, draw_voxel, texture, mapping, world, blocks
from statistics import mean
from sys import exit
import time

e = engine.Engine(600, 600, "Voxel Renderer 2.1")
c = camera.Camera(-0.5, 3, -0.5, 90, 0, 0)
w = world.World()

e.framerate = 60

w.add_block(blocks.Dirt(0,0,0))

W, A, S, D, SPACE, Q, E, I, J, K, L = 'w', 'a', 's', 'd', 'SPACE', 'LSHIFT', 'SPACE', 'i', 'j', 'k', 'l'

def drawloop(self):
    try:
        global grass, c
        #if not self.master_buffer:
        face_filter_k = []
        face_filter_v = []
        for block in w.get_world():
            face_filter_k.append(block)
            face_filter_v.append([block.face_centers.index(center) for center in sorted(block.face_centers, key=(lambda point: c.pointdist(point)))[0:3]])
            face_filter_v[face_filter_k.index(block)].reverse()
            self.master_buffer += block.get_faces(*face_filter_v[face_filter_k.index(block)])
        c.update([self.get_key(i) for i in (D, A, S, W, Q, E, L, J, K, I)])
        '''if self.get_key(W):
            c.movey(-spd)
        if self.get_key(S):
            c.movey(spd)
        if self.get_key(A):
            c.movex(-spd)
        if self.get_key(D):
            c.movex(spd)
        if self.get_key(Q):
            c.movez(spd)
        if self.get_key(E):
            c.movez(-spd)
        if self.get_key(O):
            c.roty(-rspd)
        if self.get_key(P):
            c.roty(rspd)'''
        for tile in self.master_buffer:
            self.draw_buffer.append(tile)
        self.draw_buffer.sort(key=(lambda tile: face_filter_v[face_filter_k.index(tile.parent)][list(sorted(face_filter_v[face_filter_k.index(tile.parent)], key=((lambda point: c.pointdist(tile.parent.face_centers[point]))))).index(tile.face)]))

        for tile in self.draw_buffer:
            verts = [mapping.map_point(c, e, *[tile.coords[0][i] / tile.w for i in range(3)]),
                     mapping.map_point(c, e, *[tile.coords[1][i] / tile.w for i in range(3)]),
                     mapping.map_point(c, e, *[tile.coords[2][i] / tile.w for i in range(3)]),
                     mapping.map_point(c, e, *[tile.coords[3][i] / tile.w for i in range(3)])]
            self.col = (int(tile.color[1:3], 16),
                        int(tile.color[3:5], 16),
                        int(tile.color[5:7], 16))
            self.poly(verts)
        self.draw_buffer.clear()
        self.master_buffer.clear()

        self.text(35, 10, ("X: %.3f" % c.x))
        self.text(35, 25, ("Y: %.3f" % c.y))
        self.text(35, 40, ("Z: %.3f" % c.z))
        self.text(35, 70, ("FPS: %.2f" % self.clock.get_fps()))
    except KeyboardInterrupt:
        print("Application closed by user.")
        exit(0)

e.drawloop = drawloop
e.dlargs = [e,]
e.mainloop()
