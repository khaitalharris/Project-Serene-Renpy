label chapter4:
    #*DONG* 
    Bell "SUNRISE!" 
    #*DONGGGGG* 
    Bell "SUNRIIIIIISE!"

    narrator "You can still be seen in bed before giving off a deep, heavy sigh."
    se "(I'm never getting used to this.)"
    Amara "Sereneeeee! Are ya awakeeeeee!"
    Serene "Noooooooo."
    #Amara laughs
    Amara "Come down. I cooked breakfastttttt."
    #*now suddenly full of energy*
    Serene "I'M COMIN'."
    with fade
    # - [Transition to downstairs in Amara's shop]
    Amara "It's bread and some soup I made."
    narrator "You peer into the bowl."
    Serene "What kind of soup is it?"
    Amara "Like, the really good kind? Try it and find out."
    narrator "You grab a spoon and have a sip."
    Serene "Oh, this is good. What kind of seasoning is in this? {w=1.0}It has some spice!"
    Amara "Alright, I'll fess up. Leif cooked it." 
    Serene "Ah, makes sense."
    Amara "I mean I helped!"
    Serene "Right."
    Amara "I'm serious!"
    Serene "I know."
    Amara "So, I heard you both had an eventful day yesterday. A little elf girl, right?"
    narrator "You take another spoonful of soup."
    Serene "Poor girl, she was really having a bad day. She was soaking wet out there in the rain."
    Amara "And you had chocolate."
    Serene "Right, we gave her some to cheer her up."
    Amara "No, you don't understand. You guys had chocolate."
    Serene "...Uh huh...? You've said that already...?"
    play sound "SFX/wham.mp3" volume 0.75
    with vpunch
    Amara "DO YOU NOT KNOW HOW EXPENSIVE. {w=1.5}CHOCOLATE.{w=1.0} IS.{w=0.5} There is a reason elves have a monopoly on the market."
    Serene "...OH." 
    Serene "You know, you have a point there actually."
    Amara "Some countries even pass the cocoa beans around in lieu of currency. {w=3.0}It's {i}that{/i} valuable." 
    Amara "And you offered to waste it on a couple of drinks?!"
    Serene "I'm sorry...? I honestly didn't even think about it like that."
    play sound "SFX/wham.mp3" volume 0.75
    Amara "WITHOUT ME?!" with vpunch
    #*Amara begins weeping fake tears*"
    Serene "Amara..."
    Amara "Ahhhh, I'm just foolin' with ya. Leif saved some of those truffles for me too."
    # *huge sigh of relief* 
    Serene "Okay...You got me."
    #(nervous laughter)
    se "(Don't make Amara mad. {w=1.5}{i}Noted.{/i})"
    $ renpy.notify("You've unlocked: Context (!)")
    pause(2)
    # - [Notebook Update: Context (!) Added.]
    Amara "So, what are your plans for today, ma'am?"
    Serene "Good question. Uh, we're just figuring it out as we go I guess." 
    Amara "Well, keep it going! Sounds like you've gotten your first customer already."
    Serene "About that. I don't know about asking people to pay me for this if this is how things are going to go." 
    Serene "I feel a little bad focusing on the bottom line?"
    Amara "Meh, I already told you that your dues are paid." 
    Amara "You could sit around on your bed wasting away, but what's the fun in that?" 
    Amara "Go out there! {w=1.5} Do something! {w=1.5}That's what I always say!" 
    Amara "There's more to life than just making money!"
    Serene "Truly motivational words I see, Amara."
    #Amara chuckles
    Amara "You already know the story. I'm special because I have something to prove with this business, but it's not about the money." 
    Amara "If I just wanted some gold, I never would have sailed all the way to this continent."
    Serene "Hold on, did you say {i}continent?{/i} As in crossing the ocean?! You?"
    #Amara chuckles
    Amara "Is it really that hard to believe?"
    Amara "Yes, I'm not from here. Do you really not know?"
    Amara "Wait, of course you don't. I almost forgot you were summoned here."
    Serene "How much info are you holding out on me, Amara?"
    #Amara shrugs
    Amara "{i}WELL{/i}, look at how loud those birds are chirping, sounds like you need to visit your little friend across the road." 
    #Amara laughs
    Amara "Okay bye-byeeeee! Have fun!"
    narrator "Amara rushes to the back of her shop."
    se "(Oh, I am absolutely coming back here later.)"
    
    # - [Transition: Leif's shop.]
    
    narrator "As you enter your shop, you're immediately greeted by a sack of equipment."
    Serene "Gooood mornin--"
    play sound "SFX/crash.mp3" volume 0.5
    with hpunch
    pause(2.0)
    narrator "Of course, you trip over the bag of supplies on the floor."
    #*Leif shouts from another room*
    Leif "Serene?! Is that you?"
    narrator "Leif enters the room."
    Leif "Ouch. Okay, sorry about that."
    #*Leif helps Serene back up*  
    Leif "I probably shouldn't have left that by the door."
    Serene "It's okay, but what is all of this?"
    Leif "Ready for an expedition?"
    Serene "You're kidding, right?"
    narrator "Leif stands there expectantly."
    Serene "You're not kidding. {w=1.5}Okay. What are we working with...?"
    narrator "You dig through the bag and see maps, bottles of water, wrapped bread, and a knife, among other things."
    
    Leif "Can I consider that a yes?"
    Serene "Do I have a choice?"
    narrator "Leif stands there with a grin."

