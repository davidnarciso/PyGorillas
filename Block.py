##---------------------------##
##                           ##
## BY MICHAEL, KENNY, MATT   ##
##                           ##
##---------------------------##

import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
import random

class Block(DirectObject):
    
    def __init__(self):
        self.health = 2
        self.myBlock = loader.loadModelCopy("models/box")
        self.width = self.getSize(self.myBlock).getX()
        self.height = self.getSize(self.myBlock).getY()
        
    def getSize(self, givenModel):
        bbox = givenModel.getTightBounds()
        size = bbox[1]-bbox[0]
        return size
