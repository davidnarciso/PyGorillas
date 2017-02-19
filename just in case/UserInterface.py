# LORD OF !AWESOME(aka ryan)-07

import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
import sys,random,math
from direct.showbase import DirectObject
from direct.task import Task
from direct.gui.OnscreenImage import OnscreenImage
from Projectile import Projectile
from direct.directtools.DirectSelection import DirectBoundingBox

maxPower = 100 # Just guessing, but this is prolly the max power...
maxangle = 90 # max angle? maybe?
PowerBarPos = Vec3(.1,.1,-.9) # where the powerbar and the power textbox will appear
anglePos = Vec3(-1.2,.1,-.9) # where the angle textbox and angle control will appear
Asize = 0.1# size of the finger image
OriginalPsize = 1.0

AmountByWhichToChange = 1# this represents the amount to iterate the power and
#angle by, so each time an arrow key is pressed one is taken or added to the power
moveangleText = Vec3(-.2,0,.02) #so you can move the angle text if you so wish
movePowerText = Vec3(-.2,.02,.02) #so you can move the power text if you so wish
changeRate = .05 # how fast the controls iterate when held down


class UserInterface(DirectObject.DirectObject):
  def __init__(self,whichPlayer,Gorillas,buildingList,theScores,mySun,myNode,AL,p1Name,p2Name):
    self.worldNode = myNode
    self.AL = AL
    self.dkS1 = self.AL.getAudio(15)
    self.dkS2 = self.AL.getAudio(16)
    self.number = -1
    self.sun = mySun
    self.playerOneName = p1Name
    self.playerTwoName = p2Name
    self.sunNode = render.attachNewNode("sunNode")
    self.sunNode.reparentTo(self.worldNode)
    self.sunNode.setPos(Vec3(0,115,175))
    self.sun.reparentTo(self.sunNode)
    self.sun.setHpr(Vec3(90,180,0))
    self.sun.setScale(.2)
    self.done = 0
    self.Player = whichPlayer # what players turn it is
    self.shot = 0
    self.isNotThrown = 1
    self.hasExpYet=1
    self.myBuildingList = buildingList
    self.Power = maxPower/2 # this is the number value of the angle
    self.angle = maxangle # this is the number value of the power
    self.Psize = OriginalPsize/2 # size of the power bar image
    self.scaleFactor = ((OriginalPsize/maxPower)*AmountByWhichToChange) #scale factor for power
    self.Degree = 0 #adjust hpr, more of a placeholder and reps the angle
    self.PWidthHeight = (OriginalPsize/10) #width and hieght of the power bar
    self.gorilla = Gorillas
    self.GorPos1 = self.gorilla[0].getPos()
    self.GorPos2 = self.gorilla[1].getPos()
    self.scores = theScores

    self.arrow = loader.loadModel("models/squarrow-model")
    self.arrow.setHpr(90,0,0)
    self.arrow.setPos(Vec3(self.GorPos1.getX(),self.GorPos1.getY(),self.GorPos1.getZ()+30))
    
    self.arrowScaleInterval1 = self.arrow.scaleInterval(.5,Vec3(4,2,2),startScale = Vec3(2,1,1) )  
    self.arrowScaleInterval2 = self.arrow.scaleInterval(.5,Vec3(2,1,1),startScale = Vec3(4,2,2) ) 
    self.arrowHprInterval1 = self.arrow.hprInterval(.5,Vec3(180,0,0),startHpr = Vec3(0,0,0))
    self.arrowHprInterval2 = self.arrow.hprInterval(.5,Vec3(0,0,0),startHpr = Vec3(180,0,0))
    self.arrowScaleInterval = Sequence(self.arrowScaleInterval1, self.arrowScaleInterval2)
    self.arrowHprInterval  = Sequence(self.arrowHprInterval1, self.arrowHprInterval2)
    self.arrowInterval = Parallel(self.arrowScaleInterval,self.arrowHprInterval)
    
    self.arrowInterval.loop()
    self.arrow.reparentTo(render)

    self.gorilla1Fire = Sequence(self.gorilla[0].hprInterval(.5,Vec3(-90,-45,0), startHpr = Vec3(-90,0,0)),
                                 self.gorilla[0].hprInterval(1,Vec3(-90,45,0), startHpr = Vec3(-90,-45,0)),
                                 self.gorilla[0].hprInterval(.5,Vec3(-90,0,0), startHpr = Vec3(-90,45,0)))
    self.gorilla2Fire = Sequence(self.gorilla[1].hprInterval(.5,Vec3(90,-45,0), startHpr = Vec3(90,0,0)),
                                 self.gorilla[1].hprInterval(1,Vec3(90,45,0), startHpr = Vec3(90,-45,0)),
                                 self.gorilla[1].hprInterval(.5,Vec3(90,0,0), startHpr = Vec3(90,45,0)))

    self.frame = OnscreenImage(image = 'images/frame.png', pos = Vec3(0,0,0))
    ##self.frame = OnscreenImage(image = 'images/frame.png', pos = Vec3(-.45,-.3,0))
    self.frame.setScale(1.35,1,.25)
    self.frame.setPos(-.3,0,-.75)
    ##self.frame.setPos(-.3,-10,0)
    self.frame.setTransparency(TransparencyAttrib.MAlpha)
    
    self.powerBar = OnscreenImage(image = 'images/powerbar.jpg', pos = PowerBarPos)
    self.powerBar.setScale(self.Psize,self.PWidthHeight,self.PWidthHeight)

    self.pointer = OnscreenImage(image = 'images/fingerpoint.png', pos = anglePos)
    self.pointer.setScale(Asize, Asize, Asize)
    self.pointer.setTransparency(TransparencyAttrib.MAlpha)
    
    if self.Player == 1:
      self.pointer.setHpr(180,0,self.Degree)
    else:
      self.pointer.setHpr(0,0,self.Degree)
      
    self.accept("escape", sys.exit)
    self.accept("arrow_left", self.pDecrementer, [1])
    self.accept("arrow_left-up", self.pDecrementer, [0])
    self.accept("arrow_right", self.pIncrementer, [1])
    self.accept("arrow_right-up", self.pIncrementer, [0])
    self.accept("arrow_up", self.aIncrementer, [1])
    self.accept("arrow_up-up", self.aIncrementer, [0])
    self.accept("arrow_down", self.aDecrementer, [1])
    self.accept("arrow_down-up", self.aDecrementer, [0])
    self.accept("space", self.FireAway)


    self.text = TextNode('POW-AH')
    self.textNodePath = aspect2d.attachNewNode(self.text)
    self.textNodePath.setScale(0.07)
    self.textNodePath.setPos((PowerBarPos.getX()+self.PWidthHeight)+movePowerText.getX(),
                             (PowerBarPos.getY()+self.PWidthHeight)+movePowerText.getY(),
                             (PowerBarPos.getZ()+self.PWidthHeight)+movePowerText.getZ())
    self.textNodePath.setColor(0,0,0,1)
    
    self.text.setText("Power: "+str(self.Power))
    
    self.text2 = TextNode('AN-GEL')
    self.textNodePath = aspect2d.attachNewNode(self.text2)
    self.textNodePath.setScale(0.07)
    self.textNodePath.setPos((anglePos.getX()+Asize)+moveangleText.getX(),
                             (anglePos.getY()+Asize)+moveangleText.getY(),
                             (anglePos.getZ()+Asize)+moveangleText.getZ())
    self.text2.setText("Angle: "+str(self.angle))
    self.textNodePath.setColor(0,0,0,1)

    #DAVIE, HERE IS THE DEAL, THE FRAME IS OVERLAPING THE BANANA CAMERA
    #THIS IS YOUR CALL WHETHER OR NOT TO USE THE FRAME, IF YOU JUST DONT
    #WANT IT TO SHOW JUST GO WHERE I SET IT UP (UP IN THIS PROJECT) AND KILL IT
    #I REALLY DONT MIND SO IF IT WOULD BE MORE WORK TO FIX BANANACAM, GO AHEAD
    #AND GET RID OF THE FRAME
    #THANK YOU FOR YOUR TIME AND GODSPEED LITTLE ONE.
    #-Kenny
    self.playerOne = Projectile(1, Vec3(self.GorPos1.getX(),self.GorPos1.getY(),self.GorPos1.getZ()+10),self.worldNode,self.AL)
    self.playerTwo = Projectile(2, Vec3(self.GorPos2.getX(),self.GorPos2.getY(),self.GorPos2.getZ()+10),self.worldNode,self.AL)
    print'here'
    taskMgr.add(self.doTurn,"ChangeTurns")
    taskMgr.add(self.checkCollision,"collisionCheck")
    
  def reset(self,Gorillas,buildingList,theScores,mySun,myNode):
    self.worldNode= myNode
    self.sun = mySun
    self.sunNode = render.attachNewNode("sunNode")
    self.sunNode.reparentTo(self.worldNode)
    self.sunNode.setPos(Vec3(0,115,175))
    self.sun.reparentTo(self.sunNode)
    self.sun.setHpr(Vec3(90,180,0))
    self.sun.setScale(.2)
    self.done = 0
    self.shot = 0
    self.myBuildingList = buildingList
    self.Power = maxPower/2 # this is the number value of the angle
    self.angle = maxangle # this is the number value of the power
    self.Psize = OriginalPsize/2 # size of the power bar image
    self.scaleFactor = ((OriginalPsize/maxPower)*AmountByWhichToChange) #scale factor for power
    self.Degree = 0 #adjust hpr, more of a placeholder and reps the angle
    self.PWidthHeight = (OriginalPsize/10) #width and hieght of the power bar
    self.gorilla = Gorillas
    self.GorPos1 = self.gorilla[0].getPos()
    self.GorPos2 = self.gorilla[1].getPos()
    self.scores = theScores
    self.playerOne = Projectile(1, Vec3(self.GorPos1.getX(),self.GorPos1.getY(),self.GorPos1.getZ()+10),self.worldNode,self.AL)
    self.playerTwo = Projectile(2, Vec3(self.GorPos2.getX(),self.GorPos2.getY(),self.GorPos2.getZ()+10),self.worldNode,self.AL)
    
