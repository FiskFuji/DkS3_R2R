################################################################################
#                                                                              # 
#                       DARK SOULS 3 - RAGS TO RICHES                          # 
#                               DEVELOPED BY:                                  # 
#                              KIRK C. WORLEY                                  # 
#                                (c) 2016.                                     # 
#                           Licensed under GPL 3.0                             # 
#                For more information about this license, see:                 # 
#               http://www.gnu.org/licenses/quick-guide-gplv3.html             # 
#                                                                              #
################################################################################
#                            SPECIAL THANKS:                                   # 
#                    KYLE P. WORLEY, TYLER J. COCHRAN                          #
################################################################################
#                                                                              # 
#                   Welcome to Dark Souls 3 Rags to Riches!                    # 
#   You are currently viewing the source code to DkS 3 Rags to Riches. This    # 
#   code was made open source by GitHub and Cloud9 IDE. This program is        # 
#   written in Python 2.7.9 with the use of PyGame 1.7.9.                      # 
#   Check out the official pages below:                                        # 
#   ===================================                                        # 
#   Python:                                                                    # 
#   https://www.python.org/                                                    # 
#   ===================================                                        # 
#   PyGame 1.7.9:                                                              # 
#   http://www.pygame.org/hifi.html                                            # 
#   ===================================                                        # 
#                                                                              # 
#   This code is licensed under the General Public License 3.0. For more       # 
#   information about this license, please see the following link:             # 
#   http://www.gnu.org/licenses/quick-guide-gplv3.html                         # 
#                                                                              # 
#   Feel free to tweet serious (or not serious) questions/feedback to me       # 
#   at the following twitter handle:                                           # 
#   ==================================                                         # 
#   Twitter Handle:                                                            # 
#   @Kirk_CW                                                                   # 
#   https://twitter.com/Kirk_CW                                                # 
#   ==================================                                         #
#                                                                              # 
#   Special thanks to DreadedCone, Oroboro, and LobosJR for inspiring me.      #
#   ==================================                                         # 
#   Dreaded Cone: https://www.youtube.com/user/DreadedCone/featured            # 
#   ==================================                                         # 
#   Oroboro: https://www.youtube.com/user/OroboroTheNinja                      # 
#   ==================================                                         # 
#   Lobos Jr: https://www.youtube.com/user/LobosjrGaming                       #
#                                                                              # 
#   As a side note to any programmer viewing this: I have purposefully         # 
#   chosen to not take an object-oriented style of programming while making    # 
#   this. While creating object would be beneficial here, I am leaving that    # 
#   up to those who wish to alter the code for their own purposes.             # 
#                                                                              #
################################################################################
#==============================================================================#
#                   BEGIN PROGRAM                                              # 
#==============================================================================#            
#                   BEGIN IMPORTS                                              # 
#==============================================================================#
#!/usr/bin/env python
import pygame as dks
import webbrowser as wb
import sys
import random as rnd

rnd.seed(None)
#==============================================================================#
#                   INITIALIZE ELEMENTS                                        # 
#==============================================================================#
dks.mixer.pre_init(44200, -16, 8, 1024)
dks.mixer.init()

dks.init()
dks.font.init()

#Width, Height of Screen in pixels. If this is changed, the background image
#will also need to be rescaled to fit the new sizes. <<images/bkgrnd.png>>
#This will mean the loot-images will be off place as well. Be careful when
#adjusting these values.
WIDTH = 950
HEIGHT = 600

dks.display.set_caption("Rags to Riches")

ICON        =   dks.image.load("images/system/icon.png")
dks.display.set_icon(ICON)

screen      =   dks.display.set_mode((WIDTH, HEIGHT))
CL          =   dks.time.Clock()

RUNNING     =   True

LOOT_CLICK1 =   False;  LOOT_CLICK2 =   False;  LOOT_CLICK3 =   False
LOOT_CLICK4 =   False;  LOOT_CLICK5 =   False;  LOOT_CLICK6 =   False
LOOT_1ON    =   False;  LOOT_2ON    =   False;  LOOT_3ON    =   False
LOOT_4ON    =   False;  LOOT_5ON    =   False;  LOOT_6ON    =   False

