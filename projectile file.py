import direct.directbase.DirectStart
from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.actor import Actor
from random import random
from direct.showbase.DirectObject import DirectObject
import sys
from direct.interval.MetaInterval import Sequence
import random
import math
from direct.task import Task
from pandac.PandaModules import BaseParticleEmitter,BaseParticleRenderer
from pandac.PandaModules import PointParticleFactory,SpriteParticleRenderer
from pandac.PandaModules import LinearNoiseForce,DiscEmitter
from pandac.PandaModules import LightAttrib,TextNode
from pandac.PandaModules import AmbientLight,DirectionalLight
from pandac.PandaModules import Point3,Vec3,Vec4
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
base.setBackgroundColor(.25,.25,.25)
class projectileFirer(DirectObject):
    def __init__(self, player,startPos, gravity, angle, velocity, wind, timeflow, explosionSize, explosionBursts):
        self.startPos = startPos
        self.gravity = gravity
        self.angle = math.radians(angle)
        self.player = player
        self.velocity = velocity
        self.wind = wind
        self.timeflow = timeflow
        self.explosionSize = explosionSize
        self.explosionBursts = explosionBursts
        self.fire()
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky_tex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.reparentTo(render)
        self.sky.setScale(500)
    def fire(self):
        if self.player==2:
            self.angle = 180 - self.angle
        self.proj = loader.loadModel('models/ball')
        self.proj.reparentTo(render)
        taskMgr.add(self.update, "updater")
        self.accept("HIT", self.hit)
    def update(self, task):
        if task.time > 10:
            taskMgr.remove("updater")
            messenger.send("HIT")
        newPos = projectPoint(self.angle, self.velocity, self.gravity, task.time * self.timeflow,self.startPos, self.wind)
        self.proj.setPos(Point3(newPos[0], 0, newPos[1]))
        return Task.cont
    def explode(self, size, minibursts, length):
        self.boomnode = render.attachNewNode("boomnode")
        self.boomnode.reparentTo(render)
        self.boomnode.setPos(self.proj.getPos())
        self.boomnode.setScale(size)
        self.exsize = size
        self.exnumbbursts = minibursts
        self.exlength = length
        taskMgr.add( self.updateExplode, "BOOM")
        base.enableParticles()
        self.pe = [0 for i in range(self.exnumbbursts)]
        for i in range(self.exnumbbursts):
            self.pe[i] = ParticleEffect()
            self.pe[i].setPos(Vec3(random.random() - .5, random.random() - .5,random.random() - .5))
            p0 = Particles("particles-1")
            # Particles parameters
            p0.setFactory("PointParticleFactory")
            p0.setRenderer("LineParticleRenderer")
            p0.setEmitter("SphereVolumeEmitter")
            p0.setPoolSize(5000)
            p0.setBirthRate(0.05)
            p0.setLitterSize(10)
            p0.setLitterSpread(0)
            p0.setSystemLifespan(self.exlength * 2)
            p0.setLocalVelocityFlag(1)
            p0.setSystemGrowsOlderFlag(0)
            # Factory parameters
            p0.factory.setLifespanBase(1.7500)
            p0.factory.setLifespanSpread(0.0500)
            p0.factory.setMassBase(1.0000)
            p0.factory.setMassSpread(0.0000)
            p0.factory.setTerminalVelocityBase(400.0000)
            p0.factory.setTerminalVelocitySpread(25.0000)
            # Point factory parameters
            # Renderer parameters
            p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
            p0.renderer.setUserAlpha(1.00)
            # Line parameters
            p0.renderer.setHeadColor(Vec4(1.00, 1.00, 1.00, 1.00))
            p0.renderer.setTailColor(Vec4(1.00, 0.59, 0.00, 1.00))
            p0.renderer.setLineScaleFactor(4.00)
            # Emitter parameters
            p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
            p0.emitter.setAmplitude(7.500* self.exsize)
            p0.emitter.setAmplitudeSpread(2.5000)
            p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.2500))
            p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
            p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
            # Sphere Volume parameters
            p0.emitter.setRadius(1.0500)
            f0 = ForceGroup('vertex')
            # Force parameters
            force0 = LinearVectorForce(0,0,-5)
            force0.setActive(1)
            force0.setVectorMasks(False, False, True) 
            f0.addForce(force0)
            self.pe[i].addForceGroup(f0)
            self.pe[i].addParticles(p0)
            self.pe[i].start(self.boomnode)
        self.pe2 = ParticleEffect()
        self.pe2.setPos(0,0,0)##self.proj.getPos())
        p1 = Particles('particles-2')
        # Particles parameters
        p1.setFactory("ZSpinParticleFactory")
        p1.setRenderer("SpriteParticleRenderer")
        p1.setEmitter("SphereVolumeEmitter")
        p1.setPoolSize(5000)
        p1.setBirthRate(0.0050)
        p1.setLitterSize(10)
        p1.setLitterSpread(0)
        p1.setSystemLifespan(0)
        p1.setLocalVelocityFlag(1)
        p1.setSystemGrowsOlderFlag(0)
        # Factory parameters
        p1.factory.setLifespanBase(1.000)
        p1.factory.setLifespanSpread(0.0000)
        p1.factory.setMassBase(1.0000)
        p1.factory.setMassSpread(0.0000)
        p1.factory.setTerminalVelocityBase(400.0000)
        p1.factory.setTerminalVelocitySpread(0.0000)
        # Z Spin factory parameters
        p1.factory.setInitialAngle(0.0000)
        p1.factory.setInitialAngleSpread(360.0000)
        p1.factory.enableAngularVelocity(1)
        p1.factory.setAngularVelocity(360.0000)
        p1.factory.setAngularVelocitySpread(360.0000)
        # Renderer parameters
        p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        p1.renderer.setUserAlpha(1.00)
        # Sprite parameters
        p1.renderer.addTextureFromFile('models/sparkle.png')
        p1.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
        p1.renderer.setXScaleFlag(0)
        p1.renderer.setYScaleFlag(0)
        p1.renderer.setAnimAngleFlag(3)
        p1.renderer.setInitialXScale(3)
        p1.renderer.setFinalXScale(3)
        p1.renderer.setInitialYScale(3)
        p1.renderer.setFinalYScale(4)
        p1.renderer.setNonanimatedTheta(0.0000)
        p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        p1.renderer.setAlphaDisable(0)
        p1.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOneMinusIncomingAlpha)
        p1.renderer.getColorInterpolationManager().addConstant(0.0,1.0,Vec4(1.0,1.0,1.0,0.39215686917304993),1)
        p1.renderer.getColorInterpolationManager().addLinear(0.0,1.0,Vec4(1.0,1.0,1.0,1.0),Vec4(1.0,1.0,1.0,0.0),1)
        # Emitter parameters
        p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        p1.emitter.setAmplitude(15.0000)
        p1.emitter.setAmplitudeSpread(0.0000)
        p1.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
        p1.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
        p1.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
        # Sphere Volume parameters
        p1.emitter.setRadius(1.0000)
        self.pe2.addParticles(p1)
        self.pe2.start(self.boomnode)
        self.pe3 = ParticleEffect()
        self.pe3.reset()
        self.pe3.setPos(0,0,0)##self.proj.getPos())
        self.pe3.setHpr(0.000, 0.000, 0.000)
        self.pe3.setScale(1.000, 1.000, 1.000)
        p2 = Particles('particles-1')
        # Particles parameters
        p2.setFactory("PointParticleFactory")
        p2.setRenderer("SpriteParticleRenderer")
        p2.setEmitter("SphereSurfaceEmitter")
        p2.setPoolSize(10000)
        p2.setBirthRate(0.03500)
        p2.setLitterSize(10)
        p2.setLitterSpread(0)
        p2.setSystemLifespan(0.0000)
        p2.setLocalVelocityFlag(1)
        p2.setSystemGrowsOlderFlag(0)
        # Factory parameters
        p2.factory.setLifespanBase(3.0000)
        p2.factory.setLifespanSpread(0.2500)
        p2.factory.setMassBase(2.0000)
        p2.factory.setMassSpread(0.0100)
        p2.factory.setTerminalVelocityBase(400.0000)
        p2.factory.setTerminalVelocitySpread(0.0000)
        # Point factory parameters
        # Renderer parameters
        p2.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        p2.renderer.setUserAlpha(1)
        # Sprite parameters
        p2.renderer.addTextureFromFile('models/smoke.png')
        p2.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
        p2.renderer.setXScaleFlag(0)
        p2.renderer.setYScaleFlag(0)
        p2.renderer.setAnimAngleFlag(0)
        p2.renderer.setInitialXScale(3)
        p2.renderer.setFinalXScale(3)
        p2.renderer.setInitialYScale(3)
        p2.renderer.setFinalYScale(3)
        p2.renderer.setNonanimatedTheta(0.0000)
        p2.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        p2.renderer.setAlphaDisable(0)
        p2.renderer.setColorBlendMode(ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha, ColorBlendAttrib.OOneMinusIncomingAlpha)
        p2.renderer.getColorInterpolationManager().addConstant(0.0,1.0,Vec4(1.0,1.0,1.0,.25),1)
        # Emitter parameters
        p2.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        p2.emitter.setAmplitude(10)
        p2.emitter.setAmplitudeSpread(0.0000)
        p2.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 5.0000))
        p2.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
        p2.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
        # Sphere Surface parameters
        p2.emitter.setRadius(0.0100)
        self.pe3.addParticles(p2)
        self.pe4 = ParticleEffect()
        self.pe4.reset()
        self.pe4.setPos(0,0,0)##self.proj.getPos())
        self.pe4.setHpr(0.000, 0.000, 0.000)
        self.pe4.setScale(7.000, 7.000, 7.000)
        p3 = Particles('particles-1')
        # Particles parameters
        p3.setFactory("PointParticleFactory")
        p3.setRenderer("SpriteParticleRenderer")
        p3.setEmitter("DiscEmitter")
        p3.setPoolSize(1024)
        p3.setBirthRate(0.0200)
        p3.setLitterSize(10)
        p3.setLitterSpread(0)
        p3.setSystemLifespan(1200.0000)
        p3.setLocalVelocityFlag(1)
        p3.setSystemGrowsOlderFlag(0)
        # Factory parameters
        p3.factory.setLifespanBase(10.0000)
        p3.factory.setLifespanSpread(0.0000)
        p3.factory.setMassBase(1.0000)
        p3.factory.setMassSpread(0.0000)
        p3.factory.setTerminalVelocityBase(400.0000)
        p3.factory.setTerminalVelocitySpread(0.0000)
        # Point factory parameters
        # Renderer parameters
        p3.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        p3.renderer.setUserAlpha(0.10)
        # Sprite parameters
        p3.renderer.setTexture(loader.loadTexture('models/smoke.png'))
        p3.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
        p3.renderer.setXScaleFlag(1)
        p3.renderer.setYScaleFlag(1)
        p3.renderer.setAnimAngleFlag(0)
        p3.renderer.setInitialXScale(0.0050)
        p3.renderer.setFinalXScale(0.0400)
        p3.renderer.setInitialYScale(0.0100)
        p3.renderer.setFinalYScale(0.0400)
        p3.renderer.setNonanimatedTheta(0.0000)
        p3.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        p3.renderer.setAlphaDisable(0)
        # Emitter parameters
        p3.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        p3.emitter.setAmplitude(1.75000)
        p3.emitter.setAmplitudeSpread(0.0000)
        p3.emitter.setOffsetForce(Vec3(0.1000, 0.0000, 0.1000))
        p3.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
        p3.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
        # Disc parameters
        p3.emitter.setRadius(0.5000)
        self.pe4.addParticles(p3)
        f0 = ForceGroup('vertex')
        # Force parameters
        force0 = LinearCylinderVortexForce(4.0000, 1.0000, 1.0000, 1.0000, 0)
        force0.setActive(1)
        f0.addForce(force0)
        force1 = LinearVectorForce(Vec3(0.0000, 0.0000, 1.0000), 0.0500, 0)
        force1.setActive(1)
        f0.addForce(force1)
        self.pe4.addForceGroup(f0)
        self.pe4.start(self.boomnode)
    def hit(self):
        self.explode(self.explosionSize, self.explosionBursts, .75)
    def updateExplode(self, task):
        ## for i in range(1, len(self.bursts) - 1):
            ## self.bursts[i].setPos(Vec3(random.random() * self.exsize - self.exsize/2,random.random() * self.exsize - self.exsize/2,random.random() * self.exsize - self.exsize/2)* .2)
            ## ##self.bursts[i].setPos(Vec3(random.random() * self.exsize - self.exsize/2,0,0)
            ## self.bursts[i].setScale((random.random()) * self.exsize * .05)
            ## self.bursts[i].setHpr(random.random() * 360, random.random() * 360, random.random() * 360)
        ## if task.time < self.exlength:
            ## self.explodesphere.setScale(task.time/self.exlength * self.exsize)
            ## self.explodesphere.setHpr(random.random() * 360, random.random() * 360, random.random() * 360)
        ## elif task.time < self.exlength * 2:
            ## ## self.explodesphere.setScale(self.explodesphere.getScale() - Vec3(1,1,1) * (task.time-self.exlength)/self.exlength * (self.exsize))
            ## self.explodesphere.setScale((2 *self.exlength - task.time)/self.exlength * (self.exsize))
            ## self.explodesphere.setHpr(random.random() * 360, random.random() * 360, random.random() * 360)
        ## else:
        if task.time > self.exlength * 2:
            for i in range(len(self.pe)):
                self.pe[i].softStop()
            self.pe2.softStop()
            self.pe4.softStop()
            self.pe3.start(self.boomnode)
        if task.time > self.exlength * 10:
            self.pe3.softStop()
            taskMgr.remove("BOOM")
        return Task.cont
def projectPoint(angle, velocity, gravity, time, location, wind):
    return [math.sin(90 - angle) * velocity * time + wind[0] * time + location[0],
         math.cos(90 - angle) * velocity * time - gravity * time * time + wind[1] * time + location[1]]
projfire = projectileFirer(
        float(input('Player?')),
        [0,0],
        float(input('Gravity?')),
        float(input('Angle?')), 
        float(input('velocity?')),
        [float(input('wind?')),0],
        float(input("timeflow?")),
        1, 20)
