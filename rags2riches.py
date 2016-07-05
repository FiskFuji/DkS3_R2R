################################################################################
#                                                                              # 
#                       DARK SOULS 3 - RAGS TO RICHES                          # 
#                               DEVELOPED BY:                                  # 
#                              KIRK C. WORLEY                                  # 
#                                (c) 2016.                                     # 
#                        Licensed under GNU GPL 3.0                            # 
#                For more information about this license, see:                 # 
#               http://www.gnu.org/licenses/quick-guide-gplv3.html             # 
#                                                                              #
################################################################################
#                            SPECIAL THANKS:                                   # 
#                KYLE W., TYLER C., KAI D., BRANDON A.                         #
#                           AUSTIN (@NE_austin)                                #
#               for being an amazing person and always finding                 # 
#           a way to brighten my day with inspiration. Thank you.              # 
#                                  AND                                         # 
#               everyone who encouraged me to attempt this,                    # 
#       and put up with my constant questions about design choices.            # 
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
#   this. While creating objects would be beneficial here, I am leaving that   # 
#   up to those who wish to alter the code for their own purposes.             # 
#                                                                              #
################################################################################
#                                                                              #
#                   !! EASY EDITABLE PARTS FOR PROGRAMMERS !!                  # 
#                                                                              #
################################################################################

#==============================================================================#
#               == USER SPECIFIED LOOT TABLES ==                               #
#==============================================================================#
# Set ENABLE_USER_LOOT to True if you would like to use your own loot tables.
# you can edit the loot tables below.
# The format for loot tables is as follows:
#------------------------------------------------------------------------------#

ENABLE_USER_LOOT = False

#------------------------------------------------------------------------------#
# USR_LOOT_[CATEGORY] = {}
#           This is the category of loot.
#
# { <- This begins the dictionary. Do not remove it.
# } <- This ends the dictionary. Do not remove it.
#
#------------------------------------------------------------------------------#
#               == HOW TO WRITE THE LOOT ENTRIES ==                            #
#------------------------------------------------------------------------------#
# Loot structure: If you know Python, this is simply a dictionary. The values
# that the keys are assigned to are image files from an OBJ dictionary.
# The dictionaries that exist are listed below in ** Location.
#
# Name*, followed by a :, Location**, [Name of Loot item***]  
# "Weapon Name":          WPN_OBJ["Loot Item Name"]
#
#   * Name must be in quotes. What you type here will show up in the
#       current item bar.
#
#   ** Location is one of six dictionaries:
#       Weapons:        WPN_OBJ[]
#       Shields:        SHIELD_OBJ[]
#       Pyro:           SPELL_OBJ[]
#       Armor:          ARMOR_OBJ[]
#       Misfortunes:    MISF_OBJ[]
#       Consumables:    CONS_OBJ[]
#
#   *** Name of loot item must be encased in brackets.
#           Name should also be in quotes.
#
#   If the loot is NOT the last in the list, add a comma after the ]
#   If you need more help, see the commented example below.
#------------------------------------------------------------------------------#
#               == BEGIN USER LOOT ==                                          #
#------------------------------------------------------------------------------#

def enableUserLoot():
#------------------------------------------------------------------------------#
#               !! DO NOT REMOVE GLOBAL DECLARATIONS !!                        #
#------------------------------------------------------------------------------#
    global LOOT_CMN; global LOOT_RARE; global LOOT_ULTRA; global LOOT_MISF;
    global WPN_OBJ; global ARMOR_OBJ; global MISF_OBJ; global SHIELD_OBJ; global SPELL_OBJ; global CONS_OBJ
    
#------------------------------------------------------------------------------#
#               EDITABLE LOOT TABLES                                           #
#------------------------------------------------------------------------------#
#
#   Example Loot Entry:
#   USR_LOOT_EXAMPLE    = {"User Weapon":   WPN_OBJ["Longsword"]}
#                          "Weapon name":   Location ["Object name"],
#   
#------COMMON------------------------------------------------------------------#
    USR_LOOT_COMMON     = { #Don't touch this.
                        #"User Weapon 1":        WPN_OBJ["Longsword"],
        
                        } #Don't touch this.
#------RARE--------------------------------------------------------------------#
    USR_LOOT_RARE       = { #Don't touch this.
        
                        } #Don't touch this.
#------ULTRA-------------------------------------------------------------------#
    USR_LOOT_ULTRA      = { #Don't touch this.
        
                        } #Don't touch this.
#------MISFORTUNE--------------------------------------------------------------#
    USR_LOOT_MISFORTUNE = { #Don't touch this.
        
                        } #Don't touch this.
    
#------------------------------------------------------------------------------#
#               !! FAILSAFE SYSTEMS - DO NOT EDIT !!                           #
#------------------------------------------------------------------------------#
    if(bool(USR_LOOT_COMMON)):
        LOOT_CMN = USR_LOOT_COMMON
    if(bool(USR_LOOT_RARE)):
        LOOT_RARE = USR_LOOT_RARE
    if(bool(USR_LOOT_ULTRA)):
        LOOT_ULTRA = USR_LOOT_ULTRA
    if(bool(USR_LOOT_MISFORTUNE)):
       LOOT_MISF = USR_LOOT_MISFORTUNE
#==============================================================================#
#               == END USER SPECIFIED LOOT TABLES ==                           #
#==============================================================================#

################################################################################
#                                                                              #
#                   !! END OF EASY EDITABLE PARTS FOR PROGRAMMERS !!           # 
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

