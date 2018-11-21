import pygame,sys,random
from player_combat import *
from monster_combat import *
from combat_button import *
import setting_combat
pygame.init()
# Creates window screen
window_width=1200
window_height=800
window_title="Brave Heroes"
pygame.display.set_caption((window_title))
window = pygame.display.set_mode((window_width,window_height))
# Color
WHITE=(255,255,255)
Red=(255,0,0)
Gray=(235,235,235)
Yellow=(255,255,0)
Blue=(0,0,255)
Black=(0,0,0)
# NPC Shopkeeper
merchant=pygame.image.load("textures\\merchant.png")
merchant=pygame.transform.scale(merchant,(300,300))
# Combat Stage Buttons (Forest,Cave,Beach)
Dungeon=Button(window,450,300,300,50,"Dungeon")
BossFight=Button(window,450,400,300,50,"Boss Fight")
# Combat Stage Buttons (Snow and Volcano)
SVDungeon=Button(window,450,300,300,50,"Dungeon 1")
SVDungeon2=Button(window,450,400,300,50,"Dungeon 2")
SVBossFight=Button(window,450,500,300,50,"Boss Fight")
# Combat Stage Buttons (Dark Castle)
DarkDungeon=Button(window,400,200,350,50,"Dungeon 1")
DarkDungeon2=Button(window,400,400,350,50,"Dungeon 2")
MidBossFight=Button(window,400,300,350,50,"Mid-Boss Fight")
FinalBossFight=Button(window,400,500,350,50,"Final Boss Fight")
#Return Button
BackBtn=Button(window,0,750,150,50,"Back")
#Inn Button
BattleBtn=Button(window,900,400,200,50,"Battle!")
ShopBtn=Button(window,300,100,150,50,"Shop")
SaveBtn=Button(window,800,0,150,50,"Save")
LoadBtn=Button(window,1000,0,150,50,"Load")
HelpBtn=Button(window,600,0,150,50,"Help")
# Save and Load Button
Data1=Button(window,150,300,150,50,"Data 1")
Data2=Button(window,450,300,150,50,"Data 2")
Data3=Button(window,750,300,150,50,"Data 3")
#Shop Button
BuyBtn=Button(window,625,325,125,50,"Buy")
BuyBtn2=Button(window,775,325,125,50,"Buy")
BuyBtn3=Button(window,925,325,125,50,"Buy")
BuyBtn4=Button(window,1075,325,125,50,"Buy")
# World Map Buttons
ForestBtn=Button(window,50,200,200,50,"Forest")
CaveBtn=Button(window,450,200,200,50,"Cave")
BeachBtn=Button(window,850,200,200,50,"Beach")
SnowBtn=Button(window,50,600,200,50,"Snow")
VolcanoBtn=Button(window,450,600,200,50,"Volcano")
DarkCastleBtn=Button(window,850,600,250,50,"Dark Castle")
#Menu Interfaces
Menu_Title_font=pygame.font.SysFont("Verdana",48)
Menu_Title=Menu_Title_font.render("Brave Heroes",True,WHITE)
MenuBg=pygame.image.load("textures\\BG.png")
MenuBg=pygame.transform.scale(MenuBg,(window_width,window_height))
StartBtn=Button(window,50,200,200,50,"Start")
QuitBtn=Button(window,50,300,200,50,"Quit")
# Player Selection Buttons
Nova_Btn = Button(window,100,350,200,50,"Nova")
Tyler_Btn = Button(window,500,350,200,50,"Tyler")
Lyna_Btn = Button(window,900,350,200,50,"Lyna")
# Background Combat
forest_bg=pygame.image.load("textures\\forest_bg.png")
forest_bg=pygame.transform.scale(forest_bg,(window_width,window_height))
cave_bg = pygame.image.load("textures\\cave_bg.png")
cave_bg=pygame.transform.scale(cave_bg,(window_width,window_height))
beach_bg = pygame.image.load("textures\\Beach_bg.jpg")
beach_bg=pygame.transform.scale(beach_bg,(window_width,window_height))
snow_bg = pygame.image.load("textures\\snow_bg1.png")
snow_bg=pygame.transform.scale(snow_bg,(window_width,window_height))
volcano_bg = pygame.image.load("textures\\volcano_bg.jpg")
volcano_bg=pygame.transform.scale(volcano_bg,(window_width,window_height))
dark_castle_bg = pygame.image.load("textures\\demon_castle_bg3.jpg")
dark_castle_bg=pygame.transform.scale(dark_castle_bg,(window_width,window_height))
dark_castle_bg2 = pygame.image.load("textures\\demon_castle_bg1.png")
dark_castle_bg2=pygame.transform.scale(dark_castle_bg2,(window_width,window_height))
dark_castle_bg3 = pygame.image.load("textures\\demon_castle_bg2.png")
dark_castle_bg3=pygame.transform.scale(dark_castle_bg3,(window_width,window_height))
# Inn Background
inn=pygame.image.load("textures\\inn.jpg")
inn=pygame.transform.scale(inn,(window_width,window_height))
# Background World Map
forest_map = pygame.image.load("textures\\forest_bg.png")
forest_map = pygame.transform.scale(forest_map,(400,400))
cave_map = pygame.image.load("textures\\cave_bg.png")
cave_map = pygame.transform.scale(cave_map,(400,400))
beach_map = pygame.image.load("textures\\Beach_bg.jpg")
beach_map = pygame.transform.scale(beach_map,(400,400))
snow_map = pygame.image.load("textures\\Snow_bg1.png")
snow_map = pygame.transform.scale(snow_map,(400,400))
volcano_map = pygame.image.load("textures\\volcano_bg.jpg")
volcano_map = pygame.transform.scale(volcano_map,(400,400))
dark_castle_map=pygame.image.load("textures\\demon_castle_bg3.jpg")
dark_castle_map=pygame.transform.scale(dark_castle_map,(400,400))
#Function to show intro story
def Intro():
    intro1=font_status_player.render("The Demon King has stolen four crystals from us!",True,WHITE)
    intro2=font_status_player.render("Without those crystals, our world will be in a perished situation.",True,WHITE)
    intro3=font_status_player.render("The King orders you, one of bravest heroes, to defeat him and retrieve those crystals back.",True,WHITE)
    intro4=font_status_player.render("Have a good journey. May Our Goddess blesses you, {}.".format(p1.name),True,WHITE)
    skip=font_status_player.render("Press Enter to continue",True,WHITE)
    window.fill((0,0,0))
    window.blit(intro1,(300,200))
    window.blit(intro2,(300,300))
    window.blit(intro3,(300,400))
    window.blit(intro4,(300,500))
    window.blit(skip,(300,600))
    pygame.display.update()
#Function to show ending after final boss is defeated
def Ending():
    ending1=font_status_monster.render("Congratulations!",True,Black)
    ending2=font_status_player.render("You have defeated the Demon King and retrieve our four crytals back",True,Black)
    ending3=font_status_player.render("Also, you will promoted by the King as General of his armies",True,Black)
    ending4=font_status_player.render("Thank you for playing it",True,Black)
    skip=font_status_player.render("Press Enter to continue",True,Black)
    window.blit(MenuBg,(0,0))
    window.blit(ending1,(500,200))
    window.blit(ending2,(300,300))
    window.blit(ending3,(300,400))
    window.blit(ending4,(300,500))
    window.blit(skip,(300,600))
    pygame.display.update()
#Function to show credits
def Credit():
    credit=font_status_monster.render("Credits",True,WHITE)
    developer=font_status_player.render("Game Developer: Stanley Tantysco",True,WHITE)
    api=font_status_player.render("APIs: Pygame, Random, Sys",True,WHITE)
    reference=font_status_player.render("Thanks to: Livander and Eris (Attack rendering and sound effects references)",True,WHITE)
    window.fill((0,0,0))
    window.blit(credit,(500,200))
    window.blit(developer,(300,300))
    window.blit(api,(300,400))
    window.blit(reference,(300,500))
    pygame.display.update()
#Functioon to show chapter
def Chapter(chapter,title,titlex):
    chapter=font_chapter.render(chapter,True,WHITE)
    chapter_title=font_chapter_title.render(title,True,WHITE)
    window.fill((0,0,0))
    window.blit(chapter,(500,200))
    window.blit(chapter_title,(titlex,400))
    pygame.display.update()
#Load Data Function
def LoadData(filename):
    # Read text file
    with open(filename,"r") as file:
        f = file.read()
    #Split string and integer data
    data = f.split(":")
    # Get name and job data
    datastr=data[0]
    # Get HP data
    dataHP=data[1]
    # Get level data
    datalvl=data[2]
    # Get damage data
    datadmg=data[3]
    # Get exp data
    dataexp=data[4]
    # Get potion data
    datapot=data[5]
    # Get gold data
    datagold=data[6]
    # Get evade
    dataevade=data[7]
    # Get critical hit
    datacrit= data[8]
    # Get story progress
    datastory=data[9]
    # Get mid and final boss
    databoss=data[10]
    # Get the data of boss monster
    databossHP=data[11]
    data.remove(datagold)
    data.remove(datapot)
    data.remove(dataexp)
    data.remove(datadmg)
    data.remove(datalvl)
    data.remove(dataHP)
    data.remove(datastr)
    data.remove(datastory)
    data.remove(databoss)
    data.remove(databossHP)
    dataHP = dataHP.split(",")
    datadmg=datadmg.split(",")
    dataexp=dataexp.split(",")
    datastr = datastr.split(",")
    datacrit=datacrit.split(",")
    datastory=datastory.split(",")
    databoss=databoss.split(",")
    databossHP=databossHP.split(",")
    p1.name= datastr[0]
    p1.job = datastr[1]
    p1.health,p1.max_health,p1.level,p1.basedamage,p1.damage=int(dataHP[0]),int(dataHP[1]),int(datalvl),int(datadmg[0]),int(datadmg[1])
    p1.exp,p1.max_exp,p1.potion,p1.gold = int(dataexp[0]),int(dataexp[1]),int(datapot),int(datagold)
    p1.evade,p1.crit_chance,p1.crit_atk=int(dataevade),int(datacrit[0]),float(datacrit[1])
    setting_combat.chapter1,setting_combat.chapter2,setting_combat.chapter3=int(datastory[0]),int(datastory[1]),int(datastory[2])
    setting_combat.chapter4,setting_combat.chapter5,setting_combat.chapter6=int(datastory[3]),int(datastory[4]),int(datastory[5])
    setting_combat.midboss,setting_combat.finalboss=int(databoss[0]),int(databoss[1])
    eagle.health,golem.health,leviathan.health=float(databossHP[0]),float(databossHP[1]),float(databossHP[2])
    skeletonKing.health,dragon.health,darkLeviathan.health=float(databossHP[3]),float(databossHP[4]),float(databossHP[5])
    #Get sprite
    if p1.job == "Warrior":
        p1.sprite = warrior.sprite
    elif p1.job == "Rogue":
        p1.sprite = rogue.sprite
    elif p1.job == "Archer":
        p1.sprite = archer.sprite
