import sys, math, pygame, numpy as np, rotationMatrices as rM
pygame.init()
pygame.font.init()

def setPlates():
    spatialPixelIncrement = (rayLength/arrayLength)*2

    pixelSize = math.floor((windowSize/arrayLength))
    print(pixelSize)

    vertTheta = 0
    horizTheta = 0

    cameraPos = np.array([0,0,0])
    cameraRay = np.array([rayLength,0,0])
    cameraRayTop = np.array([rayLength,0,rayLength])

    topLeft = np.array([rayLength,rayLength,rayLength])

    plate = np.array([[[rayLength,rayLength,rayLength]]*(arrayLength+1)]*(arrayLength+1))
    for row in range(arrayLength+1):
        for j in range(arrayLength+1):
            plate[row,j,1] = plate[row,j,1] - j*spatialPixelIncrement
            plate[row,j,2] = plate[row,j,2] - row*spatialPixelIncrement
    
    YZplate = np.array([[[-rayLength,rayLength,rayLength]]*(arrayLength+1)]*(arrayLength+1))
    for row in range(arrayLength+1):
        for j in range(arrayLength+1):
            YZplate[row,j,0] = YZplate[row,j,0] + j*spatialPixelIncrement
            YZplate[row,j,2] = YZplate[row,j,2] - row*spatialPixelIncrement

WHITE = (255,255,255)

#pygame.event.set_grab(1)

windowSize = 800
screen = pygame.display.set_mode((windowSize,windowSize))


arrayLength = 25



rayLength = 1.0

spatialPixelIncrement = (rayLength/arrayLength)*2

pixelSize = math.floor((windowSize/arrayLength))
print(pixelSize)

pygame.display.set_caption("swag")

done = 0
clock = pygame.time.Clock()

vertTheta = 0
horizTheta = 0

cameraPos = np.array([0,0,0])
cameraRay = np.array([rayLength,0,0])
cameraRayTop = np.array([rayLength,0,rayLength])

topLeft = np.array([rayLength,rayLength,rayLength])

plate = np.array([[[rayLength,rayLength,rayLength]]*(arrayLength+1)]*(arrayLength+1))
for row in range(arrayLength+1):
    for j in range(arrayLength+1):
        plate[row,j,1] = plate[row,j,1] - j*spatialPixelIncrement
        plate[row,j,2] = plate[row,j,2] - row*spatialPixelIncrement



#print(plate[100,100])

YZplate = np.array([[[-rayLength,rayLength,rayLength]]*(arrayLength+1)]*(arrayLength+1))
for row in range(arrayLength+1):
    for j in range(arrayLength+1):
        YZplate[row,j,0] = YZplate[row,j,0] + j*spatialPixelIncrement
        YZplate[row,j,2] = YZplate[row,j,2] - row*spatialPixelIncrement





class Sphere:
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

class Plane:
    
    def __init__(self,corner1,corner2,corner3,rMax,rMin,qMax,qMin):
        self.corner1 = corner1
        self.corner2 = corner2
        self.corner3 = corner3
        self.rMax = rMax
        self.rMin = rMin
        self.qMax = qMax
        self.qMin = qMin

    
testPlane = Plane([0,5,0],[-10,5,0],[6,11,11],100,0,100,0)





light = [8,0,20]
sphere1 = Sphere([8,0,0],5)
sphere2 = Sphere([8,0,6],2)

sphereBobNum = 0.0