#------------------------------------------------------------------------------#
#               !! FOR VERSIONING PURPOSES !!                                  #
#------------------------------------------------------------------------------#
VERSION_NO  = "v0.7"
BETA        = True

if(BETA):
    VERSION_NO += " BETA"
    
CAPTION     = ("Rags to Riches " + str(VERSION_NO))

#------------------------------------------------------------------------------#
#               !! DO NOT EDIT !!                                              #
#------------------------------------------------------------------------------#
dks.display.set_caption(CAPTION)

#------------------------------------------------------------------------------#
# Width, Height of Screen in pixels. If this is changed, the background images #
# will also need to be rescaled to fit the new sizes.                          # 
# Location: <<images/system/intro1.png>>, <<images/system/intro1_1.png>>, etc. # 
# This will mean the loot-images will be off place as well. Be careful when    #
# adjusting these values.                                                      # 
#------------------------------------------------------------------------------#
#               !! Changing this is NOT recommended. !!                        #
#------------------------------------------------------------------------------#
WIDTH       = 950
HEIGHT      = 600
DISP        = (WIDTH, HEIGHT)
#------------------------------------------------------------------------------#

ICON        =   dks.image.load("images/system/icon.png")
dks.display.set_icon(ICON)

screen      =   dks.display.set_mode(DISP)
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

TXT_CHANGER =   False

MUTE_FX     =   False
INCL_PYRO   =   False

DIFF        =   1
INTRO       =   1

FONT        =   "fonts/OptimusPrinceps.ttf"
FNT         =   dks.font.Font(FONT, 30)
FNT2        =   dks.font.Font(FONT, 23)

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
challenge_fx    =   dks.mixer.Sound("sounds/challenge.ogg")
switch_fx       =   dks.mixer.Sound("sounds/switch1.ogg")
switch2_fx      =   dks.mixer.Sound("sounds/switch2.ogg")
accept_fx       =   dks.mixer.Sound("sounds/confirm1.ogg")
coin_fx         =   dks.mixer.Sound("sounds/coin.ogg")
reset_fx        =   dks.mixer.Sound("sounds/cancel1.ogg")
IN_1            =   dks.image.load("images/system/intro1.png").convert()
IN_1ON          =   dks.image.load("images/system/intro1_1.png").convert()
IN_1T           =   dks.image.load("images/system/intro1_2.png").convert()
IN_1G           =   dks.image.load("images/system/intro1_3.png").convert()
IN_2            =   dks.image.load("images/system/intro2.png").convert()
IN_2ON          =   dks.image.load("images/system/intro2_1.png").convert()
IN_3            =   dks.image.load("images/system/intro3.png").convert()
IN_3ON          =   dks.image.load("images/system/intro3_1.png").convert()
DIFF_E          =   dks.image.load("images/system/Difficulty_E.png").convert()
DIFF_E2         =   dks.image.load("images/system/Difficulty_E2.png").convert()
DIFF_H          =   dks.image.load("images/system/Difficulty_H.png").convert()
DIFF_H2         =   dks.image.load("images/system/Difficulty_H2.png").convert()
PYRO_ON         =   dks.image.load("images/system/PyroSwitch_ON.png").convert()
PYRO_OFF        =   dks.image.load("images/system/PyroSwitch_OFF.png").convert()
PYRO_DISABLE    =   dks.image.load("images/system/PyroSwitch_DISABLED.png").convert()
MN_MAIN         =   dks.image.load("images/system/main1.png").convert()
MN_L            =   dks.image.load("images/system/main1_L.png").convert()
MN_R            =   dks.image.load("images/system/main1_R.png").convert()
MN_I            =   dks.image.load("images/system/main1_I.png").convert()
ABOUT_SCREEN    =   dks.image.load("images/system/aboutScreen.png").convert()
MUTE_ICON       =   dks.image.load("images/system/muted.png").convert()
UNMUTE_ICON     =   dks.image.load("images/system/unmuted.png").convert()
CHNGR_MAIN      =   dks.image.load("images/system/clr/clr_changer.png").convert()
CHNGR_RED       =   dks.image.load("images/system/clr/changer_Red.png").convert()
CHNGR_ORANGE    =   dks.image.load("images/system/clr/changer_Orange.png").convert()
CHNGR_YELLOW    =   dks.image.load("images/system/clr/changer_Yellow.png").convert()
CHNGR_GREEN     =   dks.image.load("images/system/clr/changer_Green.png").convert()
CHNGR_BLUE      =   dks.image.load("images/system/clr/changer_Blue.png").convert()
CHNGR_PURPLE    =   dks.image.load("images/system/clr/changer_Purple.png").convert()
CHNGR_CYAN      =   dks.image.load("images/system/clr/changer_Cyan.png").convert()
CHNGR_WHITE     =   dks.image.load("images/system/clr/changer_White.png").convert()
CHNGR_CONFIRM   =   dks.image.load("images/system/clr/clr_confirm.png").convert()
CMN_COIN        =   dks.image.load("images/system/coin/cmn_coin.png").convert_alpha()
RARE_COIN       =   dks.image.load("images/system/coin/rare_coin.png").convert_alpha()
ULTRA_COIN      =   dks.image.load("images/system/coin/ultra_coin.png").convert_alpha()
MISF_COIN       =   dks.image.load("images/system/coin/misf_coin.png").convert_alpha()