currentLoot1 =  None;   currentLoot2 =  None;   currentLoot3 =  None;
currentLoot4 =  None;   currentLoot5 =  None;   currentLoot6 =  None;

currentRoll =   ""
lootRoll_ON =   False

INTRO       =   1

FONT        =   "fonts/OptimusPrinceps.ttf"
FNT         =   dks.font.Font(FONT, 30)

arrow =  ("          x             ",
          "         X.X            ",
          "        X...X           ",
          "       X..X..X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "  X.X  X.X.X.X  X.X     ",
          "  X.XXXX.....XXXX.X     ",
          "   X.............X      ",
          "    X...X...X...X       ",
          "        X..XX           ",
          "        X.X.X           ",
          "        X...X           ",
          "        X...X           ",
          "         X.X            ",
          "                        ",
          "                        ",
          "                        ")

start_fx        =   dks.mixer.Sound("sounds/start.wav"); start_fx.set_volume(0.25)
mtheme          =   dks.mixer.Sound("sounds/MainMenu_Theme.wav"); mtheme.set_volume(0.08)
select_fx       =   dks.mixer.Sound("sounds/$draw.wav"); select_fx.set_volume(0.75)
IN_1            =   dks.image.load("images/system/intro1.png").convert()
IN_1ON          =   dks.image.load("images/system/intro1_1.png").convert()
IN_1T           =   dks.image.load("images/system/intro1_2.png").convert()
IN_1G           =   dks.image.load("images/system/intro1_3.png").convert()
IN_2            =   dks.image.load("images/system/intro2.png").convert()
IN_2ON          =   dks.image.load("images/system/intro2_1.png").convert()
IN_3            =   dks.image.load("images/system/intro3.png").convert()
IN_3ON          =   dks.image.load("images/system/intro3_1.png").convert()
MN_MAIN         =   dks.image.load("images/system/main1.png").convert()
MN_L            =   dks.image.load("images/system/main1_L.png").convert()
MN_R            =   dks.image.load("images/system/main1_R.png").convert()
CMN_COIN        =   dks.image.load("images/system/cmn_coin.png").convert_alpha()
RARE_COIN       =   dks.image.load("images/system/rare_coin.png").convert_alpha()
ULTRA_COIN      =   dks.image.load("images/system/ultra_coin.png").convert_alpha()
MISF_COIN       =   dks.image.load("images/system/misf_coin.png").convert_alpha()

