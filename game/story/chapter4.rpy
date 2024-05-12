label chapter4:

    Bell "*DONG* SUNRISE *DONGGGGG* SUNRIIIIIISE."

    "You can still be seen in bed before giving off a deep, heavy sigh."
    "(I'm never getting used to this.)"
    Amara "Sereneeeee! Are ya awakeeeeee!"
    Serene "Noooooooo."
    Amara "(laughs) Come down. I cooked breakfastttttt."
    Serene "*now suddenly full of energy* I'M COMIN'."
    
    # - [Transition to downstairs in Amara's shop]
    Amara "It's bread and some soup I made."
    "You peer into the bowl."
    Serene "What kind of soup is it?"
    Amara "Like, the really good kind? Try it and find out."
    "You grab a spoon and have a sip."
    Serene "Oh, this is good. What kind of seasoning is in this? It has some spice."
    Amara "Alright, I'll fess up. Leif cooked it." 
    Serene "Ah, makes sense."
    Amara "I mean I helped!"
    Serene "Right."
    Amara "I'm serious!"
    Serene "I know."
    Amara "So, I heard you both had an eventful day yesterday. A little elf girl, right?"
    Serene "*Taking another spoonful of soup* Poor girl, she was really having a bad day. She was soaking wet out there in the rain."
    Amara "And you had chocolate."
    Serene "Right, we gave her some to cheer her up."
    Amara "No, you don't understand. You guys had chocolate."
    Serene "...Uh huh...? You've said that already...?"
    Amara "DO YOU NOT KNOW HOW EXPENSIVE. CHOCOLATE. IS. There is a reason elves have a monopoly on the market."
    Serene "...OH. You know, you have a point there actually."
    Amara "Some countries even pass the cocoa beans around in lieu of currency." 
    extend "It's that valuable. And you offered to waste it on a couple of drinks?!"
    Serene "I'm sorry...? I honestly didn't even think about it like that."
    Amara "WITHOUT ME?! *Amara begins weeping fake tears*"
    Serene "Amara..."
    Amara "Ahhhh, I'm just foolin' with ya. Leif saved some of those truffles for me too."
    Serene "*huge sigh of relief* Okay...You got me. (nervous laughter)"
    "(Don't make Amara mad. Noted.)"
    $ renpy.notify("You've unlocked: Context (!)")
    # - [Notebook Update: Context (!) Added.]
    Amara "So, what are your plans for today, ma'am?"
    Serene "Good question. Uh, we're just figuring it out as we go I guess." 
    Amara "Well, keep it going! Sounds like you've gotten your first customer already."
    Serene "About that. I don't know about asking people to pay me for this if this is how things are going to go." 
    Serene "I feel a little bad focusing on the bottom line?"
    Amara "Meh, I already told you that your dues are paid." 
    Amara "You could sit around on your bed wasting away, but what's the fun in that?" 
    Amara "Go out there!"
    extend " Do something!" 
    extend " That's what I always say!" 
    Amara "There's more to life than just making money!"
    Serene "Truly motivational words I see, Amara. (chuckle)"
    Amara "You already know the story. I'm special because I have something to prove with this business, but it's not about the money." 
    Amara "If I just wanted some gold, I never would have sailed all the way to this continent."
    Serene "Hold on, did you say continent. As in crossing the ocean?! You?"
    Amara "(Laughs) Is it really that hard to believe?"
    Amara "Yes, I'm not from here. Do you really not know?"
    Amara "Wait, of course you don't. I almost forgot you were summoned here."
    Serene "How much info are you holding out on me, Amara?"
    Amara "*shrugs* WELL, look at how loud those birds are chirping, sounds like you need to visit your little friend across the road." 
    Amara "*hehehe* Okay bye-byeeeee! Have fun!"
    "Amara rushes to the back of her shop."
    "(Oh, I am absolutely coming back here later.)"
    
    # - [Transition: Leif's shop.]
    
    "As you enter your shop, you're immediately greeted by a sack of equipment."
    Serene "Gooood mornin--"
    "Of course, you trip over the bag of supplies on the floor."
    Leif "*shouting from another room* Serene?! Is that you?"
    "Leif enters the room."
    Leif "Ouch okay sorry about that. *Leif helps Serene back up* Probably shouldn't have left that by the door."
    Serene "It's okay, but what is all of this?"
    Leif "Ready for an expedition?"
    Serene "You're kidding, right?"
    "Leif stands there expectantly."
    Serene "You're not kidding. Okay. What are we working with...?"
    "You dig through the bag and see maps, bottles of water, wrapped bread, and a knife, among other things."
    
    Leif "Can I consider that a yes?"
    Serene "Do I have a choice?"
    "Leif stands there with a grin."