WPN_IMG_NAMES       =   ["AnriSword", "ArstorsSpear", "AstoraGreatsword",
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

ARMOR_IMG_NAMES     =   ["Alva", "Alva_F", "Antiquated", "Antiquated_F",
                         "Archdeacon", "Archdeacon_F", "Assassin", "Assassin_F",
                         "BlackDress", "BlackDress_F", "BlackHand", "BlackHand_F",
                         "BlackIron", "BlackIron_F", "BlackKnight", "BlackKnight_F",
                         "BlackLeather", "BlackLeather_F", "Brass", "Brass_F",
                         "Brigand", "Brigand_F", "Catarina", "Catarina_F",
                         "Cathedral", "Cathedral_F", "Chain", "Chain_F",
                         "Clandestine", "Clandestine_F", "ClericBlue", "ClericBlue_F",
                         "Conjurator", "Conjurator_F", "Cornyx", "Cornyx_F",
                         "CourtSorcerer", "CourtSorcerer_F", "Dancers", "Dancers_F",
                         "Dark", "Dark_F", "Deacon", "Deacon_F",
                         "Deserter", "Deserter_F", "Dragonscale", "Dragonscale_F",
                         "Dragonslayer", "Dragonslayer_F", "Drakeblood", "Drakeblood_F",
                         "Drang", "Drang_F", "Eastern", "Eastern_F",
                         "EliteKnight", "EliteKnight_F", "Evangelist", "Evangelist_F",
                         "Executioner", "Executioner_F", "Exile", "Exile_F",
                         "FallenKnight", "FallenKnight_F", "Faraam", "Faraam_F",
                         "Favor", "Favor_F", "Firekeeper", "Firekeeper_F",
                         "Firelink", "Firelink_F", "FireWitch", "FireWitch_F",
                         "Gundyr", "Gundyr_F", "HardLeather", "HardLeather_F",
                         "Havel", "Havel_F", "Herald", "Herald_F",
                         "Jailer", "Jailer_F", "Karla", "Karla_F",
                         "Knight", "Knight_F", "Leather", "Leather_F",
                         "Legion", "Legion_F", "Leonhard", "Leonhard_F",
                         "Lorian", "Lorian_F", "Lothric", "Lothric_F",
                         "Maiden", "Maiden_F", "Masters", "Masters_F",
                         "Mirrah", "Mirrah_F", "MirrahChain", "MirrahChain_F",
                         "Morne", "Morne_F", "NamelessKnight", "NamelessKnight_F",
                         "Northern", "Northern_F", "OldSorcerer", "OldSorcerer_F",
                         "Outrider", "Outrider_F", "Painting", "Painting_F",
                         "PaleShade", "PaleShade_F", "PontiffKnight", "PontiffKnight_F",
                         "Prayer", "Prayer_F", "Pyromancer", "Pyromancer_F",
                         "Sellsword", "Sellsword_F", "Shadow", "Shadow_F",
                         "SilverKnight", "SilverKnight_F", "Smough", "Smough_F",
                         "Sorcerer", "Sorcerer_F", "SunArmor", "SunArmor_F",
                         "Sunless", "Sunless_F", "Sunset", "Sunset_F",
                         "Thorns", "Thorns_F", "Warden", "Warden_F",
                         "WingedKnight", "WingedKnight_F", "WolfKnight", "WolfKnight_F",
                         "Worker", "Worker_F", "Xanthous", "Xanthous_F"]

SHIELD_IMG_NAMES    =   ["AncientDragon", "BlackIron", "BlackKnight", "BlueWooden",
                         "Bonewheel", "Buckler", "CaduceusRound", "Carthus",
                         "CathedralKnight", "Crest", "Crimson", "CurseWard",
                         "DragonCrest", "Dragonslayer", "EasternIron", "EastWest",
                         "ElkhornRound", "GhruRotshield", "GoldenFalcon", "GoldenWingCrest",
                         "GrassCrest", "GreatshieldOfGlory", "Havels", "Hawkwoods",
                         "IronRound", "Kite", "Knight", "LargeLeather",
                         "Leather", "Llewellyn", "LothricGreatshield", "LothricKnight",
                         "Moaning", "Pierce", "Plank", "PontiffKnight",
                         "Porcine", "Round", "SacredBloom", "ShieldOfWant",
                         "SilverEagleKite", "SilverKnight", "SmallLeather", "Spiked",
                         "SpiritTreeCrest", "Stone", "StoneParma", "Sunlight",
                         "Sunset", "Target", "WarriorsRound", "WolfKnights", "Wooden"]

SPELL_IMG_NAMES     =   ["AcidSurge", "BlackFireOrb", "BlackFlame", "BlackSerpent",
                         "BoulderHeave", "BurstingFireball", "CarthusBeacon", "CarthusFlameArc",
                         "ChaosBedVestiges", "ChaosStorm", "Fireball", "FireOrb",
                         "Firestorm", "FireSurge", "FireWhip", "FlashSweat",
                         "GreatChaosFireOrb", "GreatCombustion", "IronFlesh", "PoisonMist",
                         "PowerWithin", "ProfanedFlame", "ProfuseSweat", "Rapport",
                         "SacredFlame", "ToxicMist", "Warmth"]

MISF_IMG_NAMES      =   ["Chest", "Confused", "Cursed", "Hand", "Head",
                         "Leg", "LH1", "LH2", "LH3", "Lucky",
                         "RH1", "RH2", "RH3", "Ring1", "Ring2",
                         "Ring3", "Ring4", "Spell", "Tripped"]

CONS_IMG_NAMES      =   ["BlackFirebomb_5", "BlackFirebomb_10", "CarthusRouge_5",
                         "CarthusRouge_10", "CharcoalBundle_5", "CharcoalBundle_10",
                         "CharcoalResin_5", "CharcoalResin_10", "DuelCharm_5",
                         "Firebomb_5", "Firebomb_10", "GoldBundle_5",
                         "GoldBundle_10", "GoldResin_5", "GoldResin_10",
                         "GoldResin_20", "GreenBlossom_5", "GreenBlossom_10",
                         "HumanResin_5", "HumanResin_10", "Kukri_5",
                         "Kukri_10", "LightningUrn_5", "LightningUrn_10",
                         "PaleResin_5", "PaleResin_10", "PoisonThrowingKnife_5",
                         "PoisonThrowingKnife_10", "RopeBlackFirebomb_5", "RopeBlackFirebomb_10",
                         "RopeFirebomb_5", "RopeFirebomb_10", "RottenResin_5",
                         "RottenResin_10", "ThrowingKnife_5", "ThrowingKnife_10",
                         "Repaired"]

ABOUT_TXT           =   ["Thanks for trying out DkS III: Rags to Riches.",
                         "Credits:",
                         "Art and Programming: Myself.",
                         "Game Images themselves: Dark Souls 3 Wiki",
                         "(www.darksouls3.wikidot.com).",
                         "Difficulty Screenshots: Myself.",
                         "Main Theme: Dark Souls 3 Main Theme.",
                         "Other misc. images used under Creative Commons.",
                         "To report a bug, please tweet at me (@Kirk _ CW).",
                         "Or, I guess you could e-mail me. It's on the screen",
                         "somewhere, unless I forgot.",
                         "Thank you, so much."]

#==============================================================================#
#                   BEGIN LOADING ITEMS                                        # 
#==============================================================================#

WPN_OBJ	    =   {name: dks.image.load("images/loot/weapons/{}.png".format(name)).convert_alpha()
			for name in WPN_IMG_NAMES}

MISF_OBJ    =   {name: dks.image.load("images/loot/misfortunes/{}.png".format(name)).convert_alpha()
			for name in MISF_IMG_NAMES}

ARMOR_OBJ   =   {name: dks.image.load("images/loot/armor/{}.png".format(name)).convert_alpha()
			for name in ARMOR_IMG_NAMES}

SHIELD_OBJ  =   {name: dks.image.load("images/loot/shields/{}.png".format(name)).convert_alpha()
			for name in SHIELD_IMG_NAMES}

SPELL_OBJ   =   {name: dks.image.load("images/loot/spells/{}.png".format(name)).convert_alpha()
			for name in SPELL_IMG_NAMES}

CONS_OBJ    =   {name: dks.image.load("images/loot/consumables/{}.png".format(name)).convert_alpha()
			for name in CONS_IMG_NAMES}


#==============================================================================#
#                   LOOT TABLES                                                # 
#==============================================================================#
#      !! NOTE !!                                                              #     
# Place a space after a FULL armor set key, so dictionaries make it a new key. #
#------------------------------------------------------------------------------#

LOOT_CMN    =   {"Longsword":                   WPN_OBJ["Longsword"]}

LOOT_RARE   =   {"Uchigatana":                  WPN_OBJ["Uchigatana"],
                 "Chaos Blade":                 WPN_OBJ["ChaosBlade"]}

LOOT_ULTRA  =   {"Black Knight Greataxe":       WPN_OBJ["BlackKnightGA"],
                 "Black Knight Glaive":         WPN_OBJ["BlackKnightHalberd"],
                 "Butchers Knife":              WPN_OBJ["ButchersKnife"],
                 "Dancer's Enchanted Swords":   WPN_OBJ["DancersTwinswords"],
                 "Dark Sword":                  WPN_OBJ["DarkSword"],
                 "Dragonslayer Swordspear":     WPN_OBJ["DragonslayerCross"],
                 "Dragonslayer Greataxe":       WPN_OBJ["DragonslayerGA"],
                 "Estoc":                       WPN_OBJ["Estoc"],
                 "Exile Greatsword":            WPN_OBJ["ExileGreatsword"],
                 "Farron Greatsword":           WPN_OBJ["FarronGreatsword"],
                 "Fume Ultra Greatsword":       WPN_OBJ["FumeUltraGS"],
                 "Gotthard Twinswords":         WPN_OBJ["GotthardTwinswords"],
                 "Gundyr's Halberd":            WPN_OBJ["GundyrHalberd"],
                 "Lothric's Holy Sword":        WPN_OBJ["LothricHolySword"],
                 "Morne's Great Hammer":        WPN_OBJ["MornesHammer"],
                 "Profaned Greatsword":         WPN_OBJ["ProfanedGreatsword"],
                 "Smough's Great Hammer":       WPN_OBJ["SmoughsHammer"],
                 "Sunlight Straight Sword":     WPN_OBJ["SunlightSword"],
                 "Twin Princes' Sword":         WPN_OBJ["TwinPrinceSword"],
                 "Washing Pole":                WPN_OBJ["WashingPole"],
                 "Witch's Locks":               WPN_OBJ["WitchLocks"],
                 "Wolf Knight Greatsword":      WPN_OBJ["WolfGreatsword"],
                 "Yhorm's Great Machete":       WPN_OBJ["YhormsMachete"],
                 "Alva Set":                    ARMOR_OBJ["Alva_F"],
                 "Catarina Set":                ARMOR_OBJ["Catarina_F"],
                 "Cathedral Knight Set":        ARMOR_OBJ["Cathedral_F"],
                 "Dark Set":                    ARMOR_OBJ["Dark_F"],
                 "Dragonscale Set":             ARMOR_OBJ["Dragonscale_F"],
                 "Dragonslayer Set":            ARMOR_OBJ["Dragonslayer_F"],
                 "Drang Set":                   ARMOR_OBJ["Drang_F"],
                 "Elite Knight Set":            ARMOR_OBJ["EliteKnight_F"],
                 "Fallen Knight Set":           ARMOR_OBJ["FallenKnight_F"],
                 "Faraam Set":                  ARMOR_OBJ["Faraam_F"],
                 "Firekeeper Set":              ARMOR_OBJ["Firekeeper_F"],
                 "Havel's Set":                 ARMOR_OBJ["Havel_F"],
                 "Undead Legion Set":           ARMOR_OBJ["Legion_F"],
                 "Lorian's Set":                ARMOR_OBJ["Lorian_F"],
                 "Painting Guardian Set":       ARMOR_OBJ["Painting_F"],
                 "Silver Knight Set":           ARMOR_OBJ["SilverKnight_F"],
                 "Thorns Set":                  ARMOR_OBJ["Thorns_F"],
                 "Winged Knight Set":           ARMOR_OBJ["WingedKnight_F"],
                 "Wolf Knight Set":             ARMOR_OBJ["WolfKnight_F"],
                 "Bonewheel Shield":            SHIELD_OBJ["Bonewheel"],
                 "Dragonslayer Greatshield":    SHIELD_OBJ["Dragonslayer"],
                 "Golden Wing Crest Shield":    SHIELD_OBJ["GoldenWingCrest"],
                 "Havel's Shield":              SHIELD_OBJ["Havels"],
                 "Llewellyn Shield":            SHIELD_OBJ["Llewellyn"],
                 "Silver Knight Shield":        SHIELD_OBJ["SilverKnight"],
                 "Target Shield":               SHIELD_OBJ["Target"],
                 "Gold Pine Resin +20":         CONS_OBJ["GoldResin_20"],
                 "Repaired a Ring!":            CONS_OBJ["Repaired"]}

LOOT_MISF   =   {"Chest Broken":                MISF_OBJ["Chest"],
                 "Confused!":                   MISF_OBJ["Confused"],
                 "Cursed!":                     MISF_OBJ["Cursed"],
                 "Guantlets Broken":            MISF_OBJ["Hand"],
                 "Helm Broken":                 MISF_OBJ["Head"],
                 "Leggings Broken":             MISF_OBJ["Leg"],
                 "Left Hand 1 Broken":          MISF_OBJ["LH1"],
                 "Left Hand 2 Broken":          MISF_OBJ["LH2"],
                 "Left Hand 3 Broken":          MISF_OBJ["LH3"],
                 "Lucked Out!":                 MISF_OBJ["Lucky"],
                 "Right Hand 1 Broken":         MISF_OBJ["RH1"],
                 "Right Hand 2 Broken":         MISF_OBJ["RH2"],
                 "Right Hand 3 Broken":         MISF_OBJ["RH3"],
                 "Ring 1 Broken":               MISF_OBJ["Ring1"],
                 "Ring 2 Broken":               MISF_OBJ["Ring2"],
                 "Ring 3 Broken":               MISF_OBJ["Ring3"],
                 "Ring 4 Broken":               MISF_OBJ["Ring4"],
                 "Spell Forgotten":             MISF_OBJ["Spell"],
                 "Tripped!":                    MISF_OBJ["Tripped"]}

if(ENABLE_USER_LOOT == True):
    enableUserLoot()

#==============================================================================#
#                   COLORS DEFINITIONS                                         # 
#==============================================================================#
# Color Defs.   =       (R,   G,   B)
RED 	        =       (237, 28,  36)
ORANGE          =       (255, 69,  0)
YELLOW 	        =       (241, 255, 0)
GREEN 	        =       (78,  255, 87)
BLUE 	        =       (25,  25,  112)
PURPLE 	        =       (203, 0,   255)
CYAN            =       (0,   255, 255)
WHITE           =       (255, 255, 255)
BLACK           =       (0,   0,   0)

# Initial Text Color
TXT_COLOR = PURPLE

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

def includePyro():
    global LOOT_CMN; global LOOT_RARE; global LOOT_ULTRA;

    LOOT_ULTRA.update({"Black Serpent":         SPELL_OBJ["BlackSerpent"],
                       "Carthus Flame Arc":     SPELL_OBJ["CarthusFlameArc"],
                       "Chaos Bed Vestiges":    SPELL_OBJ["ChaosBedVestiges"],
                       "Great Chaos Fire Orb":  SPELL_OBJ["GreatChaosFireOrb"],
                       "Warmth":                SPELL_OBJ["Warmth"]})
    LOOT_RARE.update({"Great Combustion":       SPELL_OBJ["GreatCombustion"],
                      "Chaos Storm":            SPELL_OBJ["ChaosStorm"]})

def setTxtColor(color):
    global TXT_COLOR
    
    TXT_COLOR = color

def textChanger():
    global TXT_COLOR; global TXT_CHANGER;
    global RED; global ORANGE; global YELLOW; global GREEN;
    global BLUE; global PURPLE; global CYAN; global WHITE

    tempColor   = TXT_COLOR
    
    inDONE      = dks.Rect((368, 0), (32, 32))
    inRED       = dks.Rect((24, 43), (60, 64))
    inORANGE    = dks.Rect((119, 43), (60, 64))
    inYELLOW    = dks.Rect((217, 43), (60, 64))
    inGREEN     = dks.Rect((313, 43), (60, 64))
    inBLUE      = dks.Rect((24, 118), (60, 64))
    inPURPLE    = dks.Rect((119, 118), (60, 64))
    inCYAN      = dks.Rect((217, 118), (60, 64))
    inWHITE     = dks.Rect((313, 118), (60, 64))

    while(TXT_CHANGER):

        pos = dks.mouse.get_pos()
        CL.tick(60)
        
        screen.blit(CHNGR_MAIN, (0, 0))

        if(tempColor == RED):
            screen.blit(CHNGR_RED, (0, 0))
        elif(tempColor == ORANGE):
            screen.blit(CHNGR_ORANGE, (0, 0))
        elif(tempColor == YELLOW):
            screen.blit(CHNGR_YELLOW, (0, 0))
        elif(tempColor == GREEN):
            screen.blit(CHNGR_GREEN, (0, 0))
        elif(tempColor == BLUE):
            screen.blit(CHNGR_BLUE, (0, 0))
        elif(tempColor == PURPLE):
            screen.blit(CHNGR_PURPLE, (0, 0))
        elif(tempColor == CYAN):
            screen.blit(CHNGR_CYAN, (0, 0))
        elif(tempColor == WHITE):
            screen.blit(CHNGR_WHITE, (0, 0))

        if(inDONE.collidepoint(pos) == 1):
            screen.blit(CHNGR_CONFIRM, (368, 0))
            
        dks.display.update()
        
        for event in dks.event.get():
            
            if event.type == dks.MOUSEBUTTONUP and (inRED.collidepoint(pos) == 1):
                tempColor = RED
            elif event.type == dks.MOUSEBUTTONUP and (inORANGE.collidepoint(pos) == 1):
                tempColor = ORANGE
            elif event.type == dks.MOUSEBUTTONUP and (inYELLOW.collidepoint(pos) == 1):
                tempColor = YELLOW
            elif event.type == dks.MOUSEBUTTONUP and (inGREEN.collidepoint(pos) == 1):
                tempColor = GREEN
            elif event.type == dks.MOUSEBUTTONUP and (inBLUE.collidepoint(pos) == 1):
                tempColor = BLUE
            elif event.type == dks.MOUSEBUTTONUP and (inPURPLE.collidepoint(pos) == 1):
                tempColor = PURPLE
            elif event.type == dks.MOUSEBUTTONUP and (inCYAN.collidepoint(pos) == 1):
                tempColor = CYAN
            elif event.type == dks.MOUSEBUTTONUP and (inWHITE.collidepoint(pos) == 1):
                tempColor = WHITE
            elif event.type == dks.MOUSEBUTTONUP and (inDONE.collidepoint(pos) == 1):
                if not (MUTE_FX):
                    switch2_fx.play()
                setTxtColor(tempColor)
                TXT_CHANGER = False
            #If the program is closed, exit:
            elif event.type == dks.QUIT:
                RUNNING = False
                dks.quit()
                sys.exit()
                

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
    elif((cmn_rand >= 100) & (cmn_rand < 755)): #65.5% Chance, 1 common
        currentRoll += "1 Common"
    elif(cmn_rand >= 755): #24.5% Chance, 2 common
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

    print("IP: ", INCL_PYRO)
    print("DIFF: ", DIFF)
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, CMN_COIN, (10, 258), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, CMN_COIN, (10, 258), 255-i)
                blitAlpha(screen, LOOT_CMN[currentLoot1], (20, 230), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, CMN_COIN, (166, 258), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                blitAlpha(screen, CMN_COIN, (166, 258), 255-i)
                blitAlpha(screen, LOOT_CMN[currentLoot2], (176, 230), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, RARE_COIN, (323, 258), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, RARE_COIN, (323, 258), 255-i)
                blitAlpha(screen, LOOT_RARE[currentLoot3], (333, 230), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, RARE_COIN, (480, 258), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, RARE_COIN, (480, 258), 255-i)
                blitAlpha(screen, LOOT_RARE[currentLoot4], (490, 230), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, ULTRA_COIN, (636, 258), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                blitAlpha(screen, ULTRA_COIN, (636, 258), 255-i)
                blitAlpha(screen, LOOT_ULTRA[currentLoot5], (648, 230), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
                dks.display.update()
                CL.tick(600)

            LOOT_5ON = True

    elif(category.lower() == "misfortune"):
        
        if(spot == 1):

            currentLoot6 = grabLoot("misfortune")
            
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
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, MISF_COIN, (795, 258), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
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
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                    
                blitAlpha(screen, MISF_COIN, (795, 258), 255-i)
                blitAlpha(screen, LOOT_MISF[currentLoot6], (805, 230), i)
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))
                dks.display.update()
                CL.tick(600)

            LOOT_6ON = True
            
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
                INTRO = 5
            
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
#                   DIFFICULTY SELECT SCREEN                                   # 
#==============================================================================#

if(INTRO == 3):

    inCONTINUE      =   dks.Rect((659, 516), (255, 73))
    inEASY          =   dks.Rect((39, 55),  (415, 444))
    inHARD          =   dks.Rect((496, 55), (415, 444))
    inPYRO          =   dks.Rect((465, 525), (150, 65))
    
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
        PYRO_OFF.set_alpha(i)
        DIFF_E.set_alpha(i)
        screen.blit(DIFF_E, (0, 0))
        screen.blit(PYRO_OFF, (465, 525))
        dks.display.update()
        CL.tick(120)

dks.event.clear()

while(INTRO == 3):

    pos = dks.mouse.get_pos()

    CL.tick(60)
    dks.display.update()
        
    if(DIFF == 1):
        screen.blit(DIFF_E, (0, 0))
    elif(DIFF == 2):
        INCL_PYRO = False
        screen.blit(DIFF_H, (0, 0))
        screen.blit(PYRO_DISABLE, (465, 525))
    
    if(inCONTINUE.collidepoint(pos) == 1):
        if(DIFF == 1):
            if(INCL_PYRO):
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_ON, (465, 525))
                dks.display.update()
            if not (INCL_PYRO):
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_OFF, (465, 525))
                dks.display.update()
                
        elif(DIFF == 2):
            screen.blit(DIFF_H2, (0, 0))
            screen.blit(PYRO_DISABLE, (465, 525))
            dks.display.update()
            
    if((INCL_PYRO) and (DIFF == 1)):
        screen.blit(PYRO_ON, (465, 525))
    elif ((not (INCL_PYRO)) and (DIFF == 1)):
        screen.blit(PYRO_OFF, (465, 525))
            
    #Event Handler:
    for event in dks.event.get():

        if event.type == dks.MOUSEBUTTONUP and (inCONTINUE.collidepoint(pos) == 1):
            select_fx.play()
            INTRO = 4

        elif event.type == dks.MOUSEBUTTONUP and (inEASY.collidepoint(pos) == 1):
            if(DIFF == 2):
                switch2_fx.play()
                DIFF = 1

        elif event.type == dks.MOUSEBUTTONUP and (inHARD.collidepoint(pos) == 1):
            if(DIFF == 1):
                switch2_fx.play()
                DIFF = 2

        elif event.type == dks.MOUSEBUTTONUP and (inPYRO.collidepoint(pos) == 1):
            if(DIFF == 1):
                switch_fx.play()
                if(INCL_PYRO):
                    INCL_PYRO = False
                else:
                    INCL_PYRO = True                
                
        #If the program is closed, exit:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()    
    
