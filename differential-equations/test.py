
import vtk
import random
from scipy.integrate import odeint



class Camera (vtk.vtkCamera) :
    
    def updatePosition () :
        return 1

#
# Represents the Lorenz attractor screen saver.
#
class ScreenSaver ():

    renderer        = None

    rendererWindow  = None

    renderInteract  = None

    camera          = None

    #
    # Initialize the screen save.
    #
    def __init__(self) :
        # Initialize the window and renderer
        self.renderer           = vtk.vtkRenderer()
        self.rendererWindow     = vtk.vtkRenderWindow()
        self.rendererWindow.AddRenderer(ren)
        self.rendererWindow.SetSize (1200, 800)

        renderInteract = vtk.vtkRenderWindowInteractor()
        self.rendererWindow.SetRenderWindow(renderInteract)

        # Initialize camera
        self.camera = Camera()

    def run (self) :
        return 0

    



class vtkTimerCallback():

    x = 1.0
    y = 1.0
    z = 1.0

    assembly = None
    
    def __init__(self):
        self.timer_count = 0
 
    def execute(self,obj,event):
        self.appendLine()
       

    def updateCamera (self) :
        self.camera.SetFocalPoint(self.x,self.y,self.z)

    def appendLine (self) :

        
        
        source = vtk.vtkLineSource()
        source.SetPoint1(self.x,self.y,self.z)
        self.computeNext ()
        source.SetPoint2(self.x,self.y,self.z)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInput(source.GetOutput())
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0,0,1)
        
        self.assembly.AddPart(actor)


        #self.rendered.AddActor(actor)
        iren.GetRenderWindow().Render()
        self.timer_count += 1

        if self.timer_count % 100 == 0 :
            #self.rendered.RemoveActor(self.assembly)
            self.fadeOut()
                   
        self.updateCamera()


    def fadeOut (self) :
        return 1
        #self.assembly.GetProperty().SetColor(1,0,1)

        
    def computeNext (self) :
        #self.x += random.uniform(-0.1, 0.1)
        #self.y += random.uniform(-0.1, 0.1)
        #self.z += random.uniform(-0.1, 0.1)
        v = [self.x, self.y, self.z]
        
        def lorenz (y, x) :
           
            r       = 28
            b       = 8/3
            sigma   = 10
            dx      = sigma*(y[1]-y[0])
            dy      = r*y[0]-y[1]-y[0]*y[2]
            dz      = y[0]*y[1] - b * y[2]
            
            return [dx, dy, dz]

        r = odeint(lorenz, v, [0.0, 0.01])
        self.x = r[1][0]
        self.y = r[1][1]
        self.z = r[1][2]


# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.	SetSize (1200, 800)
 
# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 
 
# create source
source = vtk.vtkLineSource()
source.SetPoint1(0,0,0)
source.SetPoint2(-5.8,-5,-5)
 
# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInput(source.GetOutput())
 
# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)



 
# color actor
actor.GetProperty().SetColor(1,0,1)
 
# assign actor to the renderer
#ren.AddActor(actor)

sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0.0, 0.0, 0.0)
sphereSource.SetRadius(0.001)

sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphereSource.GetOutputPort())
sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)

#ren.AddActor(sphereActor)


transform = vtk.vtkTransform()
transform.Translate(1.0, 0.0, 0.0)
 
camera = vtk.vtkCamera ()
camera.SetPosition(0, 0,0)
camera.SetFocalPoint(0, 0, 0)

#ren = vtk.vtkRenderer();
ren.SetActiveCamera(camera)

iren.Initialize()
renWin.Render()

cb = vtkTimerCallback()
cb.actor = actor
cb.rendered = ren
cb.camera = camera
assembly = vtk.vtkAssembly()
cb.assembly = assembly
ren.AddActor(assembly)

iren.AddObserver('TimerEvent', cb.execute)
timerId = iren.CreateRepeatingTimer(10);

# enable user interface interactor

iren.Start()
