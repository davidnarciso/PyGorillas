import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from random import random
from direct.showbase.DirectObject import DirectObject
from direct.interval.MetaInterval import Sequence
import random,math,sys,os
from direct.task import Task
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
from types import *
from Explosion import Explode

class Projectile(DirectObject):
    def __init__(self, player, startPos, myNode,AL):
##        self.accept("space", self.incrementSideWindowNumber)
        self.worldNode = myNode
        self.AL = AL
        self.bombSound = self.AL.getAudio(3)
        self.happySound = self.AL.getAudio(0)
        self.startPos = startPos
        self.player = player
        self.exploded = 0
        self.fired = 0
        self.newPos =Vec3(0,0,0)
        self.mainWindow=base.win
        self.altBuffer=self.mainWindow.makeTextureBuffer("hello", 256, 256)
          
    def fire(self, gravity, angle, velocity, wind, timeflow, explosionSize,
             explosionBursts,sideWindowNum):
        self.number = sideWindowNum
        self.removeAll()
        self.fired = 1
        self.gravity = gravity
        self.angle = angle
        self.velocity = velocity*5
        self.wind = wind
        ##### Crockets speed #####
        self.timeflow = timeflow*8
        ##### Crockets size #####
        self.explosionSize = explosionSize
        self.explosionBursts = explosionBursts
        if self.player==2:
            self.angle = 180 - self.angle
        self.proj = loader.loadModel('models/banana')
        self.projTex = loader.loadTexture('models/building_yellow.bmp')
        self.proj.setTexture(self.projTex)
        self.proj.setPos(self.startPos)
        self.projNode = render.attachNewNode('proj')
        self.projNode.reparentTo(self.worldNode)
        self.proj.setScale(10)
        self.proj.reparentTo(self.projNode)
        taskMgr.add(self.update, "updater")
        self.sideWindow()
        self.explosionStarted = 1
        
        
##    def createSideWindow(self):
##        mainWindow=base.win
##        altBuffer=mainWindow.makeTextureBuffer("texBuffer", 256, 256)
##        altRender=NodePath("new render")
##        self.altCam=base.makeCamera(altBuffer)
##        self.altCam.reparentTo(altRender)
##        self.altCam.setPos(0,-401,105)
##        altRender.reparentTo(render)
##        self.altCam.lookAt(self.proj)
##        base.bufferViewer.setPosition("llcorner")
##        base.bufferViewer.setCardSize(.75, .75)
##        base.bufferViewer.enable(1)
##        base.bufferViewer.setLayout('cycle')
##        base.bufferViewer.selectCard(self.number)
        
    def sideWindow(self):
        altCam=base.makeCamera(self.altBuffer)
        self.camRoot = self.proj.attachNewNode('cam')
        self.camRoot.setPos(Vec3(-15,-5,10))
        self.camRoot.lookAt(self.proj)
        altCam.reparentTo(self.camRoot)
        base.bufferViewer.setPosition("llcorner")
        base.bufferViewer.setCardSize(.75,.75)
        base.bufferViewer.setLayout('cycle')
        base.bufferViewer.selectCard(self.number)
##        mainWindow=base.win
##        altBuffer=mainWindow.makeTextureBuffer("texBuffer", 256, 256)
##        altRender=NodePath("new render")
##        self.altCam=base.makeCamera(altBuffer)
##        self.altCam.reparentTo(altRender)
##        self.altCam.setPos(0,-401,105)
##        altRender.reparentTo(render)
##        self.altCam.lookAt(self.proj)
##        base.bufferViewer.setPosition("llcorner")
##        base.bufferViewer.setCardSize(.75, .75)
##        base.bufferViewer.enable(1)
##        base.bufferViewer.setLayout('cycle')
##        base.bufferViewer.selectCard(self.number)
        
    def update(self, task):
        self.newPos = self.projectPoint(self.angle,self.velocity,
                                   self.gravity,task.time*
                                   self.timeflow,self.startPos,
                                   self.wind)
        if self.proj.getX()>175 or self.proj.getX()<-175 or self.proj.getZ()<0:
            self.hit("building")
            self.proj.setR(0)
##        self.proj.setR(task.time*360*3)
        self.proj.setPos(self.newPos)
        return Task.cont
                       
    def projectPoint(self,angle, velocity, gravity, time, location, wind):
        return Vec3(math.sin(math.radians(90.0 - angle)) *
                    velocity * time + wind[0] * time + location.getX(),
                    location.getY(),math.cos(math.radians(90.0 - angle)) *
                    velocity * time - gravity * time * time + wind[1] *
                    time + location.getZ())
    
    def hit(self, target):
        if self.explosionStarted:
            self.explosionStarted = 0
            self.fired = 0
            taskMgr.remove("updater")
            self.explode =  Explode(self.explosionSize, self.explosionBursts, .75,self.proj.getPos(), target)
            taskMgr.add( self.updateExplode, "BOOM")            
            self.bombSound.play()

    def updateExplode(self, task):
        if task.time > self.explode.exlength * 2:
            self.explode.sparkoff()
            if self.explode.target=="gorilla":
                self.explode.mushroom.start(self.explode.mushroomNode)
                self.explode.pe4.softStop()
            self.explode.pe3.start(self.explode.boomnode)
        if task.time > self.explode.exlength * 7.5 and self.explode.target=="building":
            self.explode.pe3.softStop()
            taskMgr.remove("BOOM")
            self.exploded = 1
            self.explode.remove()
            return Task.done
        if task.time > 5 and self.explode.target=="gorilla":
            self.explode.pe3.softStop()
            taskMgr.remove("BOOM")
            self.exploded = 1
            self.explode.mushroom.softStop()
            self.explode.remove()
            return Task.done
        return Task.cont

    def removeAll(self):
        base.bufferViewer.toggleEnable()
        print'beingremoved'
        if taskMgr.hasTaskNamed("updater"):
            taskMgr.remove("updater")
        if taskMgr.hasTaskNamed("BOOM"):
            taskMgr.remove("BOOM")
        try:
            self.projNode.detachNode()
        except:
            1+1
        self.exploded = 0
        self.ignoreAll()
        try:
            self.explode.remove()
        except:
            1+1