if((INCL_PYRO == True) and (DIFF == 1)):
    includePyro()
#==============================================================================#
#                   FOURTH INTRO SCREEN: RULES OF R2R                          # 
#==============================================================================#

if(INTRO == 4):

    inSTART     =   dks.Rect((129, 531), (166, 60))
    
    #Fade out
    for i in range(255): 
        screen.fill((0, 0, 0))
        if(DIFF == 1):
            if(INCL_PYRO):
                PYRO_ON.set_alpha(255-i)
                DIFF_E2.set_alpha(255-i)
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_ON, (465, 525))
                
            elif(INCL_PYRO == False):
                PYRO_OFF.set_alpha(255-i)
                DIFF_E2.set_alpha(255-i)
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_OFF, (465, 525))
                
        elif(DIFF == 2):
            PYRO_DISABLE.set_alpha(255-i)
            DIFF_H2.set_alpha(255-i)
            screen.blit(DIFF_H2, (0, 0))
            screen.blit(PYRO_DISABLE, (465, 525))
            
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

while(INTRO == 4):

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
            INTRO = 5

        #If the program is closed, exit:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()
            
#==============================================================================#
#                   MAIN PROGRAM LOOP / HOME SCREEN                            # 
#==============================================================================#

if(INTRO == 5):
    
    inGEM       =   dks.Rect((109, 73),  (108, 108))
    inRESET     =   dks.Rect((358, 497), (248, 60))
    inCOMM1     =   dks.Rect((20,  230), (125, 216))
    inCOMM2     =   dks.Rect((176, 230), (125, 216))
    inRARE1     =   dks.Rect((333, 230), (125, 216))
    inRARE2     =   dks.Rect((490, 230), (125, 216))
    inULTRA     =   dks.Rect((648, 230), (125, 216))
    inMISF      =   dks.Rect((802, 230), (125, 216))
    inTXTC      =   dks.Rect((890, 22),  (42, 41))
    inABT       =   dks.Rect((890, 68),  (40, 40))
    inMUTE      =   dks.Rect((20, 517),  (29, 25))
    
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
        UNMUTE_ICON.set_alpha(i)
        screen.blit(MN_MAIN, (0, 0))
        screen.blit(UNMUTE_ICON, (20, 517)) 
        dks.display.update()
        CL.tick(120)