menu:
    extend ""
    "Decline.":
        jump leif_adventure
    "Accept.":
        jump leif_adventure
    "Go back to Amara's.":
        jump leif_adventure
    "Kick him.":
        jump leif_adventure

label leif_adventure:
    Serene "...Yes."
    Leif "Perfect. Let's march."
    Serene "March?! You don't have a horse..? Or something?"
    Leif "Don't worry. Walking builds character." 
    
    # -[The screen transitions to a map with chibi character sprites exiting the city to the woods right outside "the city walls]
    Serene "So, where are we going exactly?"
    Leif "I've been tracking a crop of Angelica not too far from the city."
    Serene "Ouuu, so we're gathering some of it?"
    Leif "Right, it's a bit early since spring barely started, but it's a good time to gather roots."
    Serene "Why just the roots? You don't want the rest of it?"
    Leif "You could harvest the whole plant, but it's better to leave it mostly intact until summer. That's when you get the good stuff."
    Serene "Ah, that makes sense."
    Serene "Internally: Dang, this guy's serious."
    
    # - [The scene transitions back to a forest background]
    Serene "Oh, nice. I think I hear a stream nearby."
    Leif "We're close, then."
    
    # - *The sounds of the river stream grow louder*
    # - *A flowerbed of Sweet Woodruff can be seen nearby*
    Serene "These flowers look so beautiful. How long have you been coming here?"
    
    # - *A small breeze blows through*
    # - *Leif puts his bag down near the bed of flowers*
    # - *Leif gives an exaggerated grunt as he sits down*
   
    Serene "Okay, old man. (grin)"
    Leif "Ahhhh, how long has it been?" 
    #- *Serene "walks closer to inspect the flowers*
    Leif "I come here every few weeks or so, I guess. It's nice."
    "Serene flashback's to a memory of Aelrie Back home" 
    
    # - "Sea-salt truffles were really common!"
    
menu:
    extend ""
    "Enjoy the flowers.":
        jump leif_adventure2
    "\"Does this place remind you of home too?\"":
        jump leif_adventure2
    "Get up and find Angelica. We need to keep moving.":
        jump leif_adventure2
    "Kick him.":
        jump leif_adventure2

label leif_adventure2:
    Leif "(laughs) Did that bracelet give you mind-reading powers? Yes. My family stayed in the woods. We were in the fur trade."
    $ renpy.notify("You've unlocked: Context (!)")
    # - [Notebook Update: Context (!) Added.]
    Serene "Makes sense why you know so much about nature." 
    Serene "You didn't want to work with your parents?"
    Leif "It's one thing to hunt for survival, but the way everyone operated in that line of work...It made me question myself."
    "(Makes sense. Fur coats have been controversial for a long time.)"
menu:
    extend ""
    "\"Was the fur trade really that bad?\"":
        jump leif_adventure3
    "\"Sounds awful.\"":
        jump leif_adventure3
    "\"What were they doing?\"":
        jump leif_adventure3
    "\"Is that why you chose to write about food instead?\"":
        jump leif_adventure3

label leif_adventure3:
    Leif "I guess so. When you grow up learning about edible plants, and what animals enjoy, it's hard to forget about it." 
    Leif "I wanted to help people appreciate the food they eat a bit more-"
    Leif "The people who gathered the ingredients and grew the crops, the livestock sacrificed to keep us moving, and the people who put it altogether on a plate for you to eat." 
    "(I can feel his deep sense of respect for cuisine...)"
    Leif "Are you rested up? We're almost at the spot."
    Serene "Oh, right. Yeah, I'm ready."
    
    "The duo approaches the planted Angelica's."
    Serene "Ah, so that's what they look like."
    "Leif takes a spade out from his bag."
    Leif "Looks like I'm up."
    "Leif starts digging up the roots of a few plants, while leaving most of the other plants intact. You can sense Leif's care as he pulls."
    Serene "Wow, Leif. I didn't think you'd have such a green thumb for somebody of your size."
    Leif "If only you knew how many times I've heard that line. (laughs)"
    "Leif gathers a bundle of roots and packs them into his bag."
    Leif "All done."
    Serene "That was fast. It took us longer just getting here."
    Leif "Well, you know the saying, It's about the journey, not the destina--"
    "Suddenly there's loud shuffling in the bushes."
    Serene "Ouuu, are there deer here? Maybe we could feed them with--"
    "Leif rushes over and grabs Serene behind a tree."
    "Seconds later, two large trolls wielding clubs following a short third goblin wearing a stolen garb of jewelry walk through the bushes."
    Troll1 "Hiff Hiff."
    IcyGoblin "(Snickers)" 
    "The second large troll looks around."
    Troll2 "Smelly."
    IcyGoblin "Shut up. I talk. You walk."
    Troll1 "Hufffffff. Hiffffff."
    "The IcyGoblin drops his gold."
    IcyGoblin "What are ya standin there for? Pick it up!"
    "The large trolls drop their clubs. Two loud thuds come across, scaring away the birds."
    "Serene covers her mouth in horror."
    "Leif gestures towards Serene to back away."
    Leif "*whispering* I'll distract them." 
    "(Should I leave Leif behind and run for it?)"
