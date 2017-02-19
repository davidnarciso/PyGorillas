from random import random
from direct.showbase.DirectObject import DirectObject
from direct.interval.MetaInterval import Sequence
from pandac.PandaModules import *
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
from types import *
import random,math,sys,os

class Explode(DirectObject):
    def __init__(self, size, minibursts, length, pos, target):
        self.boomnode = render.attachNewNode("boomnode")
        self.boomnode.reparentTo(render)
        self.boomnode.setPos(pos)
        self.boomnode.setScale(size)
        if target=="gorilla":
            self.boomnode.setScale(size/4.)
        else:
            self.boomnode.setScale(size/2.)
        self.exsize = size
        self.exnumbbursts = minibursts
        self.exlength = length/10
        base.enableParticles()
        self.sparknode = self.boomnode.attachNewNode("sparknode")
        if target=="gorilla":
            self.sparknode.setScale(5)
        self.sparknode.reparentTo(self.boomnode)
        self.pe = [0 for i in range(self.exnumbbursts)]
        for i in range(self.exnumbbursts):
            self.pe[i] = ParticleEffect()
            self.pe[i].setPos(Vec3(random.random() - .5,
                                   random.random() - .5,
                                   random.random() - .5))
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
            self.pe[i].start(self.sparknode)
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
        p1.renderer.setColorBlendMode(ColorBlendAttrib.MAdd,
                                      ColorBlendAttrib.OIncomingAlpha,
                                      ColorBlendAttrib.OOneMinusIncomingAlpha)
        p1.renderer.getColorInterpolationManager().addConstant(
            0.0,1.0,Vec4(1.0,1.0,1.0,0.39215686917304993),1)
        p1.renderer.getColorInterpolationManager().addLinear(
            0.0,1.0,Vec4(1.0,1.0,1.0,1.0),Vec4(1.0,1.0,1.0,0.0),1)
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
        if target=="gorilla":
            p2.setBirthRate(100)
        else:
            p2.setBirthRate(.01)##.035)
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
        if target == "gorilla":
            p2.renderer.addTextureFromFile('models/mushroomsmoke.png')
        else:
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
        p2.renderer.setColorBlendMode(
            ColorBlendAttrib.MAdd, ColorBlendAttrib.OIncomingAlpha,
            ColorBlendAttrib.OOneMinusIncomingAlpha)
        p2.renderer.getColorInterpolationManager().addConstant(
            0.0,1.0,Vec4(1.0,1.0,1.0,.25),1)
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
        if target=="gorilla":
            self.ringnode = self.boomnode.attachNewNode("ringnode")
            self.ringnode.setScale(2)
            self.ringnode.reparentTo(self.boomnode)
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
            p3.factory.setLifespanBase(7.5)
            p3.factory.setLifespanSpread(0.0000)
            p3.factory.setMassBase(1.0000)
            p3.factory.setMassSpread(0.0000)
            p3.factory.setTerminalVelocityBase(400.0000)
            p3.factory.setTerminalVelocitySpread(0.0000)
            # Point factory parameters
            # Renderer parameters
            p3.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
            p3.renderer.setUserAlpha(0.2)##10)
            # Sprite parameters
            p3.renderer.setTexture(loader.loadTexture('models/mushroomsmoke.png'))
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
            self.pe4.start(self.ringnode)
        self.target = target
        
        self.mushroomNode = self.boomnode.attachNewNode("mushroomNode")
        self.mushroomNode.reparentTo(self.boomnode)
        self.mushroomNode.setScale(32)
        self.mushroom = ParticleEffect()
        self.mushroom.reset()
        self.mushroom.setPos(0,0,0)
        self.mushroom.setHpr(0.000, 0.000, 0.000)
        self.mushroom.setScale(1.000, 1.000, 1.000)
        p0 = Particles('particles-1')
        # Particles parameters
        p0.setFactory("ZSpinParticleFactory")
        p0.setRenderer("SpriteParticleRenderer")
        p0.setEmitter("SphereVolumeEmitter")
        p0.setPoolSize(3000)
        p0.setBirthRate(0.0400)
        p0.setLitterSize(10)
        p0.setLitterSpread(0)
        p0.setSystemLifespan(0.0000)
        p0.setLocalVelocityFlag(1)
        p0.setSystemGrowsOlderFlag(0)
        # Factory parameters
        p0.factory.setLifespanBase(7.5000)
        p0.factory.setLifespanSpread(0.0000)
        p0.factory.setMassBase(1.0000)
        p0.factory.setMassSpread(0.0000)
        p0.factory.setTerminalVelocityBase(400.0000)
        p0.factory.setTerminalVelocitySpread(0.0000)
        # Z Spin factory parameters
        p0.factory.setInitialAngle(0.0000)
        p0.factory.setInitialAngleSpread(360.0000)
        p0.factory.enableAngularVelocity(1)
        p0.factory.setAngularVelocity(1.0000)
        p0.factory.setAngularVelocitySpread(360.0000)
        # Renderer parameters
        p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
        p0.renderer.setUserAlpha(.35)##0.15)
        # Sprite parameters
        p0.renderer.addTextureFromFile('models/mushroomsmoke.png')
        p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
        p0.renderer.setXScaleFlag(0)
        p0.renderer.setYScaleFlag(0)
        p0.renderer.setAnimAngleFlag(0)
        p0.renderer.setInitialXScale(0.3500)
        p0.renderer.setFinalXScale(1.0000)
        p0.renderer.setInitialYScale(0.3500)
        p0.renderer.setFinalYScale(1.0000)
        p0.renderer.setNonanimatedTheta(0.0000)
        p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
        p0.renderer.setAlphaDisable(0)
        p0.renderer.getColorInterpolationManager().addLinear(0.5,1.0,Vec4(1.0,1.0,1.0,1.0),Vec4(0.0,0.19607843458652496,0.19607843458652496,1.0),1)
        # Emitter parameters
        p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
        p0.emitter.setAmplitude(0.2500)
        p0.emitter.setAmplitudeSpread(0.0500)
        p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 1.0000))
        p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
        p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
        # Sphere Volume parameters
        p0.emitter.setRadius(0.7500)
        self.mushroom.addParticles(p0)
        f0 = ForceGroup('a')
        # Force parameters
        force0 = LinearSinkForce(Point3(0.0000, 0.0000, 2.5000), LinearDistanceForce.FTONEOVERR, 2.0000, 11.3978, 1)
        force0.setVectorMasks(0, 0, 1)
        force0.setActive(1)
        f0.addForce(force0)
        force1 = LinearSourceForce(Point3(0.0000, 0.0000, 2.5000), LinearDistanceForce.FTONEOVERR, 0.2500, 0.0250, 1)
        force1.setVectorMasks(1, 1, 0)
        force1.setActive(1)
        f0.addForce(force1)
        force2 = LinearFrictionForce(1.0000, 2.0000, 0)
        force2.setVectorMasks(0, 0, 0)
        force2.setActive(1)
        f0.addForce(force2)
        force3 = LinearFrictionForce(0.5000, 0.5000, 0)
        force3.setVectorMasks(1, 1, 1)
        force3.setActive(1)
        f0.addForce(force3)
        force4 = LinearFrictionForce(1.0000, 1.0000, 0)
        force4.setVectorMasks(0, 0, 1)
        force4.setActive(1)
        f0.addForce(force4)
        force5 = LinearJitterForce(4.0000, 0)
        force5.setVectorMasks(0, 0, 1)
        force5.setActive(1)
        force6 = LinearCylinderVortexForce(1.0000, 1.0000, 1.0000, 1.0000, 0)
        force6.setVectorMasks(1, 1, 1)
        force6.setActive(1)
        f0.addForce(force6)
        self.mushroom.addForceGroup(f0)
    def remove(self):
        try:
            for i in range(self.exnumbbursts):
                self.explode.pe[i].reset()
        except:
            1+1
        try:
            self.explode.pe2.reset()
        except:
            1+1
        try:
            self.explode.pe3.reset()
        except:
            1+1
        try:
            if self.target == "gorilla":
                self.explode.pe4.reset()
        except:
            1+1
        try:
            if self.target == "gorilla":
                self.explode.mushroom.reset()
        except:
            1+1
    def sparkoff(self):
        for i in range(len(self.pe)):
            self.pe[i].softStop()
        self.pe2.softStop()