#Pembertr0n did some health stuff here for the blocks, but they're now invincible
#So... someone should prolly figure out why, I don't have time right now
  def checkCollision(self, task):
    check=1
    if self.playerOne.fired:
      self.sunNode.lookAt(self.playerOne.proj)
      numberOfBuildings = 15
      projPos = self.playerOne.proj.getPos()
      projX = projPos.getX()
      if projX>0:
        self.sun.setColor(.8,.2,.2,.5)
      projZ = projPos.getZ()
      projBounds = self.playerOne.proj.getTightBounds()
      projBounds = projBounds[0]-projBounds[1]
      projRadius = projBounds.getZ()
      for i in range(numberOfBuildings):
        blockList = self.myBuildingList[i].blockList
        buildingBounds = blockList[0].myBlock.getTightBounds()
        buildingBounds = buildingBounds[0]-buildingBounds[1]
        width = buildingBounds.getX()
        buildingPos = blockList[0].myBlock.getPos()
        buildingX = buildingPos.getX()
        if projX+projRadius<buildingX-(width/2) and projX-projRadius>buildingX+(width/2):
          numberOfBlocks = self.myBuildingList[i].blockCount
          buildingHeight = buildingBounds.getZ()
          for x in range(numberOfBlocks):
            blockPos = blockList[x].myBlock.getPos()
            blockZ = blockPos.getZ()
            if projZ-projRadius > (blockZ+buildingHeight) and projZ+projRadius<blockZ and check:
              if blockList[x].health>0:
                self.playerOne.hit("building")
                blockList[x].health = blockList[x].health-1
                if blockList[x].health<=0:
                   blockList[x].myBlock.setScale(Vec3(.5,.5,1))##blockList[x].myBlock.getScale()/5,1,.5))
                   self.myBuildingList[i].changeTexture(x)
                   break
                elif blockList[x].health==1:
                   self.myBuildingList[i].changeTexture(x)
                   break
                break
              check = 0
              break
            if not check:
              break
      gBounds = self.gorilla[0].getTightBounds()
      gBounds = gBounds[0]-gBounds[1]
      if check:
        for i in range(2):
            gX = self.gorilla[i].getX()
            gWidth = gBounds.getX()
            if projX+projRadius<gX-(gWidth/2)and projX-projRadius>gX+(gWidth/2):
                gZ = self.gorilla[i].getZ()
                gHeight = gBounds.getZ()
                if projZ-projRadius>(gZ+gHeight)and projZ+projRadius<gZ:
                    self.playerOne.hit("gorilla")
                    if i==0:
                        self.scores[1]=self.scores[1]+1
                        print "Player 2: "+str(self.scores[1])
                        self.done = 1
                    else:
                        self.scores[0]=self.scores[0]+1
                        print "Player 1: "+str(self.scores[0])
                        self.done = 1
                    if self.scores[0]<self.scores[2] or self.scores[1]<self.scores[2]:
                        self.resetControls()
        
        
    elif self.playerTwo.fired:
      self.sunNode.lookAt(self.playerTwo.proj)
      numberOfBuildings = 15##self.myBuildingList.numOfBuildings
      for i in range(numberOfBuildings):
        blockList = self.myBuildingList[i].blockList
        projPos = self.playerTwo.proj.getPos()
        projX = projPos.getX()
        if projX<0:
          self.sun.setColor(.8,.2,.2,.5)
        buildingBounds = blockList[0].myBlock.getTightBounds()
        buildingBounds = buildingBounds[0]-buildingBounds[1]
        width = buildingBounds.getX()
        buildingPos = blockList[0].myBlock.getPos()
        projBounds = self.playerTwo.proj.getTightBounds()
        projBounds = projBounds[0]-projBounds[1]
        projRadius = projBounds.getZ()
        buildingX = buildingPos.getX()
        if projX+projRadius<buildingX-(width/2) and projX-projRadius>buildingX+(width/2):
          numberOfBlocks = self.myBuildingList[i].blockCount
          projZ = projPos.getZ()
          buildingHeight = buildingBounds.getZ()
          for x in range(numberOfBlocks):
            blockPos = blockList[x].myBlock.getPos()
            blockZ = blockPos.getZ()
            if projZ-projRadius > (blockZ+buildingHeight) and projZ+projRadius<blockZ and check:
              if blockList[x].health>0:
                self.playerTwo.hit("building")
                blockList[x].health = blockList[x].health-1
                if blockList[x].health<=1:
                   self.myBuildingList[i].changeTexture(x)
                   break
                break
              break
            if not check:
              break
      gBounds = self.gorilla[0].getTightBounds()
      gBounds = gBounds[0]-gBounds[1]
      if check:
        for i in range(2):
            gX = self.gorilla[i].getX()
            gWidth = gBounds.getX()
            if projX+projRadius<gX-(gWidth/2)and projX-projRadius>gX+(gWidth/2):
                gZ = self.gorilla[i].getZ()
                gHeight = gBounds.getZ()
                if projZ-projRadius>(gZ+gHeight)and projZ+projRadius<gZ:
                    self.playerTwo.hit("gorilla")
                    if i==0:
                        self.scores[1]=self.scores[1]+1
                        print "Player 2: "+str(self.scores[1])
                        self.done = 1
                    else:
                        self.scores[0]=self.scores[0]+1
                        print "Player 1: "+str(self.scores[0])
                        self.done = 1
                    if self.scores[0]<self.scores[2] or self.scores[1]<self.scores[2]:
                        self.resetControls()
    return task.cont

  def resetControls(self):
    self.sun.setColor(1,1,1,1)
    self.sunNode.setHpr(0,0,0)
    self.Psize = OriginalPsize/2
    self.Power = maxPower/2 # this is the number value of the angle
    self.angle = maxangle # this is the number value of the power
    self.Degree = 0 #adjust hpr, more of a placeholder and reps the angle
    self.text.setText("Power: "+str(self.Power))
    self.powerBar.setScale(self.Psize,self.PWidthHeight,self.PWidthHeight)
    self.text2.setText("Angle: "+str(self.angle))
    if self.Player == 1:
      self.pointer.setHpr(180,0,self.Degree)
      self.arrow.setPos(Vec3(self.GorPos1.getX(),self.GorPos1.getY(),self.GorPos1.getZ()+30))
    else:
      self.pointer.setHpr(0,0,self.Degree)
      self.arrow.setPos(Vec3(self.GorPos2.getX(),self.GorPos2.getY(),self.GorPos2.getZ()+30))
         
  def removeAll(self):
    taskMgr.remove("changeTurns")
    taskMgr.remove("collisionCheck")
    self.playerOne.removeAll()
    self.playerTwo.removeAll()
    self.text.setText("")
    self.powerBar.destroy()
    self.text2.setText("")
    self.pointer.destroy()
    base.bufferViewer.toggleEnable()
    
  def FireAway(self):
    if self.playerOne.fired == 0 and self.playerTwo.fired == 0:
      self.isNotThrown = 0
      self.incrementSideWindowNumber()
      if self.hasExpYet:
        if self.Player == 1:
          ##MAYBE NOT WORK SOUND, CHECK THIS OUT IF PROBLEM!!
          self.dkS1.play()
          self.gorilla1Fire.start()
          self.playerOne.fire(.1,self.angle, self.Power/50., [0,0], 1, 2, 5,self.number)
        else:
          self.dkS2.play()
          self.gorilla2Fire.start()
          self.playerTwo.fire(.1,self.angle, self.Power/50., [0,0], 1, 2, 5,self.number)
        self.hasExpYet = 0

  def incrementSideWindowNumber(self):
    self.number = self.number + 1
        
          
  def genLabelText(self, text, i):
    return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                        align = TextNode.ALeft, scale = .05)

  def Decrement(self, whatToDecrement):