menu:
    extend ""
    "Decline.":
        jump leif_adventure
    "Accept.":
        jump leif_adventure
    "Kick him.":
        jump leif_adventure

label leif_adventure:
    Serene "...Yes."
    Leif "Perfect. Let's march."
    Serene "March?! You don't have a horse...? {w=1.5}Or something?"
    Leif "Don't worry. Walking builds character." 
    with fade
    # -[The screen transitions to a map with chibi character sprites exiting the city to the woods right outside "the city walls]
    Serene "So, where are we going exactly?"
    Leif "I've been tracking a crop of Angelica not too far from the city."
    Serene "Ouuu, so we're gathering some of it?"
    Leif "Right, it's a bit early since spring barely started, but it's a good time to gather roots."
    Serene "Why just the roots? You don't want the rest of it?"
    Leif "You could harvest the whole plant, but it's better to leave it mostly intact until summer. That's when you get the good stuff."
    Serene "Ah, that makes sense."
    se "(Dang, this guy's serious.)"
    with fade
    # - [The scene transitions back to a forest background]
    Serene "Oh, nice. I think I hear a stream nearby."
    Leif "We're close, then."
    
    # - *The sounds of the river stream grow louder*
    # - *A flowerbed of Sweet Woodruff can be seen nearby*
    Serene "These flowers look so beautiful. How long have you been coming here?"
    
    # - *A small breeze blows through*
    # - *Leif puts his bag down near the bed of flowers*
    # - *Leif gives an exaggerated grunt as he sits down*
   
    Serene "Okay, old man."
    #Serene grins
    Leif "Ahhhh, how long has it been?" 
    #- *Serene "walks closer to inspect the flowers*
    Leif "I come here every few weeks or so, I guess. It's nice."
    narrator "Serene flashback's to a memory of Aelrie Back at the shop." 
    Aelrie "Sea-salt truffles were really common!"
    
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
    #Leif laughs
    Leif "Did that bracelet give you mind-reading powers? {w=2.0}Yes. My family stayed in the woods. We were in the fur trade."
    $ renpy.notify("You've unlocked: Context (!)")
    pause(2)
    # - [Notebook Update: Context (!) Added.]
    Serene "Makes sense why you know so much about nature." 
    Serene "You didn't want to work with your parents?"
    Leif "It's one thing to hunt for survival, but the way everyone operated in that line of work...It made me question myself."
    se "(Makes sense. Fur coats have been controversial for a long time.)"
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
    se "(I can feel his deep sense of respect for cuisine...)"
    Leif "Are you rested up? We're almost at the spot."
    Serene "Oh, right. Yeah, I'm ready."
    
    narrator "The duo approaches the planted Angelica's."
    Serene "Ah, so that's what they look like."
    narrator "Leif takes a spade out from his bag."
    Leif "Looks like I'm up."
    narrator "Leif starts digging up the roots of a few plants, while leaving most of the other plants intact. {w=2.0}You can sense Leif's care as he pulls."
    Serene "Wow, Leif. I didn't think you'd have such a green thumb for somebody of your size."
    Leif "If only you knew how many times I've heard that line."
    #Leif laughs
    narrator "Leif gathers a bundle of roots and packs them into his bag."
    Leif "All done."
    Serene "That was fast. It took us longer just getting here."
    Leif "Well, you know the saying, It's about the journey, not the destina--"
    narrator "Suddenly, there's loud shuffling in the bushes."
    Serene "Ouuu, are there deer here? Maybe we could feed them with--"
    narrator "Leif rushes over and grabs Serene behind a tree."
    narrator "Seconds later, two large trolls wielding clubs following a short third goblin wearing a stolen garb of jewelry walk through the bushes."
    Troll1 "Hiff Hiff."
    IcyGoblin "(Snickers)" 
    narrator "The second large troll looks around."
    Troll2 "Smelly."
    IcyGoblin "Shut up. I talk. You walk."
    Troll1 "Hufffffff. Hiffffff."
    narrator "The goblin drops his gold."
    IcyGoblin "What are ya standin there for? Pick it up!"
    narrator "The large trolls drop their clubs. Two loud thuds come across, scaring away the birds."
    narrator "Serene covers her mouth in horror."
    narrator "Leif gestures towards Serene to back away and begins to whisper."
    Leif "I'll distract them." 
    se "(Should I leave Leif behind and run for it?)"
