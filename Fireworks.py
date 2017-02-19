import direct.directbase.DirectStart
from random import random
from direct.showbase.DirectObject import DirectObject
from direct.interval.MetaInterval import Sequence
from pandac.PandaModules import *
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
from types import *
import random,math,sys,os
from direct.task import Task
base.setBackgroundColor(0,0,0)
class Fireworks:
    def __init__(self, node, numbbooms, rang):
        
        self.boomnode = node
        self.booms = [0 for i in range(numbbooms)]
        self.fireworks = [0 for i in range(numbbooms)]
        self.numbbooms = numbbooms
        print range(self.numbbooms)
        i = 1
        if i == 1:
            self.booms[i]= render.attachNewNode("booms")
            self.booms[i].reparentTo(self.boomnode)
            self.booms[i].setPos(Vec3( random.random() * rang,
                                       random.random() * rang,
                                       random.random() * rang))
            self.fireworks[i] = ParticleEffect()
            self.fireworks[i].reset()
            self.fireworks[i].setPos(0.000, 0.000, 0.000)
            self.fireworks[i].setHpr(0.000, 0.000, 0.000)
            self.fireworks[i].setScale(1.000, 1.000, 1.000)
            p0 = Particles('particles-1')
            # Particles parameters
            p0.setFactory("ZSpinParticleFactory")
            p0.setRenderer("SpriteParticleRenderer")
            p0.setEmitter("SphereVolumeEmitter")
            p0.setPoolSize(1000)
            p0.setBirthRate(3.0000)
            p0.setLitterSize(100)
            p0.setLitterSpread(0)
            p0.setSystemLifespan(0.0000)
            p0.setLocalVelocityFlag(1)
            p0.setSystemGrowsOlderFlag(0)
            # Factory parameters
            p0.factory.setLifespanBase(0.5000)
            p0.factory.setLifespanSpread(0.0000)
            p0.factory.setMassBase(1.0000)
            p0.factory.setMassSpread(0.0000)
            p0.factory.setTerminalVelocityBase(400.0000)
            p0.factory.setTerminalVelocitySpread(0.0000)
            # Z Spin factory parameters
            p0.factory.setInitialAngle(0.0000)
            p0.factory.setInitialAngleSpread(360.0000)
            p0.factory.enableAngularVelocity(1)
            p0.factory.setAngularVelocity(360.0000)
            p0.factory.setAngularVelocitySpread(360.0000)
            # Renderer parameters
            p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
            p0.renderer.setUserAlpha(1)
            # Sprite parameters
            p0.renderer.addTextureFromFile('sparkle2.png')
            p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
            p0.renderer.setXScaleFlag(0)
            p0.renderer.setYScaleFlag(0)
            p0.renderer.setAnimAngleFlag(1)
            p0.renderer.setInitialXScale(0.1000)
            p0.renderer.setFinalXScale(0.0500)
            p0.renderer.setInitialYScale(0.1000)
            p0.renderer.setFinalYScale(1.0000)
            p0.renderer.setNonanimatedTheta(0.0000)
            p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
            p0.renderer.setAlphaDisable(0)
            p0.renderer.getColorInterpolationManager().addStepwave(0.0,1.0,Vec4(random.random(),random.random(),random.random(),1.0),Vec4(random.random(),random.random(),random.random(),1.0),0.0099999997764825821,0.0099999997764825821,1)
            # Emitter parameters
            p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
            p0.emitter.setAmplitude(1.0000)
            p0.emitter.setAmplitudeSpread(3.0000)
            p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
            p0.emitter.setExplicitLaunchVector(Vec3(0, 0.0000, 0.0000))
            p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
            # Sphere Volume parameters
            p0.emitter.setRadius(0.2000)
            self.fireworks[i].addParticles(p0)
            ## f0 = ForceGroup('a')
            ## # Force parameters
            ## force0 = LinearJitterForce(9.8075, 0)
            ## force0.setVectorMasks(1, 1, 1)
            ## force0.setActive(1)
            ## f0.addForce(force0)
            ## self.fireworks[i].addForceGroup(f0)
            self.fireworks[i].start(render)
            print self.booms[i]
boomnode = render.attachNewNode("boomnode")
boomnode.reparentTo(render)
fireworks = Fireworks(boomnode, 5, 0)
run()