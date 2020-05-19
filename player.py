# Bring comments to order because.. it's getting away from me

# Health, equipment, spell list (if applicable), attacks/weapons?, bonuses, back story?, status changes?, proficiencies
# Class-, level-, or race-specific bonuses
# For player background, add personality traits, ideals, bonds, flaws?
# Race-dependent - Alignment(?), Age, Size(Height and weight), Speed, Language, subraces
# Class-dependent - Hit die, primary ability(?), Saving throw proficiencies, armor/weapon proficiencies
# Multiclassing? RIP to Me

# Classes: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
# (Major) Races: Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Half-Orc, Halfling, Human, Tiefling
# Backgrounds: 18 located in PHB alone

# Current HP vs Max HP
# Saving throws and skills based on ability score/mod
# Spellcasters - spellcasting ability, spell save DC, Spell attack bonus
import math


class Player:
    def __init__(self, playerName):
        self.player_name = playerName
        self.player_level = self.get_player_level()
        self.player_race = self.get_player_race()
        self.player_class = self.get_player_class()
        self.player_background = self.get_player_background()
        self.player_alignment = self.get_player_alignment()
        self.player_str, self.player_dex, self.player_con, self.player_int, self.player_wis, self.player_cha \
            = self.get_ability_scores()
        self.str_mod, self.dex_mod, self.con_mod, self.int_mod, self.wis_mod, self.cha_mod \
            = self.calc_ability_modifiers()
        self.player_max_hit_points = "PHB P1st Level - self.con_mod + max hit die for class"
        self.player_initiative_mod = "self.dex_mod + ??more??proficiency?"
        self.player_ac = "PHB P145 (sometimes + self.dex_mod)"
        self.player_prof_bonus = "Based on level"
        # Skills may be good as a dict?
        self.player_skills_lst = "18 skills, calculated with relevant ability mod + self.player_prof_bonus  (if " \
                                 "chosen to be proficient) + other modifiers"

    def get_player_level(self):
        self.player_level = input("What is your player's level?")
        return self.player_level

    def get_player_race(self):
        self.player_race = input("What is your player's race?")
        return self.player_race

    def get_player_class(self):
        self.player_class = input("What is your player's class?")
        return self.player_class

    def get_player_background(self):
        self.player_background = input("What is your player's background?")
        return self.player_background

    def get_player_alignment(self):
        self.player_alignment = input("What is your player's alignment?")
        return self.player_alignment

    def get_ability_scores(self):
        self.player_str = int(input("What is the STR stat?"))
        self.player_dex = int(input("What is the DEX stat?"))
        self.player_con = int(input("What is the CON stat?"))
        self.player_int = int(input("What is the INT stat?"))
        self.player_wis = int(input("What is the WIS stat?"))
        self.player_cha = int(input("What is the CHA stat?"))
        return self.player_str, self.player_dex, self.player_con, self.player_int, self.player_wis, self.player_cha

    def calc_ability_modifiers(self):
        self.str_mod = math.floor((self.player_str - 10) / 2)
        self.dex_mod = math.floor((self.player_dex - 10) / 2)
        self.con_mod = math.floor((self.player_con - 10) / 2)
        self.int_mod = math.floor((self.player_int - 10) / 2)
        self.wis_mod = math.floor((self.player_wis - 10) / 2)
        self.cha_mod = math.floor((self.player_cha - 10) / 2)
        return self.str_mod, self.dex_mod, self.con_mod, self.int_mod, self.wis_mod, self.cha_mod

    def display_player_info(self):
        return "Player name: " + self.player_name + \
               "\nPlayer level: " + self.player_level + \
               "\nPlayer race: " + self.player_race + \
               "\nPlayer class: " + self.player_class + \
               "\nSTR: " + str(self.player_str) + " MOD: " + str(self.str_mod) + \
               "\nDEX: " + str(self.player_dex) + " MOD: " + str(self.dex_mod) + \
               "\nCON: " + str(self.player_con) + " MOD: " + str(self.con_mod) + \
               "\nINT: " + str(self.player_int) + " MOD: " + str(self.int_mod) + \
               "\nWIS: " + str(self.player_wis) + " MOD: " + str(self.wis_mod) + \
               "\nCHA: " + str(self.player_cha) + " MOD: " + str(self.cha_mod)
