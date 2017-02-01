import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *   #Needed to use Intervals
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from direct.showbase.PythonUtil import *
from direct.actor import Actor 
from math import pi, sin
import sys, string, random
#from Environment import Environment
from VirtualWorlds import Cars

class myEnvironment(DirectObject):
        def __init__(self):
                self.scale = .5
                self.loadmodels()
                self.loadLighting()
                self.otherEnvironment = Environment(12*self.scale)
                
        def loadmodels(self):
                self.clouds = loader.loadModel("models/env")
                self.clouds.reparentTo(render)#base.camera)
                self.clouds.setScale(700*self.scale)
                self.clouds.setZ(-3*self.scale)
                self.cloudTex = loader.loadTexture("models/env_sky.jpg")
                self.clouds.setTexture(self.cloudTex)

                self.sun = loader.loadModel("models/sun")
                self.sun.reparentTo(render)
                #self.sunTex = loader.loadTexture("models/happySun.jpg")
                #self.sun.setTexture(self.sunTex)
                self.sun.setHpr(Vec3(90,180,0))
                self.sun.setPos(Vec3(0,100,160)*self.scale)
                self.sun.setScale(.25*self.scale)
                #self.sun.setColor(Vec4(.8,.2,.5,.5))
                #self.sun.lookAt(base.camera)

                self.camera_root = base.camera.attachNewNode('root')#self.car[0].attachNewNode('root')
                #self.camera_root.setPos(Vec3(0,0,3))
                #self.camera_root.lookAt(self.car[i])
                #base.camera.reparentTo(self.camera_root)
                
                self.cars1 = Cars(self.scale*.5,500*self.scale,0,0,"car1")
                self.makeRoad(20,0,-.01,25)
                self.cars2 = Cars(self.scale*.5,500*self.scale,175/2,0,"car2")
                self.makeRoad(0,175,0,25)

                self.loadBuildings(35,250,0)
                self.cars3 = Cars(self.scale*.5,500*self.scale,275/2,0,"car3")
                self.makeRoad(20,275,-.01,25)
                self.loadBuildings(5,350,0)
                self.cars4 = Cars(self.scale*.5,500*self.scale,375/2,0,"car4")
                self.makeRoad(20,375,-.01,25)
                self.loadBuildings(50,450,0)

        def makeRoad(self,x,y,z,num):
                road = [ loader.loadModelCopy("models/road")
                              for i in range(num)]
                for i in range(num):
                        x = 500-(i*48.25)
                        road[i].reparentTo(render)
                        road[i].setH(90)
                        road[i].setPos(Vec3(x,y,z)*self.scale)
                        road[i].setScale(Vec3(1.5,10,.05)*self.scale)


        def loadBuildings(self, offset, y, facing):
                self.num_of_buildings = 15
##                self.building = [Actor.Actor('models/glassbuildingMove')
##                                 for i in range(self.num_of_buildings)]
                self.building = [loader.loadModelCopy('models/glassbuildingMove')
                                 for i in range(self.num_of_buildings)]
                for i in range(self.num_of_buildings):
                        self.building[i].reparentTo(render)
                        x = -400+(120*i*self.scale)+offset
                        z = 0
                        h = random.randint(2,4)
                        height = h*.15
                        self.building[i].setScale(Vec3(.3,.3,height)*5*self.scale)
                        self.building[i].setPos(Vec3(x,y,z)*self.scale)
##                        self.buildingMove[i] = Sequence(
##                                self.building[i].actorInterval('buildingMove'))
##                        self.buildingMove[i].loop()

        def loadLighting(self):
##                alight = AmbientLight('alight')
##                alight.setColor(Vec4(.5,.5,.5,1))
##                alnp = render.attachNewNode(alight.upcastToPandaNode())
##                render.setLight(alnp)

##                slight = Spotlight('slight')
##                slight.setColor(Vec4(1, 1, 1, 1)) 
##                lens = PerspectiveLens() 
##                slight.setLens(lens) 
##                slight = render.attachNewNode(slight.upcastToLensNode()) 
##                slight.reparentTo(self.camera_root) 
##                #slight.lookAt(self.car[0]) 
##                render.setLight(slight)

                plight = PointLight('plight') 
                plight.setColor(VBase4(1, 1, 1, 1)) 
                plnp = render.attachNewNode(plight.upcastToPandaNode()) 
                self.sun.setLight(plnp) 
                plnp.reparentTo(self.sun)

e = myEnvironment()
run()