# Save Data Function
def SaveData(p1,filename):
    # Write data into text file
    data=p1.name+","+p1.job+":"+str(p1.health)+","+str(p1.max_health)+":"+str(p1.level)+":"+str(p1.basedamage)+","+str(p1.damage)+":"+str(p1.exp)+","+str(p1.max_exp)+":"+\
         str(p1.potion)+":"+str(p1.gold)+":"+str(p1.evade)+":"+str(p1.crit_chance)+","+str(p1.crit_atk)+":"+str(setting_combat.chapter1)+","+str(setting_combat.chapter2)+","+str(setting_combat.chapter3)+","+\
    str(setting_combat.chapter4)+","+str(setting_combat.chapter5)+","+str(setting_combat.chapter6)+":"+str(setting_combat.midboss)+","+str(setting_combat.finalboss)+":"+\
        str(eagle.health)+","+str(golem.health)+","+str(leviathan.health)+","+str(skeletonKing.health)+","+str(dragon.health)+","+str(darkLeviathan.health)
    with open(filename,"w") as file:
        file.write(data)
# Save Data scene function
def SaveMenu():
    #Get RGBA color mode
    s = pygame.Surface((window_width,window_height),pygame.SRCALPHA)
    s.fill((255,255,255,10))
    # Blit buttons
    if setting_combat.scene == "save":
        window.blit(s,(0,0))
        Data1.draw_button()
        Data2.draw_button()
        Data3.draw_button()
        BackBtn.draw_button()
    pygame.display.update()
# Load Data scene function
def LoadMenu():
    #Get RGBA color mode
    s = pygame.Surface((window_width,window_height),pygame.SRCALPHA)
    s.fill((255,255,255,10))
    # Blit buttons
    if setting_combat.scene == "load":
        window.blit(s,(0,0))
        Data1.draw_button()
        Data2.draw_button()
        Data3.draw_button()
        BackBtn.draw_button()
    pygame.display.update()
#Function to show help
def HelpScene():
    howtoplay=font_status_monster.render("How To Play",True,Black)
    enterkey=font_status_player.render("Press Enter to skip scene",True,Black)
    quitkey=font_status_player.render("Press Q to quit game",True,Black)
    zkey=font_status_player.render("Press Z to attack (Dungeon and Boss Fight Only)",True,Black)
    xkey=font_status_player.render("Press X to use potion (Dungeon and Boss Fight Only)",True,Black)
    ckey=font_status_player.render("Press C to flee (Dungeon Only)",True,Black)
    #Get RGBA color mode
    s = pygame.Surface((window_width,window_height),pygame.SRCALPHA)
    s.fill((255,255,255,10))
    # Blit buttons
    if setting_combat.scene == "help":
        window.blit(s,(0,0))
        window.blit(howtoplay,(500,50))
        window.blit(enterkey,(300,150))
        window.blit(quitkey,(300,250))
        window.blit(zkey,(300,350))
        window.blit(xkey,(300,450))
        window.blit(ckey,(300,550))
        BackBtn.draw_button()
    pygame.display.update()
# Player Selection
def PlayerSelection():
    s = pygame.Surface((window_width,window_height),pygame.SRCALPHA)
    s.fill((135,206,235,78))
    window.blit(s,(0,0))
    window.blit(warrior.sprite,(50,0))
    window.blit(rogue.sprite,(450,0))
    window.blit(archer.sprite,(850,0))
    show_my_status(100,450,0,400,warrior)
    show_my_status(500,450,400,400,rogue)
    show_my_status(900,450,800,400,archer)
    # Blit buttons
    if setting_combat.scene == "player" and setting_combat.playerselect:
        Nova_Btn.draw_button()
        Tyler_Btn.draw_button()
        Lyna_Btn.draw_button()
    pygame.display.update()
# Menu Function
def Menu():
    window.blit(MenuBg,(0,0))
    window.blit(Menu_Title,(50,100))
    # Blit buttons
    if setting_combat.bg_scene == "menu" and setting_combat.scene == "menu":
        StartBtn.draw_button()
        QuitBtn.draw_button()
    pygame.display.update()
# function to enter into shop.
def Shop():
    potionvalue=font_status_player.render("100G",True,Yellow)
    atkupvalue=font_status_player.render("300G",True,Yellow)
    hpupvalue=font_status_player.render("300G",True,Yellow)
    critupvalue=font_status_player.render("1000G",True,Yellow)
    potioninfo=font_status_player.render("Potion +1",True,Blue)
    atkupinfo=font_status_player.render("MinDmg +5",True,Blue)
    atkupinfo2=font_status_player.render("MaxDmg +25",True,Blue)
    hpupinfo=font_status_player.render("HP +250",True,Blue)
    critupinfo=font_status_player.render("Crit Hit +0.5X",True,Blue)
    window.blit(inn,(0,0))
    window.blit(merchant,(300,200))
    window.blit(item,(650,275))
    window.blit(attack,(800,275))
    window.blit(shield,(950,275))
    window.blit(skill,(1100,275))
    window.blit(status3,(525,75))
    window.blit(potionvalue,(650,250))
    window.blit(atkupvalue,(800,250))
    window.blit(hpupvalue,(950,250))
    window.blit(critupvalue,(1100,250))
    window.blit(potioninfo,(650,200))
    window.blit(atkupinfo,(800,175))
    window.blit(atkupinfo2,(800,200))
    window.blit(hpupinfo,(950,200))
    window.blit(critupinfo,(1075,200))
    show_my_status(100,50,0,0,p1)
    if setting_combat.scene == "shop":
        BackBtn.draw_button()
        BuyBtn.draw_button()
        BuyBtn2.draw_button()
        BuyBtn3.draw_button()
        BuyBtn4.draw_button()
    pygame.display.update()
# function to enter into inn
def Inn():
    window.blit(inn,(0,0))
    window.blit(merchant,(300,200))
    window.blit(p1.sprite,(900,500))
    show_my_status(100,350,0,300,p1)
    # Blit buttons
    if setting_combat.bg_scene == "inn" and setting_combat.scene == "inn":
        LoadBtn.draw_button()
        SaveBtn.draw_button()
        BattleBtn.draw_button()
        ShopBtn.draw_button()
        HelpBtn.draw_button()
        BackBtn.draw_button()
    pygame.display.update()
# function to show world map background
def WorldMap():
    window.blit(forest_map,(0,0))
    window.blit(cave_map,(400,0))
    window.blit(beach_map,(800,0))
    window.blit(snow_map,(0,400))
    window.blit(volcano_map,(400,400))
    window.blit(dark_castle_map,(800,400))
    # Blit buttons
    if setting_combat.bg_scene == "world" and setting_combat.scene == "world":
        ForestBtn.draw_button()
        CaveBtn.draw_button()
        BeachBtn.draw_button()
        SnowBtn.draw_button()
        VolcanoBtn.draw_button()
        DarkCastleBtn.draw_button()
        BackBtn.draw_button()
    pygame.display.update()
# function to show select stages
def Stage_Selection(bg):
    pygame.mouse.set_visible(True)
    window.blit(bg,(0,0))
    #Checking which area is chosen
    if setting_combat.bg_scene == "forest" and not setting_combat.battle:
        Dungeon.draw_button()
        BossFight.draw_button()
        BackBtn.draw_button()
    elif setting_combat.bg_scene == "cave" and not setting_combat.battle:
        Dungeon.draw_button()
        BossFight.draw_button()
        BackBtn.draw_button()
    elif setting_combat.bg_scene == "beach" and not setting_combat.battle:
        Dungeon.draw_button()
        BossFight.draw_button()
        BackBtn.draw_button()
    elif setting_combat.bg_scene == "snow" and not setting_combat.battle:
        SVDungeon.draw_button()
        SVDungeon2.draw_button()
        SVBossFight.draw_button()
        BackBtn.draw_button()
    elif setting_combat.bg_scene == "volcano" and not setting_combat.battle:
        SVDungeon.draw_button()
        SVDungeon2.draw_button()
        SVBossFight.draw_button()
        BackBtn.draw_button()
    elif setting_combat.bg_scene == "dark castle" and not setting_combat.battle:
        DarkDungeon.draw_button()
        MidBossFight.draw_button()
        DarkDungeon2.draw_button()
        FinalBossFight.draw_button()
        BackBtn.draw_button()
    elif setting_combat.bg_scene == "dark castle 2" and not setting_combat.battle:
        DarkDungeon.draw_button()
        MidBossFight.draw_button()
        DarkDungeon2.draw_button()
        FinalBossFight.draw_button()
        BackBtn.draw_button()
    elif setting_combat.bg_scene == "dark castle 3" and not setting_combat.battle:
        DarkDungeon.draw_button()
        MidBossFight.draw_button()
        DarkDungeon2.draw_button()
        FinalBossFight.draw_button()
        BackBtn.draw_button()
    pygame.display.update()
