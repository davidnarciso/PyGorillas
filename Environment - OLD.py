##---------------------------##
##                           ##
## BY MICHAEL, KENNY, MATT P.##
##                           ##
##---------------------------##

import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.gui.DirectGui import *
import random
from building import Building

class Environment(DirectObject):
    def __init__(self):
        #DEBUG
        print "ENTERING CREATE ENVIRONMENT"
        
        self.THENUMBER = 15
        self.buildingNodeList = [render.attachNewNode("building"+str(i)) for i in range(self.THENUMBER)]
        self.buildingList = [Building() for i in range(self.THENUMBER)]
        #
        #self.buildingList[1].blockList[2].myBlock.getPos()
        #
        self.WIDTH = .45


        self.background = loader.loadModel("gorilla/env")
        #self.background.reparentTo(render)
        self.background.setScale(10)

       # for i in range(self.THENUMBER):
       #     self.buildingList[i].Build(self.buildingNodeList[i], self.WIDTH * i)
       #     self.buildingNodeList[i].reparentTo(render)


        #Create Monkey One
        self.monkeyOne = loader.loadModel("kong")
        self.monkeyOne.setColor(0.9,0,0)
        #self.monkeyOne.setZ(self.Building.playerOneBlock)
        #self.monkeyOne.setScale(0)
        self.monkeyOne.setX(-5.0)
        self.monkeyOne.setHpr(-90,0,0)
        self.monkey1 = CollisionSphere('m1')
        self.monkey1.addSolid(CollisionSphere(self.monkeyOne.getX(),2))
        self.monkey1.show()
        self.monkeyOne.attachNewNode(self.monkey1)
        

        #Create Monkey Two
        self.monkeyTwo = loader.loadModel("kong")
        self.monkeyTwo.setColor(0.0,0,0.9)
        self.monkeyTwo.setX(5.0)
        #self.monkeyTwo.setPos(self.buildingList[0].blockList[2].myBlock.getPos())
        #self.monkeyTwo.setScale(0)
        self.monkeyTwo.setHpr(90,0,0)

        #DEBUG
        print "END OF ENVIRONMENT"

    def Explode(self):
        exploded = random.randint(0, self.THENUMBER-1)
        self.buildingList[exploded].Explode()

