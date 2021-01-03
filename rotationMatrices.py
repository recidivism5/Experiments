import numpy as np

def rotClockwiseXY(vector,theta):

    return np.dot(vector,np.array([[np.cos(theta),np.sin(theta),0],[-np.sin(theta),np.cos(theta),0],[0,0,1]]))

def rotAnticlockwiseXY(vector,theta):

    return np.dot(vector,np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]]))

def rotClockwiseYZ(vector,theta):

    return np.dot(vector,np.array([[1,0,0],[0,np.cos(theta),np.sin(theta)],[0,-np.sin(theta),np.cos(theta)]]))

def rotAnticlockwiseYZ(vector,theta):

    return np.dot(vector,np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]]))


