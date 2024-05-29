label chapter3:
    #*DONG* 
    Bell "SUNRISE!" 
    #*DONGGGGG* 
    Bell "SUNRIIIIIISE!"
    se "(I should talk to Amara a bit more on starting the shop...)"
    # - *The shuffling of several footsteps can be heard thumping downstairs*
    Amara "Welcome, welcome! We have new items in stock for Floraliaaaa!" 
    se "(Amara has the shop open already? Sounds like a busy day.)"
    se "(There's a new set of clothes by the wardrobe...!)"
    se "(And what's this...?)"
    # -*Serene "sees a letter next to the garment*
    #- Letter (use nvl mode for this part):
    letter "Serene, I'm so very sorry for barging into your room while you were resting. I just saw this outfit in this morning's shipment and just knew it was put together specifically for you." 
    letter "I hope you like it! Today should be pretty busy at the shop, so I won't be able to walk you around today." 
    letter "Can you visit the big oaf next door? He'll help you gather your bearings-I'm looking forward to seeing you blossom just like the beautiful flowers of Floralia!"
    letter "Yours truly,"
    letter "Amara"

    nvl clear

    se "(The clothes Amara got for me look like my size. Should I try them on?)"
menu:
    extend ""
    "Keep wearing your office attire.": #(<-- Not wearing the outfit gives a unique response "from Amara later)
        jump amara_clothes
    "Wear the clothes Amara gave me.":
        jump amara_clothes

label amara_clothes:
    se "(Amazing. The dress fits perfectly and is this cotton?)" 
    se "(This is some high-quality material. I need to say thank you to Amara later.)"
    narrator "Serene walks downstairs, and is immediately greeted by a mob of customers."
    Amara "Aaaaand the lucky winner of a brand-new pair of diamond earrings is...!"
    Customer12 "Pick twelve, please pick twelve!"
    # - *The crowd continues clamoring in excitement*
    Amara "Number nineeeee! Come right up for your prize!"
    Customer6 "Oh! Me! Meeee!"
    Amara "Unfortunately, that's an upside down six."
    Customer9 "I got it!"
    Customer6 "Hey! How can you tell, the six and nine look exactly the same!"
    Amara "Congratulations, number nine!" 
    Amara "And nono, look see, I wrote the 9 with a little line on the bottom like this." 
    Amara "Wait, did I do that on both of them...? {w=2.0}Uh oh." 
    # - *The crowd starts to get quiet*
    Customer7 "Redo the raffle that doesn't count!"
    Customer9 "...But I won!"
    se "(Sounds like things are getting a little tense. Should I intervene?)"
menu:
    extend ""
    "Help out Amara.":
        jump amara_solution0
    "Amara's got it under control.":
        jump amara_solution

label amara_solution0:    
    menu:
        extend ""
        "Fix the numbers and redo the raffle.": # (The cards are presented to the player. Can use "the mouse "to erase "the lines. Might be complicated because "you could erase "the whole card.)
            jump amara_solution
        "Split the earrings between #6 and #9.": # (Unique Dialogue.)
            jump amara_solution
        "Have #6 and #9 rock, paper, scissors for the prize.": # (Requires explaining the process of what the game is. Player could make up their own rules.)
            jump amara_solution
        "Find another pair of earrings to give to each customer.": # (Could present three different choices of earrings.)
            jump amara_solution
        "Give the earrings to customer #9.": # (Unique dialogue)
            jump amara_solution
        "...": #(Skips the entire scene altogether if the player thinks the idea is boring.)
            jump amara_solution

label amara_solution:
    se "(I'm sure Amara's got it. I need to head over next door and talk to Leif.)"
    #"*Serene walks to the next building to see Leif*"
    # - *Serene "appears in front of the store*
    # - *Serene "enters the building*
    Serene  "Helloooo. I'm back."
    Leif "Well, hellooooo to you too!"

    Serene  "Amara was a little busy today, so she told me to come talk to you."
    Leif "Oh, right. She stopped by this morning to let me know."
    se "(This morning? It is morning.)"
    Leif "Okay so there's a couple of forms you'll need to fill out here before we start."
    # "*Leif slides over a form*"
    Leif "So, this is the first one. It's the most important."
    # - *Serene starts reading the document*
    # - *The document is an illustration of some food he ate yesterday*

