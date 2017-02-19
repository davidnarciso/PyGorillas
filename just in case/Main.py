from direct.showbase.DirectObject import DirectObject
import direct.directbase.DirectStart
from AudioLibrary import AudioLibrary
from Menu import Menu
from World import World
from Credits import finalie
import sys

class Main(DirectObject):
    def __init__(self):
        self.AL = AudioLibrary()
        self.scores = [int for i in range(3)]
        self.scores[0] = 0
        self.scores[1] = 0
        self.loadMenu()

    def loadMenu(self):
        self.myMenu = Menu()
        self.world = World(self.AL)
        self.world.menuBackGround()
        taskMgr.add(self.playYet,"playYet?")
        self.roundLimit = 0

    def playYet(self, task):
        if self.myMenu.play:
            self.roundLimit = self.myMenu.getRoundLimit()
            print self.roundLimit
            self.scores[2] = self.roundLimit
            self.loadWorld()
        return task.cont
    
    def loadWorld(self):
        self.endTime = 0
        taskMgr.remove("playYet?")
        self.world.createWorld(self.scores)
        self.player1 = self.myMenu.p1Name
        self.player2 = self.myMenu.p2Name
        self.world.createUI(self.player1, self.player2)
        taskMgr.add(self.checkScore, "checkScore")
        
    def checkScore(self,task):
        for i in range(2):
            if self.scores[i] == self.roundLimit:
                if self.endTime==0:                
                    print "Player "+str(i+1)+" Wins"
                    self.world.removeAll()
                    taskMgr.remove("checkScore")
                    self.world.stopSounds()
                if self.endTime >3:
                    base.camera.reparentTo(render)
                    self.credits = finalie(self.AL)
##                    self.credits.camMove()
                else:
                    self.endTime = self.endTime + 1
        return task.cont

#,p1Name,p2Name

        #self.playerOneName = p1Name
w = Main()
run()
