#
# CS Problem 26
# Author: Daniel Wechsler
#

#
# A screen saver drawing trajectories following the Lorenz equation.
# It's based on vtk (see http://www.vtk.org)
#


import vtk
import random
from scipy.integrate import odeint


#
# The camara shooting the sceene. Inherits
# from vtkCamera and adds the update method
# which moves the camera.
#
class Camera (vtk.vtkCamera) :

    # Determines the focus point of the camera
    # the object needs properties x, y, z
    focusPointDet = None

    pitch = 0.5

    def __init__(self) :
        self.SetFocalPoint(0, 0, 0)
        self.SetPosition(60, 60, 60)

    def update (self) :
        self.updatePosition()
        self.updateFocusPoint()

    #
    # Updates the position of the camera. Let it rotate
    # around the focus point
    #
    def updatePosition (self) :       
        self.Azimuth 	 (self.pitch)		

    #
    # Updates the focus point such that the camera points
    # to the x,y,z valus of the focusPointDet object.
    # 
    def updateFocusPoint (self) :
        if self.focusPointDet != None :
             self.SetFocalPoint(self.focusPointDet.x, self.focusPointDet.y, self.focusPointDet.z)   
        



#
# The clas is responsible for drawing a trajectroy
# following the Lorenz equation an thus produce an
# image of the Lorenz attractor. 
#
class LorenzTrajectory (vtk.vtkAssembly) :

    STEP_SIZE = 0.015       # Step size used to compuet next position
    
    x = 1.0

    y = 1.0
    
    z = 1.0

    color = [0, 1, 0]

    #
    # Init a random starting point and choose
    # a random color.
    #
    def __init__(self) :
        self.x          = random.uniform(-4, 4)
        self.y          = random.uniform(-4, 4)
        self.z          = random.uniform(-4, 4)
        self.color[0]   = random.random()
        self.color[1]   = random.random()
        self.color[2]   = random.random()
        

    def update (self) :

        # Draw a line from current to next position.
        source      = vtk.vtkLineSource()
        source.SetPoint1(self.x,self.y,self.z)
        self.computeNextPosition ()
        source.SetPoint2(self.x,self.y,self.z)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInput(source.GetOutput())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        # Visual effects
        actor.GetProperty().SetColor(self.color)
        actor.GetProperty().SetOpacity (0.6)
        self.AddPart(actor)
        

    #
    # For the corrent x,y,z position the method computes
    # the next position according to the Lorenz equation
    # using scipy odeint.
    #
    def computeNextPosition (self) :

        v = [self.x, self.y, self.z]
        def lorenz (y, x) :
            r       = 28
            b       = 8/3
            sigma   = 10
            dx      = sigma*(y[1]-y[0])
            dy      = r*y[0]-y[1]-y[0]*y[2]
            dz      = y[0]*y[1] - b * y[2]
            return [dx, dy, dz]
        
        r = odeint(lorenz, v, [0.0, self.STEP_SIZE])
        self.x = r[1][0]
        self.y = r[1][1]
        self.z = r[1][2]
        

#
# Represents the Lorenz attractor screen saver.
#
class ScreenSaver ():

    MAX_ITERATIONS  = 1500 # Max number of iterations until reset of scene.

    renderer        = None

    rendererWindow  = None

    renderInteract  = None

    camera          = None

    trajectory      = None

    iteration       = 0

    #
    # Initialize the screen save.
    #
    def __init__(self) :
        # Initialize the window and renderer
        self.renderer           = vtk.vtkRenderer()
        self.rendererWindow     = vtk.vtkRenderWindow()
        
        self.rendererWindow.AddRenderer(self.renderer)
        self.rendererWindow.SetSize (1200, 800)

        self.renderInteract = vtk.vtkRenderWindowInteractor()
        self.renderInteract.SetRenderWindow(self.rendererWindow)     
        
        # Cerate the camara observing the scene
        self.camera = Camera()
        self.rendererWindow.Size;

        

    #
    # Puts trajectories and the camara into the scene
    #
    def setUpScene (self) :
        # Init the trajectory
        self.trajectory = LorenzTrajectory()
        self.renderer.AddActor(self.trajectory)
       
        # Initialize camera position
        self.camera.focusPointDet = self.trajectory
        self.renderer.SetActiveCamera(self.camera)
         
    #
    # Removes all actors from the scene. Used before reinitialization.
    # 
    def tearDownScene (self) :
        self.renderer.RemoveActor(self.trajectory);


    def resetScene (self) :
        self.tearDownScene()
        self.setUpScene()
        iteration = 0
        

    #
    # The main loop of the screen saver
    #
    def run (self) :
        self.setUpScene()
        self.renderInteract.Initialize()
        self.rendererWindow.Render()
   
        # Init a timer event that periodically calls the update method
        self.renderInteract.AddObserver('TimerEvent', self.update)
        self.renderInteract.CreateRepeatingTimer(10);
        self.renderInteract.Start()


    #
    # Periodically called method the updates the scene
    # 
    def update (self, obj,event) :
        self.trajectory.update()
        
        self.camera.update()
        self.renderInteract.GetRenderWindow().Render()
        self.iteration += 1
        # Reset the scene after some iterations (rendering becomse too slow otherwise) 
        if self.iteration % self.MAX_ITERATIONS == 0 : 
            self.resetScene()
    

screenSaver = ScreenSaver()
screenSaver.run()

