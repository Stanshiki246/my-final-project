import pygame
pygame.init()
# All Player objects
class Player:
    # Constructor function
    def __init__(self,name,job,health,max_health,level,basedamage,damage,evade,crit_chance,crit_atk):
        self.name=name
        self.job=job
        self.health=int(health)
        self.max_health=int(max_health)
        self.level=int(level)
        self.basedamage=int(basedamage)
        self.damage=int(damage)
        self.exp=0
        self.max_exp=100
        self.gold=0
        self.potion=1
        self.evade= int(evade)
        self.crit_chance = int(crit_chance)
        self.crit_atk = float(crit_atk)
    #Level up function
    def levelup(self,max_health,basedamage,damage,screen):
        if self.exp >= self.max_exp:
            self.max_health += int(max_health)
            self.basedamage += int(basedamage)
            self.damage += int(damage)
            self.level += 1
            self.exp = self.exp - (100*(self.level-1))
            self.max_exp += 100
            self.health = self.max_health
            self.font=pygame.font.SysFont("Verdana",20)
            self.text_rendering=self.font.render("Your level becomes level {}".format(self.level),True,(0,0,0))
            self.blitme=screen.blit(self.text_rendering,(500,450))
# Warrior object
class Warrior(Player):
    def __init__(self):
        super().__init__("Nova","Warrior",150,150,1,2,10,50,50,2)
        self.sprite=pygame.image.load("textures\\warrior_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Rogue object
class Rogue(Player):
    def __init__(self):
        super().__init__("Tyler","Rogue",75,75,1,4,20,75,50,2)
        self.sprite=pygame.image.load("textures\\assassin_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Archer object
class Archer(Player):
    def __init__(self):
        super().__init__("Lyna","Archer",100,100,1,3,15,50,75,2)
        self.sprite=pygame.image.load("textures\\archer_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