WPN_IMG_NAMES   =   ["AnriSword", "ArstorsSpear", "AstoraGreatsword",
                     "AstoraStraightSword", "Avelyn", "BanditsKnife",
                     "BarbedSword", "BastardSword", "BattleAxe",
                     "BlackBlade", "BlackKnightGA", "BlackKnightGS",
                     "BlackKnightHalberd", "BlackKnightSword", "Bloodlust",
                     "BrigandAxe", "BrigandDaggers", "Broadsword",
                     "BrokenSword", "ButchersKnife", "Caestus",
                     "CandleDagger", "CarthusCurvedGS", "CarthusCurvedSword",
                     "CarthusShotel", "CathedralGreatsword", "ChaosBlade",
                     "Claw", "Claymore", "ClericCandle",
                     "Club", "CompositeBow", "CorvianDagger",                
                     "CrescentAxe", "CrescentShotel", "CrystalSageRapier",
                     "Dagger", "DancersTwinswords", "Darkdrift",
                     "DarkHand", "DarkSword", "DemonFist",
                     "DemonGreataxe", "DragonslayerAxe", "DragonslayerCross",
                     "DragonslayerGA", "DragonslayerSpear", "DragonTooth",
                     "DrakebloodSword", "DrangHammers", "DrangTwinspears",
                     "Eleonora", "Estoc", "ExecutionerSword",
                     "ExileGreatsword", "Falchion", "FarronGreatsword",
                     "FirelinkGreatsword", "Flamberge", "FourProngedPlow",
                     "FumeUltraGS", "GargoyleFlameHammer", "GargoyleFlameSpear",
                     "GhruCurvedSword", "GhruDagger", "GhruSpear",
                     "Glaive", "GoldenRitualSpear", "GotthardKatanas",
                     "GotthardTwinswords", "Greataxe", "GreatClub",
                     "CorvianGreatScythe", "Greatlance", "GreatMace",
                     "GreatMachete", "GreatScythe", "Greatsword",
                     "GreatswordJudgement", "GundyrHalberd", "Halberd",
                     "HandAxe", "HandmaidDagger", "Harpe",
                     "HeyselPick", "HollowslayerSword", "ImmolationTinder",
                     "IrithyllRapier", "IrithyllSword", "LargeClub",
                     "Longsword", "LoriansSword", "LothricGreatsword",
                     "LothricHolySword", "LothricSpear", "LothricStraightSword",
                     "Lucerne", "Mace", "MailBreaker",
                     "ManikinClaw", "ManSerpentAxe", "MoonlightGreatsword",
                     "MorionBlade", "MornesHammer", "MorningStar",
                     "Murakumo", "NotchedWhip", "OldKingHammer",
                     "PaintingCurvedSword", "ParryDagger", "Partizan",
                     "Pickaxe", "Pike", "PontiffCurvedSword",
                     "PontiffGreatScythe", "ProfanedGreatsword", "Rapier",
                     "RedHalberd", "ReinforcedClub", "RicardsRapier",
                     "SaintBident", "Scimitar", "SellswordTwinblades",
                     "Shortsword", "Shotel", "SmithHammer",
                     "SmoughsHammer", "SolderingIron", "Spear",
                     "SpikedMace", "SpottedWhip", "StormCurvedSword",
                     "Stormruler", "SunlightSword", "TailboneDagger",
                     "TailboneSpear", "ThrallAxe", "TwinPrinceSword",
                     "Uchigatana", "VordtsHammer", "WardenTwinblades",
                     "Warpick", "WashingPole", "Whip",
                     "WingedKnightHalberd", "WingedKnightTwinaxes", "WingedSpear",
                     "WitchLocks", "WolfCurvedGS", "WolfGreatsword",
                     "WolnirsHolyBlade", "WoodenHammer", "YhormsMachete",
                     "YorshkasSpear", "Zweihander"]
                     
SHIELD_IMG_NAMES    =   []
SPELL_IMG_NAMES     =   []
AMOR_IMG_NAMES      =   []

#==============================================================================#
#                   BEGIN LOADING ITEMS                                        # 
#==============================================================================#

WPN_OBJ	    =   {name: dks.image.load("images/loot/weapons/{}.png".format(name)).convert_alpha()
			for name in WPN_IMG_NAMES}
SHIELD_OBJ  =   {}
SPELL_OBJ   =   {}
ARMOR_OBJ   =   {}
#==============================================================================#
#                   LOOT TABLES                                                # 
#==============================================================================#

LOOT_CMN    =   {"Longsword":   WPN_OBJ["Longsword"],
                 "Broadsword":  WPN_OBJ["Broadsword"],
                 "Spear":       WPN_OBJ["Spear"]}

LOOT_RARE   =   {"Uchigatana":  WPN_OBJ["Uchigatana"],
                 "Chaos Blade": WPN_OBJ["ChaosBlade"]}

LOOT_ULTRA  =   {"Dark Sword":  WPN_OBJ["DarkSword"]}

LOOT_MISF   =   {}


#==============================================================================#
#                   COLORS DEFINITIONS                                         # 
#==============================================================================#
#Color Defs.    =       (R,   G,   B)
WHITE           =       (255, 255, 255)
GREEN 	        =       (78,  255, 87)
YELLOW 	        =       (241, 255, 0)
BLUE 	        =       (80,  255, 239)
PURPLE 	        =       (203, 0,   255)
RED 	        =       (237, 28,  36)
BLACK           =       (0,   0,   0)

