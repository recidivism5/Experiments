import pygame
import numpy as np
import rotationMatrices as rm

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screenWidth = 800
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Window Caption
pygame.display.set_caption("Perspective Projection")

done = 0
clock = pygame.time.Clock()

tris_OS = np.array([[[0.5, 0.5, -0.5],[0.5, -0.5, -0.5],[-0.5, -0.5, -0.5]],\
                   [[0.5, 0.5, -0.5],[-0.5, 0.5, -0.5],[-0.5, -0.5, -0.5]],\

                   [[0.5, 0.5, -0.5],[-0.5, 0.5, -0.5],[-0.5, 0.5, 0.5]],\
                   [[0.5, 0.5, -0.5],[-0.5, 0.5, -0.5],[0.5, 0.5, 0.5]],\

                   [[0.5, 0.5, 0.5],[0.5, -0.5, 0.5],[-0.5, -0.5, 0.5]],\
                   [[0.5, 0.5, 0.5],[-0.5, 0.5, 0.5],[-0.5, -0.5, 0.5]],\

                   [[0.5, -0.5, -0.5],[-0.5, -0.5, -0.5],[-0.5, -0.5, 0.5]],\
                   [[0.5, -0.5, -0.5],[-0.5, -0.5, -0.5],[0.5, -0.5, 0.5]],\

                   [[0.5, 0.5, -0.5],[0.5, -0.5, -0.5],[0.5, -0.5, 0.5]],\
                   [[0.5, 0.5, -0.5],[0.5, 0.5, 0.5],[0.5, -0.5, 0.5]],\

                   [[-0.5, 0.5, -0.5],[-0.5, -0.5, -0.5],[-0.5, -0.5, 0.5]],\
                   [[-0.5, 0.5, -0.5],[-0.5, 0.5, 0.5],[-0.5, -0.5, 0.5]]])

tris_WS = np.zeros((tris_OS.shape[0],3,3))
cube_center = np.array([0.0, 0.0, -4.0])

tris_pixel = np.zeros((tris_OS.shape[0],3,2))

y_theta = 0

def rotate_tris_y(y_theta):
    for i in range(tris_OS.shape[0]):
        for vector in range(tris_OS.shape[1]):
            tris_WS[i][vector] = rm.rotClockwiseXY(tris_OS[i][vector], y_theta)
def rotate_tris_x(x_theta):
    for i in range(tris_OS.shape[0]):
        for vector in range(tris_OS.shape[1]):
            tris_WS[i][vector] = rm.rotClockwiseYZ(tris_WS[i][vector], y_theta)

def translate_tris():
    for i in range(tris_OS.shape[0]):
        for vector in range(tris_OS.shape[1]):
            tris_WS[i][vector] = np.add(tris_WS[i][vector], cube_center)

def perspective_divide():
    for i in range(tris_OS.shape[0]):
        for vector in range(tris_OS.shape[1]):
            tris_pixel[i][vector][0] = int(800*((tris_WS[i][vector][0] / tris_WS[i][vector][2] + 1.0)/2))
            tris_pixel[i][vector][1] = int(800*((tris_WS[i][vector][1] / tris_WS[i][vector][2] + 1.0)/2))

def draw():
    for i in range(tris_pixel.shape[0]):
        pygame.draw.polygon(screen, WHITE, ((tris_pixel[i][0][0],tris_pixel[i][0][1]),(tris_pixel[i][1][0],tris_pixel[i][1][1]),(tris_pixel[i][2][0],tris_pixel[i][2][1])), 1)

while done == False:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1

    keys = pygame.key.get_pressed()

    screen.fill(BLACK)

    rotate_tris_y(y_theta)
    rotate_tris_x(y_theta)
    translate_tris()
    perspective_divide()
    draw()

    if y_theta < (2 * 3.1459):
        y_theta += 0.01
    else:
        y_theta = 0.0

    pygame.display.update()

pygame.quit()
