from direct.showbase.DirectObject import DirectObject
from BuildingEnvironment import BuildingEnvironment
from direct.interval.IntervalGlobal import *
import direct.directbase.DirectStart
from pandac.PandaModules import *
from UserInterface import UserInterface
import sys,random
from Menu import Menu

class World(DirectObject):
  def __init__(self, AudioL):
    self.worldNotDone=1
    self.number = -1
    base.disableMouse()
    self.AL = AudioL
    self.worldNode = render.attachNewNode("world")
    base.camLens.setFar(1700)
    self.superMan = self.AL.getAudio(9)
    self.wildNFree = self.AL.getAudio(12)
    self.funky = self.AL.getAudio(11)
    self.bohemian = self.AL.getAudio(6)
    self.time = 0
    self.accept("space",self.incrementSideWindowNumber)
    self.accept("p",self.togglePositiveBGBuildings)
    self.accept("n",self.toggleNegitiveBGBuildings)
    self.accept("0",self.stopSounds)
    self.accept("1",self.bohemianRhapsody)
    self.accept("2",self.funkyItUp)
    self.accept("3",self.supMan)
    self.accept("4",self.wildItUP)
    self.supMan()
    

  def menuBackGround(self):
    myBuildingEnvironment = BuildingEnvironment(self.worldNode)
    self.buildingToggle = 1
    self.positiveBackgroundBuildingBool = 1
    self.negitiveBackgroundBuildingBool = 1
    self.backgroundBuildingNum = 14
    self.loadmodels(1)
    self.togglePositiveBGBuildings()
    self.toggleNegitiveBGBuildings()
    self.funWithBuildings(1)
    self.toggleBuildings()
    self.spin()

  def spin(self):
    self.cam = render.attachNewNode("cam")
    self.cam.reparentTo(self.worldNode)
    self.cam.setPos(0,0,150)
    self.camSpin1 = LerpFunc(self.spinCamera,
                                  duration = 10)
    self.camNode = render.attachNewNode("camNode")
    self.camNode.setPos(250,250,150)
    self.camNode.reparentTo(self.cam)
    self.camNode.lookAt(self.cam)
    base.camera.reparentTo(self.camNode)
    self.camSpin1.loop()

  def setCameraControl(self, task):
    if self.worldNotDone:
      if task.time < 3.0:
        base.camera.setPos(0, (97 * task.time) - 800, 105 + (task.time*80))
        base.camera.setHpr(0, (task.time * -7), 0)
        return task.cont

  ##    elif task.time < 5.0:
  ##      base.camera.setPos((self.gorillas[0].getX()/2) * (task.time - 3), self.gorillas[0].getY() - 50, self.gorillas[0].getZ())
  ##      return Task.cont
  ##  elif task.time <8.0:
  ##    base.camera.setHpr(-29 *(task.time - 5), (task.time - 5)*3, 0)
  ##    return Task.cont
  ##    pos = self.gorillas[0].getX()
  ##    return task.cont
      print "removed"
      taskMgr.remove("camControl")
      return task.done
    else:
      base.camera.setPos(0,0,0)
      taskMgr.remove("camControl")

  def incrementSideWindowNumber(self):
    self.number = self.number + 1
    
  def spinCamera(self,rad):
    self.cam.setH(rad*360)
    
  def createWorld(self,scores):
    taskMgr.add(self.setCameraControl,"camControl")
    base.camera.reparentTo(render)
    self.camNode.detachNode()
    self.cam.detachNode()
    self.camSpin1.finish()
    self.worldNode.detachNode()
    self.worldNode = render.attachNewNode("world")
    self.scores = scores
    taskMgr.add(self.checkScore,"checkScore")
    myBuildingEnvironment = BuildingEnvironment(self.worldNode)
    self.myBuildingList = myBuildingEnvironment.getBuildingList()
    self.gorillas = myBuildingEnvironment.getGorillas()
    self.backgroundBuildingNum = 14
    self.loadmodels(2)
    self.funWithBuildings(2)
    self.toggleBuildings()

  def supMan(self):
    self.wildNFree.stop()
    self.bohemian.stop()
    self.funky.stop()
    self.superMan.play()

  def bohemianRhapsody(self):
    self.wildNFree.stop()
    self.funky.stop()
    self.superMan.stop()
    self.bohemian.play()
    
  def funkyItUp(self):
    self.wildNFree.stop()
    self.superMan.stop()
    self.bohemian.stop()
    self.funky.play()
    
  def wildItUP(self):
    self.bohemian.stop()
    self.funky.stop()
    self.superMan.stop()
    self.wildNFree.play()
    
  def stopSounds(self):
    self.bohemian.stop()
    self.funky.stop()
    self.superMan.stop()
    self.wildNFree.stop()
    
  def createUI(self,p1Name, p2Name):
    self.UI = UserInterface(1,self.gorillas,self.myBuildingList,self.scores,self.sun, self.worldNode,self.AL,p1Name,p2Name)

  def resetUI(self):
    self.UI.reset(self.gorillas,self.myBuildingList,self.scores,self.sun,self.worldNode)

  def checkScore(self,task):
    if self.UI.done:
      if self.scores[2]>self.scores[1] or self.scores[2]>self.scores[0]:
        taskMgr.add(self.resetEverything,"resetEverything")
    return task.cont
  
  def resetEverything(self,task):
    if task.time>11:
      self.worldNode.detachNode()
      self.worldNode = render.attachNewNode("world")
      self.createWorld(self.scores)
      self.UI.done = 0
      self.resetUI()
      self.time = 0
      taskMgr.remove("resetEverything")
    return task.cont

  def removeAll(self):
    self.worldNode.detachNode()
    self.UI.removeAll()
    self.stopSounds()

  def loadmodels(self,menuOrNot):
    self.clouds = loader.loadModel('models/env')
    self.clouds.reparentTo(self.worldNode)
    self.clouds.setScale(Vec3(400,400,500))
    
    self.sun = loader.loadModel('models/sun')

    self.backgroundBuilding = [loader.loadModelCopy('models/glassbuilding')
                     for i in range(self.backgroundBuildingNum*8)]
    self.buildingNode = render.attachNewNode("buildings")
    self.buildingNode.reparentTo(self.worldNode)
    self.loadBuildings(menuOrNot)
    self.time = 0

    self.makeRoad(50)
    self.makeRoad(-25)

  def loadBuildings(self, menuOrNot):
    self.loadBackGroundBuildings(0,80,0)
    self.loadBackGroundBuildings(35,140,self.backgroundBuildingNum)
    self.loadBackGroundBuildings(-20,200,self.backgroundBuildingNum*2)
    self.loadBackGroundBuildings(15,260,self.backgroundBuildingNum*3)
    if menuOrNot==1:
      self.loadBackGroundBuildings(0,-150,self.backgroundBuildingNum*4)
      self.loadBackGroundBuildings(35,-200,self.backgroundBuildingNum*5)
      self.loadBackGroundBuildings(-20,-260,self.backgroundBuildingNum*6)
      self.loadBackGroundBuildings(15,-330,self.backgroundBuildingNum*7)

  def toggleBuildings(self):
    self.myParallel.loop()
      
  def funWithBuildings(self, menuOrNot):
    if menuOrNot==1:
      self.buildingFun = [self.backgroundBuilding[0].scaleInterval
                     for i in range(self.backgroundBuildingNum*8)]
      self.myParallel = Parallel(name = "buildingFun")
      for i in range(self.backgroundBuildingNum*8):
        movementSpeed = random.randint(2,6)/10.
        h = random.randint(20,40)/2./10.
        hpr1 = random.randint(-20,20)
        hpr2 = random.randint(-20,20)
        hprMove1 = self.backgroundBuilding[i].hprInterval(movementSpeed,Vec3(hpr1,-hpr1/2,hpr1/2),startHpr = Vec3(hpr2,hpr2/2,-hpr2/2))
        hprMove2 = self.backgroundBuilding[i].hprInterval(movementSpeed,Vec3(hpr2,hpr2/2,-hpr2/2),startHpr = Vec3(hpr1,-hpr1/2,hpr1/2))
        firstMovement = self.backgroundBuilding[i].scaleInterval(movementSpeed,Vec3(1.15,1.15,h),startScale = self.backgroundBuilding[i].getScale())
        secondMovement = self.backgroundBuilding[i].scaleInterval(movementSpeed,self.backgroundBuilding[i].getScale(),startScale = Vec3(1.15,1.15,h))
        sequence1 = Sequence(firstMovement, secondMovement)
        sequence2 = Sequence(hprMove1,hprMove2)
        self.myParallel.append(sequence1)
        self.myParallel.append(sequence2)
    elif menuOrNot == 2:
      self.buildingFun = [self.backgroundBuilding[0].scaleInterval
                     for i in range(self.backgroundBuildingNum*4)]
      self.myParallel = Parallel(name = "buildingFun")
      for i in range(self.backgroundBuildingNum*4):
        movementSpeed = random.randint(2,6)/10.
        h = random.randint(20,40)/2./10.
        hpr1 = random.randint(-20,20)
        hpr2 = random.randint(-20,20)
        hprMove1 = self.backgroundBuilding[i].hprInterval(movementSpeed,Vec3(hpr1,-hpr1/2,hpr1/2),startHpr = Vec3(hpr2,hpr2/2,-hpr2/2))
        hprMove2 = self.backgroundBuilding[i].hprInterval(movementSpeed,Vec3(hpr2,hpr2/2,-hpr2/2),startHpr = Vec3(hpr1,-hpr1/2,hpr1/2))
        firstMovement = self.backgroundBuilding[i].scaleInterval(movementSpeed,Vec3(1.15,1.15,h),startScale = self.backgroundBuilding[i].getScale())
        secondMovement = self.backgroundBuilding[i].scaleInterval(movementSpeed,self.backgroundBuilding[i].getScale(),startScale = Vec3(1.15,1.15,h))
        sequence1 = Sequence(firstMovement, secondMovement)
        sequence2 = Sequence(hprMove1,hprMove2)
        self.myParallel.append(sequence1)
        self.myParallel.append(sequence2)
            
    
  def makeRoad(self,y):
    numberOfPieces = 20
    road = [ loader.loadModelCopy('models/road')
             for i in range(numberOfPieces)]
    for i in range(numberOfPieces):
      x = -numberOfPieces*48.25/2+(i*48.25)
      z = 0
      road[i].reparentTo(self.worldNode)
      road[i].setH(90)
      road[i].setPos(Vec3(x,y,z))
      road[i].setScale(Vec3(1.5,10,.05))
    car = [loader.loadModelCopy("models/carnsx")
           for i in range(2)]
    for i in range(2):
      car[i].setColor(random.random(), random.random(), random.random())
      car[i].setPos(Vec3(-numberOfPieces*48.25*1/2,y+i*7-3,0))
      car[i].setH(90)
      car[i].setScale(2.5)
      car[i].reparentTo(self.worldNode)
      carPosInterval1= car[i].posInterval(random.randint(6,15),Point3(numberOfPieces*48.25*1/2, y+i*7-3, 0), startPos=Point3(-numberOfPieces*48.25*1/2, y+i*7-3, 0))
      carPosInterval2= car[i].posInterval(random.randint(6,15),Point3(-numberOfPieces*48.25*1/2, y+i*7-3, 0), startPos=Point3(numberOfPieces*48.25*1/2, y+i*7-3, 0))
      carHprInterval1= car[i].hprInterval(random.uniform(.20, .50) * 5,Point3(270,0,0), startHpr=Point3(90,0,0)) 
      carHprInterval2= car[i].hprInterval(random.uniform(.20, .50) * 5,Point3(90,0,0), startHpr=Point3(270,0,0))

      carMove = Sequence(carPosInterval1, carHprInterval1, carPosInterval2,
                           carHprInterval2, name = "carMove"+str(i)+str(y))
      carMove.loop()

  def togglePositiveBGBuildings(self):
    if(self.positiveBackgroundBuildingBool):
      for i in range(self.backgroundBuildingNum*4):
        self.backgroundBuilding[i].show()
      self.positiveBackgroundBuildingBool = 0
    else:
      for i in range(self.backgroundBuildingNum*4):
        self.backgroundBuilding[i].hide()
      self.positiveBackgroundBuildingBool = 1
                        
  def toggleNegitiveBGBuildings(self):
    if(self.negitiveBackgroundBuildingBool):
      for i in range(self.backgroundBuildingNum*4):
        self.backgroundBuilding[i+self.backgroundBuildingNum*4].show()
      self.negitiveBackgroundBuildingBool = 0
    else:
      for i in range(self.backgroundBuildingNum*4):
        self.backgroundBuilding[i+self.backgroundBuildingNum*4].hide()
      self.negitiveBackgroundBuildingBool = 1
      
  def loadBackGroundBuildings(self, offset, y, buildingNumber):
    for i in range(self.backgroundBuildingNum):
      self.backgroundBuilding[i+buildingNumber].reparentTo(self.buildingNode)
      x = -self.backgroundBuildingNum*50/2+(50*i)+offset
      z = 0
      h = random.randint(20,40)/2./10.
      self.backgroundBuilding[i+buildingNumber].setScale(Vec3(1.15,1.15,h))
      self.backgroundBuilding[i+buildingNumber].setPos(Vec3(x,y,z))

  def makeSunMad(self):
    self.sun.setColor(Vec4(.8,.2,.5,.5))
