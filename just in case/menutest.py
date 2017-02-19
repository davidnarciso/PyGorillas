import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from Main import Main


from pandac.PandaModules import TextNode
from direct.gui.OnscreenImage import OnscreenImage
##from Main import Main


imageObject = OnscreenImage(image = 'Images/gorilla-bananas.jpg', pos = (.75, 0, 0.2))
imageObject.setScale(.5)
#add some text
bk_text = "This is my Demo"
textObject = OnscreenText(text = bk_text, pos = (0.95,-0.95), 
scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)
anthem = loader.loadSfx("Sounds/Stats.wav")
anthem.setLoop(True)
anthem.play()
base.setBackgroundColor( 200, 200, 0)
p1Name = 'Player 1'
p2Name = 'Player 2'
rounds = '3'

#
#CHANGE THE SOUND ADRESS, THEY ARE NOW ON THE 'SOUNDS' FOLDER RIGHT OFF OF 'GORILLA THE GAME'!!!!!
#



#callback function to set  text
def p1saveText(textEntered):
        p1Name = textEntered

def p2saveText(textEntered):
        p2Name = textEntered

def roundssaveText(textEntered):
        rounds = textEntered

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
def getp1name():
        return p1Name
def getp2name():
        return p2Name
def getRounds():
        return rounds
def setPlayGame():
        #newGame = Main(1)
        #sys.exit()
        print "HI"
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
playGameButton = DirectButton(text = ("Play Game", "Play Game", "Play Game", "Play Game"),scale=.05,command=setPlayGame)
playGameButton.setX(.5)
playGameButton.setZ(.5)

p1Text = DirectEntry(text = "" ,scale=.05,command=p1saveText,
initialText="Player 1", numLines = 1,focus=0,focusInCommand=p1clearText)
p1Text.setZ(.3)
p1Text.setX(-.5)
p2Text = DirectEntry(text = "" ,scale=.05,command=p2saveText,
initialText="Player 2", numLines = 1,focus=0,focusInCommand=p2clearText)
p2Text.setZ(.15)
p2Text.setX(-.5)
roundsText = DirectEntry(text = "" ,scale=.05,command=roundssaveText,
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

