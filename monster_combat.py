import pygame
pygame.init()
#All Monster Objects
class Monster:
    # Constructor function
    def __init__(self,name,health,max_health,level,basedamage,damage,evade):
        self.name =  name
        self.health = float(health)
        self.max_health = int(max_health)
        self.level = int(level)
        self.basedamage=int(basedamage)
        self.damage = int(damage)
        self.evade = int(evade)

# Objects for forest monsters.
class Goblin(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Goblin",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\goblin_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Spider(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Spider",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\spider_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
#Object for forest boss monster
class Eagle(Monster):
    def __init__(self,health,max_health,level,basedamage,damage,evade):
        super().__init__("Swift Eagle",health,max_health,level,basedamage,damage,evade)
        self.sprite=pygame.image.load("textures\\eagle_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Objects for Cave monsters
class Ogre(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Ogre",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\ogre_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Orc(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Orc",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\Orc_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Object for Cave boss monster
class Golem(Monster):
    def __init__(self,health,max_health,level,basedamage,damage,evade):
        super().__init__("Earth Golem",health,max_health,level,basedamage,damage,evade)
        self.sprite=pygame.image.load("textures\\golem_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Objects for Beach monsters
class Crab(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Crab",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\Crab_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Octopus(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Octopus",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\octopus_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Object for beach boss monster
class Leviathan(Monster):
    def __init__(self,health,max_health,level,basedamage,damage,evade):
        super().__init__("Leviathan",health,max_health,level,basedamage,damage,evade)
        self.sprite=pygame.image.load("textures\\leviathan_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Objects for snow monsters
class SnowWolf(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Snow Wolf",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\snow_wolf_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Skeleton(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Skeleton",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\Skeleton_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Yeti(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Yeti",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\Yeti_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Object for snow boss monster
class SkeletonKing(Monster):
    def __init__(self,health,max_health,level,basedamage,damage,evade):
        super().__init__("Skeleton King",health,max_health,level,basedamage,damage,evade)
        self.sprite=pygame.image.load("textures\\Skeleton_king_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
#Objects for volcano monsters
class Cerberus(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Cerberus",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\cerberus_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Phoenix(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Phoenix",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\phoenix_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Wyvern(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Wyvern",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\fire_wyvern_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class Dragon(Monster):
    def __init__(self,health,max_health,level,basedamage,damage,evade):
        super().__init__("Fire Dragon",health,max_health,level,basedamage,damage,evade)
        self.sprite=pygame.image.load("textures\\fire_dragon_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
#Objects for dark castle monsters
class DarkEagle(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Dark Eagle",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\Dark_Eagle_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class AncientGolem(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Ancient Golem",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\dark_golem_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class SkeletonChampion(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Skeleton Champion",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\skeleton_champion_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
class DeathDragon(Monster):
    def __init__(self,health,max_health,level,basedamage,damage):
        super().__init__("Death Dragon",health,max_health,level,basedamage,damage,10)
        self.sprite=pygame.image.load("textures\\death_dragon_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Object for Dark Castle mid boss monster
class DarkLeviathan(Monster):
    def __init__(self,health,max_health,level,basedamage,damage,evade):
        super().__init__("Dark Leviathan",health,max_health,level,basedamage,damage,evade)
        self.sprite=pygame.image.load("textures\\Dark_Leviathan_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
# Object for Dark Castle final boss monster
class DemonKing(Monster):
    def __init__(self,health,max_health,level,basedamage,damage,evade):
        super().__init__("Demon King",health,max_health,level,basedamage,damage,evade)
        self.sprite=pygame.image.load("textures\\demon_lord_combat.png")
        self.sprite=pygame.transform.scale(self.sprite,(300,300))