menu:
    extend ""
    "\"Is this uh...?\"":
        jump leif_letter
    "\"Looks tasty.\"":
        jump leif_letter
    "\"I think you grabbed the wrong form.\"":
        jump leif_letter

label leif_letter:
    Leif "Wrong form? What do you mean-"
    extend " OH. Yup. Wrong form my bad." 
    #*nervous laughter*" 
    Leif "I'll head back to the city plaza later to get you the right ones." 
    Leif "Well, actually this kind of works out. {w=1.5}We need to register what kind of business this is going to be anyway."
    Serene  "Ouuuu. This sounds so official! {w=1.0} So, do I just tell them what I want to do? {w=1.5} Or pick from a list or something?"
    Leif "Not really. I think for you-{w=1} all we need is a name and the location. We can always change the job category later." 
    Leif "But I'm curious, what {i}do{/i} you want to do?"
    Serene "Maybe something to do with helping people?"
    Leif "A business where you just help people...?" 
    Leif "It's a little unorthodox, but I think there's a lot of people out there that need a shoulder to cry on."
    Serene  "Huh. Like a therapist?"
    Leif "What's a therapist?"
    Serene  "Yeah. This will definitely work."
    Leif "Okay, great. We've got that settled." 
    Leif "So, the next thing we need to do is spread the word around so we can get some customers into the shop."
    Serene  "I wanted to ask about that too. You write food reviews, right? Where do you usually post them?" 
    Serene "We could add a little spot somewhere that we give people advice too." 
    Leif "Well, about that." 
    Leif "Reading and writing aren't very common skills around here, so trying to describe what we do in detail might be a little tough."
    Serene  "Hm. That might be a problem then."
    narrator "Suddenly, the sound of rain begins flooding down."
    Leif "It's really pouring down today."
    Serene  "Ah, are the windows open too?"
    Leif "Oh right."
    Serene  "It's okay, I got it."
    narrator "As Serene walks over to the window, she spots a girl running in the rain."
    se "(Oh my goodness, she's soaked.)"
    Serene  "Hey! Over here! Come inside!"
    #"*The girl looks over to Serene and begins running inside*"
    Serene "Leif! Do you have something dry over there?"
    Leif "I do, actually-{w=1.0}hold on."
    narrator "The girl, now at the front door, is catching her breath."
    Aelrie "No please...! {w=1.0}It's okay...!!{w=1.0} I don't want to be an inconvenience!!"
    narrator "Leif returns with a wool blanket."
    Leif "You're soaked, it's alright. We don't want you to catch a cold."
    narrator "You notice there's also clothes hanging up nearby."
    se "(Should I bring her a pair of clothes?)"
menu: 
    extend ""
    "No.":
        jump help_aelrie
    "Yes.":
        jump help_aelrie
    "Wait and see what Leif does.":
        jump help_aelrie

label help_aelrie:       
    Aelrie "Thank you...But.."
    se "(Maybe I shouldn't be too pushy.)"
    Serene  "Oh! No problem! But at least stay here until the rain dies down."
    Aelrie "...! Thank you so much!"
    Serene "It's really coming down out there." 
    Serene "You didn't bring an umbrella-{w=0.8}I mean something to protect you from the rain?"
    se "(Do umbrellas exist in this world? {w=0.8}How do people stay dry...?)"
    #Aelrie shivers
    Aelrie "N-n-no. I forgot to bring my cloak..."
    se "(A cloak? Would that have made a big difference...?)"
    narrator "The rain continues to fall with silence in the room."
    se "(The silence is deafening, should I say something?)"
    #Aelrie gasps
    Aelrie "Are those..!"
    narrator "Aelrie stares directly at the small table next to Leif's desk."
    Leif "You mean those sweets? You've seen them before?"
    se "(What! Chocolate? How long were those sitting there? I'm about to go feral.)"
    Aelrie "Sea-salt truffles...!" 
    Leif "Don't be shy, try some! It's a concoction I read up on a while back."
    Leif "The trip across the coastline made it a lot more satisfying."
    #"*Aelrie's eye, initially covered by her hair, is full of joy.*"
    Aelrie "Really!! Is that alright?" 
    #*Aelrie gleams towards Serene as if asking for permission*
    Serene  "Aww of course! Sharing is caring!"
    se "(I'm demolishing the rest of those the second she leaves.)"
    Aelrie "I haven't seen a Sea-salt truffle in so long!"
    Leif "That's understandable. Making chocolate is already difficult, and salt prices have really gone up as of late."
    Aelrie "Well...That too." 
    se "(Sounds like there's a story about that. Should I ask about it...?)"

