#By Kenneth Kozan as of 4/24/2007
#ask me in person if you have questions
import direct.directbase.DirectStart
from pandac.PandaModules import * 
from direct.showbase.DirectObject import DirectObject

class TextureLibrary(DirectObject):
    
    def __init__(self):        
        
        #TEXTURES AFTER A NUMBER '9' WILL START TO BE THE BURNT VERSION OF  1-9
        #SO TEXTURE NUMBER 10 IS BURN VERSION OF NUMBER 1, 11 IS OF 2 AND SO ON...
        
        
        #I know this is not the best way to do this but it works so whatever.
        self.texArray = []
        
        self.toptexture = loader.loadTexture("models/building/toptex.PNG")

        self.texture1 = loader.loadTexture("models/building/building_0.PNG")
        self.texture10 = loader.loadTexture("models/building/building_0b.PNG")
       
        self.texture2 = loader.loadTexture("models/building/building_1.PNG")
        self.texture11 = loader.loadTexture("models/building/building_1b.PNG")
       
        self.texture3 = loader.loadTexture("models/building/building_2.PNG")
        self.texture12 = loader.loadTexture("models/building/building_2b.PNG")
        
        self.texture4 = loader.loadTexture("models/building/building_3.PNG")
        self.texture13 = loader.loadTexture("models/building/building_3b.PNG")
                
        self.texture5 = loader.loadTexture("models/building/building_4.PNG")
        self.texture14 = loader.loadTexture("models/building/building_4b.PNG")
        
        self.texture6 = loader.loadTexture("models/building/building_5.PNG")
        self.texture15 = loader.loadTexture("models/building/building_5b.PNG")
        
        self.texture7 = loader.loadTexture("models/building/building_6.PNG")
        self.texture16 = loader.loadTexture("models/building/building_6b.PNG")
        
        self.texture8 = loader.loadTexture("models/building/building_7.PNG")
        self.texture17 = loader.loadTexture("models/building/building_7b.PNG")
        
        self.texture9 = loader.loadTexture("models/building/building_8.PNG")
        self.texture18 = loader.loadTexture("models/building/building_8b.PNG")

        self.texArray = [loader.loadTexture("models/building/toptex.PNG") for i in range(19)]
        
        self.texArray[0] = (self.toptexture)
        self.texArray[1] = (self.texture1)
        self.texArray[2] = (self.texture2)
        self.texArray[3] = (self.texture3)
        self.texArray[4] = (self.texture4)
        self.texArray[5] = (self.texture5)
        self.texArray[6] = (self.texture6)
        self.texArray[7] = (self.texture7)
        self.texArray[8] = (self.texture8)
        self.texArray[9] = (self.texture9)
        self.texArray[10] = (self.texture10)
        self.texArray[11] = (self.texture11)
        self.texArray[12] = (self.texture12)
        self.texArray[13] = (self.texture13)
        self.texArray[14] = (self.texture14)
        self.texArray[15] = (self.texture15)
        self.texArray[16] = (self.texture16)
        self.texArray[17] = (self.texture17)
        self.texArray[18] = (self.texture18)

#Gets texture depending in the index given.  Add a '9' to make it "burnt"
    def getTexture(self, index):
        return self.texArray[index]
        
