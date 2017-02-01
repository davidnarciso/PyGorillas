import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.showbase import DirectObject
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.task import * 
import math,random, sys, string

class Cars(DirectObject):
  def genLabelText(self, text, i):
    return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                       align = TextNode.ALeft, scale = .05, mayChange = 1)
  def __init__(self,scale,x,y,z,name):
    self.scale = scale
    self.startX = x
    self.startY = y
    self.startZ = z
    self.name = name
    
    self.numberOfCars = 1
    self.cars = [loader.loadModelCopy("models/carnsx")
      for i in range(self.numberOfCars)]
    for i in range(self.numberOfCars):
      self.cars[i].setColor(random.random(), random.random(), random.random())

    for i in range(self.numberOfCars):
      self.cars[i].reparentTo(render)
      self.cars[i].setPosHpr(0, i - self.numberOfCars / 2, 200, 90, 0, 0)
      self.cars[i].setScale(2.5)

    self.moveCars()
      
  def moveCars(self):
    for i in range(self.numberOfCars):
      carPosInterval1= self.cars[i].posInterval(random.uniform(.20, .50) * 5*self.scale*10,Point3(self.startX, self.startY , self.startZ), startPos=Point3(self.startX*-1,self.startY, self.startZ))
      carPosInterval2= self.cars[i].posInterval(random.uniform(.20, .50) * 5*self.scale*10,Point3(self.startX*-1,self.startY, self.startZ), startPos=Point3(self.startX,self.startY,self.startZ))
      carHprInterval1= self.cars[i].hprInterval(random.uniform(.20, .50) * 5,Point3(270,0,0), startHpr=Point3(90,0,0)) 
      carHprInterval2= self.cars[i].hprInterval(random.uniform(.20, .50) * 5,Point3(90,0,0), startHpr=Point3(270,0,0))

      carMove = Sequence(carPosInterval1, carHprInterval1, carPosInterval2,
                         carHprInterval2, name = "carMove" + str(i)+self.name)
      carMove.loop()
      
#w = World()
#run()