##    global Psize# this has to be here so I can access global variables such as Psize
    if self.isNotThrown:
      if (whatToDecrement == 'power' and (self.Power - AmountByWhichToChange) >= 0):
        self.Psize = self.Psize - self.scaleFactor
        self.powerBar.setScale(self.Psize,self.PWidthHeight,self.PWidthHeight)
        self.Power = self.Power - AmountByWhichToChange 
        self.text.setText("Power: " + str(self.Power))
        
      elif (whatToDecrement == 'angle' and (self.angle - AmountByWhichToChange) >= 0):
        self.Degree = self.Degree - AmountByWhichToChange  
        if(self.Player == 1):
          self.pointer.setHpr(180,0,self.Degree)
        else:
          self.pointer.setHpr(0,0,self.Degree)

        self.angle = self.angle - AmountByWhichToChange
        self.text2.setText("Angle: " + str(self.angle))
    
  def Increment(self, whatToIncrement):
    if self.isNotThrown:
      if (whatToIncrement == 'power' and (self.Power + AmountByWhichToChange) <=
          maxPower):
        self.Psize = self.Psize + self.scaleFactor
        self.powerBar.setScale(self.Psize,self.PWidthHeight,self.PWidthHeight)
        self. Power = self.Power + AmountByWhichToChange 
        self.text.setText("Power: " + str(self.Power))
      elif (whatToIncrement == 'angle' and (self.angle + AmountByWhichToChange) <=
            maxangle):
        self.Degree  = self.Degree + AmountByWhichToChange 
        if(self.Player == 1):
          self.pointer.setHpr(180,0,self.Degree)
          # so it faces right way for p1
        else:
          self.pointer.setHpr(0,0,self.Degree)
          
        self.angle = self.angle + AmountByWhichToChange
        self.text2.setText("Angle: " + str(self.angle))
      
  def aIncrementer(self, toTask):
    if toTask == 0:
      taskMgr.remove("aincrement")
    else:
      taskMgr.add(self.aInc,"aincrement")
      self.timer = 0
      self.Increment("angle")
  def aInc(self, task):
    if task.time - self.timer >= changeRate:
      self.Increment("angle")
      self.timer = task.time
    return task.cont
  

  def aDecrementer(self, toTask):
    if toTask == 0:
      taskMgr.remove("adecrement")
    else:
      taskMgr.add(self.aDec,"adecrement")
      self.timer = 0
      self.Decrement("angle")
  def aDec(self, task):
    if task.time - self.timer >= changeRate:
      self.Decrement("angle")
      self.timer = task.time
    return task.cont

  def pIncrementer(self, toTask):
    if toTask == 0:
      taskMgr.remove("pincrement")
    else:
      taskMgr.add(self.pInc,"pincrement")
      self.timer = 0
      self.Increment("power")
  def pInc(self, task):
    if task.time - self.timer >= changeRate:
      self.Increment("power")
      self.timer = task.time
    return task.cont
  
  def pDecrementer(self, toTask):
    if toTask == 0:
      taskMgr.remove("pdecrement")
    else:
      taskMgr.add(self.pDec,"pdecrement")
      self.timer = 0
      self.Decrement("power")
  def pDec(self, task):
    if task.time - self.timer >= changeRate:
      self.Decrement("power")
      self.timer = task.time
    return task.cont

  def doTurn(self,task):
    if self.playerOne.exploded == 1 or self.playerTwo.exploded == 1:
      self.hasExpYet = 1
      self.isNotThrown = 1
      if self.Player == 1:
        self.Player = 2
        self.playerOne.removeAll()
        self.resetControls()
      else:
        self.Player = 1
        self.playerTwo.removeAll()
        self.resetControls()
    return task.cont

  def gorillaHit(self):
    if self.playerOne.exploded == 1 or self.playerTwo.exploded == 1:
      self.hasExpYet = 1
      self.isNotThrown = 1
      if self.Player == 1:
        self.Player = 2
        self.playerOne.removeAll()
        self.resetControls()
      else:
        self.Player = 1
        self.playerTwo.removeAll()
        self.resetControls()

  def player1Label(self):
    self.playerOneLabel = TextNode('Im-a-playa')
    self.playerOneLabelNodePath = aspect2d.attachNewNode(self.playerOneLabel)
##    self.play1labelInterval = self.playerOneLabelNodePath.hprInterval()

##    self.text = TextNode('POW-AH')
##    self.textNodePath = aspect2d.attachNewNode(self.text)
##    self.textNodePath.setScale(0.07)
##    self.textNodePath.setPos(
  def player2Label(self):
    self.playerTwoLabel = TextNode('Im-two-playas-in-one')
    self.playerTwoLabelNodePath = aspect2d.attachNewNode(self.playerTwoLabel)
        
