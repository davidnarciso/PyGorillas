import random
class Projectile(object):


    def __init__(self, angle, power):
        self.myAngle = angle
        self.myPower = power

        
    def shootProjectile(self):
        hit = random.randint(1,5)
        if hit == 3:
            return 1
        else:
            return 0
        
        