while done == False:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1
            
    #sphere1.center[2] = sphere1.center[2] + np.sin(sphereBobNum)/10
    #sphere1.center[1] = sphere1.center[1] + np.cos(sphereBobNum)/10
    if sphereBobNum < 10: 
        sphereBobNum += 0.01
    else: sphereBobNum = 0.0

    
    

    if keys[pygame.K_w]:
        light = np.add((plate[int(arrayLength/2),int(arrayLength/2)]/(-10)),light)
        sphere1.center = np.add((plate[int(arrayLength/2),int(arrayLength/2)]/(-10)),sphere1.center)
    if keys[pygame.K_s]:
        light = np.add((plate[int(arrayLength/2),int(arrayLength/2)]/(10)),light)
        sphere1.center = np.add((plate[int(arrayLength/2),int(arrayLength/2)]/(10)),sphere1.center)
    if keys[pygame.K_q]:
        upVector = np.subtract(plate[arrayLength,int(arrayLength/2)],plate[int(arrayLength/2),int(arrayLength/2)])/10
        light = np.add(upVector,light)
        sphere1.center = np.add(upVector,sphere1.center)
    if keys[pygame.K_e]:
        upVector = np.subtract(plate[arrayLength,int(arrayLength/2)],plate[int(arrayLength/2),int(arrayLength/2)])/10
        light = np.add(-upVector,light)
        sphere1.center = np.add(-upVector,sphere1.center)
    if keys[pygame.K_a]:
        leftVector = np.subtract(plate[int(arrayLength/2),arrayLength],plate[int(arrayLength/2),int(arrayLength/2)])/10
        light = np.add(leftVector,light)
        sphere1.center = np.add(leftVector,sphere1.center)
    if keys[pygame.K_d]:
        leftVector = np.subtract(plate[int(arrayLength/2),arrayLength],plate[int(arrayLength/2),int(arrayLength/2)])/10
        light = np.add(-leftVector,light)
        sphere1.center = np.add(-leftVector,sphere1.center)
    if keys[pygame.K_UP]:
        light[0] -= 1
    if keys[pygame.K_DOWN]:
        light[0] += 1
    if keys[pygame.K_i]:
        vertTheta += .05
    if keys[pygame.K_k]:
        vertTheta -= .05
    if keys[pygame.K_j]:
        horizTheta -= .05
    if keys[pygame.K_l]:
        horizTheta += .05

    if keys[pygame.K_p]:
        arrayLength += 5
        setPlates()
    if keys[pygame.K_o]:
        arrayLength -= 5
        setPlates()

    #mRel = pygame.mouse.get_rel()
    #horizTheta = horizTheta + mRel[0]/100
    #vertTheta = vertTheta + mRel[1]/100

    #modYZplate = YZplate
    #print(YZplate[int(arrayLength/2),int(arrayLength/2)])
    if vertTheta != 0:
        for row in range(arrayLength+1):
            for j in range(arrayLength+1):
                YZplate[row,j] = rM.rotClockwiseYZ(YZplate[row,j],vertTheta)

    if horizTheta != 0:
        for row in range(arrayLength+1):
            for j in range(arrayLength+1):
                YZplate[row,j] = rM.rotClockwiseXY(YZplate[row,j],-horizTheta)
        
        #print(modYZplate[int(arrayLength/2),int(arrayLength/2)])
        #print(horizTheta)

    plate = YZplate
    YZplate = np.array([[[-rayLength,rayLength,rayLength]]*(arrayLength+1)]*(arrayLength+1))
    for row in range(arrayLength+1):
        for j in range(arrayLength+1):
            YZplate[row,j,0] = YZplate[row,j,0] + j*spatialPixelIncrement
            YZplate[row,j,2] = YZplate[row,j,2] - row*spatialPixelIncrement
    

    for row in range(arrayLength+1):
        for j in range(arrayLength+1):
            b = -2 * np.dot(plate[row,j],sphere1.center)
            a = np.dot(plate[row,j],plate[row,j])
            c = np.dot(sphere1.center,sphere1.center) - (sphere1.radius)*(sphere1.radius)

            if b*b - 4*a*c >= 0:
                t1 = (-b + np.sqrt(b*b - 4*a*c))/(2*a)
                t2 = (-b - np.sqrt(b*b - 4*a*c))/(2*a)
                if t1 < t2:
                    scalar = t1
                else:
                    scalar = t2
                if scalar < 0:
                    break
                point = np.multiply(scalar,plate[row,j])
                pointRay = np.subtract(light,point)
                swagPoint = np.subtract(point,sphere1.center)

                a = np.dot(pointRay,pointRay)
                b = 2 * np.dot(pointRay,swagPoint)
                c = np.dot(swagPoint,swagPoint) - sphere1.radius * sphere1.radius

                if b*b - 4*a*c >= 0:
                    r1 = (-b + np.sqrt(b*b - 4*a*c))/(2*a)
                    r2 = (-b - np.sqrt(b*b - 4*a*c))/(2*a)
                    #print(r1,r2)

                    
                        
                    maxR1 = (sphere1.radius * 2) / np.sqrt(np.dot(pointRay,pointRay))
                    minR1 = 0
                    newR1 = np.interp(r1,[minR1,maxR1],[200,0])
                        
                    pygame.draw.rect(screen,(newR1,newR1,newR1),[(pixelSize*j),(pixelSize*row),pixelSize,pixelSize])
                    
                    

            else:
                pygame.draw.rect(screen,(85,30,70),[(pixelSize*j),(pixelSize*row),pixelSize,pixelSize])

    
    for row in range(arrayLength+1):
        for j in range(arrayLength+1):
            
            testPlaneMatrix = np.array([testPlane.corner2,testPlane.corner3,-plate[row,j]])
            solution = np.dot(np.negative(testPlane.corner1),np.linalg.inv(testPlaneMatrix))
            if solution[0] in range(testPlane.rMin,testPlane.rMax): #and solution[1] in range(testPlane.qMin,testPlane.qMax):
                pygame.draw.rect(screen,(255,255,255),[(pixelSize*j),(pixelSize*row),pixelSize,pixelSize])


    #if horizTheta != 0:
     #   for row in range(arrayLength+1):
      #      for j in range(arrayLength+1):
       #         plate[row,j] = rM.rotClockwiseXY(plate[row,j],-horizTheta)
    #if horizTheta < 0:
     #   for row in range(arrayLength+1):
      #      for j in range(arrayLength+1):
       #         plate[row,j] = rM.rotAnticlockwiseXY(plate[row,j],horizTheta)
    #if vertTheta != 0:
        
     #   p = np.resize(plate[int(arrayLength/2),int(arrayLength/2)],(2))
        #print(p)
      #  nTheta = np.arccos(np.dot(p,[0,rayLength])/np.sqrt((np.dot(p,p))*rayLength))
        #print(nTheta)
       # newMatrix = np.matmul(np.array([[np.cos(nTheta),np.sin(nTheta),0],[-np.sin(nTheta),np.cos(nTheta),0],[0,0,1]]),np.array([[1,0,0],[0,np.cos(vertTheta),-np.sin(vertTheta)],[0,np.sin(vertTheta),np.cos(vertTheta)]])), 
        #print(newMatrix)

        #for row in range(arrayLength+1):
         #   for j in range(arrayLength+1):
                
          #      plate[row,j] = np.dot(plate[row,j],newMatrix)

    
    #print(horizTheta)
        
    

    


    pygame.display.update()



pygame.quit()
