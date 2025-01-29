import pygame
import random
from character import Character, skill

class Enemy(Character):

    def __init__(self, game, pos, size):
        super().__init__(game, 'Enemy', pos, size)

        self.name = ' '
        self.InfectRate = 0.0

        self.attackstat = 0.8
        self.sp = 100

        # How much the attack 
        self.attackDmg = 10
        self.maxHp = 100
        self.currentHp = self.maxHp
        #self.skillCooldown = []
        self.skills = [skill, skill]

        self.attackFlip = False

    def TakeDmg(self, amount):

        # Reduces the current hp of enemy by amount of inflicted attack.
        # Have to use max(0, ...) or the enemy's health 
        # will eventually become negative.
        self.currentHp = max(0, self.currentHp - amount)

        if self.currentHp <= 0:
            print(self.name + " has been defeated.")
       
    def heal(self, amount):

        # Increases the current hp of enemy by amount of healing.
        # Have to use min(eslf.maxHp, ...) or the enemy's health 
        # will eventually overcap.
        self.currentHp = min(self.maxHp, self.currentHp + amount)

    def basicAttack(self):
        self.attackDmg = 10 * self.attackstat
        return self.attackDmg
    
    def TakeTurn(self):
        #if skill 1 of cooldown and has enough sp use it
        if self.skills[0].cooldown == 0 and self.sp > self.skills[0].sp:
            self.sp -= self.skills[0].sp # lose sp based on skill
            return self.skills[0].use

        #if skill 2 on cooldown and skill 2 of cooldown use it
        elif self.skills[1].cooldown == 0 and self.sp > self.skills[1].sp:
            self.sp -= self.skills[1].sp # lose sp based on skill
            return self.skills[1].use

        #if either skill is about to be off cooldown then gaurd
        elif self.skills[0].cooldown == 1 or self.skills[1].cooldown == 1:
            self.gaurd()
            return 0
    
        else:
            return self.basicAttack()
        
    def infected(self, defaultInfectionRate):
        pass

    def getinfectresist(self):
        return self.InfectRate
        
#    def skillAttack(self):
#        self.attackDmg = 30 * self.attacksta
#        return self.attackDmg

#    def skillAttack2(self):
#        self.attackDmg = 50 * self.attackstat
#        return self.attackDmg        


    
class RSoldier(Enemy):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

        self.name = 'Revived Soldier'
        self.InfectRate = 0.5


        self.attackstat = 0.8
        self.sp = 100

        # How much the attack 
        self.attackDmg = 10
        self.maxHp = 150
        self.currentHp = self.maxHp
        self.skillCooldown = []

        # Skills
        BSlash = skill('Big Slash', 20, 3, 10)
        SBash = skill('Shield Bash', 10, 2, 5)

        self.skills = [BSlash, SBash]
        self.attackFlip = False


class Orc(Enemy):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

        self.name = 'Orc'
        self.InfectRate = 0.5

        self.attackstat = 1.0
        self.sp = 150

        # How much the attack 
        self.attackDmg = 10
        self.maxHp = 200
        self.currentHp = self.maxHp
        self.skillCooldown = []

        # Skills
        Bonk = skill('Bonk', 15, 2, 20)
        Big_Bonk = skill('Big Bonk', 40, 5, 40)

        self.skills = [Bonk, Big_Bonk]
        self.attackFlip = False


