from random import randint
from PIL import Image

imgx = 500; imgy = 500
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()
color = [(0,0, 0), (255, 255, 255)]

sx=101
sy=101
nm=50
maze = [[0 for x in range(sx)] for y in range(sy)]
dx=[0,1,0,-1]
dy=[-1,0,1,0]

'''
cx=randint(0,mx-1)
cy=randint(0,my-1)
stack.append((cx,cy))
print(stack)
'''
stack = [(randint(0, sx - 1),randint(0, sy - 1))]
while len(stack) > 0:
    (cx, cy) = stack[-1]
    maze[cy][cx] = 1
    # find a new cell to add
    nlst = [] # list of available neighbors
    for i in range(4):
        nx = cx + dx[i]; ny = cy + dy[i]
        if nx >= 0 and nx < sx and ny >= 0 and ny < sy:
            if maze[ny][nx] == 0:
                # of occupied neighbors must be 1
                ctr = 0
                for j in range(4):
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < sx and ey >= 0 and ey < sy:
                        if maze[ey][ex] == 1: ctr += 1
                if ctr == 1: nlst.append(i)
    # if 1 or more neighbors available then randomly select one and move
    if len(nlst) > 0:
        ir = nlst[randint(0, len(nlst) - 1)]
        cx += dx[ir]; cy += dy[ir]
        stack.append((cx, cy))
    else: stack.pop()

counter=1
for row in maze:
    print("line: ",counter)
    for cell in row:
        print (cell, end='')
    print ('\n')
    counter+=1
