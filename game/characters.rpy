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
define Devon  = CharTemplate("Devon", file="vb_low1.ogg",         speaker=("tamati"))

# Misc images
image asset base = "images/char/tamati/neutral_base.png"
image asset eyes = "images/char/tamati/neutral_eyes.png"
image asset mouth = "images/char/tamati/neutral_mouth.png"
image asset grimace = "images/char/tamati/grimace_mouth_i.png"
image asset closed = "images/char/tamati/closed_eyes.png"


define npc2 = Character("npc2")
define Manager = Character("Manager")
define Phone = Character("AI")
define narrator = Character (None)
define Serene = Character("Serene")
define Panna = Character("Panna")
define Moonga = Character("Moonga")
define Sunela = Character("Sunela")
define npc1 = Character("npc1")
define Statue = Character("Suspicious Statue")
define Professor = Character("Professor")
define Mama = Character("Mama")
define Amara = Character("Amara")
define Customer = Character("Customer") 
define Elder = Character("Elder")
define Bell = Character("Bell Man")
define Leif = Character("Leif")
define Trisha = Character("Trisha")
define Customer6 = Character("Customer 6")
define Customer7 = Character("Customer 7")
define Customer9 = Character("Customer 9")
define Customer12 = Character("Customer 12")
define Aelrie = Character("Aelrie")
define Troll1 = Character("Stoic Troll")
define Troll2 = Character("Curious Troll")
define IcyGoblin = Character("Iced-Out Goblin")
define Elowen = Character("Elowen")
define Mage = Character("The Mage")


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
