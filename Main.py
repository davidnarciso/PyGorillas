import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from direct.showbase.DirectObject import DirectObject
import sys,random,math
from direct.interval.MetaInterval import Sequence
from direct.task import Task
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
from World import World
from UserInterface import OfTheAwesomeSupremeRulerOfTheCosmos

class Main(DirectObject):
    ####################MENU#################
    #Calls the menu class which asks for our
    #Player's names and the max score
    #########################################
    def __init__(self,roundLimit):
        self.world = World()
        g1pos = self.world.Environment.gorilla1TotalPos
        g2pos = self.world.Environment.gorilla2TotalPos
        self.isShowing = 1
        self.UI = OfTheAwesomeSupremeRulerOfTheCosmos(1,g1pos,g2pos)
        taskMgr.add(self.checkForCollisions,'checking') 

        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.roundLimit = roundLimit
        self.continuePlaying = 1

    def checkForCollisions(self,task):
        if self.UI.JonsWizardry1.fired==1:
            bounds = self.UI.JonsWizardry1.newPos
            #print str(bounds.getX())
            for i in range(self.world.Environment.THENUMBER):
                buildingNX = self.world.Environment.buildingList[i].nX
                buildingPX = self.world.Environment.buildingList[i].pX
                if bounds.getX()>buildingNX and bounds.getX()<buildingPX:
                    print 'i: '+str(i+1)+' tnob: '+str(self.world.Environment.THENUMBER)+' CP: '+str(bounds.getX())+' BOB: '+str(buildingNX)+'-'+str(buildingPX)
                    if self.isShowing:
                        for p in range(self.world.Environment.buildingList[i].THENUMBER):
                            self.world.Environment.buildingList[i].blockList[p].myBlock.hide()
                        self.isShowing=0
                    else:
                        for p in range(self.world.Environment.buildingList[i].THENUMBER):
                            self.world.Environment.buildingList[i].blockList[p].myBlock.show()
                        self.isShowing=1
                            
##                        blockUY = self.world.Environment.buildingList[i].blockList[p].uY
##                        blockDY = self.world.Environment.buildingList[i].blockList[p].dY
##                        if bounds.getY()<=blockUY and bounds.getY()>=blockDY:
##                            xp =random.randint(0,100)
##                            print'done'+str(i)+str(p)+str(xp)
        return task.cont

    def checkScore(self,task):
        if self.playerOneScore == self.roundLimit:
            print "Player One Wins!"
            self.continuePlaying = 0
        elif self.playerTwoScore == self.roundLimit:
            print "Player Two Wins!"
            self.continuePlaying = 0

newGame = Main(3)
run()


