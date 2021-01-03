import pygame
import numpy as np
import rotationMatrices as rm

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
pygame.font.init()

screenWidth = 800
screenHeight = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Window Caption
pygame.display.set_caption("Perspective Projection")

done = 0
clock = pygame.time.Clock()


#------FSHEF_---------

xy_theta = 0.0
yz_theta = 0.0


camera_loc = np.array([0.0,0.0,0.0,1.0])
camera_to_plane_dist = 1
toCameraSpaceMatrix = np.array([[np.cos(xy_theta),np.sin(xy_theta),0,0],[-np.sin(xy_theta),np.cos(xy_theta),0,0],[0,0,1,0],[0,0,0,1]])

fov = 90.0
near = 0.1
far = 100.0

persp = np.zeros([4,4])
s = 1/np.tan((np.pi*fov)/360)
persp[0][0] = s
persp[1][1] = s
persp[2][2] = (-far)/(far - near)
persp[3][2] = (-far * near)/(far - near)
persp[2][3] = -1
#print(persp)

combinedMatrix = np.array([])




vertices = np.array([[3,6,5,1],[2,7,4,1],[6,6,6,1]])
vertCount, num_columns = vertices.shape
screenVertices = np.zeros([3,4])
print(vertices)


#---------------bob----------------
while done == False:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        yz_theta -= .01
    if keys[pygame.K_DOWN]:
        yz_theta += .01
    if keys[pygame.K_LEFT]:
        xy_theta -= .01
    if keys[pygame.K_RIGHT]:
        xy_theta += .01

    if keys[pygame.K_w]:
        camera_loc -= .2 * toCameraSpaceMatrix[:,2]
    if keys[pygame.K_a]:
        camera_loc[0] += 1
    if keys[pygame.K_s]:
        camera_loc += .2 * toCameraSpaceMatrix[:,2]
    if keys[pygame.K_d]:
        camera_loc[0] += 1

    screen.fill(BLACK)


    #------------the stuff------------

    toCameraSpaceMatrix = np.identity(4)
    toCameraSpaceMatrix = np.matmul(toCameraSpaceMatrix, np.array([[np.cos(xy_theta),np.sin(xy_theta),0,0],[-np.sin(xy_theta),np.cos(xy_theta),0,0],[0,0,1,0],[0,0,0,1]]))
    toCameraSpaceMatrix = np.matmul(toCameraSpaceMatrix, np.array([[1,0,0,0],[0,np.cos(yz_theta),np.sin(yz_theta),0],[0,-np.sin(yz_theta),np.cos(yz_theta),0],[0,0,0,1]]))
    toCameraSpaceMatrix[3] = camera_loc
    
    combinedMatrix = np.matmul(toCameraSpaceMatrix, persp)
    
    i = 0
    for vertex in vertices:
        screenVertices[i] = np.dot(vertex, combinedMatrix)
        i += 1
        
    for vertex in range(vertCount):
        for i in range(4):
            screenVertices[vertex][i] = np.interp(screenVertices[vertex][i]/screenVertices[vertex][2], [-1,1], [0,screenWidth])

    pygame.draw.polygon(screen, WHITE, ((screenVertices[0][0],screenVertices[0][1]),(screenVertices[1][0],screenVertices[1][1]),(screenVertices[2][0],screenVertices[2][1])), 1)


    pygame.display.update()

pygame.quit()