menu:
    extend ""
    "Run":
        jump leif_adventure4
    "Wait.":
        jump leif_adventure4
    
label leif_adventure4:
    #Serene whispers
    Serene "No way. I can't."
    Troll2 "SMELLY."
    narrator "The troll stands upright, looking and moving towards Leif and Serene."
    IcyGoblin "Did I say you could leave?" 
    narrator "The goblin walks closely behind the troll as it stands next to the remaining Angelica's."
    IcyGoblin "This?"
    Troll2 "Hmfffff..."
    narrator "The large troll plomps on its butt before gently plucking one of the plants off the ground. Inspecting it with curiosity"
    IcyGoblin "What the hell are you doin'. Pick up my gold I said." 
    narrator "The goblin is visibly pissed off."
    se "(It looks like they're distracted. Should we run now?)"
menu:
    extend ""
    "Run":
        jump leif_adventure5
    "Wait.":
        jump leif_adventure5

label leif_adventure5:
    narrator "The large troll ignores the goblin, sniffing the flower."
    narrator "The goblin looks over to the first large troll."
    IcyGoblin "You. C'mere. Bring the club."
    narrator "The large troll slowly picks up its club and walks towards the others."
    Troll1 "Hifffffff."
    IcyGoblin "Smash."
    se "(I don't like where this is going. Should we move now?)"
menu:
    extend ""
    "Run.":
        jump leif_adventure6
    "Wait.":
        jump leif_adventure6

    
label leif_adventure6:
    narrator "The large troll raises its club."
    narrator "The goblin points at the plants."
    IcyGoblin "Now."
    narrator "In one blow the large troll flattens the entire crop of Angelicas. The leaves of nearby trees fall apart, including the leaves hiding Serene and Leif."
    se "(I should have listened to Leif and ran when I had the chance. What now?)"
menu:
    extend ""
    "Run.":
        jump leif_adventure7
    "Wait.":
        jump leif_adventure7
    "Look at Leif.":
        jump leif_adventure7

label leif_adventure7:
    narrator "Leif grabs a bottle out from his pack."
    Leif "Cover your face, Serene."
    Serene "W-what? Okay!"
    narrator "Leif prepares to throw the bottle."
    IcyGoblin "THROW."
    narrator "The troll lifts his club to throw at Leif like a boomerang."
    Leif "What?!"
    narrator "Leif freezes while the troll viscously throws its club at Leif."
    narrator "An evoking sound is quickly overheard."
    narrator "A loud ricochet."
    narrator "The club is knocked off-target."
    IcyGoblin "Another...?!" 
    # *The goblin stomps the ground repeatedly and looks at the second troll*" 
    IcyGoblin" Stand!" 
    IcyGoblin "Attack!!"
    narrator "The goblin continues to give progressively more violent exclamations..."

    narrator "Another evoking sound is overheard."
    narrator "The first troll is immediately wrapped in purplish-black magical chains."
    narrator "The goblin clenches its teeth." 
    IcyGoblin "Screw this." 
    narrator "The globin takes out a poison-tipped knife." 
    IcyGoblin "Quit hidin' and FIGHT me."
    IcyGoblin "I've slain your kind several times OVER. You're worthless, I cou--"
    narrator "Another evoking sound is heard."
    narrator "The sound of metal scraping against itself in quick succession is heard."
    narrator "The goblin disintegrates almost immediately."
    narrator "A stone drops to the floor."
    narrator "A mage emerges out from the trees and walks calmly towards the stone."
    Mage "You let this one talk more than usual, Elowen. Were you growing a liking to it, perhaps?"
    #The Mage gives a wide grin
    narrator "A man, radiating heat, can be seen already in front of where the goblin was previously."
    narrator "Elowen stands stoically in silence."
    narrator "The mage picks up the stone, revealing itself to be a glistening dark purple marble."
    Mage "You can come out now. It's safe."
    narrator "The bound troll continues to writhe in the magic chains, while the other stays seated with its Angelica, seemingly unbothered."
    Serene "What about the trolls?"
    Mage "(chuckles) Don't fret."
    narrator "Elowen walks towards the stream to fill his bottle."
    narrator "The mage calmly levitates and presses two fingers on the chained troll's forehead."
    Mage "Fateor."
    narrator "The sound of shattered glass resonates."
    narrator "What was previously a troll, reverts to a wild boar."
    Leif "...Now I remember...!"
    narrator "The mage calmly walks over to the first large troll still admiring the Angelica, now lying on its back."
    Mage "Good girl...Now let's get you home... "
    #The mage gives another gentle whisper
    Mage "...Fateor."
    #narrator "The troll returns to a young piglet."

    #jump chapter5
    return