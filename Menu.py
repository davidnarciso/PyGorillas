import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from pandac.PandaModules import TextNode
from direct.gui.OnscreenImage import OnscreenImage
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import WindowProperties

class Menu(DirectObject):
        def __init__(self):
                wp = WindowProperties()
                wp.setFullscreen(True)
                base.win.requestProperties(wp)
                
                self.bk_text = "Gorillas"
                self.textObject = OnscreenText(text = self.bk_text,
                                               pos = (0, 0.65, 0), 
                                               scale = 0.07,
                                               fg=(1,1,0,1),
                                               align=TextNode.ACenter,
                                               mayChange=1)
                indistar = loader.loadFont('images/SF Distant Galaxy.ttf')
                self.textObject.setFont(indistar)
                self.p1Name = 'Player 1'
                self.p2Name = 'Player 2'
                self.rounds = '3'
                self.accept("enter", self.runGame)

                self.play = 0

                self.runMenu()
                self.labelsOfAreas()
                
        def p1saveText(self, textEntered):
                self.p1Name = textEntered

        def p2saveText(self, textEntered):
                self.p2Name = textEntered

        def roundssaveText(self, textEntered):
                self.rounds = textEntered

        def p1popUp(self):
                self.textObject.setText("Enter Player 1's name in the box to the left and press the 'Enter' Key")
                self.textObject.setWordwrap(15.0)
                self.textObject.setColor(0,0,1,1)

        def p2popUp(self):
                self.textObject.setText("Enter Player 2's name in the box to the left and press the 'Enter' Key")
                self.textObject.setWordwrap(15.0)
                self.textObject.setColor(1,0,0,1)
                
        def roundspopUp(self):
                self.textObject.setText("Enter the number of round wins needed to win the game in the box to the left and press the 'Enter' Key")
                self.textObject.setWordwrap(15.0)
                self.textObject.setColor(0,1,1,1)

        def p1clearText(self):
                self.p1Text.enterText('')
                
        def p2clearText(self):
                self.p2Text.enterText('')
                
        def roundsClearText(self):
                self.roundsText.enterText('')
                
        def getp1name(self):
                return self.p1Name
        
        def getp2name(self):
                return self.p2Name

        def getNames(self):
                self.names = [str for i in range(2)]
                self.names[0] = self.p1Name
                self.names[1] = self.p2Name
                return self.names
        
        def getRounds(self):
                return self.rounds
        
        def runMenu(self):
                #add button
                self.p1Button = DirectButton(text = ("?", "?", "?", "?"),
                                             scale=.05,
                                             command=self.p1popUp)
                self.p1Button.setZ(.3)
                self.p1Button.setX(.15)
                
                self.p2Button = DirectButton(text = ("?", "?", "?", "?"),
                                             scale=.05,
                                             command=self.p2popUp)
                self.p2Button.setZ(.15)
                self.p2Button.setX(.15)
                
                self.roundsButton = DirectButton(text = ("?", "?", "?", "?"),
                                                 scale=.05,
                                                 command=self.roundspopUp)
                self.roundsButton.setX(.15)
                
                self.playGameButton = DirectButton(text = ("Play Game", "Play Game", "Play Game", "Play Game"),
                                                   scale=.07,
                                                   command=self.runGame)
                self.playGameButton.setX(.5)
                self.playGameButton.setZ(.15)

                self.p1Text = DirectEntry(text = "",
                                          scale=.05,
                                          command=self.p1saveText,
                                          initialText="Player 1",
                                          numLines = 1,
                                          focus=0,
                                          focusInCommand=self.p1clearText)
                self.p1Text.setZ(.3)
                self.p1Text.setX(-.5)
                
                self.p2Text = DirectEntry(text = "",
                                          scale=.05,
                                          command=self.p2saveText,
                                          initialText="Player 2",
                                          numLines = 1,
                                          focus=0,
                                          focusInCommand=self.p2clearText)
                self.p2Text.setZ(.15)
                self.p2Text.setX(-.5)
                
                self.roundsText = DirectEntry(text = "",
                                              scale=.05,
                                              command=self.roundssaveText,
                                              initialText="3",
                                              numLines = 1,
                                              focus=0,
                                              focusInCommand=self.roundsClearText)
                self.roundsText.setX(-.5)
                
        def labelsOfAreas(self):
                self.p1Label=DirectLabel(text = "Player 1's Name:", scale=.05)
                self.p1Label.setZ(.3)
                self.p1Label.setX(-.75)
                self.p2Label=DirectLabel(text = "Player 2's Name:", scale=.05)
                self.p2Label.setZ(.15)
                self.p2Label.setX(-.75)
                self.roundsLabel=DirectLabel(text = "Number of Rounds:", scale=.05)
                self.roundsLabel.setX(-.75)

        def getRoundLimit(self):
                rounds = self.roundsText.get()
                self.p1Label.destroy()
                self.p2Label.destroy()#setScale(0.0007)#hide()
                self.p1Text.destroy()#hide()
                self.p2Text.destroy()#hide()
                self.p1Button.destroy()#hide()
                self.p2Button.destroy()#hide()
                self.roundsButton.destroy()#hide()
                self.roundsText.destroy()#hide()
                self.textObject.destroy()
                self.playGameButton.destroy()
                self.roundsLabel.destroy()
                return int(rounds)
        
        def runGame(self):
                self.play = 1
                

##M = Menu()
##run()

