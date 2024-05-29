# Declare characters used by this game. The color argument colorizes the
# name of the character.

image Devon neutral     = Portrait("tamati", "neutral", (298, 209), (339, 277))
image Devon neutral closed = Portrait("tamati", "neutral", (298, 209, None, "closed"), (339, 277))
image Devon scowl       = Portrait("tamati", "neutral", (298, 209, "scowl"), (339, 277))
image Devon scowl aside = Portrait("tamati", "neutral", (298, 209, "scowlaside"), (339, 277)) 
image Devon grimace     = Portrait("tamati", "neutral", (298, 209, "scowl"), (339, 277, None, "grimace"))
        
##############################################################################
# Character definitions

define nv      = CharTemplate(quote=False, mode=nvl)


# Misc images
image asset base = "images/char/tamati/neutral_base.png"
image asset eyes = "images/char/tamati/neutral_eyes.png"
image asset mouth = "images/char/tamati/neutral_mouth.png"
image asset grimace = "images/char/tamati/grimace_mouth_i.png"
image asset closed = "images/char/tamati/closed_eyes.png"

init python:
    def character_callback(event, **kwargs):
        if event == "end":
            renpy.music.play("shuffle.mp3", channel="audio", relative_volume=0.3)
    
define letter = nvl_narrator
define Devon  = CharTemplate("Devon", file="vb_low1.ogg",         speaker=("tamati"))
define se = Character(None, ctc="ctc_blink_serene", ctc_position="fixed", callback=character_callback) #window_background=Frame("gui/textbox_back.png", 1, 1))
define npc2 = Character("npc2", ctc="continimg")
define Manager = Character("Manager", ctc="continimg", callback=character_callback)
define Phone = Character("AI", ctc="continimg", callback=character_callback)
define narrator = Character (None, ctc="ctc_blink", ctc_position="fixed", callback=character_callback)
define Serene = Character("Serene", ctc="continimg", callback=character_callback)
define Panna = Character("Panna", ctc="continimg", callback=character_callback)
define Moonga = Character("Moonga", ctc="continimg", callback=character_callback)
define Sunela = Character("Sunela", ctc="continimg", callback=character_callback)
define npc1 = Character("npc1", ctc="continimg")
define Statue = Character("Suspicious Statue", ctc="continimg", callback=character_callback)
define Professor = Character("Professor", ctc="continimg", callback=character_callback)
define Mama = Character("Mama", ctc="continimg", callback=character_callback)
define Amara = Character("Amara", ctc="continimg", callback=character_callback)
define Customer = Character("Customer", ctc="continimg", callback=character_callback) 
define Elder = Character("Elder", ctc="continimg", callback=character_callback)
define Bell = Character("Bell Man", ctc="continimg", callback=character_callback)
define Leif = Character("Leif", ctc="continimg", callback=character_callback)
define Trisha = Character("Trisha", ctc="continimg", callback=character_callback)
define Customer6 = Character("Customer 6", ctc="continimg", callback=character_callback)
define Customer7 = Character("Customer 7", ctc="continimg", callback=character_callback)
define Customer9 = Character("Customer 9", ctc="continimg", callback=character_callback)
define Customer12 = Character("Customer 12", ctc="continimg", callback=character_callback)
define Aelrie = Character("Aelrie", ctc="continimg", callback=character_callback)
define Troll1 = Character("Stoic Troll", ctc="continimg", callback=character_callback)
define Troll2 = Character("Curious Troll", ctc="continimg", callback=character_callback)
define IcyGoblin = Character("Iced-Out Goblin", ctc="continimg", callback=character_callback)
define Elowen = Character("Elowen", ctc="continimg", callback=character_callback)
define Mage = Character("The Mage", ctc="continimg", callback=character_callback)


# Blob's layers and mouth movement            
layeredimage npc1:
    always:
        "npc1.png"
    
    group eyes auto:
        attribute normal default:
            "npc1_eyes_normal"

    group mouth:
        attribute mouth_A:
            "mouth_open.png"
        attribute mouth_B:
            "mouth_half.png"
        attribute mouth_C:
            "mouth_open.png"
        attribute mouth_D:
            "mouth_open.png"
        attribute mouth_E:
            "mouth_open.png"
        attribute mouth_F:
            "mouth_half.png"
        attribute mouth_G:
            "mouth_half.png"
        attribute mouth_H:
            "mouth_half.png"
        attribute mouth_X default:
            "mouth_closed.png"

layeredimage npc2:
    always:
        "npc1.png"
    
    group eyes:
        attribute eyes_open default:
            "npc1_eyes_normal"
        
    group mouth:
        attribute mouth_A:
            "mouth_open.png"
        attribute mouth_B:
            "mouth_half.png"
        attribute mouth_C:
            "mouth_open.png"
        attribute mouth_D:
            "mouth_open.png"
        attribute mouth_E:
            "mouth_open.png"
        attribute mouth_F:
            "mouth_half.png"
        attribute mouth_G:
            "mouth_half.png"
        attribute mouth_H:
            "mouth_half.png"
        attribute mouth_X default:
            "mouth_closed.png"



##### Experimental Stuff
define nv = CharTemplate(quote=False, mode=nvl)
image Serene neutral     = Portrait("Serene", "neutral", (0, 160), (-980, -160))
image side Serene = "side_image.png"
image npc1 cut = LayeredImageMask("npc1", mask="circle")
