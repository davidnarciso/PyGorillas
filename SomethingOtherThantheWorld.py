import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *   #Needed to use Intervals
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from direct.showbase.PythonUtil import *
from direct.actor import Actor 
from math import pi, sin
import sys, string, random
from Environment import Environment
from VirtualWorlds import Cars

class myEnvironment(DirectObject):
        def __init__(self):
                #base.disableMouse()
                print "Created Env."
                mainWindow=base.win
                altBuffer=mainWindow.makeTextureBuffer("hello", 256, 256)
                self.rendNode = render.attachNewNode('rendNode')
                #self.rendNode.reparentTo(render)
                self.scale = .5
                self.loadmodels()
                self.pBoolean = 1
                self.nBoolean = 0
                self.togglePBuildings()
                self.toggleNBuildings()
                self.accept("p",self.togglePBuildings)
                self.accept("n",self.toggleNBuildings)
                self.cameraTricks()
                self.otherEnvironment = Environment(1,-100)
                #render.explore()
                self.setLoops()

        def setLoops(self):
                self.thl = LerpFunc(
                        self.spinBanana,
                        duration = .5)
                self.thl.loop()
                
        def spinBanana(self,rad):
                h = self.proj.getH()
                p = self.proj.getP()
                r = (rad*360) #- self.teeth.getR()
                self.proj.setHpr(Vec3(h,p,r))

        def cameraTricks(self):
                self.cNode = self.rendNode.attachNewNode("camNode")
                base.camera.reparentTo(self.cNode)
                self.cNode.reparentTo(self.rendNode)
                self.cNode.setPos(Vec3(0,-80,100))
##                self.altCam=base.makeCamera(altBuffer)
##                self.altCam.reparentTo(self.cam_root)
##                self.buff = base.bufferViewer
##                self.buff.setPosition("llcorner")
##                self.buff.setCardSize(.85,.85)
                zoomIn = self.cNode.posInterval(5,Vec3(-20,-40,50)*2,startPos = Vec3(-20,40,100)*2.5)
                self.cNode.lookAt(self.sun)
                zi = Sequence(zoomIn)
                #zi.loop(1)

        def makeSunMad(self):
                self.sun.setColor(Vec4(.8,.2,.5,.5))
                
        def loadmodels(self):
                self.clouds = loader.loadModel('models/environment')
                self.clouds.reparentTo(self.rendNode)
                self.clouds.setScale(700*self.scale)
                self.clouds.setZ(-3*self.scale)
                #self.cloudTex = loader.loadTexture('models/env_sky.jpg')
                #self.clouds.setTexture(self.cloudTex)

                self.sun = loader.loadModel('models/sun')
                self.sun.reparentTo(self.rendNode)
                self.sun.setHpr(Vec3(90,180,0))
                self.sun.setPos(Vec3(0,80,200)*self.scale)
                self.sun.setScale(.25*self.scale)
                #self.sun.lookAt(self.cNode)

                self.camera_root = base.camera.attachNewNode('root')
                
                self.makeRoad(75,25)
                self.cars1 = Cars(self.scale*.5,500*self.scale,75/2,0,'car-1')
                self.makeRoad(-75,25*1.5)
                self.cars2 = Cars(self.scale*.5,500*self.scale,-75/2*1.5,0,"car-2")
                
                #the roads values are affected by the scale
        def togglePBuildings(self):
                if(self.pBoolean):
                        self.loadBuildings(5,120)
                        self.loadBuildings(30,200)
                        self.pBoolean = 0
                else:
                        self.pBoolean = 1
                        
        def toggleNBuildings(self):
                if(self.nBoolean):
                        self.loadBuildings(20,-175*1.5)
                        self.loadBuildings(60,-250*1.5)
                        self.nBoolean = 0
                else:
                        self.nBoolean = 1

        def makeRoad(self,y,num):
                road = [ loader.loadModelCopy('models/road')
                              for i in range(num)]
                for i in range(num):
                        x = (475-(i*48.25))
                        z = 0
                        road[i].reparentTo(self.rendNode)
                        road[i].setH(90)
                        road[i].setPos(Vec3(x,y,z)*self.scale)
                        road[i].setScale(Vec3(3,10,.05)*self.scale)


        def loadBuildings(self, offset, y):
                self.num_of_buildings = 25
##                self.building = [Actor.Actor('models/glassbuildingMove')
##                                 for i in range(self.num_of_buildings)]
                self.building = [loader.loadModelCopy('models/glassbuilding')
                                 for i in range(self.num_of_buildings)]
##                tex1 = loader.loadTexture('models/gbRed.png')
##                tex2 = loader.loadTexture('models/gbYellow.png')
##                tex3 = loader.loadTexture('models/gbLightBlue.png')
##                tex4 = loader.loadTexture('models/gbGreen.png')
##                tex5= loader.loadTexture('models/gbSkyBlue.png')
##                color = [for i in range(self.num_of_buildings)]
                for i in range(self.num_of_buildings):
                        self.building[i].reparentTo(self.rendNode)
                        x = -425+(120*i*self.scale)+offset
                        z = 0
                        h = random.randint(2,4)
                        height = h*.15
                        self.building[i].setScale(Vec3(.3,.3,height)*5*self.scale*.75)
                        self.building[i].setPos(Vec3(x,y*1.25,z)*self.scale*.75)
                        
##                        color[i] = random.randint(1,5)
##                        if(color[i]==1):
##                                self.building[i].setTexture(tex1)
##                        elif(color[i]==2):
##                                self.building[i].setTexture(tex2)
##                        elif(color[i]==3):
##                                self.building[i].setTexture(tex3) 
##                        elif(color[i]==4):
##                                self.building[i].setTexture(tex4)
##                        elif(color[i]==5):
##                                self.building[i].setTexture(tex5)

#e = myEnvironment()
#run()
