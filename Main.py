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
            self.names = self.myMenu.getNames()
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
                self.winner = i
                self.world.worldNotDone = 0
                taskMgr.add(self.endGame,"endGame")
                taskMgr.remove("checkScore")
        return task.cont
    def endGame(self,task):
        if task.time > 11:
            print "And the winner is: " + str(self.names[self.winner])
            base.bufferViewer.toggleEnable()
            self.world.removeAll()
            self.credits = finalie(self.AL,self.names)
            taskMgr.remove("endGame")
        return task.cont
#,p1Name,p2Name

        #self.playerOneName = p1Name
w = Main()
run()