#Text Color
TXT_COLOR = YELLOW

#==============================================================================#
#                   FUNCTION DEFINITIONS                                       # 
#==============================================================================#

def newCursor(arrow):
    hotspot = None
    for y in range(len(arrow)):
        for x in range(len(arrow[y])):
            if arrow[y][x] in ['x', ',', 'O']:
                hotspot = x,y
                break
        if hotspot != None:
            break
    if hotspot == None:
        raise Exception("No hotspot specified for cursor 'Arrow'!")
    s2 = []
    for line in arrow:
        s2.append(line.replace('x', 'X').replace(',', '.').replace('O','o'))
    cursor, mask = dks.cursors.compile(s2, 'X', '.', 'o')
    size = len(arrow[0]), len(arrow)
    dks.mouse.set_cursor(size, hotspot, cursor, mask)

def resetLoot():
    global currentLoot1; global currentLoot2; global currentLoot3
    global currentLoot4; global currentLoot5; global currentLoot6
    
    global LOOT_1ON; global LOOT_2ON; global LOOT_3ON
    global LOOT_4ON; global LOOT_5ON; global LOOT_6ON

    global currentRoll; global lootRoll_ON
    
    LOOT_1ON = False; LOOT_2ON = False;
    LOOT_3ON = False; LOOT_4ON = False;
    LOOT_5ON = False; LOOT_6ON = False;

    currentLoot1 = None; currentLoot2 = None;
    currentLoot3 = None; currentLoot4 = None;
    currentLoot5 = None; currentLoot6 = None;

    currentRoll = ""; lootRoll_ON = False
    
#Credit to Blake for this workaround: http://www.nerdparadise.com/tech/python/pygame/blitopacity/
def blitAlpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = dks.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

def generateRoll():
    global currentRoll
    global lootRoll_ON

    currentRoll = ""

    for i in range(rnd.randint(1, 5)):
        cmn_rand    = rnd.randint(0, 1000)
        rare_rand   = rnd.randint(0, 1000)
        ultra_rand  = rnd.randint(0, 1000)
        misf_rand   = rnd.randint(0, 1000)

    if(cmn_rand < 100): #10% Chance, 0 common
        currentRoll += "0 Common"
    elif((cmn_rand >= 100) & (cmn_rand < 805)): #70.5% Chance, 1 common
        currentRoll += "1 Common"
    elif(cmn_rand >= 805): #19.5% Chance, 2 common
        currentRoll += "2 Common"
    print ("CMN: ",cmn_rand)
    
    currentRoll += ", "

    if(rare_rand < 710): #71% Chance, 0 rare
        currentRoll += "0 Rare"
    elif((rare_rand >= 710) & (rare_rand < 910)): #20% Chance, 1 rare
        currentRoll += "1 Rare"
    elif(rare_rand >= 910): #9% Chance, 2 rare
        currentRoll += "2 Rare"
    print ("RARE: ",rare_rand)
    
    currentRoll += ", "

    if(ultra_rand < 975): #97.5% Chance, 0 ultra
        currentRoll += "0 Ultra"
    elif(ultra_rand >= 975): #2.5% Chance, 1 ultra
        currentRoll += "1 Ultra"
    print ("ULTRA: ",ultra_rand)
    
    currentRoll += ", "

    if(misf_rand < 950): #95% Chance, 0 misfortune
        currentRoll += "0 Misfortune"
    elif(misf_rand >= 950): #5% Chance, 1 misfortune
        currentRoll += "1 Misfortune"
    print ("MISF: ",misf_rand)

    if((cmn_rand < 100) & (rare_rand < 720) & (ultra_rand < 985) & (misf_rand < 945)):
        staleRand = rnd.randint(1, 9)
        if(staleRand < 7):
            currentRoll = "1 Common, 0 Rare, 0 Ultra, 0 Misfortune"
        elif(staleRand >= 7):
            currentRoll = "0 Common, 1 Rare, 0 Ultra, 0 Misfortune" 
    
    lootRoll_ON = True