menu:
    extend ""
    "Leave her be.":
        jump aelrie_chocolate1
    "Ask about it.":
        jump aelrie_chocolate1
    "Talk about how tasty the chocolates are.":
        jump aelrie_chocolate1

label aelrie_chocolate1:
    narrator "You take one of the chocolates on the table and have a bite."
    narrator "The texture is unusually grainy, but there's still a subtle sweetness in the chocolate complimented by flakes of salt." 
    narrator "It's an interesting combination."
    Serene "Wow Leif, you made these? I'm really impressed!"
    Leif "Thank you. I figured if I was going to sit here writing about food all day, {w=1.5}I should probably get a feel for how the food was made too." 
    Leif "Working on it was a nightmare, but I think I grew a better appreciation for the people who make it every day." 
    #Leif laughs
    Leif "Speaking of people...Sorry, I can't help but notice your ears-"
    Aelrie "Uhm...Yes." 
    se "(...! She's an elf!)" 
    Leif "Ahhhhh, so that's probably what you meant, right? When you said it's been a while?"
    Aelrie "Right...!" 
    extend " Back home Sea-salt truffles were really common!" 
    Aelrie "When I was little, we used to pack them in these cute little containers." 
    Aelrie "My mother let me decorate them sometimes too!" 
    $ renpy.notify("You've unlocked: Context (!)")
    pause(1)
    # - [Prompt: Context (!) Added. "Aelrie's Life back Home"] 
    Serene  "That {i}is{/i} cute." 
    Leif "Well, it looks like I happened to find the right person to try these out."
    Leif "I'm curious what you think."
    narrator "Aelrie takes one of the chocolates and is instantly surprised."
    Aelrie "They're not quite the same but this flavor is amazing!"
    Leif "Hey, I'll take that as a high compliment, considering its an elvish recipe."
    Aelrie "Ahhh! Nono! It wouldn't have been possible without the trade arrangements everyone made!!" 
    narrator "Aelrie appears to be minimizing her family's importance."
    se "(Hmm. Should I ask more about it?)"
menu:
    extend ""
    "Ask about her family.":
        jump aelrie_chocolate2
    "Ask about being an elf.":
        jump aelrie_chocolate2
    "Talk about the rain.":
        jump aelrie_chocolate2
    "Sit in silence and enjoy the chocolate.":
        jump aelrie_chocolate2
    "\"What is it like making chocolate for a living?\"":
        jump aelrie_chocolate2

label aelrie_chocolate2:
    Serene  "So, what is your family like?"
    Aelrie "My family? Hmmm. Well, they're nice."
    se "(Well. That was a quick answer. Should I ask more about it?)"

menu: 
    extend ""
    "Ask for more.":
        jump aelrie_chocolate3
    "Change the subject.":
        jump aelrie_chocolate3
    "Sit in silence and enjoy the chocolate. Leif is eating them now, oh no.":
        jump aelrie_chocolate3
    
label aelrie_chocolate3:
    narrator "Leif inhales an entire truffle in one bite."
    Leif "Holy mother of-{w=1.5}These {i}ARE{/i} good."
    Serene  "I'm guessing your hometown is far away from here?"
    Aelrie "Yes! There was an opportunity to join the academy here! It's my second year."
    Serene "Aww, that sounds great. Do you like the whole experience so far?"
    Serene "I can imagine being so far away from home can be a little scary."
    #*Aelrie nods*
    Aelrie "Mm. It was at first, but I met so many good...!" 
    #*Aelrie begins to hesitate for a second*
    Aelrie "...Friends here..."
    #*Aelrie begins to tear up*