# function to show win scene
def WinScene():
    #Get RGBA color mode
    s = pygame.Surface((window_width,window_height),pygame.SRCALPHA)
    s.fill((205,205,205,78))
    #All turns become disabled
    setting_combat.myturn = False
    setting_combat.enemyturn = False
    setting_combat.scene="victory"
    # Get Exp and Gold based on monster's level
    GetExp = monster.level*50
    GetGold = (monster.level*25)+(monster.max_health//10)
    #Checking player's job to level up
    if p1.level < 20:
        if p1.job == "Warrior":
            p1.exp += GetExp
            p1.levelup(75,1,5,window)
        elif p1.job == "Rogue":
            p1.exp += GetExp
            p1.levelup(25,3,15,window)
        elif p1.job == "Archer":
            p1.exp += GetExp
            p1.levelup(50,2,10,window)
    elif 20 <= p1.level < 50:
        if p1.job == "Warrior":
            p1.exp += GetExp
            p1.levelup(150,2,10,window)
        elif p1.job == "Rogue":
            p1.exp += GetExp
            p1.levelup(50,4,20,window)
        elif p1.job == "Archer":
            p1.exp += GetExp
            p1.levelup(100,3,15,window)
    elif p1.level == 50:
        p1.exp = 0
        p1.max_exp = 0
    p1.gold += GetGold
    pygame.mixer.music.load("music_and_sfx\\Victory.mid")
    pygame.mixer.music.play()
    victory=font_status_player.render("You Win!",True,Black)
    ExpPoint=font_status_player.render("You get {} EXP".format(GetExp),True,Black)
    GoldPoint=font_status_player.render("You get {} Gold".format(GetGold),True,Black)
    EnterKey=font_status_monster.render("Press Enter to return stage selection",True,Black)
    window.blit(s,(0,0))
    window.blit(victory,(500,300))
    window.blit(ExpPoint,(500,350))
    window.blit(GoldPoint,(500,400))
    window.blit(EnterKey,(400,500))
    pygame.display.update()
# Function to show lose scene
def LoseScene():
    #Get RGBA color mode
    s = pygame.Surface((window_width,window_height),pygame.SRCALPHA)
    s.fill((0,0,0,128))
    #All turns become disabled
    setting_combat.myturn = False
    setting_combat.enemyturn = False
    setting_combat.scene="Defeat"
    Defeat=font_status_player.render("You Lose!",True,Red)
    GameOver=font_status_monster.render("Game Over",True,Red)
    Quit=font_status_monster.render("Press Q to quit game",True,Red)
    pygame.mixer.music.load("music_and_sfx\\GameOver.mid")
    pygame.mixer.music.play()
    window.blit(s,(0,0))
    window.blit(GameOver,(500,300))
    window.blit(Defeat,(500,350))
    window.blit(Quit,(450,500))
    pygame.display.update()
# Function to buy potion.
def BuyPotion():
    #Checking whether gold is enough to buy or not
    if p1.gold >= 100:
        p1.potion += 1
        p1.gold -= 100
        item_can = font_status_player.render("Thank you for buying it.",True,Red)
        window.blit(item_can,(400,600))
        thankyou.set_volume(1)
        thankyou.play()
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        item_cannot=font_status_player.render("Sorry. You do not have enough gold.",True,Red)
        window.blit(item_cannot,(400,600))
        pygame.display.flip()
        pygame.time.wait(1000)
# Function to power up damage
def AttackUp():
    #Checking whether gold is enough to buy or not
    if p1.gold >= 300:
        p1.basedamage += 5
        p1.damage += 25
        p1.gold -= 300
        dmg_up = font_status_player.render("Your damage becomes {}-{}".format(p1.basedamage,p1.damage),True,Red)
        item_can = font_status_player.render("Thank you for buying it.",True,Red)
        window.blit(dmg_up,(400,550))
        window.blit(item_can,(400,600))
        thankyou.set_volume(1)
        thankyou.play()
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        item_cannot=font_status_player.render("Sorry. You do not have enough gold.",True,Red)
        window.blit(item_cannot,(400,600))
        pygame.display.flip()
        pygame.time.wait(1000)
# Function to power up HP
def HPUp():
    #Checking whether gold is enough to buy or not
    if p1.gold >= 300:
        p1.max_health += 250
        p1.health = p1.max_health
        p1.gold -= 300
        hp_up=font_status_player.render("Your HP becomes {}".format(p1.max_health),True,Red)
        item_can = font_status_player.render("Thank you for buying it.",True,Red)
        window.blit(hp_up,(400,550))
        window.blit(item_can,(400,600))
        thankyou.set_volume(1)
        thankyou.play()
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        item_cannot=font_status_player.render("Sorry. You do not have enough gold.",True,Red)
        window.blit(item_cannot,(400,600))
        pygame.display.flip()
        pygame.time.wait(1000)
# Function to power up critical hit
def CritUp():
    #Checking whether gold is enough to buy or not
    if p1.gold >= 1000:
        #Checking whether critical hit has reached its limit or not
        if p1.crit_atk < 8.0:
            p1.crit_atk += 0.5
            p1.gold -= 1000
            crit_up=font_status_player.render("Your Critical Hit becomes {} times".format(p1.crit_atk),True,Red)
            item_can = font_status_player.render("Thank you for buying it.",True,Red)
            window.blit(crit_up,(400,550))
            window.blit(item_can,(400,600))
            thankyou.set_volume(1)
            thankyou.play()
        elif p1.crit_atk >= 8.0:
            full_crit=font_status_player.render("Your Critical Hit has reached its limit.",True,Red)
            window.blit(full_crit,(400,600))
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
        item_cannot=font_status_player.render("Sorry. You do not have enough gold.",True,Red)
        window.blit(item_cannot,(400,600))
        pygame.display.flip()
        pygame.time.wait(1000)
# Attack Command Key
def Attack():
    # turning local variables into global one
    global p1,monster
    # My turn to attack
    if setting_combat.myturn:
        if p1.health > 0:
            # Blit attack rendering
            if not setting_combat.effect:
                mydmg=random.randrange(p1.basedamage,p1.damage)
                # Get critical hit chance
                chance=random.randrange(0,100)
                # Checking whether attack is missed or not
                enemychance=random.randrange(0,100)
                if monster.evade >= enemychance:
                    miss_render=font_status_monster.render("Miss",True,Red)
                    window.blit(slash2,(900,500))
                    window.blit(miss_render,(900,500))
                    # Play attack sound
                    if not setting_combat.soundeffect:
                        monster.health -= 0
                        # to differ sound attack of archer from warrior and rogue
                        if p1.job == "Warrior" or p1.job == "Rogue":
                            slash_sound = pygame.mixer.Sound("music_and_sfx\\sword_slash.wav")
                            slash_sound.set_volume(1)
                            slash_sound.play()
                        elif p1.job == "Archer":
                            bow_sound = pygame.mixer.Sound("music_and_sfx\\bow.wav")
                            bow_sound.set_volume(1)
                            bow_sound.play()
                        setting_combat.soundeffect = True
                    pygame.display.flip()
                    pygame.time.wait(1000)
                else:
                    if p1.crit_chance >= chance:
                        mycrit=mydmg*p1.crit_atk
                        crit_render=font_status_monster.render("Critical Hit!",True,Red)
                        mycrit_render=font_status_monster.render("-{}".format(mycrit),True,Red)
                        window.blit(critical,(900,500))
                        window.blit(slash2,(900,500))
                        window.blit(crit_render,(900,450))
                        window.blit(mycrit_render,(900,500))
                        # Play attack sound
                        if not setting_combat.soundeffect:
                            monster.health -= mycrit
                            # to differ sound attack of archer from warrior and rogue
                            if p1.job == "Warrior" or p1.job == "Rogue":
                                slash_sound = pygame.mixer.Sound("music_and_sfx\\sword_slash.wav")
                                slash_sound.set_volume(1)
                                slash_sound.play()
                            elif p1.job == "Archer":
                                bow_sound = pygame.mixer.Sound("music_and_sfx\\bow.wav")
                                bow_sound.set_volume(1)
                                bow_sound.play()
                            setting_combat.soundeffect = True
                        pygame.display.flip()
                        pygame.time.wait(1000)
                    else:
                        mydmg_render=font_status_monster.render("-{}".format(mydmg),True,Red)
                        window.blit(slash2,(900,500))
                        window.blit(mydmg_render,(900,500))
                        # Play attack sound
                        if not setting_combat.soundeffect:
                            monster.health -= mydmg
                            # to differ sound attack of archer from warrior and rogue
                            if p1.job == "Warrior" or p1.job == "Rogue":
                                slash_sound = pygame.mixer.Sound("music_and_sfx\\sword_slash.wav")
                                slash_sound.set_volume(1)
                                slash_sound.play()
                            elif p1.job == "Archer":
                                bow_sound = pygame.mixer.Sound("music_and_sfx\\bow.wav")
                                bow_sound.set_volume(1)
                                bow_sound.play()
                            setting_combat.soundeffect = True
                        pygame.display.flip()
                        pygame.time.wait(1000)
                setting_combat.effect = True
            # After attacking enemy, it will be changed to enemy turn
            setting_combat.myturn = False
            setting_combat.enemyturn = True
            setting_combat.soundeffect = False
            setting_combat.effect = False
        # Player cannot get turn if his/her HP drops to 0 or less than 0.
        elif p1.health <= 0:
            setting_combat.myturn = False
    # Enemy turn to attack
    if setting_combat.enemyturn:
        if monster.health > 0:
            # Blit attack rendering
            if not setting_combat.effect:
                enemydmg=random.randrange(monster.basedamage,monster.damage)
                chance=random.randrange(0,100)
                # Get evade chance
                if p1.evade >= chance:
                    miss_render=font_status_monster.render("Miss",True,Red)
                    missattack = 0
                    #to differ boss monster attack from normal monster attack
                    if monster == eagle:
                        MonAttack(miss_render,wind,wind_sound,missattack)
                    elif monster == golem:
                        MonAttack(miss_render,earth,earth_sound,missattack)
                    elif monster == leviathan:
                        MonAttack(miss_render,water,water_sound,missattack)
                    elif monster == skeletonKing:
                        MonAttack(miss_render,ice,earth_sound,missattack)
                    elif monster == dragon:
                        MonAttack(miss_render,fire,fire_sound,missattack)
                    elif monster == darkLeviathan:
                        MonAttack(miss_render,ice2,ice_sound,missattack)
                    elif monster == demonKing:
                        MonAttack(miss_render,dark,dark_sound,missattack)
                    else:
                        MonAttack(miss_render,claw,claw_sound,missattack)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                else:
                    enemydmg_render=font_status_monster.render("-{}".format(enemydmg),True,Red)
                    #to differ boss monster attack from normal monster attack
                    if monster == eagle:
                        MonAttack(enemydmg_render,wind,wind_sound,enemydmg)
                    elif monster == golem:
                        MonAttack(enemydmg_render,earth,earth_sound,enemydmg)
                    elif monster == leviathan:
                        MonAttack(enemydmg_render,water,water_sound,enemydmg)
                    elif monster == skeletonKing:
                        MonAttack(enemydmg_render,ice,earth_sound,enemydmg)
                    elif monster == dragon:
                        MonAttack(enemydmg_render,fire,fire_sound,enemydmg)
                    elif monster == darkLeviathan:
                        MonAttack(enemydmg_render,ice2,ice_sound,enemydmg)
                    elif monster == demonKing:
                        MonAttack(enemydmg_render,dark,dark_sound,enemydmg)
                    else:
                        MonAttack(enemydmg_render,claw,claw_sound,enemydmg)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                setting_combat.effect = True
            # After attacking player, enemy cannot attack again until player's turn is done
            setting_combat.enemyturn = False
            setting_combat.soundeffect = False
            setting_combat.effect = False
        # Enemy cannot get turn if its HP drops to 0 or less than that
        elif monster.health <= 0:
            setting_combat.enemyturn = False

# Potion Command Key
def Potion():
    # turning local variables into global one
    global p1,monster
    # My turn to attack
    if setting_combat.myturn:
        #when potion is empty
        if p1.potion == 0:
            potion_empty = font_status_player.render("Potion is Empty",True,Red)
            window.blit(potion_empty,(600,700))
            pygame.display.flip()
            pygame.time.wait(1000)
            setting_combat.effect = False
        #when player's HP is still full
        elif p1.health == p1.max_health:
            HP_full = font_status_player.render("Your HP is still full",True,Red)
            window.blit(HP_full,(600,700))
            pygame.display.flip()
            pygame.time.wait(1000)
            setting_combat.effect = False
        else:
            # Blit heal rendering
            if not setting_combat.effect:
                heal_render=font_status_monster.render("Fully Recovered",True,Red)
                window.blit(healing,(0,500))
                window.blit(heal_render,(0,500))
                # Play heal sound
                if not setting_combat.soundeffect:
                    p1.health = p1.max_health
                    p1.potion -= 1
                    healsound=pygame.mixer.Sound("music_and_sfx\\heal.ogg")
                    healsound.set_volume(1)
                    healsound.play()
                    setting_combat.soundeffect = True
                pygame.display.flip()
                pygame.time.wait(1000)
                setting_combat.effect = True
            # After healing is done, it will be changed into enemy turn
            setting_combat.myturn=False
            setting_combat.enemyturn = True
            setting_combat.soundeffect = False
            setting_combat.effect = False
    # Enemy turn to attack
    if setting_combat.enemyturn:
        if monster.health > 0:
            # Blit attack rendering
            if not setting_combat.effect:
                enemydmg=random.randrange(monster.basedamage,monster.damage)
                chance=random.randrange(0,100)
                # Get evade chance
                if p1.evade >= chance:
                    miss_render=font_status_monster.render("Miss",True,Red)
                    missattack = 0
                    #to differ boss monster attack from normal monster attack
                    if monster == eagle:
                        MonAttack(miss_render,wind,wind_sound,missattack)
                    elif monster == golem:
                        MonAttack(miss_render,earth,earth_sound,missattack)
                    elif monster == leviathan:
                        MonAttack(miss_render,water,water_sound,missattack)
                    elif monster == skeletonKing:
                        MonAttack(miss_render,ice,earth_sound,missattack)
                    elif monster == dragon:
                        MonAttack(miss_render,fire,fire_sound,missattack)
                    elif monster == darkLeviathan:
                        MonAttack(miss_render,ice2,ice_sound,missattack)
                    elif monster == demonKing:
                        MonAttack(miss_render,dark,dark_sound,missattack)
                    else:
                        MonAttack(miss_render,claw,claw_sound,missattack)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                else:
                    enemydmg_render=font_status_monster.render("-{}".format(enemydmg),True,Red)
                    #to differ boss monster attack from normal monster attack
                    if monster == eagle:
                        MonAttack(enemydmg_render,wind,wind_sound,enemydmg)
                    elif monster == golem:
                        MonAttack(enemydmg_render,earth,earth_sound,enemydmg)
                    elif monster == leviathan:
                        MonAttack(enemydmg_render,water,water_sound,enemydmg)
                    elif monster == skeletonKing:
                        MonAttack(enemydmg_render,ice,earth_sound,enemydmg)
                    elif monster == dragon:
                        MonAttack(enemydmg_render,fire,fire_sound,enemydmg)
                    elif monster == darkLeviathan:
                        MonAttack(enemydmg_render,ice2,ice_sound,enemydmg)
                    elif monster == demonKing:
                        MonAttack(enemydmg_render,dark,dark_sound,enemydmg)
                    else:
                        MonAttack(enemydmg_render,claw,claw_sound,enemydmg)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                setting_combat.effect = True
            # After attacking player, enemy cannot attack again until player's turn is done
            setting_combat.enemyturn = False
            setting_combat.soundeffect = False
            setting_combat.effect = False
        # Enemy cannot get turn if its HP drops to 0 or less than that
        elif monster.health <= 0:
            setting_combat.enemyturn = False
# Flee Command Key
def Run():
    #there is no battle after fleeing from dungeon
    setting_combat.battle = False
    setting_combat.myturn = False
    setting_combat.enemyturn = False
    #Depends on which area that player fleeing from specific dungeon
    if setting_combat.scene=="combat" and setting_combat.bg_scene == "forest":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\forest.mp3")
        pygame.mixer.music.play(-1)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "cave":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\cave.mp3")
        pygame.mixer.music.play(-1)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "beach":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\beach.mp3")
        pygame.mixer.music.play(-1)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "snow":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\snow.mp3")
        pygame.mixer.music.play(-1)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "volcano":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\volcano.mp3")
        pygame.mixer.music.play(-1)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "dark castle":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\dark_castle.mp3")
        pygame.mixer.music.play(-1)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "dark castle 2":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\dark_castle.mp3")
        pygame.mixer.music.play(-1)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "dark castle 3":
        setting_combat.scene = "combat_stage"
        pygame.mixer.music.load("music_and_sfx\\dark_castle.mp3")
        pygame.mixer.music.play(-1)
# Commands
def CommandKey():
    window.blit(status2,(400,725))
    window.blit(attack,(450,750))
    window.blit(attackkey,(450,750))
    window.blit(item,(525,750))
    window.blit(itemkey,(525,750))
    window.blit(run,(600,750))
    window.blit(runkey,(600,750))
# Player Objects
warrior = Warrior()
archer=Archer()
rogue=Rogue()
#Forest Monster Objects
goblin1 = Goblin(100,100,1,1,5)
goblin2 = Goblin(110,110,2,2,7)
spider1 = Spider(110,110,2,2,7)
spider2 = Spider(120,120,3,3,9)
spider3= Spider(130,130,4,4,11)
ForestMon=[goblin1,goblin2,spider1,spider2,spider3]
eagle = Eagle(420,420,5,15,39,20)
#Cave Monster Objects
ogre1 = Ogre(180,180,7,7,21)
ogre2 = Ogre(200,200,8,8,25)
ogre3 = Ogre(220,220,9,9,29)
orc1 = Orc(140,140,5,5,13)
orc2 =Orc(160,160,6,6,17)
orc3 =Orc(180,180,7,7,21)
golem = Golem(960,960,10,40,99,25)
CaveMon=[ogre1,ogre2,ogre3,orc1,orc2,orc3]
#Beach Monster Objects
crab1 = Crab(240,240,10,10,33)
crab2 = Crab(280,280,11,11,41)
crab3 = Crab(320,320,12,12,49)
octopus1 = Octopus(320,320,12,12,49)
octopus2 = Octopus(360,360,13,13,57)
octopus3 = Octopus(400,400,14,14,65)
leviathan = Leviathan(2200,2200,15,75,209,30)
BeachMon=[crab1,crab2,crab3,octopus1,octopus2,octopus3]
#Snow Monster Objects
snowWolf1 = SnowWolf(440,440,15,15,73)
snowWolf2 = SnowWolf(520,520,16,16,89)
snowWolf3 = SnowWolf(600,600,17,17,105)
skeleton1 = Skeleton(600,600,17,17,105)
skeleton2 = Skeleton(680,680,18,18,121)
skeleton3=Skeleton(760,760,19,19,137)
yeti1 = Yeti(840,840,20,20,153)
yeti2 = Yeti(1000,1000,21,21,185)
yeti3 = Yeti(1160,1160,22,22,217)
skeletonKing = SkeletonKing(7920,7920,23,115,996,40)
SnowMon=[snowWolf1,snowWolf2,snowWolf3,skeleton1,skeleton2,skeleton3]
SnowMon2=[yeti1,yeti2,yeti3,skeleton2,skeleton3]
#Volcano Monster Objects
cerberus1=Cerberus(1320,1320,23,23,249)
cerberus2=Cerberus(1480,1480,24,24,281)
cerberus3=Cerberus(1640,1640,25,25,313)
phoenix1=Phoenix(1640,1640,25,25,313)
phoenix2=Phoenix(1960,1960,26,26,377)
phoenix3=Phoenix(2280,2280,27,27,441)
wyvern1=Wyvern(2600,2600,28,28,505)
wyvern2=Wyvern(2920,2920,29,29,569)
wyvern3=Wyvern(3240,3240,30,30,633)
dragon=Dragon(23280,23280,31,155,2788,50)
VolcanoMon=[cerberus1,cerberus2,cerberus3,phoenix1,phoenix2,phoenix3]
VolcanoMon2=[phoenix2,phoenix3,wyvern1,wyvern2,wyvern3]
#Dark Castle Monster Objects
darkEagle1=DarkEagle(3880,3880,31,31,697)
darkEagle2=DarkEagle(4520,4520,32,32,761)
darkEagle3=DarkEagle(5160,5160,33,33,825)
ancientGolem1=AncientGolem(5160,5160,33,33,889)
ancientGolem2=AncientGolem(5800,5800,34,34,953)
ancientGolem3=AncientGolem(6460,6460,35,35,1017)
darkLeviathan =DarkLeviathan(42600,42600,36,196,4324,60)
skeletonChamp1=SkeletonChampion(7100,7100,36,36,1081)
skeletonChamp2=SkeletonChampion(7740,7740,37,37,1145)
skeletonChamp3=SkeletonChampion(8380,8380,38,38,1209)
deathDragon1=DeathDragon(8380,8380,38,38,1209)
deathDragon2=DeathDragon(9020,9020,39,39,1273)
deathDragon3=DeathDragon(9660,9660,40,40,1337)
demonKing=DemonKing(61800,61800,41,164,5604,60)
DarkCastleMon=[darkEagle1,darkEagle2,darkEagle3,ancientGolem1,ancientGolem2,ancientGolem3]
DarkCastleMon2=[skeletonChamp1,skeletonChamp2,skeletonChamp3,deathDragon1,deathDragon2,deathDragon3]
# Font Status
font_status_player = pygame.font.SysFont("Verdana",16)
font_status_monster = pygame.font.SysFont("Verdana",20)
font_chapter=pygame.font.SysFont("Verdana",24)
font_chapter_title=pygame.font.SysFont("Verdana",48)
# Monster attack render
claw=pygame.image.load("textures\\claw_scratch.png")
claw=pygame.transform.scale(claw,(300,300))
# Player attack render
slash2=pygame.image.load("textures\\slash2.png")
slash2=pygame.transform.scale(slash2,(300,300))
critical=pygame.image.load("textures\\blood.png")
critical=pygame.transform.scale(critical,(300,300))
#Heal render
healing=pygame.image.load("textures\\healing.png")
# Status graphic
status=pygame.image.load("textures\\scroll.png")
status=pygame.transform.scale(status,(400,400))
status2=pygame.image.load("textures\\scroll2.png")
status2=pygame.transform.scale(status2,(300,100))
status3=pygame.transform.scale(status2,(800,200))
#Command Key Rendering
attack=pygame.image.load("textures\\attack.png")
attack=pygame.transform.scale(attack,(50,50))
attackkey=font_status_player.render("Z",True,Red)
item=pygame.image.load("textures\\item.png")
item=pygame.transform.scale(item,(50,50))
itemkey=font_status_player.render("X",True,Red)
run=pygame.image.load("textures\\flee.png")
runkey=font_status_player.render("C",True,Red)
#Item rendering
skill=pygame.image.load("textures\\dagger.png")
skill=pygame.transform.scale(skill,(50,50))
shield=pygame.image.load("textures\\shield.png")
shield=pygame.transform.scale(shield,(50,50))
#Boss Attack rendering
wind=pygame.image.load("textures\\windattack.png")
water=pygame.image.load("textures\\waterattack.png")
earth=pygame.image.load("textures\\earthattack.png")
fire=pygame.image.load("textures\\fireattack.png")
ice=pygame.image.load("textures\\iceattack.png")
ice2=pygame.image.load("textures\\iceattack2.png")
dark=pygame.image.load("textures\\darkattack.png")
#Monster Attack sound
claw_sound = pygame.mixer.Sound("music_and_sfx\\claw.wav")
#Boss Attack sound
wind_sound=pygame.mixer.Sound("music_and_sfx\\wind.ogg")
water_sound=pygame.mixer.Sound("music_and_sfx\\water.ogg")
earth_sound=pygame.mixer.Sound("music_and_sfx\\stomp.ogg")
ice_sound=pygame.mixer.Sound("music_and_sfx\\freeze.ogg")
fire_sound=pygame.mixer.Sound("music_and_sfx\\fire.ogg")
dark_sound=pygame.mixer.Sound("music_and_sfx\\final_boss.ogg")
#Shopkeeper voices
welcome=pygame.mixer.Sound("music_and_sfx\\shopkeeper.wav")
thankyou=pygame.mixer.Sound("music_and_sfx\\shopkeeper2.wav")
farewell=pygame.mixer.Sound("music_and_sfx\\shopkeeper3.wav")
#Player character voice
warriorsound=pygame.mixer.Sound("music_and_sfx\\warrior.wav")
archersound=pygame.mixer.Sound("music_and_sfx\\archer.wav")
roguesound=pygame.mixer.Sound("music_and_sfx\\rogue.wav")
#Button sound
button=pygame.mixer.Sound("music_and_sfx\\Button.wav")
#Monster attack rendering and sound function
def MonAttack(text,image,file,dmg):
    global p1
    #text is for text rendering
    #image is for image rendering
    #file is for sound
    #dmg is for value of damage
    window.blit(image,(0,500))
    window.blit(text,(300,500))
    # Play attack sound
    if not setting_combat.soundeffect:
        p1.health -= dmg
        file.set_volume(1)
        file.play()
        setting_combat.soundeffect = True
# Function to show my status
def show_my_status(x,y,statx,staty,p1):
    myname = font_status_player.render("Name: {}".format(p1.name),True,WHITE)
    myjob = font_status_player.render("Job: {}".format(p1.job),True,WHITE)
    mylevel=font_status_player.render("Level: {}".format(p1.level),True,WHITE)
    myHP=font_status_player.render("HP: {}/{}".format(p1.health,p1.max_health),True,WHITE)
    myDamage=font_status_player.render("Damage: {}-{}".format(p1.basedamage,p1.damage),True,WHITE)
    exp=font_status_player.render("Exp: {}/{}".format(p1.exp,p1.max_exp),True,WHITE)
    gold=font_status_player.render('Gold: {}G'.format(p1.gold),True,WHITE)
    potion=font_status_player.render('Potion: {}'.format(p1.potion),True,WHITE)
    myevade=font_status_player.render("Evade: {}%".format(p1.evade),True,WHITE)
    mycrit_chance=font_status_player.render("Critical Chance: {}%".format(p1.crit_chance),True,WHITE)
    mycrit_atk=font_status_player.render("Critical attack: {}X".format(p1.crit_atk),True,WHITE)
    # x is for player status x rect
    # y is for player status y rect
    # statx is for status x rect
    # staty is for status y rect
    # p1 is for player object
    window.blit(status,(statx,staty))
    window.blit(myname,(x,y))
    window.blit(myjob,(x,y+25))
    window.blit(mylevel,(x,y+50))
    window.blit(myHP,(x,y+75))
    window.blit(myDamage,(x,y+100))
    window.blit(exp,(x,y+125))
    window.blit(gold,(x,y+150))
    window.blit(potion,(x,y+175))
    window.blit(myevade,(x,y+200))
    window.blit(mycrit_chance,(x,y+225))
    window.blit(mycrit_atk,(x,y+250))
# Function to show enemy status
def show_enemy_status(monster):
    enemyname = font_status_monster.render("Name: {}".format(monster.name),True,Red)
    enemylevel=font_status_monster.render("Level: {}".format(monster.level),True,Red)
    enemyHP=font_status_monster.render("HP: {}/{}".format(monster.health,monster.max_health),True,Red)
    enemyDamage=font_status_monster.render("Damage: {}-{}".format(monster.basedamage,monster.damage),True,Red)
    # monster is for monster object
    window.blit(status,(800,0))
    window.blit(enemyname,(850,50))
    window.blit(enemylevel,(850,75))
    window.blit(enemyHP,(850,100))
    window.blit(enemyDamage,(850,125))
# Function to show combat.
def Combat(bg):
    #battle becomes activated if it is in combat.
    if setting_combat.battle:
        window.blit(bg,(0,0))
        window.blit(p1.sprite,(0,500))
        window.blit(monster.sprite,(900,500))
        show_my_status(50,50,0,0,p1)
        show_enemy_status(monster)
        CommandKey()
        pygame.display.update()
    # Show win scene
    if p1.health > 0 and monster.health <= 0:
        setting_combat.battle = False
        WinScene()
    # Show lose scene
    if p1.health <= 0 and monster.health > 0:
        setting_combat.battle = False
        LoseScene()

# Function to enter into area
def AreaButton():
    # Clicking button to enter into forest stages
    if forest_btnclicked and setting_combat.bg_scene == "world":
        button.set_volume(1)
        button.play()
        # Requirement to open stage
        if setting_combat.chapter1 == 1:
            setting_combat.scene = "combat_stage"
            setting_combat.bg_scene = "forest"
            pygame.mixer.music.load("music_and_sfx\\forest.mp3")
            pygame.mixer.music.play(-1)
        elif setting_combat.chapter1 == 0:
            cannot_enter=font_status_player.render("You have to complete intro first",True,WHITE)
            window.blit(cannot_enter,(400,300))
            pygame.display.flip()
            pygame.time.wait(1000)
    # Clicking button to enter into cave stages
    elif cave_btnclicked and setting_combat.bg_scene == "world":
        button.set_volume(1)
        button.play()
        # Requirement to open stage
        if setting_combat.chapter2 == 1:
            setting_combat.scene = "combat_stage"
            setting_combat.bg_scene = "cave"
            pygame.mixer.music.load("music_and_sfx\\cave.mp3")
            pygame.mixer.music.play(-1)
        elif setting_combat.chapter2 == 0:
            cannot_enter=font_status_player.render("You have to defeat Swift Eagle in Forest",True,WHITE)
            window.blit(cannot_enter,(400,300))
            pygame.display.flip()
            pygame.time.wait(1000)
    # Clicking button to enter into beach stages
    elif beach_btnclicked and setting_combat.bg_scene == "world":
        button.set_volume(1)
        button.play()
        # Requirement to open stage
        if setting_combat.chapter3 == 1:
            setting_combat.scene = "combat_stage"
            setting_combat.bg_scene = "beach"
            pygame.mixer.music.load("music_and_sfx\\beach.mp3")
            pygame.mixer.music.play(-1)
        elif setting_combat.chapter3 == 0:
            cannot_enter=font_status_player.render("You have to defeat Earth Golem in Cave",True,WHITE)
            window.blit(cannot_enter,(400,300))
            pygame.display.flip()
            pygame.time.wait(1000)
    # Clicking button to enter into snow stages
    elif snow_btnclicked and setting_combat.bg_scene == "world":
        button.set_volume(1)
        button.play()
        # Requirement to open stage
        if setting_combat.chapter4 == 1:
            setting_combat.scene = "combat_stage"
            setting_combat.bg_scene = "snow"
            pygame.mixer.music.load("music_and_sfx\\snow.mp3")
            pygame.mixer.music.play(-1)
        elif setting_combat.chapter4 == 0:
            cannot_enter=font_status_player.render("You have to defeat Leviathan in Beach",True,WHITE)
            window.blit(cannot_enter,(400,300))
            pygame.display.flip()
            pygame.time.wait(1000)
    # Clicking button to enter into volcano stages
    elif volcano_btnclicked and setting_combat.bg_scene == "world":
        button.set_volume(1)
        button.play()
        # Requirement to open stage
        if setting_combat.chapter5 == 1:
            setting_combat.scene = "combat_stage"
            setting_combat.bg_scene = "volcano"
            pygame.mixer.music.load("music_and_sfx\\volcano.mp3")
            pygame.mixer.music.play(-1)
        elif setting_combat.chapter5 == 0:
            cannot_enter=font_status_player.render("You have to defeat Skeleton King in Snow",True,WHITE)
            window.blit(cannot_enter,(400,300))
            pygame.display.flip()
            pygame.time.wait(1000)
    # Clicking button to enter into dark castle stages
    elif dark_castle_btnclicked and setting_combat.bg_scene == "world":
        button.set_volume(1)
        button.play()
        # Requirement to open stage
        if setting_combat.chapter6 == 1:
            setting_combat.scene = "combat_stage"
            setting_combat.bg_scene = "dark castle"
            pygame.mixer.music.load("music_and_sfx\\dark_castle.mp3")
            pygame.mixer.music.play(-1)
        elif setting_combat.chapter6 == 0:
            cannot_enter=font_status_player.render("You have to defeat Fire Dragon in Volcano",True,WHITE)
            window.blit(cannot_enter,(400,300))
            pygame.display.flip()
            pygame.time.wait(1000)

#Main Music
pygame.mixer.music.load("music_and_sfx\\menu.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
#Main program
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        #Keys get pressed
        if event.type == pygame.KEYDOWN:
            # Button for Attack
            if event.key == pygame.K_z:
                #Can be activated if player is in battle
                if setting_combat.battle:
                    setting_combat.myturn = True
                    Attack()
            # Button for Item
            elif event.key == pygame.K_x:
                #Can be activated if player is in battle
                if setting_combat.battle:
                    setting_combat.myturn = True
                    Potion()
            # Button for Run
            elif event.key == pygame.K_c:
                #Can be activated if player is in battle
                if setting_combat.battle:
                    setting_combat.myturn = True
                    #Usable only in dungeon
                    if not setting_combat.bossmode:
                        Run()
            # Button to quit game
            elif event.key == pygame.K_q:
                #to quit from lose scene
                if setting_combat.scene == "Defeat":
                    sys.exit()
                #to quit from world,inn, or combat stages
                elif setting_combat.scene == "combat_stage" or setting_combat.scene == "world" or setting_combat.scene == "inn":
                    sys.exit()
            # Button to skip scene
            elif event.key ==  pygame.K_RETURN:
                #If it is in victory scene, it will return to combat stage selection based on specific area
                if setting_combat.scene == "victory" and setting_combat.bg_scene == "forest":
                    # If there is boss fight or not in forest
                    if monster == eagle:
                        setting_combat.scene = "chapter 2"
                        setting_combat.bg_scene = "chapter"
                        setting_combat.bossmode=False
                    else:
                        setting_combat.scene = "combat_stage"
                        setting_combat.bossmode=False
                        pygame.mixer.music.load("music_and_sfx\\forest.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                elif setting_combat.scene == "victory" and setting_combat.bg_scene == "cave":
                    # If there is boss fight or not in cave
                    if monster == golem:
                        setting_combat.scene = "chapter 3"
                        setting_combat.bg_scene = "chapter"
                        setting_combat.bossmode=False
                    else:
                        setting_combat.scene = "combat_stage"
                        setting_combat.bossmode=False
                        pygame.mixer.music.load("music_and_sfx\\cave.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                elif setting_combat.scene == "victory" and setting_combat.bg_scene == "beach":
                    # If there is boss fight or not in beach
                    if monster == leviathan:
                        setting_combat.scene = "chapter 4"
                        setting_combat.bg_scene = "chapter"
                        setting_combat.bossmode=False
                    else:
                        setting_combat.scene = "combat_stage"
                        setting_combat.bossmode=False
                        pygame.mixer.music.load("music_and_sfx\\beach.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                elif setting_combat.scene == "victory" and setting_combat.bg_scene == "snow":
                    # If there is boss fight or not in snow
                    if monster == skeletonKing:
                        setting_combat.scene = "chapter 5"
                        setting_combat.bg_scene = "chapter"
                        setting_combat.bossmode=False
                    else:
                        setting_combat.scene = "combat_stage"
                        setting_combat.bossmode=False
                        pygame.mixer.music.load("music_and_sfx\\snow.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                elif setting_combat.scene == "victory" and setting_combat.bg_scene == "volcano":
                    # If there is boss fight or not in volcano
                    if monster == dragon:
                        setting_combat.scene = "chapter 6"
                        setting_combat.bg_scene = "chapter"
                        setting_combat.bossmode=False
                    else:
                        setting_combat.scene = "combat_stage"
                        setting_combat.bossmode=False
                        pygame.mixer.music.load("music_and_sfx\\volcano.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                elif setting_combat.scene == "victory" and setting_combat.bg_scene == "dark castle":
                    setting_combat.scene = "combat_stage"
                    setting_combat.bossmode=False
                    pygame.mixer.music.load("music_and_sfx\\dark_castle.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                elif setting_combat.scene == "victory" and setting_combat.bg_scene == "dark castle 2":
                    setting_combat.scene = "combat_stage"
                    setting_combat.bg_scene= "dark castle"
                    setting_combat.bossmode=False
                    pygame.mixer.music.load("music_and_sfx\\dark_castle.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # Setting for defeating final boss to ending scene
                elif setting_combat.scene == "victory" and setting_combat.bg_scene == "dark castle 3":
                    setting_combat.scene = "ending"
                    setting_combat.bg_scene = "ending"
                    setting_combat.bossmode=False
                    pygame.mixer.music.load("music_and_sfx\\ending.mid")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # From ending scene to credit
                elif setting_combat.scene == "ending" and setting_combat.bg_scene == "ending":
                    setting_combat.scene = "credit"
                    setting_combat.bg_scene = "credit"
                    pygame.mixer.music.load("music_and_sfx\\credit.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play()
                # From Intro to Chapter 1
                elif setting_combat.scene == "intro" and setting_combat.bg_scene == "intro":
                    setting_combat.scene = "chapter 1"
                    setting_combat.bg_scene = "chapter"
                # From Chapter 1 to Inn
                elif setting_combat.scene == "chapter 1" and setting_combat.bg_scene == "chapter":
                    pygame.mouse.set_visible(True)
                    setting_combat.chapter1=1
                    setting_combat.scene = "inn"
                    setting_combat.bg_scene = "inn"
                    pygame.mixer.music.load("music_and_sfx\\world.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # From Chapter 2 to World Map
                elif setting_combat.scene == "chapter 2" and setting_combat.bg_scene == "chapter":
                    pygame.mouse.set_visible(True)
                    setting_combat.chapter2=1
                    setting_combat.scene = "world"
                    setting_combat.bg_scene = "world"
                    pygame.mixer.music.load("music_and_sfx\\world.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # From Chapter 3 to World Map
                elif setting_combat.scene == "chapter 3" and setting_combat.bg_scene == "chapter":
                    pygame.mouse.set_visible(True)
                    setting_combat.chapter3=1
                    setting_combat.scene = "world"
                    setting_combat.bg_scene = "world"
                    pygame.mixer.music.load("music_and_sfx\\world.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # From Chapter 4 to World Map
                elif setting_combat.scene == "chapter 4" and setting_combat.bg_scene == "chapter":
                    pygame.mouse.set_visible(True)
                    setting_combat.chapter4=1
                    setting_combat.scene = "world"
                    setting_combat.bg_scene = "world"
                    pygame.mixer.music.load("music_and_sfx\\world.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # From Chapter 5 to World Map
                elif setting_combat.scene == "chapter 5" and setting_combat.bg_scene == "chapter":
                    pygame.mouse.set_visible(True)
                    setting_combat.chapter5=1
                    setting_combat.scene = "world"
                    setting_combat.bg_scene = "world"
                    pygame.mixer.music.load("music_and_sfx\\world.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # From Chapter 6 to World Map
                elif setting_combat.scene == "chapter 6" and setting_combat.bg_scene == "chapter":
                    pygame.mouse.set_visible(True)
                    setting_combat.chapter6=1
                    setting_combat.scene = "world"
                    setting_combat.bg_scene = "world"
                    pygame.mixer.music.load("music_and_sfx\\world.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                # From credit to menu and reset all progresses
                elif setting_combat.scene == "credit" and setting_combat.bg_scene == "credit":
                    setting_combat.bg_scene = "menu"
                    setting_combat.scene = "menu"
                    setting_combat.chapter1=0
                    setting_combat.chapter2=0
                    setting_combat.chapter3=0
                    setting_combat.chapter4=0
                    setting_combat.chapter5=0
                    setting_combat.chapter6=0
                    setting_combat.midboss=1
                    setting_combat.finalboss=0
                    setting_combat.playerselect=True
                    eagle.health=eagle.max_health
                    golem.health=golem.max_health
                    leviathan.health=leviathan.max_health
                    skeletonKing.health=skeletonKing.max_health
                    dragon.health=dragon.max_health
                    darkLeviathan.health=darkLeviathan.max_health
                    demonKing.health=demonKing.max_health
                    pygame.mouse.set_visible(True)
                    if p1.job == "Warrior":
                        warrior.max_health = 150
                        warrior.health = 150
                        warrior.level = 1
                        warrior.exp = 0
                        warrior.max_exp = 100
                        warrior.crit_atk = 2.0
                        warrior.potion = 1
                        warrior.gold = 0
                        warrior.basedamage = 2
                        warrior.damage = 10
                    elif p1.job == "Rogue":
                        rogue.max_health = 75
                        rogue.health = 75
                        rogue.level = 1
                        rogue.exp = 0
                        rogue.max_exp = 100
                        rogue.crit_atk = 2.0
                        rogue.potion = 1
                        rogue.gold = 0
                        rogue.basedamage = 4
                        rogue.damage = 20
                    elif p1.job == "Archer":
                        archer.max_health = 100
                        archer.health = 100
                        archer.level = 1
                        archer.exp = 0
                        archer.max_exp = 100
                        archer.crit_atk = 2.0
                        archer.potion = 1
                        archer.gold = 0
                        archer.basedamage = 3
                        archer.damage = 15
                    pygame.mixer.music.load("music_and_sfx\\menu.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
        # Mouse gets pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Get rect of mouse pointer
            mouse_x,mouse_y = pygame.mouse.get_pos()
            #Collision between buttons and mouse pointer
            # Combat Stage
            dg_buttonclicked = Dungeon.rect.collidepoint(mouse_x,mouse_y)
            boss_buttonclicked = BossFight.rect.collidepoint(mouse_x,mouse_y)
            # Combat Stage for Snow and Volcano Stage
            sv_dg_btnclicked= SVDungeon.rect.collidepoint(mouse_x,mouse_y)
            sv_dg2_btnclicked=SVDungeon2.rect.collidepoint(mouse_x,mouse_y)
            sv_boss_btnclicked=SVBossFight.rect.collidepoint(mouse_x,mouse_y)
            # Combat Stage for Dark Castle
            dark_dg_btnclicked=DarkDungeon.rect.collidepoint(mouse_x,mouse_y)
            dark_dg2_btnclicked=DarkDungeon2.rect.collidepoint(mouse_x,mouse_y)
            mid_boss_btnclicked=MidBossFight.rect.collidepoint(mouse_x,mouse_y)
            final_boss_btnclicked=FinalBossFight.rect.collidepoint(mouse_x,mouse_y)
            # Return
            back_btnclicked = BackBtn.rect.collidepoint(mouse_x,mouse_y)
            # Inn
            battle_btnclicked= BattleBtn.rect.collidepoint(mouse_x,mouse_y)
            shop_btnclicked=ShopBtn.rect.collidepoint(mouse_x,mouse_y)
            save_btnclicked=SaveBtn.rect.collidepoint(mouse_x,mouse_y)
            load_btnclicked=LoadBtn.rect.collidepoint(mouse_x,mouse_y)
            help_btnclicked=HelpBtn.rect.collidepoint(mouse_x,mouse_y)
            # Save and Load buttons
            data1_btnclicked = Data1.rect.collidepoint(mouse_x,mouse_y)
            data2_btnclicked= Data2.rect.collidepoint(mouse_x,mouse_y)
            data3_btnclicked = Data3.rect.collidepoint(mouse_x,mouse_y)
            # Shop
            buy_btnclicked=BuyBtn.rect.collidepoint(mouse_x,mouse_y)
            buy2_btnclicked=BuyBtn2.rect.collidepoint(mouse_x,mouse_y)
            buy3_btnclicked=BuyBtn3.rect.collidepoint(mouse_x,mouse_y)
            buy4_btnclicked=BuyBtn4.rect.collidepoint(mouse_x,mouse_y)
            # Menu
            start_btnclicked=StartBtn.rect.collidepoint(mouse_x,mouse_y)
            quit_btnclicked=QuitBtn.rect.collidepoint(mouse_x,mouse_y)
            # Player Selection
            Nova_btnclicked=Nova_Btn.rect.collidepoint(mouse_x,mouse_y)
            Tyler_btnclicked=Tyler_Btn.rect.collidepoint(mouse_x,mouse_y)
            Lyna_btnclicked=Lyna_Btn.rect.collidepoint(mouse_x,mouse_y)
            # World Map
            forest_btnclicked = ForestBtn.rect.collidepoint(mouse_x,mouse_y)
            cave_btnclicked = CaveBtn.rect.collidepoint(mouse_x,mouse_y)
            beach_btnclicked = BeachBtn.rect.collidepoint(mouse_x,mouse_y)
            snow_btnclicked = SnowBtn.rect.collidepoint(mouse_x,mouse_y)
            volcano_btnclicked = VolcanoBtn.rect.collidepoint(mouse_x,mouse_y)
            dark_castle_btnclicked = DarkCastleBtn.rect.collidepoint(mouse_x,mouse_y)
            # clicking buttons in forest background
            if dg_buttonclicked and not setting_combat.battle and setting_combat.bg_scene == "forest":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(ForestMon)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\battle.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if boss_buttonclicked and not setting_combat.battle and setting_combat.bg_scene == "forest":
                monster=eagle
                button.set_volume(1)
                button.play()
                #Checking if boss monster has been defeated or not
                if monster.health > 0:
                    setting_combat.scene = "combat"
                    setting_combat.battle = True
                    setting_combat.bossmode = True
                    pygame.mixer.music.load("music_and_sfx\\boss_battle.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif monster.health <= 0:
                    done=font_status_player.render("You have defeated Swift Eagle",True,Red)
                    window.blit(done,(500,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            # clicking buttons in cave background
            if dg_buttonclicked and not setting_combat.battle and setting_combat.bg_scene == "cave":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(CaveMon)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\battle.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if boss_buttonclicked and not setting_combat.battle and setting_combat.bg_scene == "cave":
                monster=golem
                button.set_volume(1)
                button.play()
                #Checking if boss monster has been defeated or not
                if monster.health > 0:
                    setting_combat.scene = "combat"
                    setting_combat.battle = True
                    setting_combat.bossmode = True
                    pygame.mixer.music.load("music_and_sfx\\boss_battle.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif monster.health <= 0:
                    done=font_status_player.render("You have defeated Earth Golem",True,Red)
                    window.blit(done,(500,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            #clicking buttons in beach background
            if dg_buttonclicked and not setting_combat.battle and setting_combat.bg_scene == "beach":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(BeachMon)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\battle.mp3")
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if boss_buttonclicked and not setting_combat.battle and setting_combat.bg_scene == "beach":
                monster=leviathan
                button.set_volume(1)
                button.play()
                #Checking if boss monster has been defeated or not
                if monster.health > 0:
                    setting_combat.scene = "combat"
                    setting_combat.battle = True
                    setting_combat.bossmode = True
                    pygame.mixer.music.load("music_and_sfx\\boss_battle.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif monster.health <= 0:
                    done=font_status_player.render("You have defeated Leviathan",True,Red)
                    window.blit(done,(500,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            #clicking buttons in snow background
            if sv_dg_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "snow":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(SnowMon)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\battle.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if sv_dg2_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "snow":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(SnowMon2)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\battle.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if sv_boss_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "snow":
                monster=skeletonKing
                button.set_volume(1)
                button.play()
                #Checking if boss monster has been defeated or not
                if monster.health > 0:
                    setting_combat.scene = "combat"
                    setting_combat.battle = True
                    setting_combat.bossmode = True
                    pygame.mixer.music.load("music_and_sfx\\boss_battle.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif monster.health <= 0:
                    done=font_status_player.render("You have defeated Skeleton King",True,Red)
                    window.blit(done,(500,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            #clicking buttons in volcano background
            if sv_dg_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "volcano":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(VolcanoMon)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\battle.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if sv_dg2_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "volcano":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(VolcanoMon2)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\battle.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if sv_boss_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "volcano":
                monster=dragon
                button.set_volume(1)
                button.play()
                #Checking if boss monster has been defeated or not
                if monster.health > 0:
                    setting_combat.scene = "combat"
                    setting_combat.battle = True
                    setting_combat.bossmode = True
                    pygame.mixer.music.load("music_and_sfx\\boss_battle.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif monster.health <= 0:
                    done=font_status_player.render("You have defeated Fire Dragon",True,Red)
                    window.blit(done,(500,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            #clicking buttons in dark castle background
            if dark_dg_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "dark castle":
                setting_combat.scene = "combat"
                setting_combat.battle = True
                monster=random.choice(DarkCastleMon)
                #Dungeon random looping
                monster.health = monster.max_health
                button.set_volume(1)
                button.play()
                pygame.mixer.music.load("music_and_sfx\\dark_castle_battle.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                pygame.mouse.set_visible(False)
            if dark_dg2_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "dark castle":
                button.set_volume(1)
                button.play()
                # Requirement for entering dark castle dungeon 2
                if not setting_combat.midboss:
                    setting_combat.scene = "combat"
                    setting_combat.bg_scene = "dark castle 2"
                    setting_combat.battle = True
                    monster=random.choice(DarkCastleMon2)
                    #Dungeon random looping
                    monster.health = monster.max_health
                    pygame.mixer.music.load("music_and_sfx\\dark_castle_battle2.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif setting_combat.midboss:
                    cannot_enter=font_status_player.render("You have to defeat Dark Leviathan first",True,WHITE)
                    window.blit(cannot_enter,(500,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            if mid_boss_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "dark castle":
                monster=darkLeviathan
                button.set_volume(1)
                button.play()
                #Checking if boss monster has been defeated or not
                if monster.health > 0:
                    setting_combat.scene = "combat"
                    setting_combat.bg_scene = "dark castle 2"
                    setting_combat.finalboss=1
                    setting_combat.midboss=0
                    setting_combat.battle = True
                    setting_combat.bossmode = True
                    pygame.mixer.music.load("music_and_sfx\\mid_boss.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif monster.health <= 0:
                    done=font_status_player.render("You have defeated Dark Leviathan",True,Red)
                    window.blit(done,(400,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            if final_boss_btnclicked and not setting_combat.battle and setting_combat.bg_scene == "dark castle":
                button.set_volume(1)
                button.play()
                # Requirement for final boss
                if setting_combat.finalboss == 1:
                    setting_combat.scene = "combat"
                    setting_combat.bg_scene = "dark castle 3"
                    setting_combat.battle = True
                    setting_combat.bossmode = True
                    monster=demonKing
                    pygame.mixer.music.load("music_and_sfx\\final_boss.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    pygame.mouse.set_visible(False)
                elif setting_combat.finalboss == 0:
                    cannot_enter=font_status_player.render("You have to defeat Dark Leviathan first",True,WHITE)
                    window.blit(cannot_enter,(400,700))
                    pygame.display.flip()
                    pygame.time.wait(1000)
            #Button from combat stages to world
            if back_btnclicked and not setting_combat.bg_scene == "world" and setting_combat.scene == "combat_stage":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "world"
                setting_combat.bg_scene = "world"
                pygame.mixer.music.load("music_and_sfx\\world.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
            #Button from world to inn
            elif back_btnclicked and setting_combat.bg_scene == "world" and setting_combat.scene == "world":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "inn"
                setting_combat.bg_scene = "inn"
                #Player's HP becomes fully recovered after returning to inn
                p1.health = p1.max_health
            #Button from shop to inn
            elif back_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "shop":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "inn"
                setting_combat.bg_scene = "inn"
                farewell.set_volume(1)
                farewell.play()
                pygame.time.wait(1000)
            #Button from inn to menu
            elif back_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "inn":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "menu"
                setting_combat.bg_scene = "menu"
                pygame.mixer.music.load("music_and_sfx\\menu.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
            #Button from save to inn
            elif back_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "save":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "inn"
                setting_combat.bg_scene = "inn"
            #Button from load to inn
            elif back_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "load":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "inn"
                setting_combat.bg_scene = "inn"
            #Button from help to inn
            elif back_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "help":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "inn"
                setting_combat.bg_scene = "inn"
            # Inn Buttons
            # From inn to world
            if battle_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "inn":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "world"
                setting_combat.bg_scene = "world"
            # From inn to shop
            if shop_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "inn":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "shop"
                welcome.set_volume(1)
                welcome.play()
            # From inn to save
            if save_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "inn":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "save"
            # From inn to load
            if load_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "inn":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "load"
            # From inn to help
            if help_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "inn":
                button.set_volume(1)
                button.play()
                setting_combat.scene = "help"
            # Data 1
            # Save Data
            if data1_btnclicked and setting_combat.scene == "save" and setting_combat.bg_scene == "inn":
                button.set_volume(1)
                button.play()
                SaveData(p1,"savedata.txt")
                save_success=font_status_player.render("Data has been saved successfully!",True,Red)
                window.blit(save_success,(400,600))
                pygame.display.flip()
                pygame.time.wait(1000)
                setting_combat.scene = "inn"
            # Load Data
            elif data1_btnclicked and setting_combat.scene == "load" and setting_combat.bg_scene == "inn":
                button.set_volume(1)
                button.play()
                LoadData("savedata.txt")
                load_success=font_status_player.render("Data has been loaded successfully!",True,Red)
                window.blit(load_success,(400,600))
                pygame.display.flip()
                pygame.time.wait(1000)
                setting_combat.scene = "inn"
            # Data 2
            # Save Data
            if data2_btnclicked and setting_combat.scene == "save" and setting_combat.bg_scene == "inn":
                button.set_volume(1)
                button.play()
                SaveData(p1,"savedata2.txt")
                save_success=font_status_player.render("Data has been saved successfully!",True,Red)
                window.blit(save_success,(400,600))
                pygame.display.flip()
                pygame.time.wait(1000)
                setting_combat.scene = "inn"
            # Load Data
            elif data2_btnclicked and setting_combat.scene == "load" and setting_combat.bg_scene == "inn":
                button.set_volume(1)
                button.play()
                LoadData("savedata2.txt")
                load_success=font_status_player.render("Data has been loaded successfully!",True,Red)
                window.blit(load_success,(400,600))
                pygame.display.flip()
                pygame.time.wait(1000)
                setting_combat.scene = "inn"
            # Data 3
            # Save Data
            if data3_btnclicked and setting_combat.scene == "save" and setting_combat.bg_scene == "inn":
                button.set_volume(1)
                button.play()
                SaveData(p1,"savedata3.txt")
                save_success=font_status_player.render("Data has been saved successfully!",True,Red)
                window.blit(save_success,(400,600))
                pygame.display.flip()
                pygame.time.wait(1000)
                setting_combat.scene = "inn"
            # Load Data
            elif data3_btnclicked and setting_combat.scene == "load" and setting_combat.bg_scene == "inn":
                button.set_volume(1)
                button.play()
                LoadData("savedata3.txt")
                load_success=font_status_player.render("Data has been loaded successfully!",True,Red)
                window.blit(load_success,(400,600))
                pygame.display.flip()
                pygame.time.wait(1000)
                setting_combat.scene = "inn"
            # Menu button clicking
            # Start game
            if start_btnclicked and setting_combat.bg_scene == "menu" and setting_combat.scene == "menu":
                button.set_volume(1)
                button.play()
                #Checking if player has been selected or not
                if setting_combat.playerselect:
                    setting_combat.scene = "player"
                if not setting_combat.playerselect:
                    setting_combat.scene = "inn"
                    setting_combat.bg_scene = "inn"
                    pygame.mixer.music.load("music_and_sfx\\world.mp3")
                    pygame.mixer.music.play(-1)
            # Quit game
            if quit_btnclicked and setting_combat.bg_scene == "menu" and setting_combat.scene == "menu":
                button.set_volume(1)
                button.play()
                pygame.time.wait(500)
                sys.exit()
            # Player Selection
            # Choose warrior
            if Nova_btnclicked and setting_combat.bg_scene == "menu" and setting_combat.scene == "player":
                button.set_volume(1)
                button.play()
                p1 = warrior
                setting_combat.bg_scene = "intro"
                setting_combat.scene = "intro"
                warriorsound.set_volume(1)
                warriorsound.play()
                #wait for player voice is done
                pygame.time.wait(1000)
                pygame.mixer.music.load("music_and_sfx\\intro.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                setting_combat.playerselect = False
                pygame.mouse.set_visible(False)
            # Choose rogue
            if Tyler_btnclicked and setting_combat.bg_scene == "menu" and setting_combat.scene == "player":
                button.set_volume(1)
                button.play()
                p1 = rogue
                setting_combat.bg_scene = "intro"
                setting_combat.scene = "intro"
                roguesound.set_volume(1)
                roguesound.play()
                #wait for player voice is done
                pygame.time.wait(1000)
                pygame.mixer.music.load("music_and_sfx\\intro.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                setting_combat.playerselect = False
                pygame.mouse.set_visible(False)
            # Choose archer
            if Lyna_btnclicked and setting_combat.bg_scene == "menu" and setting_combat.scene == "player":
                button.set_volume(1)
                button.play()
                p1 = archer
                setting_combat.bg_scene = "intro"
                setting_combat.scene = "intro"
                archersound.set_volume(1)
                archersound.play()
                #wait for player voice is done
                pygame.time.wait(2000)
                pygame.mixer.music.load("music_and_sfx\\intro.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                setting_combat.playerselect = False
                pygame.mouse.set_visible(False)
            # Buying items
            # Buy potion
            if buy_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "shop":
                button.set_volume(1)
                button.play()
                BuyPotion()
            # Buy attack up
            elif buy2_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "shop":
                button.set_volume(1)
                button.play()
                AttackUp()
            # Buy HP up
            elif buy3_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "shop":
                button.set_volume(1)
                button.play()
                HPUp()
            # Buy Critical Hit up
            elif buy4_btnclicked and setting_combat.bg_scene == "inn" and setting_combat.scene == "shop":
                button.set_volume(1)
                button.play()
                CritUp()
            AreaButton()


    # Forest Stages
    if setting_combat.scene == "combat" and setting_combat.bg_scene == "forest":
        Combat(forest_bg)
    if setting_combat.scene == "combat_stage" and setting_combat.bg_scene == "forest":
        setting_combat.battle = False
        Stage_Selection(forest_bg)
    # Cave Stages
    if setting_combat.scene == "combat" and setting_combat.bg_scene == "cave":
        Combat(cave_bg)
    if setting_combat.scene == "combat_stage" and setting_combat.bg_scene == "cave":
        setting_combat.battle = False
        Stage_Selection(cave_bg)
    # Beach Stages
    if setting_combat.scene == "combat" and setting_combat.bg_scene == "beach":
        Combat(beach_bg)
    if setting_combat.scene == "combat_stage" and setting_combat.bg_scene == "beach":
        setting_combat.battle = False
        Stage_Selection(beach_bg)
    # Snow Stages
    if setting_combat.scene == "combat" and setting_combat.bg_scene == "snow":
        Combat(snow_bg)
    if setting_combat.scene == "combat_stage" and setting_combat.bg_scene == "snow":
        setting_combat.battle = False
        Stage_Selection(snow_bg)
    # Volcano Stages
    if setting_combat.scene == "combat" and setting_combat.bg_scene == "volcano":
        Combat(volcano_bg)
    if setting_combat.scene == "combat_stage" and setting_combat.bg_scene == "volcano":
        setting_combat.battle = False
        Stage_Selection(volcano_bg)
    # Dark Castle Stages
    if setting_combat.scene == "combat" and setting_combat.bg_scene == "dark castle":
        Combat(dark_castle_bg)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "dark castle 2":
        Combat(dark_castle_bg2)
    elif setting_combat.scene == "combat" and setting_combat.bg_scene == "dark castle 3":
        Combat(dark_castle_bg3)
    if setting_combat.scene == "combat_stage" and setting_combat.bg_scene == "dark castle":
        setting_combat.battle = False
        Stage_Selection(dark_castle_bg)
    # World Map
    if setting_combat.scene == "world" and setting_combat.bg_scene == "world":
        WorldMap()
    # Inn
    if setting_combat.scene == "inn" and setting_combat.bg_scene == "inn":
        Inn()
    #Shop
    elif setting_combat.scene == "shop" and setting_combat.bg_scene == "inn":
        Shop()
    #Save and Load Menu
    #Prevent overloading
    if setting_combat.scene == "save" and setting_combat.bg_scene =="inn":
        SaveMenu()
    elif setting_combat.scene == "load" and setting_combat.bg_scene == "inn":
        LoadMenu()
    #Help Scene
    if setting_combat.scene == "help" and setting_combat.bg_scene == "inn":
        HelpScene()
    #Menu
    if setting_combat.scene == "menu" and setting_combat.bg_scene == "menu":
        Menu()
    #Player Selection
    elif setting_combat.scene == "player" and setting_combat.bg_scene == "menu":
        PlayerSelection()
    #Intro Story
    if setting_combat.scene == "intro" and setting_combat.bg_scene == "intro":
        Intro()
    #Ending Story
    if setting_combat.scene == "ending" and setting_combat.bg_scene == "ending":
        Ending()
    #Credit
    if setting_combat.scene == "credit" and setting_combat.bg_scene == "credit":
        Credit()
    #Chapter story
    if setting_combat.scene == "chapter 1" and setting_combat.bg_scene == "chapter":
        Chapter(setting_combat.chapter1_text,setting_combat.chapter1_title,250)
    elif setting_combat.scene == "chapter 2" and setting_combat.bg_scene == "chapter":
        Chapter(setting_combat.chapter2_text,setting_combat.chapter2_title,250)
    elif setting_combat.scene == "chapter 3" and setting_combat.bg_scene == "chapter":
        Chapter(setting_combat.chapter3_text,setting_combat.chapter3_title,300)
    elif setting_combat.scene == "chapter 4" and setting_combat.bg_scene == "chapter":
        Chapter(setting_combat.chapter4_text,setting_combat.chapter4_title,250)
    elif setting_combat.scene == "chapter 5" and setting_combat.bg_scene == "chapter":
        Chapter(setting_combat.chapter5_text,setting_combat.chapter5_title,350)
    elif setting_combat.scene == "chapter 6" and setting_combat.bg_scene == "chapter":
        Chapter(setting_combat.chapter6_text,setting_combat.chapter6_title,350)
#Maintain program
pygame.quit()
'''References: Livander Surya and Eris (attack and item effects)'''
'''Graphic references: attack.png (Square Enix), Dark_Eagle_combat.png, Skeleton_king_combat.png (BIizzard), merchant.png (Gravity), cerberus_combat.png (Gumi)'''
'''Music and Sound references: -battle.mp3,beach.mp3,boss_battle.mp3,credit.mp3,forest.mp3,intro.mp3,menu.mp3,snow.mp3,world.mp3 (Bandai Namco),
                               -dark_castle.mp3,dark_castle_battle.mp3,dark_castle_battle2.mp3,final_boss.mp3,mid_boss.mp3,volcano.mp3,cave.mp3 (Falcom),
                               -bow.wav, claw.wav,Button.wav,sword_slash.wav (soundbible.com),
                               -ending.mid,final_boss.ogg,freeze.ogg,fire.ogg,GameOver.mid,heal.ogg,stomp.ogg,water.ogg,wind.ogg,Victory,mid (opengameart.org),
                               -shopkeeper.wav,shopkeeper2.wav,shopkeeper3.wav,warrior.wav,archer.wav,rogue.wav (Freem.ne.jp)'''