def grabLoot(category):
    
    if(category.lower() == "common"):
        return LOOT_CMN.keys()[rnd.randint(0, len(LOOT_CMN)-1)]

    elif(category.lower() == "rare"):
        return LOOT_RARE.keys()[rnd.randint(0, len(LOOT_RARE)-1)]

    elif(category.lower() == "ultra"):
        return LOOT_ULTRA.keys()[rnd.randint(0, len(LOOT_ULTRA)-1)]

    elif(category.lower() == "misfortune"):
        return LOOT_MISF.keys()[rnd.randint(0, len(LOOT_MISF)-1)]
        
    
def lootCoin(category, spot):

    global currentLoot1; global currentLoot2; global currentLoot3
    global currentLoot4; global currentLoot5; global currentLoot6
    
    global LOOT_1ON; global LOOT_2ON; global LOOT_3ON
    global LOOT_4ON; global LOOT_5ON; global LOOT_6ON

    if(category.lower() == "common"):

        if(spot == 1):

            currentLoot1 = grabLoot("common")
            
            for i in range(255):
                screen.blit(MN_MAIN, (0, 0)) 

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, CMN_COIN, (10, 258), i)
                dks.display.update()
                CL.tick(300)

            dks.time.delay(1000)

            for i in range(255):
                screen.blit(MN_MAIN, (0, 0))
                
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, CMN_COIN, (10, 258), 255-i)
                blitAlpha(screen, LOOT_CMN[currentLoot1], (20, 230), i)
                dks.display.update()
                CL.tick(600)

            LOOT_1ON = True
                
        elif(spot == 2):
            
            currentLoot2 = grabLoot("common")
            
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, CMN_COIN, (166, 258), i)
                dks.display.update()
                CL.tick(300)

            dks.time.delay(1000)

            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))

                blitAlpha(screen, CMN_COIN, (166, 258), 255-i)
                blitAlpha(screen, LOOT_CMN[currentLoot2], (176, 230), i)
                dks.display.update()
                CL.tick(600)

            LOOT_2ON = True

    elif(category.lower() == "rare"):
        
        if(spot == 1):

            currentLoot3 = grabLoot("rare")
            
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230)) 
                    
                blitAlpha(screen, RARE_COIN, (323, 258), i)
                dks.display.update()
                CL.tick(300)

            dks.time.delay(1000)

            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, RARE_COIN, (323, 258), 255-i)
                blitAlpha(screen, LOOT_RARE[currentLoot3], (333, 230), i)
                dks.display.update()
                CL.tick(600)

            LOOT_3ON = True
                
        elif(spot == 2):

            currentLoot4 = grabLoot("rare")
            
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, RARE_COIN, (480, 258), i)
                dks.display.update()
                CL.tick(300)

            dks.time.delay(1000)

            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, RARE_COIN, (480, 258), 255-i)
                blitAlpha(screen, LOOT_RARE[currentLoot4], (490, 230), i)
                dks.display.update()
                CL.tick(600)

            LOOT_4ON = True

    elif(category.lower() == "ultra"):
        
        if(spot == 1):

            currentLoot5 = grabLoot("ultra")
            
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))  
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                    
                blitAlpha(screen, ULTRA_COIN, (636, 258), i)
                dks.display.update()
                CL.tick(300)

            dks.time.delay(1000)

            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                    
                blitAlpha(screen, ULTRA_COIN, (636, 258), 255-i)
                blitAlpha(screen, LOOT_ULTRA[currentLoot5], (648, 230), i)
                dks.display.update()
                CL.tick(600)

            LOOT_5ON = True
            
#==============================================================================#
#                   INTRO SCREEN 1: TITLE                                      # 
#==============================================================================#

newCursor(arrow)
mtheme.play(loops=-1, fade_ms=3000)