class Rat(Enemy):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

        self.name = 'Revived Soldier'
        self.InfectRate = 0.8

        self.attackstat = 0.5
        self.sp = 90

        # How much the attack 
        self.attackDmg = 10
        self.maxHp = 80
        self.currentHp = self.maxHp
        self.skillCooldown = []

        # Skills
        MaM = skill('Malicious Mandible', 10, 1, 5)
        RatK = skill('Long Live The Rat King', 50, 10, 20)

        self.skills = [MaM, RatK]
        self.attackFlip = False

    def TakeTurn(self):
        #if skill 1 of cooldown and has enough sp use it
        if self.skills[0].cooldown == 0 and self.sp > self.skills[0].sp:
            self.sp -= self.skills[0].sp # lose sp based on skill
            return self.skills[0].use

        #if skill 2 on cooldown and skill 2 of cooldown use it
        elif self.currentHp <= 40 and self.skills[1].cooldown == 0 and self.sp > self.skills[1].sp:
            self.sp -= self.skills[1].sp # lose sp based on skill
            # Skill 2 "Long Live The Rat King" heals 50 HP
            if (self.currentHp + 50) > 80: # If heal would be more than max HP set it to max
                self.currentHp = 80
            else:
                self.currentHp += 50

            return self.skills[1].use

        #if either skill is about to be off cooldown then gaurd
        elif self.skills[0].cooldown == 1 or self.skills[1].cooldown == 1:
            self.gaurd()
            return 0
    
        else:
            return self.basicAttack()


class FFaith(Enemy):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

        self.name = 'Forgotten Faithful'
        self.InfectRate = 0.3

        self.attackstat = 0.3
        self.sp = 50

        # How much the attack 
        self.attackDmg = 10
        self.maxHp = 100
        self.currentHp = self.maxHp
        self.skillCooldown = []

        # Skills
        DivR = skill('Divin Retribution', 50, 8, 0)
        Smite = skill('Smite', 20, 1, 0)

        self.skills = [DivR, Smite]
        self.attackFlip = False



class Ghoul(Enemy):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

        self.name = 'Ghoul'
        self.InfectRate = 0.4

        self.attackstat = 0.9
        self.sp = 100

        # How much the attack 
        self.attackDmg = 10
        self.maxHp = 150
        self.currentHp = self.maxHp
        self.skillCooldown = []

        # Skills
        Claw = skill('Claw Strike', 30, 2, 20)
        Rage = skill('Devilish Rage', 50, 4, 40)

        self.skills = [Claw, Rage]
        self.attackFlip = False


class Carrion(Enemy):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

        self.name = 'The Carrion'
        self.InfectRate = -11.0

        self.attackstat = 1.5
        self.sp = 1000

        # How much the attack 
        self.attackDmg = 20
        self.maxHp = 300
        self.currentHp = self.maxHp
        self.skillCooldown = []

        # Skills
        Rage = skill('Chimeric Rage', 50, 4, 60)
        Writh = skill('Homicidal Writhe', 100, 10, 100)

        self.skills = [Writh, Rage]
        self.attackFlip = False

class wiz(Enemy):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

        self.name = 'The Harbinger Of the Unwanted'
        self.InfectRate = -20.0

        self.attackstat = 2.0
        self.sp = 1000

        # How much the attack 
        self.attackDmg = 20
        self.maxHp = 350
        self.currentHp = self.maxHp
        self.skillCooldown = []

        # Skills
        Veng = skill('Vengence Of Gloryous Heros', 150, 20, 100)
        Suff = skill('Sorrow Of The Survivors', 50, 2, 60)

        self.skills = [Veng, Suff]
        self.attackFlip = False



    def TakeTurn(self):
        # if skills 1 and 2 are useable use 1 at random
        if self.skills[0].cooldown == 0 and self.sp > self.skills[0].sp:
            if self.skills[1].cooldown == 0 and self.sp > self.skills[1].sp:
                s = random.randint(0, 1)
                self.sp -= self.skills[s]
                return self.skills[s]
            
            self.sp -= self.skills[0].sp # lose sp based on skill
            return self.skills[0].use

        #if skill 2 on cooldown and skill 2 of cooldown use it
        elif self.skills[1].cooldown == 0 and self.sp > self.skills[1].sp:
            self.sp -= self.skills[1].sp # lose sp based on skill
            return self.skills[1].use

        #if either skill is about to be off cooldown then gaurd
        elif self.skills[0].cooldown == 1 or self.skills[1].cooldown == 1:
            self.gaurd()
            return 0
    
        else:
            return self.basicAttack()