menu: 
    extend ""
    "\"I'm so sorry. I didn't mean to make you cry!\"":
        jump aelrie_chocolate4
    "\"Toughen up, buttercup.\"":
        jump aelrie_chocolate4
    "\"...\"":
        jump aelrie_chocolate4
    "\"Do you really have friends?\"":
        jump aelrie_chocolate4
    "Change the subject":
        jump aelrie_chocolate4
    
label aelrie_chocolate4:
    #Aelrie sniffles
    Aelrie "Sorry, my hair must still be wet...{w=1.5}But yes, I'm learning a lot here at the academy." 
    #"*The rain begins to finally die down*"
    se "(Maybe I shouldn't pressure her too much.)"
menu:
    extend ""
    "Apologize for making her upset.":
        jump aelrie_chocolate5
    "\"Can I be friends with you?\"":
        jump aelrie_chocolate5
    "Sit in silence and offer her the rest of the chocolates.":
        jump aelrie_chocolate5
    "\"...\"":
        jump aelrie_chocolate5
    
label aelrie_chocolate5:  
    narrator "Aelrie looks up in surprise."
    Aelrie "Friends?! With me...?"
    Aelrie "Why?"
    Serene  "I can relate with you. I'm not from the town either."
    Aelrie "...!"
    Leif "You can count me in on that too. I've always been a southern man, myself." 
    Leif "You can help taste the next batch of sweets we make."
    # *Leif looks over to Serene* 
    Leif "Serene, have you stamped a {color=#f00}Rendé{/color} before?"
    Serene "A \"Rendé\"...? What's that?"
    Leif "It's a rendezvous card. You might have seen them a couple of times. I'll let you try it out with..." 
    #"Leif looks over to Aelrie." 
    Leif "Oh look at us with bad manners. I'm Leif."
    Serene "Oh-OH. And I'm Serene."
    Aelrie "Aelrie! That's mine..."
    extend "but-but you can call me Rae if that's easier to say!!"
    Serene "Aelrie, right? It's a nice name! No need to shorten it." 
    Leif "Aelrie. That sounds familiar. Okay, Aelrie and Serene. This is what we're going to do."
    # "Leif looks over towards Serene"
    Leif "Serene, I want you to hold this card and think hard of Aelrie's name, this room, and that you want to see her again."
    se "(So that's how it works, huh? How would it know?)"
    # "The card gives a faint glow."
    Leif "You're sort of getting the feel, but I can tell you're off-topic."
    #Leif laughs
    Serene "It picked up my thoughts?! "
    Leif "You didn't believe me?" 
    Serene "Hold on, let me try it again."
    
menu:
    extend ""
    "Think about the chocolate truffles.":
        jump aelrie_chocolate6
    "Think about this room and Aelrie.":
        jump aelrie_chocolate6
    "Think about going back to your home world.":
        jump aelrie_chocolate6
    "Think about Amara's shop.":
        jump aelrie_chocolate6
    "...":
        jump aelrie_chocolate6
    
label aelrie_chocolate6:
    narrator "The Rendezvous card gives a strong blue aura."
    Leif "Interesting. Even the cards you stamp act differently around you." 
    Leif "It looks like it worked though. Now all you have to do is give the card to Aelrie."
    narrator "Aelrie touches the card. Her hair begins to flutter."
    Aelrie "I think it worked..!"
    Serene "I sincerely meant it. I'd love to see you come back here again to chat." 
    Serene "Hey Leif, you still have cocoa right?"
    Leif "There are a few beans still leftover, yes."
    Serene "Ever thought of making something maybe a little more...simple?" 
    Serene "Like hot cocoa as a drink?"
    Leif "Hot cocoa, huh? I could try that out."
    Serene "Then it's settled! Come back again soon Aelrie, we'll have a cup of hot cocoa waiting for you!"
    Aelrie "That would be delightful!" 
    # *Aelrie's eye begins to shine* 
    Aelrie "Oh no, I'm late!!!" 
    Aelrie "I will see you all again soon!"
    # "Aelrie quickly leaves the shop."
    se "(What an interesting girl...)"
    with fade
    jump chapter4
