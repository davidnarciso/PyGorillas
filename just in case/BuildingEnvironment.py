from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
import direct.directbase.DirectStart
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from Building import Building
import sys,random
from TextureLibrary import TextureLibrary

class BuildingEnvironment(DirectObject):
    def __init__(self,myNode):
        self.worldNode = myNode
        box = loader.loadModel("models/box")
        box.setScale(Vec3(15, 15, 3.4))
        sizeVec = self.getSize(box)
        
        self.TL = TextureLibrary()
        self.HEIGHT = sizeVec.getZ()
        self.WIDTH = sizeVec.getX()
        self.createEnvironment()
        self.createGorillas()
        

    def createEnvironment(self):
        self.numOfBuildings = 15
        self.buildingNodeList = [render.attachNewNode("building"+str(i)) for i in range(self.numOfBuildings)]
        self.buildingList = [Building() for i in range(self.numOfBuildings)]

        for i in range(self.numOfBuildings):
            textureNum = random.randint(1,9)
            self.buildingList[i].Build(self.buildingNodeList[i],
                                       -self.WIDTH*self.numOfBuildings/2+self.WIDTH * i,
                                       self.HEIGHT, self.TL.getTexture(textureNum),
                                       self.TL.getTexture(textureNum+9),
                                       self.TL.getTexture(0))
            self.buildingNodeList[i].reparentTo(self.worldNode)

    def getBuildingList(self):
      return self.buildingList

    def createGorillas(self):
        self.gorillas = [loader.loadModel("models\kong")
                         for i in range(2)]
        
        self.G1Number = 2
        self.G1Building = self.buildingList[self.G1Number]
        self.G2Number = 12
        self.G2Building = self.buildingList[self.G2Number]
        ##-------Setting the X positions
        self.gorilla1Pos = -self.WIDTH*self.numOfBuildings/2+self.G1Number * self.WIDTH
        self.gorilla2Pos = -self.WIDTH*self.numOfBuildings/2+self.G2Number * self.WIDTH
        ##-------Loads the models and sets Positions
        self.gorillas[0].setScale(17)
        self.gorillas[0].setHpr(Vec3(-90, 0, 0))
        self.gorilla1TotalPos = Vec3(self.gorilla1Pos, 0, ((self.G1Building.GetHeight()*self.HEIGHT)-self.HEIGHT/2+self.HEIGHT/8))*8
        self.gorillas[0].setPos(self.gorilla1Pos, 0, ((self.G1Building.GetHeight()*self.HEIGHT)-self.HEIGHT/2+self.HEIGHT/8))
        self.gorillas[0].reparentTo(self.worldNode)
        

        self.gorillas[1].setScale(17)
        self.gorillas[1].setHpr(Vec3(90, 0, 0))
        self.gorilla2TotalPos = Vec3(self.gorilla2Pos, 0, ((self.G2Building.GetHeight() * self.HEIGHT)-self.HEIGHT/2+self.HEIGHT/8))*8
        self.gorillas[1].setPos(self.gorilla2Pos, 0, ((self.G2Building.GetHeight() * self.HEIGHT)-self.HEIGHT/2+self.HEIGHT/8))
        self.gorillas[1].reparentTo(self.worldNode)

    def getGorillas(self):
        return self.gorillas
    
    def Explode(self, point):
        ## for i in self.buildingList[]:
            exploded = random.randint(0, self.numOfBuildings-1)
            self.buildingList[exploded].Explode()
      
    def getSize(self, givenModel):
        bbox = givenModel.getTightBounds()
        size = bbox[1]-bbox[0]
        return size