dks.event.clear()

while(RUNNING):

    LOOT_CLICK1 = False;    LOOT_CLICK2 = False
    LOOT_CLICK3 = False;    LOOT_CLICK4 = False
    LOOT_CLICK5 = False;    LOOT_CLICK6 = False
    
    pos = dks.mouse.get_pos()

    CL.tick(120)

    if((inGEM.collidepoint(pos) == 1) & (TXT_CHANGER == False)):
        screen.blit(MN_L, (0, 0))
        
    elif((inRESET.collidepoint(pos) == 1) & (TXT_CHANGER == False)):
        screen.blit(MN_R, (0, 0))
        
    else:
        screen.blit(MN_MAIN, (0, 0))

    if((inCOMM1.collidepoint(pos) == 1) & (LOOT_1ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot1, 1, (TXT_COLOR)), (612, 178))
        
    if((inCOMM2.collidepoint(pos) == 1) & (LOOT_2ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot2, 1, (TXT_COLOR)), (612, 178))

    if((inRARE1.collidepoint(pos) == 1) & (LOOT_3ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot3, 1, (TXT_COLOR)), (612, 178))

    if((inRARE2.collidepoint(pos) == 1) & (LOOT_4ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot4, 1, (TXT_COLOR)), (612, 178))

    if((inULTRA.collidepoint(pos) == 1) & (LOOT_5ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot5, 1, (TXT_COLOR)), (612, 178))

    if((inMISF.collidepoint(pos) == 1) & (LOOT_6ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot6, 1, (TXT_COLOR)), (612, 178)) 
        
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

    if(LOOT_6ON):
        screen.blit(LOOT_MISF[currentLoot6], (805, 230))

    if(MUTE_FX):
        screen.blit(MUTE_ICON, (20, 517))
    elif(not MUTE_FX):
        screen.blit(UNMUTE_ICON, (20, 517))
            
    if(inABT.collidepoint(pos) == 1):
        screen.blit(ABOUT_SCREEN, (187, 112))
        screen.blit(FNT2.render(ABOUT_TXT[0], 1, (TXT_COLOR)), (230, 140))
        screen.blit(FNT2.render(ABOUT_TXT[1], 1, (TXT_COLOR)), (200, 180))
        screen.blit(FNT2.render(ABOUT_TXT[2], 1, (TXT_COLOR)), (200, 204))
        screen.blit(FNT2.render(ABOUT_TXT[3], 1, (TXT_COLOR)), (200, 228))
        screen.blit(FNT2.render(ABOUT_TXT[4], 1, (TXT_COLOR)), (200, 252))
        screen.blit(FNT2.render(ABOUT_TXT[5], 1, (TXT_COLOR)), (200, 276))
        screen.blit(FNT2.render(ABOUT_TXT[6], 1, (TXT_COLOR)), (200, 300))
        screen.blit(FNT2.render(ABOUT_TXT[7], 1, (TXT_COLOR)), (200, 324))
        screen.blit(FNT2.render(ABOUT_TXT[8], 1, (TXT_COLOR)), (200, 348))
        screen.blit(FNT2.render(ABOUT_TXT[9], 1, (TXT_COLOR)), (200, 372))
        screen.blit(FNT2.render(ABOUT_TXT[10], 1, (TXT_COLOR)), (200, 396))
        screen.blit(FNT2.render(ABOUT_TXT[11], 1, (TXT_COLOR)), (200, 420))
        screen.blit(FNT.render(CAPTION, 1, (TXT_COLOR)), (324, 445))
        dks.display.update()

    dks.display.update()
    
    #Event Handler:
    for event in dks.event.get():

        #If the program is closed, exit:
        if event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()

        elif event.type == (dks.MOUSEBUTTONUP) and (inRESET.collidepoint(pos) == 1) and (TXT_CHANGER == False):
            if not (MUTE_FX):
                switch2_fx.play()
            resetLoot()
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inGEM.collidepoint(pos) == 1) and (TXT_CHANGER == False):
            if not (MUTE_FX):
                coin_fx.play()
            generateRoll()
            dks.event.clear(dks.MOUSEBUTTONUP)
            
        elif event.type == (dks.MOUSEBUTTONUP) and (inCOMM1.collidepoint(pos) == 1) and (LOOT_CLICK1 == False) and (TXT_CHANGER == False):
            LOOT_CLICK1 = True
            lootCoin("common", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inCOMM2.collidepoint(pos) == 1) and (LOOT_CLICK2 == False) and (TXT_CHANGER == False):
            LOOT_CLICK2 = True
            lootCoin("common", 2)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inRARE1.collidepoint(pos) == 1) and (LOOT_CLICK3 == False) and (TXT_CHANGER == False):
            LOOT_CLICK3 = True
            lootCoin("rare", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inRARE2.collidepoint(pos) == 1) and (LOOT_CLICK4 == False) and (TXT_CHANGER == False):
            LOOT_CLICK4 = True
            lootCoin("rare", 2)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inULTRA.collidepoint(pos) == 1) and (LOOT_CLICK5 == False) and (TXT_CHANGER == False):
            LOOT_CLICK5 = True
            lootCoin("ultra", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inMISF.collidepoint(pos) == 1) and (LOOT_CLICK6 == False) and (TXT_CHANGER == False):
            LOOT_CLICK6 = True
            lootCoin("misfortune", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inMUTE.collidepoint(pos) == 1):
            if(MUTE_FX):
                switch2_fx.play()
                MUTE_FX = False
            else:
                MUTE_FX = True
            dks.event.clear(dks.MOUSEBUTTONUP)

        elif event.type == (dks.MOUSEBUTTONUP) and (inTXTC.collidepoint(pos) == 1) and (TXT_CHANGER == False):
            if not (MUTE_FX):
                switch_fx.play()
            TXT_CHANGER = True
            textChanger()
            dks.event.clear(dks.MOUSEBUTTONUP)
    



    



    
    
    


