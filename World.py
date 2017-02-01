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

class World(DirectObject):
        def __init__(self):
                #base.disableMouse()
                print "Created Env."
                mainWindow=base.win
                altBuffer=mainWindow.makeTextureBuffer("hello", 256, 256)
                self.rendNode = render.attachNewNode('rendNode')
                #self.rendNode.reparentTo(render)
                self.scale = .5
                self.num_of_buildings = 25
                self.loadmodels()
                self.pBoolean = 1
                self.nBoolean = 0
                self.togglePBuildings()
                self.toggleNBuildings()
                self.accept("p",self.togglePBuildings)
                self.accept("n",self.toggleNBuildings)
                self.cameraTricks()
                self.Environment = Environment(1,0)
                #render.explore()

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
                self.clouds = loader.loadModel('models/env')
                self.clouds.reparentTo(self.rendNode)
                self.clouds.setScale(700)

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
                self.cars2 = Cars(self.scale*.5,500*self.scale,-75/2,0,"car-2")
                
                self.building = [loader.loadModelCopy('models/glassbuilding')
                                 for i in range(self.num_of_buildings*4)]
                
                self.loadBuildings(5,120,0)
                self.loadBuildings(30,200,self.num_of_buildings)
                self.loadBuildings(20,-175*1.5,self.num_of_buildings*2)
                self.loadBuildings(60,-250*1.5,self.num_of_buildings*3)
                
                #the roads values are affected by the scale
        def togglePBuildings(self):
                ###Needs to delete buildings already there
                if(self.pBoolean):
                        for i in range(self.num_of_buildings*2):
                                self.building[i].show()#.setTransparency(TransparencyAttrib.MNone)
                        self.pBoolean = 0
                        print"changed positive buildings on"
                else:
                        for i in range(self.num_of_buildings*2):
                                self.building[i].hide()#.setTransparency(TransparencyAttrib.MAlpha)# = loader.loadModelCopy('models/nothing')
                        self.pBoolean = 1
                        
        def toggleNBuildings(self):
                if(self.nBoolean):
                        for i in range(self.num_of_buildings*2):
                                self.building[i+self.num_of_buildings*2].show()#setTransparency(TransparencyAttrib.MNone)
                        self.nBoolean = 0
                        print"changed negitive buildings on"
                else:
                        for i in range(self.num_of_buildings*2):
                                self.building[i+self.num_of_buildings*2].hide()#setTransparency(TransparencyAttrib.MAlpha)# = loader.loadModelCopy('models/nothing')
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


        def loadBuildings(self, offset, y, number):
                for i in range(self.num_of_buildings):
                        self.building[i+number].reparentTo(self.rendNode)
                        x = -500+(120*i*self.scale)+offset
                        z = 0
                        h = random.randint(2,4)
                        height = h*.15
                        self.building[i+number].setScale(Vec3(.3,.3,height)*5*self.scale*.75)
                        self.building[i+number].setPos(Vec3(x,y*1.25,z)*self.scale*.75)


#e = myEnvironment()
#run()
