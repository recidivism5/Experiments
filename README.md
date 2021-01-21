# Experiments

I made raytracer8.py in December 2019 to try and get a better idea of how to program 3d apps and use matrix transformations. It relies on a few 3x3 numpy matrices for rotating the camera frustum around.
The camera is always at the origin to simplify calculations. I didn't really look much up when I made this so the math might be funny to someone who's made a raytracer before.
I can remember working out on paper that I could use a discriminant to determine if a scan line from the camera would intersect with the surface of a sphere.
The controls are WASD for moving around based on the direction the camera is facing. Q and E move you up and down the y axis. IJKL rotates the camera. The sphere in the scene is 90 degrees to the right when you load in.

3dPerspectiveProjection.py is something I recently made to try and understand 4x4 perspective projection matrices. I'm going based off the scratchapixel guides.
At the moment it just renders a single triangle. The controls are W and S and arrow keys for rotating the camera.
