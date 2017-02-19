import direct.directbase.DirectStart
from pandac.PandaModules import *
import sys
from direct.actor import Actor
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib
from direct.interval.MetaInterval import Sequence

class finalie(DirectObject):
    ########################################################
    ###      Created by the Awsome Michael Garrison      ###
    #######################   pwnd   #######################
    ###########################  ###########################
    ########################################################

    def __init__(self, AL,namesList):
        self.names = namesList
        base.camera.setHpr(0,0,0)
        base.camera.setPos(0,0,0)
        self.AudioL = AL
        self.cred()
        self.environ()
        self.dk()
        self.sounds()
        self.camMove()
##        self.accept("escape", sys.exit)
##        self.accept("M", self.Menu.Menu())

    def environ(self):
        self.envi = loader.loadModel("models/solar_sky_sphere")
        self.envitex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.envi.setTexture(self.envitex)
        self.envi.reparentTo(base.camera)
        self.envi.setScale(250)

    def cred(self):
        print "crediting"
        self.player1 = "KingKong"
        self.player2 = "DK"
        self.credit = TextNode('credits')
        self.credit.setText("Gorillas\n" +
                            "press esc to exit" +
                            "\n\n\nCreated by the East Computer Science 2 Team\n" +
                            "\n Mr. 'M.C.' McKain:\n teacher of the class\n " +
                            "\nMichael Garrison:\nCredits, buildings, concept artist\n" +
                            "\nRyan 'Corner' Bland:\n User Interface, and ultimate wizard of the cosmos\n" +
                            "\nMatt Pemberton:\n Building\n" +
                            "\nKenny Kozan:\n Building, modeling\n" +
                            "\nDavid Welling:\n Layout, class design\n" +
                            "\nKevin 'Cranny' Cranstoun:\n Sleeping Expert, Main menu\n" +
                            "fashion expert\n" +
                            "\nDavid 'Davy' Narciso:\n Environment , UI\n" +
                            "\nMichael Diekema:\n Camera, Background Environment\n" +
                            "\nJohn Kohlas:\n Projectile\n" +
                            "\n\nHelpers\n" +
                            "\nJohn Terbot:\n I Hate CS2! AP_CS FTW!\n" +
                            "\nMatt 'Nacho' Norris:\n Yo Momma Jokes\n" +
                            "\nMitch 'The Hulk' Culbert:\n Motivational speaker\n" +
                            "\n\noriginal Gorilla:\n Creator Unkown,\n Artist Unknown\n" +
                            "\n\nThanks:\n\n Llamas:\n Monty Python and the holy grail\n" +
                            "\nLittle Tom's big stomach\n" +
                            "\nSANTANA for making awsome songs\n" +
                            "\nYanni for helping us concentrate\n" +
                            "\nKenny's parents for being awsome and helping and making our gorilla model\n" +
                            "\nAos pais do Kenny por ser tao bacanas e ajudarlo em fazer o modelo do gorilla\n" +
                            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" +
                            "\nWe would also like to thank you, "+ self.names[0]+" and "+self.names[1]+
                            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.textNodePath = aspect2d.attachNewNode(self.credit)
        indistar = loader.loadFont('images/Starjhol.ttf')
        self.credit.setFont(indistar)
        self.credit.setTextColor(1,1,0,1)
        self.credit.setWordwrap(20.0)
        self.credit.setAlign(self.credit.ACenter)
        self.textNodePath.setPos(0,0,0)
        self.textNodePath.setScale(0.07)
        #self.credit.setSmallCaps(1)

        self.textNodePath.reparentTo(render)

    def dk(self):
        self.dk = OnscreenImage(image = 'images/donkey_kong_4.png', pos = (1.15,1.15,-.8))
        self.dk.setScale(.2)
        self.dk.setTransparency(TransparencyAttrib.MAlpha)

    def sounds(self):
        ## self.starWarsTheme = loader.loadSfx("Sounds/Star Wars - Theme Song.mp3")
        ## self.ImperialMarch = loader.loadSfx("Sounds/Star Wars - Imperial March.mp3")
        self.starWarsTheme = self.AudioL.getAudio(13)
        self.ImperialMarch = self.AudioL.getAudio(14)        
        self.starWarsTheme.play()
        taskMgr.doMethodLater(71, self.stopStarWars, 'playstarWarsTheme')
        taskMgr.doMethodLater(69, self.startImperial, 'playstarWarsTheme')


    def startStarWars(self, task):
        self.starWarsTheme.play()
    
    def stopStarWars(self, task):
        self.starWarsTheme.stop()

    def startImperial(self, task):
        self.ImperialMarch.play()
        
    def camMove(self):
        self.camNode = render.attachNewNode('cameraNode')
        self.camNode.setPos(Vec3(0,-2,-1.5))
        self.camNode.setHpr(Vec3(0,55,0))

        self.camPosInterval1 = self.camNode.posInterval(.1,Vec3(0,-2,-1.5)) 
        self.camPosInterval2 = self.camNode.posInterval(98,Vec3(0,-2,-20))

        self.camMove = Sequence(self.camPosInterval1,
                                self.camPosInterval2
                                )
        self.camMove.start()
        base.camera.reparentTo(self.camNode)
        print str(base.camera.getPos())+str(self.camNode.getPos())
        
##
##al = AudioLibrary()
##F = finalie(al)
##run()