#                        (X,    Y),  (Width, Height)
inBEGIN     =   dks.Rect((304, 312), (340, 123))
inTWITTER   =   dks.Rect((545, 478), (394, 33))
inGITHUB    =   dks.Rect((281, 549), (658, 34))


#Fade in
for i in range(255): 
    screen.fill((0,0,0))
    IN_1.set_alpha(i)
    screen.blit(IN_1, (0,0))
    dks.display.update()
    CL.tick(120)

dks.event.clear()

while(INTRO == 1):
    
    pos = dks.mouse.get_pos()
    (pressed1, pressed2, pressed3) = dks.mouse.get_pressed()

    CL.tick(60)
    dks.display.update()

    if(inBEGIN.collidepoint(pos) == 1):
        screen.blit(IN_1ON, (0, 0))
        dks.display.update()
        
    elif(inTWITTER.collidepoint(pos) == 1):
        screen.blit(IN_1T, (0, 0))
        dks.display.update()
        
    elif(inGITHUB.collidepoint(pos) == 1):
        screen.blit(IN_1G, (0, 0))
        dks.display.update()
        
    else:
        screen.blit(IN_1, (0, 0))

    #Event Handler:
    for event in dks.event.get():

        if event.type == dks.MOUSEBUTTONUP and (inBEGIN.collidepoint(pos) == 1):
            start_fx.play()
            mtheme.fadeout(2000)
            INTRO = 2

        elif event.type == dks.MOUSEBUTTONUP and (inTWITTER.collidepoint(pos) == 1):
            select_fx.play()
            wb.open("https://twitter.com/Kirk_CW", 0, True)

        elif event.type == dks.MOUSEBUTTONUP and (inGITHUB.collidepoint(pos) == 1):
            select_fx.play()
            wb.open("https://github.com/KirkWorl/DarkSouls3_R2R", 0, True)

        elif event.type == dks.KEYDOWN:

            if event.key == dks.K_SPACE:
                mtheme.fadeout(1000)
                INTRO = 4
            
        #If the program is closed, exit:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()
            

#==============================================================================#
#                   SECOND INTRO SCREEN: WELCOME                               # 
#==============================================================================#

if(INTRO == 2):

    inNEXT      =   dks.Rect((614, 477), (336, 123))

    #Fade out
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_1.set_alpha(255-i)
        screen.blit(IN_1, (0, 0))
        dks.display.update()
        CL.tick(120)

    dks.time.delay(250)

    #Fade in second screen
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_2.set_alpha(i)
        screen.blit(IN_2, (0, 0))
        dks.display.update()
        CL.tick(120)

dks.event.clear()

while(INTRO == 2):
    
    pos = dks.mouse.get_pos()
    (pressed1, pressed2, pressed3) = dks.mouse.get_pressed()

    CL.tick(60)
    dks.display.update()

    if(inNEXT.collidepoint(pos) == 1):
        screen.blit(IN_2ON, (0, 0))
        dks.display.update()
    else:
        screen.blit(IN_2, (0, 0))
    
    #Event Handler:
    for event in dks.event.get():

        if event.type == dks.MOUSEBUTTONUP and (inNEXT.collidepoint(pos) == 1):
            select_fx.play()
            INTRO = 3

        #If the program is closed, exit:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()

#==============================================================================#
#                   THIRD INTRO SCREEN: RULES OF R2R                           # 
#==============================================================================#

if(INTRO == 3):

    inSTART     =   dks.Rect((129, 531), (166, 60))
    
    #Fade out
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_2.set_alpha(255-i)
        screen.blit(IN_2, (0, 0))
        dks.display.update()
        CL.tick(120)

    dks.time.delay(250)

    #Fade in third screen
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_3.set_alpha(i)
        screen.blit(IN_3, (0, 0))
        dks.display.update()
        CL.tick(120)

dks.event.clear()

