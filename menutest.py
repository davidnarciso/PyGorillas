import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *


from pandac.PandaModules import TextNode
from direct.gui.OnscreenImage import OnscreenImage
##from Main import Main


imageObject = OnscreenImage(image = 'gorilla-bananas.jpg', pos = (.75, 0, 0.2))
imageObject.setScale(.5)
#add some text
bk_text = "This is my Demo"
textObject = OnscreenText(text = bk_text, pos = (0.95,-0.95), 
scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
anthem = loader.loadSfx("Sounds/Stats.wav")
anthem.setLoop(True)
anthem.play()
base.setBackgroundColor( 200, 200, 0)

#callback function to set  text
def p1setText(textEntered):
        textObject.setText(textEntered)

def p2setText(textEntered):
        textObject.setText(textEntered)

def roundsSetText(textEntered):
        textObject.setText(textEntered)

def p1popUp():
        textObject.setText("Enter Player 1's name in the box to the left and press the 'Enter' Key")

def p2popUp():
        textObject.setText("Enter Player 2's name in the box to the left and press the 'Enter' Key")
def roundspopUp():
        textObject.setText("Enter the number of round wins needed to win the game in the box to the left and press the 'Enter' Key")

def p1clearText():
	p1Text.enterText('')
def p2clearText():
        p2Text.enterText('')
def roundsClearText():
        roundsText.enterText('')
##def playGame():
##        if p1Text.get() != "" and p2Text.get() != "" and roundsText.get() > 0:
##                newGame = Main(roundsText.get())
##                base.close()
                
#add button
p1Button = DirectButton(text = ("?", "?", "?", "?"),scale=.05,command=p1popUp)
p1Button.setZ(.3)
p1Button.setX(.15)
p2Button = DirectButton(text = ("?", "?", "?", "?"),scale=.05,command=p2popUp)
p2Button.setZ(.15)
p2Button.setX(.15)
roundsButton = DirectButton(text = ("?", "?", "?", "?"),scale=.05,command=roundspopUp)
roundsButton.setX(.15)
##playGameButton = DirectButton(text = ("Play Game", "Play Game", "?", "?"),scale=.05,command=playGame)
##playGameButton.setX(.15)
##playGameButton.setZ(.2)

p1Text = DirectEntry(text = "" ,scale=.05,command=p1setText,
initialText="Player 1", numLines = 1,focus=0,focusInCommand=p1clearText)
p1Text.setZ(.3)
p1Text.setX(-.5)
p2Text = DirectEntry(text = "" ,scale=.05,command=p2setText,
initialText="Player 2", numLines = 1,focus=0,focusInCommand=p2clearText)
p2Text.setZ(.15)
p2Text.setX(-.5)
roundsText = DirectEntry(text = "" ,scale=.05,command=roundsSetText,
initialText="1", numLines = 1,focus=0,focusInCommand=roundsClearText)
roundsText.setX(-.5)

p1Label=DirectLabel(text = "Player 1's Name:", scale=.05)
p1Label.setZ(.3)
p1Label.setX(-.75)
p2Label=DirectLabel(text = "Player 2's Name:", scale=.05)
p2Label.setZ(.15)
p2Label.setX(-.75)
roundsLabel=DirectLabel(text = "Number of Rounds:", scale=.05)
roundsLabel.setX(-.75)
#run the tutorial
run()

