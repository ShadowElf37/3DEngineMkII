from math import radians, cos, sin, tan

def rotate(xyz, theta, axis, origin=(0,0,0)):
    theta = radians(theta)
    x, y, z = xyz
    nx, ny, nz = x, y, z
    c = cos(theta)
    s = sin(theta)
    x -= origin[0]
    y -= origin[1]
    z -= origin[2]
    if axis == 0:
        ny = c*y - s*z
        nz = s*y + c*z
        ny += origin[1]
        nz += origin[2]
    elif axis == 1:
        nx = c*x - s*z
        nz = s*x + c*z
        nx += origin[0]
        nz += origin[2]
    elif axis == 2:
        nx = c*x - s*y
        ny = s*x + c*y
        nx += origin[0]
        ny += origin[1]
    else:
        return 1
    return nx, ny, nz

def map_to_cam(xyz, cam):
    x, y, z = xyz
    x += cam.ux
    y -= cam.uy
    z -= cam.uz
    x, y, z = rotate((x, y, z), cam.thetaX, 0)
    x, y, z = rotate((x, y, z), cam.thetaY, 1)
    x, y, z = rotate((x, y, z), cam.thetaZ, 2)
    return x, y, z

def map_to_2d(mapped_xyz, width, height, scale=1):
    x, y, z = mapped_xyz
    if z >= 0: #clipping
        try:
            nx = ((width / 2) * x / z) * scale
            ny = ((height / 2) * y / z) * scale
        except ZeroDivisionError:
            nx = x
            ny = y
        if nx > width/2:
            newx = 0
        elif nx < width/2:
            newx = width
        else:
            newx = x
        if ny > height/2:
            newy = 0
        elif ny < height/2:
            newy = height
        else:
            newy = y
        return newx, newy
    newx = ((width / 2) * x / z) * scale
    newy = ((height / 2) * y / z) * scale
    return newx+width/2, newy+height/2

def map_point(cam, engine, x, y, z, scale=1):
    return map_to_2d(map_to_cam((x, y, z), cam), engine.width, engine.height, scale)