while(INTRO == 3):

    pos = dks.mouse.get_pos()
    (pressed1, pressed2, pressed3) = dks.mouse.get_pressed()

    CL.tick(60)
    dks.display.update()

    if(inSTART.collidepoint(pos) == 1):
        screen.blit(IN_3ON, (0, 0))
        dks.display.update()
    else:
        screen.blit(IN_3, (0, 0))
    
    #Event Handler:
    for event in dks.event.get():

        if event.type == dks.MOUSEBUTTONUP and (inSTART.collidepoint(pos) == 1):
            select_fx.play()
            INTRO = 4

        #If the program is closed, exit:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()

#==============================================================================#
#                   MAIN PROGRAM LOOP / HOME SCREEN                            # 
#==============================================================================#

if(INTRO == 4):
    
    inGEM       =   dks.Rect((109, 73),  (108, 108))
    inRESET     =   dks.Rect((358, 497), (248, 60))
    inCOMM1     =   dks.Rect((20,  230), (125, 216))
    inCOMM2     =   dks.Rect((176, 230), (125, 216))
    inRARE1     =   dks.Rect((333, 230), (125, 216))
    inRARE2     =   dks.Rect((490, 230), (125, 216))
    inULTRA     =   dks.Rect((648, 230), (125, 216))
    inMISF      =   dks.Rect((802, 230), (125, 216))
    
    #Fade out
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_3.set_alpha(255-i)
        screen.blit(IN_3, (0, 0))
        dks.display.update()
        CL.tick(120)

    dks.time.delay(250)

    #Fade in fourth screen
    for i in range(255): 
        screen.fill((0, 0, 0))
        MN_MAIN.set_alpha(i)
        screen.blit(MN_MAIN, (0, 0))
        dks.display.update()
        CL.tick(120)

dks.event.clear()

while(RUNNING):

    LOOT_CLICK1 = False;    LOOT_CLICK2 = False
    LOOT_CLICK3 = False;    LOOT_CLICK4 = False
    LOOT_CLICK5 = False;    LOOT_CLICK6 = False
    
    pos = dks.mouse.get_pos()

    CL.tick(120)

    if(inGEM.collidepoint(pos) == 1):
        screen.blit(MN_L, (0, 0))
        
    elif(inRESET.collidepoint(pos) == 1):
        screen.blit(MN_R, (0, 0))
        
    else:
        screen.blit(MN_MAIN, (0, 0))

    if(lootRoll_ON):
        screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
        
    if(LOOT_1ON):
        screen.blit(LOOT_CMN[currentLoot1], (20, 230))
        
    if(LOOT_2ON):
        screen.blit(LOOT_CMN[currentLoot2], (176, 230))

    if(LOOT_3ON):
        screen.blit(LOOT_RARE[currentLoot3], (333, 230))

    if(LOOT_4ON):
        screen.blit(LOOT_RARE[currentLoot4], (490, 230))

    if(LOOT_5ON):
        screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))

    dks.display.update()
    
    #Event Handler:
    for event in dks.event.get():

        #If the program is closed, exit:
        if event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()

        elif event.type == (dks.MOUSEBUTTONUP) and (inRESET.collidepoint(pos) == 1):
            resetLoot()
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inGEM.collidepoint(pos) == 1):
            generateRoll()
            dks.event.clear(dks.MOUSEBUTTONUP)
            
        elif event.type == (dks.MOUSEBUTTONUP) and (inCOMM1.collidepoint(pos) == 1) and (LOOT_CLICK1 == False):
            LOOT_CLICK1 = True
            lootCoin("common", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inCOMM2.collidepoint(pos) == 1) and (LOOT_CLICK2 == False):
            LOOT_CLICK2 = True
            lootCoin("common", 2)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inRARE1.collidepoint(pos) == 1) and (LOOT_CLICK3 == False):
            LOOT_CLICK3 = True
            lootCoin("rare", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inRARE2.collidepoint(pos) == 1) and (LOOT_CLICK4 == False):
            LOOT_CLICK4 = True
            lootCoin("rare", 2)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inULTRA.collidepoint(pos) == 1) and (LOOT_CLICK5 == False):
            LOOT_CLICK5 = True
            lootCoin("ultra", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)



    



    



    
    
    


