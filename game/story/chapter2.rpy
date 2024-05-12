label chapter2:
    "It is now nightfall, with oil-lit lamps guiding her way through the town." 
    "Even though there is movement of townsfolk and horse-pulled carriages, there is a calm ambience in the air."

    "(Somehow this building looks familiar. I think I'm here.)"
    menu:
        extend ""
        "Take a look around the area first.":
            jump enter_amara_shop
        "People-watch the customers entering and leaving the shop.":
            jump enter_amara_shop
        "Enter the shop.":
            jump enter_amara_shop
    
    label enter_amara_shop:
        "You enter the shop, not knowing what to expect inside."

        "The shopkeeper, Amara, can be seen chatting with one of her regulars. Her long hair seems to bounce around her hips as she speaks." 
        Amara "Haha, see. What did I tell you! Have some confidence! The dress is perfect on you."
        "Amara stands behind a customer facing the shop mirror. She is wearing a beautiful crimson dress that seems to perfectly fit her boisterous frame." 
        Customer "You really think so?"
        Amara "I know so. I'm looking forward to seeing you and that dress at your dance recital."
        Customer "Amara you're not just saying that are you?! You'll really come! What about your shop?"
        Amara "This place will be fine, don't worry. Now let's find you something nice for your hair..."
        "You watch Amara glide through her shop like a professionally trained ballerina, every movement fluid and never lacking precision." 
        "It is evident she knows every inch of her shop despite the incredulous amount of random trinkets and items seemingly strewn everywhere." 
        "This shop is organized chaos, and this is her song and dance."  
        "(It seems like she gets along well with her customers. Maybe I should come back another time when she's not busy.)"

        # - Just then, Amara catches a glimpse of Serene*
        Amara "Now, Who. Is. That. I'll be right back, Christine. Here are the hairpins, we'll find a good color to match your dress."
        $ Customer = "Christine"
        "In an instant, Amara is already in your face, her long hair hanging like a halo around your peripherals." 
        "She bends down to meet your eye level, clearly intrigued."
        "You can't help but stare deeply into her brown eyes, admiring the specks of gold sprinkled around her iris like fairy dust."  
        Serene "...Hi?"
        Amara "Those blue eyes. In all my years I've never seen such a thing. And your HAIR? Fascinating."
        Serene "Oh, I mean I guess my hair does look a little blue if you shine the light the right way-wait blue eyes? I don't have blue eyes??"
        Amara "And that bracelet..*Amara grabs your wrist and inspects the bracelet you acquired back in the cave."
        # - Amara's face then drops like a sack of potatoes* 
        Amara "How did you find this place?"
    
    menu:
        "Lie.":
            jump amara_respond
        "Ignore the question and ask about her hairpin collection.":
            jump amara_respond
        "Show Amara the chalice.":
            jump amara_respond
    
    label amara_respond:
        "Serene opens her bag and shows Amara the chalice"
        Amara "I knew it." 
        extend "I KNEW IT." 
        Amara "You're the hero that old man kept yapping about."
        Amara "Still, you seem a little strange. Besides the hair and eyes, I really don't sense anything heroic about you."
        Customer "Ahhh!!"
        Amara "Hold on, you stay RIGHT there. I'll hold on to this in the meantime."  
        #- *Amara nonchalantly places the Chalice behind the store counter* 
        Amara "What did you find Christine?! AHHHH. That hairpin looks Gorgeous on you. It's on the house, this piece was made for you. You look absolutely divine, darling." 
        "(It looks like Amara's busy again. Should I look around?)"
    menu:
        extend ""
        "Try to leave the shop.":
            jump amara_search
        "Look around at the clothing in the store.":
            jump amara_search
        "Check the standing mirror.":
            jump amara_search
        
    label amara_search:
        # - Serene looks at the mirror to find that her hair and eye color have changed. Her once plain brown eyes are now a bright blue, and her once black hair now a deep sea blue.
        "(I really have changed. Was it when I got transported here?)"
        "You look down and inspect the bracelet around your wrist." 
        "(Did the bracelet do this?!)"
        "Suddenly, an elderly woman appears behind you in the mirror."
        Elder "Ah. You've finally awakened, I see. And you passed the trial."
        Serene "NO. What? I refuse. Why does everyone know everything about me? None of this makes any sense."
        Elder "A fair statement. Life can be quite like that sometimes, I'm afraid."
        "(If I close my eyes, this will all disappear.)"
        "You squeeze your eyes shut for a brief moment. When your eyes flutter open, your blurry vision reveals the same old woman staring at you from behind."
        Elder "Still here."
        Serene "?"
        Elder "I'll be brief. I'm here to help make some sense of your current situation. Look at your bracelet. Now clear your mind. Think of your journal."
        Serene "My journal...? Your mind flashes back to your journal back at the office." 
        "(I nearly forgot. I always kept my journal on me...)"

        # - The flashback of you and your coworker during your training days continues.
        Devon "How are you writing so fast?!"
        Serene "You don't write things down when you first learn something? That's like, the best way to learn something."
        Devon "Not really. Stuff doesn't really stick with me if I just watch it. I have to do it myself so I can learn."
        Serene "Haha, you say that. But don't come to me asking for notes after you forget everything."
        # - The flashback ends. The old lady, as if able to read your mind, nods to you in approval. 
        Elder "Yes...Good. Are you visualizing it?" 
        # - A prompt opens on the screen
        $ renpy.notify("You've unlocked: Context (!)")
        # - Insert Info card animation for this
        "Important information will now automatically be added to your journal for reference."


        Elder "I will return when the time arises. For now, stay the course, Serene."
        # - *The Elder steps outside "the shop and disappears*
        "(Yeah, I am absolutely going insane.)"
        Amara "Well, look at you admiring yourself. Be careful now. Stare too long, and you'll start seeing spirits. Come with me; I have something for you."
        # - *Scene Transitions to a dusty bedroom upstairs*
        "Amara leads you up the creaky stairs and into an empty guest room. She opens the curtains in one swift motion, dust particles flying everywhere." 
        "Covering her mouth with her sleeve and waving the air around her with her other sleeve, she turns around to face you." 
        Amara "Sooo what do you think? Not much, but it'll do."
        
    menu:
        extend ""
        "\"There's no way I'm staying in this dump.\"":
            jump amara_room
        "\"It looks cozy!\"":
            jump amara_room
        "\"Is this my room?\"":
            jump amara_room
        
    label amara_room:
        Amara "I apologize. I would have cleaned up a bit more if I knew I was going to have an esteemed guest with me."  
        Amara "Come to think of it, I don't think I ever formally introduced myself. I'm Amara. And your name was Miss..."
        Serene "Oh you don't have to be so polite, you can just call me Serene."
        Amara "Serene, huh? Has a nice ring to it. Well, try the bed out." 
        Amara "I'm about to close the shop here soon, but I'll show you around town tomorrow."
        Serene "Thank you. That would be nice."
        "You hear Amara make her way back downstairs; somehow, the creaky stairs don't seem to creak for her." 
        "(The exhaustion finally caught up to me. I should get some sleep.)"
        "Your head hits the pillow and you instantly fall asleep for the night." 

        Bell "Sunriiiiiiise! *Gong* SUNRIIIIIISE *GONGGGGG*"
        "Still in bed, your attempt to cover your ears with a pillow." 
        # - *Shuffling noises can be heard from downstairs*
        # - *Amara's Shouting from downstairs*
        Amara "Sereneeeee! A little help please!"
        "Still half-asleep, you scramble out of bed and head downstairs."
        Serene "uh. Cominggggg!"
        # - *Amara can be seen downstairs lugging a large heavy chest*
        Amara "*phew* Man, this never gets any easier. Mind if I use your help to unpack?"
        Serene "Did you bring all of this in by yourself?!"
        Amara "Hehe, something like that. The carriage got me most of the way." 
        Amara "Here, use this key to open it up! Let's see what we got."
        Serene "Okay. Wait, you don't already know what's inside?"
        Amara "Pshhhh, nah that's the best part. I have a deal with the Merchant Guild." 
        Amara "Every trader gets a chest before major festivals. Keeps things more exciting."
        "You open up the chest. It's overflowing with beads and colorful powder."
        Amara "Oh that's right. You're not from around here. The end of winter marks our first spring festival."
        Serene "Woah, really? I can kinda guess what the beads are for. Do people just hand them out to each other?"
        Amara "...That was a pretty good guess, actually. You sure you're not from around here?"
        "(Hmmm. I'm not really sure what the powder is for though. That's a new one.)"
        Amara "Okay but let's get all of this somewhere before the bags pop open." 
        Amara "Not looking forward to sweeping any of this stuff up if it spills."
        Serene "Right."
        "You work with Amara to put up the stock." 
        Amara "Hey, you're pretty good at organizing this stuff."
        Serene "You think so?" 
        Amara "Yeah, I could really use an assistant. Working the shop alone can be brutal."
        Serene "But you seem so nice, you haven't found anyone that'd work the shop with you?"
        Amara "Well..."
        "(Something seems wrong with Amara, should I probe deeper?)"

    menu:
        extend ""
        "Press her for a better answer.":
            "Really?! You would?! Oh, I mean I couldn't! I wouldn't want to inconvenience you! I mean I'm sorry I just-- *sigh* Here I go again..."
            "(It seems like she's getting a little flustered. Should I keep going?)"
            jump amara_assistant
        "Leave her be.":
            "Really?! You would?! Oh, I mean I couldn't! I wouldn't want to inconvenience you! I mean I'm sorry I just-- *sigh* Here I go again..."
            "(It seems like she's getting a little flustered. Should I keep going?)"
            jump amara_assistant
        "Offer to be her assistant.":
            "Really?! You would?! Oh, I mean I couldn't! I wouldn't want to inconvenience you! I mean I'm sorry I just-- *sigh* Here I go again..."
            "(It seems like she's getting a little flustered. Should I keep going?)"
            jump amara_assistant
        
    menu amara_assistant:
        extend ""
        "\"Why are you so nervous?\"":
            Amara "I-I was just kidding! Please. I'm sorry. I just-I need do this right, for myself. This is the one thing I need to do right."
            Amara "But thank you, Serene. Really. That really means a lot to me."
            "(\"Do it right?\" I wonder what that means. Maybe I shouldn't pressure her any further.)"
            jump amara_assistant2
        "Leave her be.":
            Amara "I-I was just kidding! Please. I'm sorry. I just-I need do this right, for myself. This is the one thing I need to do right."
            Amara "But thank you, Serene. Really. That really means a lot to me."
            "(\"Do it right?\" I wonder what that means. Maybe I shouldn't pressure her any further.)"
            jump amara_assistant2
        "Insist harder on being her assistant.":
            Amara "I-I was just kidding! Please. I'm sorry. I just-I need do this right, for myself. This is the one thing I need to do right."
            Amara "But thank you, Serene. Really. That really means a lot to me."
            "(\"Do it right?\" I wonder what that means. Maybe I shouldn't pressure her any further.)"
            jump amara_assistant2

    menu amara_assistant2:
        extend ""
        "Talk more about the festival instead.":
            jump amara_assistant3
        "Continue working in silence.":
            jump amara_assistant3
        "Go all in. You're working at her shop whether she likes it or not.":
            jump amara_assistant3
        "Admit defeat. You tried your best.":
            jump amara_assistant3
        
    label amara_assistant3:
        Amara "That does give me an idea though. Have you ever thought about running a shop for yourself?"
        Serene "My own shop?" 
        # - *You think back to your life at the office* 
        "(I've never run my own business before. Could I really do something like that...?)"
        Amara "Why the long face? I wouldn't really call it easy, but I think it's nice having something to call your own, y'know? It gets you out of your comfort zone."
        Serene "That's an interesting way to put it. I guess I just never really put much thought into it."
        Amara "Well, I think you should start! Matter of fact, I still have some room next door."
        Serene "You have ANOTHER place besides this?"
        Amara "Well, I guess you could say I had a decent investment. We already have a tenant there." 
        Amara "Big guy, but for some reason he decided he'd rather write all day instead of working. I'm sure you could kick him into shape."
    menu:
        extend ""
        "\"What kind of person is he?\"":
            Amara "Oh please, I'd insist. That big oaf still owes me rent, but your dues are paid. That includes a monthly stipend courtesy of your friend."
            jump amara_help
        "\"How much would it cost me to open up there?\"":
            Amara "Oh please, I'd insist. That big oaf still owes me rent, but your dues are paid. That includes a monthly stipend courtesy of your friend."
            jump amara_help
        "\"I don't know, sounds like a bother.\"":
            Amara "Oh please, I'd insist. That big oaf still owes me rent, but your dues are paid. That includes a monthly stipend courtesy of your friend."
            jump amara_help
        "\"Are you sure that's alright?\"":
            Amara "Oh please, I'd insist. That big oaf still owes me rent, but your dues are paid. That includes a monthly stipend courtesy of your friend."
            jump amara_help
        
    
    menu amara_help:
        extend ""
        "\"Sure. But why haven't you kicked the other guy out?\"":
            jump amara_help2
        "\"What would I do in the shop?\"":
            jump amara_help2
        "\"How do I find customers?\"":
            jump amara_help2
        "\"Friend? Who do you mean?\"":
            jump amara_help2
    
    label amara_help2:
        Amara "Hello? The professor that asked you come here? Did you already forget about that item you gave me?"
        Amara "That wasn't any old ordinary chalice. I've been eyeing that prize for a while." 
        Serene "Why? Is it worth a lot of money?"
        Amara "I mean, yes, and no? There's some sentimental value in there as well. It used to belong to my father."
        "(Her father?! Even I could tell that a family with an item like that must be rolling in cash.)"
        Amara "Yeah, yeah. I know what you're thinking. It's a long story, but it's important that I get this shop off the ground."
        Amara "I have to make it work on my own."
        "(I can feel her strong ambition. I'm sure there's something I can do to help her.)"
        Serene "Well in that case, let's make this a partnership. You help me, and I'll help you!"
        Amara "(laughs) You're so hard-headed! Let's start as friends, maybe first?"
        # - Editor's Note: In lieu of a Social Link, maybe this could be a painted portrait.
        
        Serene "Okay so, was the building I'm supposed to go to on my left or my right...?"
        Amara "Haha, right this way, ma'am."

        "Amara guides you to the next building. She said it was next door, but it really was a few blocks away. I guess this is how normal long walks are around here."

        "Amara flamboyantly shows off the building, her long hair bouncing around her waist in excitement." 
        Amara "Welcome to your new humble abode! La casa del Serene!"
        Serene "...And the other guy."
        Amara "La casa del Serene...!"
        extend " And the other guy...!" 
        extend " Unfortunately." 
        Amara "I'm being kinda' genuine here--if you're able to get that man a job you'd be a lifesaver, truly." 
        Amara "Helllooooooo! Ya big oaf, where's my money!"
        "The room is surprisingly quiet as you step inside." 
        Serene "Maybe he already stepped out?"
        Amara "Nooo, no. That doesn't sound like him. He's always been cooped up by his desk." 
        Amara "One moment-"
        extend " Leif!!" 
        extend " Where ya hiding!"

        "A thump comes from behind the door"

        Leif "I'm back. Found some quality herbs for your shop."
        Amara "Leif..You know sure well I don't sell that stuff. I specialize in clothing & jewelry, mister. How long have you known me?"
        Leif "See, that's the thing Amara. Have you ever thought of expanding? We have so many clothing stores already." 
        Leif "I think you could capture a whole new market by jumping into health and wellness."
        Amara "And what makes you so knowledgeable about that?"
        "(It looks like Amara and Leif have an interesting relationship. Should I jump into the conversation?)"
        
    menu:
        extend ""
        "\"Hi, I'm Serene! Are you two dating?\"":
            jump meet_leif
        "\"So this is some nice weather today...\"":
            jump meet_leif
        "\"I agree with Leif. That sounds like a great idea.\"":
            jump meet_leif
        "\"...\"":
            jump meet_leif
    label meet_leif:
        Leif "I'm just saying if you want to stay ahead of the curve, you shouldn't be afraid to take risks."
        Amara "Very intriguing words from a man who hasn't paid his rent yet." 
        Leif "Consider it an investment. My reviews are a little different, but I think it'll grow on you and everyone else soon."
        Amara "We'll just have to see about that then, huh? *Amara gives a wide grin as she spins around to introduce you*" 
        Amara "Anyway, here's your new roommate, Serene. She'll be sharing the space with you in the meantime."
        Serene "It's nice to meet you Leif! So you make reviews?"
        Leif "Something like that."
        Amara "He comes from a big family of hunters and somehow found himself at a desk drawing doodles."
        Leif "I wouldn't really call them doodles." 
        extend " More like illustrations." 
        Leif "It's difficult to capture the nuances of quality cuisine with words alone."
        "(Reminds me a lot of my lunch breaks with Trisha.)"
        # - *Flashback to the office*
        Trisha "Hold on don't dig in yet!! I have to take a picture for my Story!"
        Serene "Trisha pleaseeeee I'm STARVING."
        # - *Trisha snaps a photo of her dish*
        Trisha "Want me to send it to ya'?" 
        Serene "Not really. Are you done? My food's getting cold." 
        # - *Scene transitions back to the room*
        "(I guess some things never change.)"
        Bell "*DONGGG* AFTERNOOOOOOOOON *DONGGGG* AFTERNOOOOOON"
        Amara "Shoot, it's already noon, I need to head back over to the shop."
        Amara "You guys be safe. You know where your bed will be, Serene."
        Serene "Oh! Okay then, I guess I'll see you later Amar...!"
        "Amara can already be seen long gone"
        Serene "...That was fast." 
        Serene "So thennn...Leif. How's...life...?"
        "Leif can already be seen at his desk, busy with his sketch."
        Leif "*Yelling from across the room* Sorry. Serene, right?"
        Leif "Let's chat more tomorrow. I have to put my memory on paper."
        # - *Leif starts talking to himself* 
        Leif "What was that feeling...? The honeyed aroma...? No...The sweet and appetizing flavor...?"
        "(Leif looks busy; maybe I should come back another time.)"
        # - *Serene "in-game is then given freedom to explore the town before heading back to her room in Amara's shop.*
        # -*After returning to your room, there is a prompt to go to sleep in your bed*
        jump chapter3



return
   