menu:
    extend ""
    "Run":
        jump leif_adventure4
    "Wait.":
        jump leif_adventure4
    
label leif_adventure4:
    Serene "*whispering* No way. I can't."
    Troll2 "SMELLY. *The troll stands upright, looking and moving towards Leif and Serene*"
    IcyGoblin "Did I say you could leave? *The goblin walks closely behind the troll*"
    "The large troll stands next to the remaining Angelica's."
    IcyGoblin "This?"
    Troll2 "Hmfffff... *The large troll plomps on its butt before gently plucking one of the plants off the ground. Inspecting it 43with curiosity*"
    IcyGoblin "What the hell are you doin'. Pick up my gold I said. *The goblin is visibly pissed off*"
    "(It looks like they're distracted. Should we run now?)"
menu:
    extend ""
    "Run":
        jump leif_adventure5
    "Wait.":
        jump leif_adventure5

label leif_adventure5:
    "The Large Troll ignores the goblin, sniffing the flower."
    "The goblin looks over to the first large troll."
    IcyGoblin "You. C'mere. Bring the club."
    "The Large Troll slowly picks up its club and walks towards the others."
    Troll1 "Hifffffff."
    IcyGoblin "Smash."
    "(I don't like where this is going. Should we move now?)"
menu:
    extend ""
    "Run.":
        jump leif_adventure6
    "Wait.":
        jump leif_adventure6

    
label leif_adventure6:
    "The large troll raises its club."
    "The IcyGoblin points at the plants."
    IcyGoblin "Now."
    "In one blow the large troll flattens the entire crop of Angelicas. The leaves of nearby trees fall apart, including the leaves hiding Serene and Leif."
    "(I should have listened to Leif and ran when I had the chance. What now?)"
menu:
    extend ""
    "Run.":
        jump leif_adventure7
    "Wait.":
        jump leif_adventure7
    "Look at Leif.":
        jump leif_adventure7

label leif_adventure7:
    "Leif grabs a bottle out from his pack."
    Leif "Cover your face, Serene."
    Serene "W-what? Okay!"
    "Leif prepares to throw the bottle."
    IcyGoblin "THROW."
    "The Troll1 lifts his club to throw at Leif like a boomerang."
    Leif "What?!"
    "Leif freezes while the troll viscously throws its club at Leif."
    "An evoking sound is quickly overheard."
    "A loud ricochet."
    "The club is knocked off-target."
    IcyGoblin "Another...?! *The goblin stomps the ground repeatedly and looks at the second troll*" 
    extend " Stand!" 
    extend " Attack!!"
    extend "(More violent exclamations)"

    "Another evoking sound is overheard."
    "The first troll is immediately wrapped in purplish-black magical chains."
    IcyGoblin "*Clenching its teeth* Screw this." 
    IcyGoblin "*The globin takes out a poison-tipped knife*" 
    extend " Quit hidin' and FIGHT me."
    IcyGoblin "I've slain your kind several times OVER. You're worthless, I cou--"
    "Another evoking sound is heard."
    "The sound of metal scraping against itself in quick succession is heard."
    "The goblin disintegrates almost immediately."
    "A stone drops to the floor."
    "A mage emerges out from the trees and walks calmly towards the stone."
    Mage "You let this one talk more than usual, Elowen. Were you growing a liking to it, perhaps? (grin)"
    "A man, radiating heat, can be seen already in front of where the goblin was previously."
    "Elowen stands stoically in silence."
    "The mage picks up the stone, revealing itself to be a glistening dark purple marble."
    Mage "You can come out now. It's safe."
    "The bound troll continues to writhe in the magic chains, while the other stays seated with its Angelica, seemingly unbothered."
    Serene "What about the trolls?"
    Mage "(chuckles) Don't fret."
    "Elowen walks towards the stream to fill his bottle."
    "The mage calmly levitates and presses two fingers on the chained troll's forehead."
    Mage "Fateor."
    "The sound of shattered glass resonates."
    "What was previously a troll, reverts to a wild boar."
    Leif "...Now I remember...!"
    "The mage calmly walks over to the first large troll still admiring the Angelica, now lying on its back."
    Mage "Good girl...Now let's get you home... *gentle whisper* Fateor."
    "The troll returns to a young piglet."

    #jump chapter5
    return