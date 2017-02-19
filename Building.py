##---------------------------##
##                           ##
## BY MICHAEL, KENNY, MATT   ##
##                           ##
##---------------------------##
##David put some collision stuff in here....##
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.task import Task
import random
from Block import Block

class Building(DirectObject):
    
    def __init__(self):
        self.blockList = []
        self.blockCount = random.randint(4,10)
        
    def Build(self, theNode, givenWidth, givenHeight, BuildingTexture, DamageTexture, TopTexture):
        self.texture = BuildingTexture
        self.damageTex = DamageTexture
        self.topTex = TopTexture
        self.blockNodeList = [theNode.attachNewNode("block"+str(i)) for i in range(self.blockCount)]
        self.blockList = [Block() for i in range(self.blockCount)]
        
        self.top = loader.loadModel("models/box")
        self.top.setScale(Vec3(15, 15, 3.4/8))
        self.top.reparentTo(self.blockNodeList[self.blockCount-1])

        for i in range(self.blockCount):
            self.blockList[i].myBlock.setTexture(self.texture)
            self.blockList[i].myBlock.reparentTo(self.blockNodeList[i])
            self.blockList[i].myBlock.setScale(Vec3(15, 15, 3.4))
            self.top.setScale(Vec3(15, 15, 3.4/8))
            self.blockList[i].myBlock.setPos(givenWidth, 0, givenHeight * i)
            self.blockList[i].myBlock.setTexRotate(TextureStage.getDefault(), 90)
            self.blockList[i].myBlock.setTexScale(TextureStage.getDefault(),3)
            self.top.setPos(Vec3(givenWidth, 0, (givenHeight * self.blockCount) - givenHeight/2+givenHeight/16))
            self.top.setTexture(self.topTex)
            self.blockList[i].uY = givenHeight*i+givenHeight
            self.blockList[i].dY = givenHeight*i
        self.width = self.getSize(self.blockList[0].myBlock).getX()
        self.height = self.getSize(self.blockList[0].myBlock).getY()
            
    def GetHeight(self):
        return self.blockCount

    def changeTexture(self, blockNum):
        if self.blockList[blockNum].health == 1:
            self.blockList[blockNum].myBlock.setTexture(self.damageTex)
            self.blockList[blockNum].myBlock.setTexRotate(TextureStage.getDefault(), 90)
            self.blockList[blockNum].myBlock.setTexScale(TextureStage.getDefault(),3)
        elif self.blockList[blockNum].health == 0:
            self.blockList[blockNum].myBlock.setTexture(self.topTex)
            self.blockList[blockNum].myBlock.setScale(7.5, 7.5, 3.4)
        
    
    def getSize(self, givenModel):
        bbox = givenModel.getTightBounds()
        size = bbox[1]-bbox[0]
        return size
