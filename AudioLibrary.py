#By Kenneth Kozan
#ask me in person if you have questions
import direct.directbase.DirectStart
from pandac.PandaModules import * 
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from direct.interval.MetaInterval import Sequence
from direct.interval.IntervalGlobal import *


class AudioLibrary(DirectObject):  
    
    def __init__(self):
        
        #INDEX 0
        self.lucky = loader.loadSfx("Sounds/Lucky.wav")
        
        #INDEX 1
        self.stats = loader.loadSfx("Sounds/Stats.wav")
        
        #INDEX 2
        self.thunder = loader.loadSfx("Sounds/Thunder.wav")
        
        #INDEX 3
        self.bomb = loader.loadSfx("Sounds/Bomb.wav")
        
        #INDEX 4
        self.hurt = loader.loadSfx("Sounds/owow.wav")
        
        #INDEX 5
        self.dust = loader.loadSfx("Sounds/Dust.mp3")
        
        #INDEX 6
        self.bohemian = loader.loadSfx("Sounds/Bohemian.mp3")
        
        #INDEX 7
        self.click = loader.loadSfx("Sounds/Click.wav")
        
        #INDEX 8
        self.roll = loader.loadSfx("Sounds/Rollover.wav")
        
        #INDEX 9
        self.superman = loader.loadSfx("Sounds/Superman.mp3")
        
        #INDEX 10
        self.rednex = loader.loadSfx("Sounds/Rednex.mp3")
        
        #INDEX 11
        self.funky = loader.loadSfx("Sounds/Funkytown.mp3")
        
        #INDEX 12
        self.free = loader.loadSfx("Sounds/Free.mp3")
        
        #INDEX 13
        self.startheme = loader.loadSfx("Sounds/StarTheme.mp3")
        
        #INDEX 14
        self.starimperial = loader.loadSfx("Sounds/StarImperial.mp3")

        #INDEX 15
        self.dk1 = loader.loadSfx("Sounds/dk01.wav")

        #INDEX 16
        self.dk2 = loader.loadSfx("Sounds/dk02.wav")
        
        #self.rise = loader.loadSfx("Sounds/Ghost_in_the_Shell_TV_-_Rise.mp3")
        #self.balloons = loader.loadSfx("Sounds/Goldfinger - 99 Red Baloons.mp3")
        
        self.audArray = [loader.loadSfx("Sounds/StarImperial.mp3") for i in range(17)]
        
        self.audArray[0] = (self.lucky)
        self.audArray[1] = (self.stats)
        self.audArray[2] = (self.thunder)
        self.audArray[3] = (self.bomb)
        self.audArray[4] = (self.hurt) 
        self.audArray[5] = (self.dust)
        self.audArray[6] = (self.bohemian)
        self.audArray[7] = (self.click)
        self.audArray[8] = (self.roll)
        self.audArray[9] = (self.superman)
        self.audArray[10] = (self.rednex)
        self.audArray[11] = (self.funky)
        self.audArray[12] = (self.free)
        self.audArray[13] = (self.startheme)
        self.audArray[14] = (self.starimperial)
        self.audArray[15] = (self.dk1)
        self.audArray[16] = (self.dk2)
        for i in range(17):
            self.audArray[i].setVolume(1)        

    def getAudio(self, index):
        return self.audArray[index]
        
       
        
