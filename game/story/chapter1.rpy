# The script of the game goes in this file.

define config.emphasize_audio_channels = [ 'voice' ]
define config.emphasize_audio_volume = .05
define config.emphasize_audio_time = 0.5


default wall_break = False

default preferences.text_cps = 70



# The game starts here.


label splashscreen:
    scene black
    with Pause(2)
    play ambience "Ocean.mp3" volume 0.5
    play music "brazil_funk.mp3" volume 0.5 fadein 5
    show text "Now Presenting..." with dissolve
    with Pause(4)
    hide text with dissolve
    with Pause(3)
    show text "A Game by Radiant Sea..." with dissolve
    with Pause(4)
    hide text with dissolve
    with Pause(3)
    show text "Project Serene" with dissolve
    with Pause(4)
    hide text with dissolve
    
    
    
    return


label start:

    
    
    
        label chapter1:
        
        $ quick_menu = False
        stop music
        scene black

        show text "Monday, April 16th." with fade
        with Pause(3)
        hide text with fade
        stop ambience
        window hide 
        play music"butterfly.mp3" volume 0.1
        camera:
            perspective True

        #camera at parallax

        # Show a background. This uses a placeholder by default, but you can
        # add a file (named either "bg room.png" or "bg room.jpg") to the
        # images directory to show it.

        
        scene office2 with fade
        play ambience "office.mp3" loop volume 0.5
    

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        

        # These display lines of dialogue.
        $ quick_menu = True
        narrator "The fading sunlight streams through the office windows." 
        narrator "The warm 4 pm glow slowly losing its battle to the cold, fluorescent lights." 
        narrator "You hear muffled chatter around your cubicle."
        show npc1 at left, flip
        
        camera:
            pos (250, 750) zoom 2.0 
        $ lipsync(npc1, "Coworker1.wav", "Did you see the look on Patrick's face after that meeting?")
        show npc2 at right
        camera:
            subpixel True 
            pos (250, 750) zoom 2.0 
            linear 1.00 pos (1500, 751) zoom 2.0 
        with Pause(1.10)
        camera:
            pos (1500, 751) zoom 2.0 
        $ lipsync(npc2, "Coworker2.wav", "Yeah...Today's gonna' be rough...")
        
        

        show npc2: 
            parallel:
                hop
            parallel:
                linear 7.5 xalign 0.0
        
        show npc1: 
            pause 0.8
            flip
            parallel:
                hop
            parallel:
                linear 7.5 xalign 0.0
            
        
        play sound "SFX/type_in.mp3" loop volume 0.05
        narrator "Feelings of dread wash over you. You continue typing, trying to focus on the computer screen while keeping your composure." 
        narrator "A man peaks over the cubicle."
        show Devon neutral at char_fade, right, close

        window auto hide
        camera:
            subpixel True 
            ypos 751 
            linear 2.11 ypos 234 zoom 1.5 xpos 900
        show office2:
            subpixel True blur 4.0 blend None 
        with Pause(2.21)
        camera:
            ypos 234 
        window auto show

        hide npc1 
        hide npc2 
        with dissolve
        narrator "You see, your coworker, Devon, hovers over you like a lost puppy." 
        narrator "Devon was hired a month before you, but he gloms onto you like an imprinted duckling for some reason."
        jump see_devon

        label see_devon:
            Devon "Hey, Serene!"
            extend " Can I borrow your pen real fast?"
            Devon "I think I dropped it somewhere on my way back here."
            
            #Alternate choice screen is -  (screen = "grid_choice", cols = 3, rows = 1)
            
            menu annoying_devon1:
                extend "" 
                "Ignore him.":
                    jump ignore_devon
                "Humor him.":
                    $ renpy.notify("You've unlocked: Context (!)")
                    pause(1.5)
                    narrator "Are you sure? I don't think you quite understand what you're signing yourself up for." 
                    $ wall_break = True
                    jump ignore_devon

        label ignore_devon:
            show Devon scowl
            Devon "What's up? You look worried. Is it about the lay-offs? You'll be alright. " 
            play sound "SFX/type_in.mp3" volume 0.1 loop
            camera:
                linear 10.0 ypos 200 xpos 900 zoom 1.5 
            
            show Devon grimace
            narrator "Ever eager to step on eggshells, Devon delves into an unsolicited therapy session. You type, louder and more deliberate, keystrokes firing out in an attempt to ignore this nonsense. Devon does not relent."
            show Devon neutral
            Devon "I mean, they already fired like five people in our department, what are the odds they'd keep going? "
            stop sound
            narrator "You abruptly stop typing, and without turning your head, you shift your gaze to meet Devon's."
            show Devon grimace
            narrator "He's looking at you with his signature smile." 
            show Devon neutral
            narrator " His bright attitude is almost blinding sometimes." 
            narrator "You take a deep breath before summoning the patience to respond."
            play sound "SFX/chair_with_wheels.mp3"

            Serene "Devon, I appreciate you but please. I just—" 

            narrator "You are suddenly interrupted by an authoritative voice booming over your cubicle" 

            Devon "Op!" 
            
            hide Devon

            narrator "Devon ducks and quickly scurries back to his side of the cubicle." 

            Manager "Serene... Can you meet me at the corner office in five minutes?"

            Serene "Y-yes. I'll be there in a moment."

            narrator "The Manager walks back down the hallway, escorting an emotional, laid-off employee with security in tow. Their cries linger in the stale office air like forlorn dissonance."   
            narrator "You sit blankly at your desk." 
            narrator "It feels like all the blood has drained from your body, your hands are like icicles." 
            "(I hate this.  I hate this. I hate this. I hate this feeling. I HATE this.)" 
            
            #Serene breathes in and exhales deeply
            Serene "Just breathe.  Just. Breathe." 
            
            narrator "Your Phone chimes in your pocket. You've received a new message."
            #Serene reaches for Phone.
            Phone " Unknown Number - Principality of Balenci"
            
            narrator "Puzzled, you swipe on the notification to read the message." 
            
            Phone " A Shimmer request has been initiated. Reply (Y) to accept." 

            #Serene Internally:
            "(Principality of Balenci?  What is this? A scam?)"
            
            narrator "Shaking your head you set your Phone down before laughing cathartically." 
        
            #Devon yells from across the cubicle
            Devon "That's right Serene! You're finally listening to what I've been telling you!! You just need a positive attitude, and everything will be-" 
            Devon "Oh whats up...?" 
            Devon "You're on the Phone?!" 
            Devon "Keep my voice down?!"
            Devon "Oh, my fault I...!" 
            
            narrator "Devon's voice starts to fade as if he is moving further and further away." 
            
            #Serene Internally:
            "(...Okay, yeah. Never mind. I'm over it today.)"

            narrator "You pick up your Phone, and without hesitating you reply (Y)."

            Phone "Thank you for your response. It appears that you are in an unsatisfactory location." 
            Phone "Please relocate to an area away from other people."

            narrator "You look at the message in bewilderment." 
            
            #Serene Internally:
            "(Huh. That's a new one. No Nigerian prince to give money to?)"

            #Serene begins to laugh
            "(I'm so dumb.)" 
            
            Phone " Shimmer will commence in 10 seconds."
            
            "(For a second there, I was really hoping something was going to happen...)"
            
            narrator "A flash of sparkling bright white light comes across the room and envelopes the world around you."
            
            Serene "Okay, I spoke too soon; I guess I'm just dying." 
            
            Phone "Shimmer will commence in 5 seconds."
            
            #Reality begins to warp**
            
            Serene "Surprisingly, I'm okay with this."

            #########################################################################################
            #The screen fades out from white to black.
            scene cave4 
            stop ambience 
            play music "cake.mp3" volume 0.05
            camera:
                subpixel True pos (3000, 2500) zpos 300.0 zoom 3.22

            Moonga "Wait look! Something's happening!"
            Sunela "SEE! I TOLD YOU!!"
            Panna "Guys...Relax."
            #A ring of small flames materializes around you.
            
            Moonga "Aww man. Lame, it's just a girl."
            
            Sunela "HEY! Girls can be heroes too! I wonder what kind of powers she has." 
            Sunela "The book said they can do all kinds of stuff!"
            
            narrator "You stand in the middle of a bizarre, glowing circle." 
            narrator "As the flames dissipate, your eyes are drawn to three small figures standing around you." 
            narrator "Three children in identical lizard suits stand before you." 
            narrator "Wait."
            narrator "You rub your eyes in attempt to clear your vision. You look at the three small figures again."

            #Serene Internally
            "(Not costumes. Those are children, and they are lizards. Those are lizard children. Where AM I?)"
            
            Moonga "Hey Lady! Do something cool like casting light magic out of your eyes."
            Panna "Let me see the book again. I'm certain we casted the spell incorrectly."
            Sunela "Uhm. Excuse me, Miss, are you our hero?"
            
            narrator "Shakily, you manage to stand up and attempt to find your footing."
            
            Serene "Where am I...?"
            
            narrator "You briefly regain your composure before reality and time seemingly shifts and warps around you." 
            
            narrator "An advanced human-like AI echoes through the forefront of your mind." 
            
            Phone "Shimmer complete. Arrived at Destination: Principality of Balenci."
            
            narrator "Alarmed, you look around the cave frantically trying to discern where the voice was coming from."
            
            "(Am I having auditory hallunications? What is a Shimmer...? Does this have anything to do with that text earlier?!)"
            
            Phone "Good morning, Serene. The time is now 8:53 am."
            
            narrator "You look up at the cave ceiling, the rock walls cascade into the shadows, pooling around the centre like a dark lake." 
            
            Serene "You're not just a voice in my head, right? Please tell me Im not going any crazier than I already am." 
            
            Phone "Query received: Activating Internal Audio Mode. Tachypnea and rapid heart rate detected." 
            Phone "It appears you are under distress." 
            Phone "Warning: Battery life at 10\%. Switching to Low Power Mode."
            
            "(Internal audio mode?  Low battery...? I knew this voice was familiar. Is this my PHONE?)"
            
            Phone "Query received: This is the only Phone signed into your account. Powering down."
            
            #Time resumes.
            
            Serene "You can read my thoughts?! This doesn't make any sense...! Uh, power... on!"
            
            narrator "An awkward silence pierces the cave." 
            
            narrator"The silence seems to elevate the atmospheric sounds of your surroundings," 
            extend " the metronome of recurrent drips echoes through the cave." 
            
            Moonga "Power on? Maaaan. She can't even cast any spells either. She just keeps talking to herself."
            
            Sunela "Uhm... Miss...?"
        
        
        menu sunela_intro:
            narrator "You spin your heels and turn around to face Sunela."
            "Where am I?":
                jump proceed
            "Oh, I'm Serene. What's your name?":
                jump proceed
            "*Pretend to be a hero.":
                jump proceed   
            "Why do I hear a British man narrating everything in my head?" if wall_break: 
                jump proceed

    
        label proceed:
            Sunela "Uh, uhm. I'm Sunela Miss serene!! These two are my big brothers Panna and Moonga!" 
            narrator "Moonga fixes their gaze on you, looking mildly disappointed before introducing themself." 
            Moonga "...Nice to meet you, ma'am."
        
            narrator "Without lifting his head, Panna looks up from his book. He corrects his wide framed glasses before introducing himself." 
        
            Panna "Yes. Hello." 
            Panna "Anyway, Moonga, take a look at this line here. We did the wrong spell."
            Moonga "Whaaaaaat? For real? How was I supposed to know?"
            Panna "How many times have I told you-Read the manuscripts. Slowly."
            narrator "Panna and Moonga continue to drone on" 
            Sunela "There's so much I need to tell you Miss serene!! Uhm...uh..."
        menu:
            extend ""
            "Encourage Sunela":
                jump proceed2 
            "\"...\"":
                jump proceed2
            "Ask Sunela to calm down.":
                jump proceed2   

        label proceed2:
            Panna "We'll have more time to talk later, Sunela. There's still that simulacrum preventing us from leaving."

        menu:
            extend ""
            "\"Simu-what?\"":
                jump proceed3
            "\"What does it want?\"":
                jump proceed3
            "Politely, yet firmly tell Panna to stop using really big words.":
                jump proceed3

        label proceed3:
            Moonga "The dumb thing won't let us out until we answer the riddle, but it doesn't make any sense at all! That's why we needed a hero so they could smash it!"
            Sunela "But the uh simula-watcha-ma-call-it isn't a bad guy!! It's just lonely and wants a friend!"
            Panna "Regardless...This poses a problem. We don't exactly have enough food to stay down here much longer. We need a plan."
            Sunela "Oh!! I know!! Miss Serene can talk to it! She's really smart, I know she can figure it out!"
            Moonga "Yeah, right. Like she could figure it out. The riddle is so dumb. Let's just send her back and summon a REAL hero! Then we can just ask HIM to smash it."
            Panna "Unfortunately, Miss Serene is all we've got for now. I need more time to find a way to send her back."
            Sunela "Will you help us, Miss Serene?!"

        menu:
            extend ""
            "\"Well, we don't have much of a choice.\"":
                jump proceed4
            "\"Let's solve the riddle together.\"":
                jump proceed4
            "\"Good luck. I'll just stay here.\"":
                jump proceed4

        label proceed4:
            narrator "The team walks further, their footsteps uneven and sounding like soft thuds against the cave floor."
            Sunela "There it is! The sim moo laba laba!!"
            Panna " notably unamused It's Simulacrum."
            Moonga "Well, it's about to sim moo la crumble after I'm done with it. Can we just not waste our time talking and move on?"
        
            narrator "Talk to the suspicious statue?"
        
        menu: 
            extend ""
            "Yes.":
                jump statue_time
            "Yes. Unfortunately.":
                $ renpy.notify("You've unlocked: Context (!)")
                pause (2)
                $ wall_break = True
                jump statue_time

        label statue_time:

            narrator "The statue opens its eyes, its gaze seemingly piercing through you. "
            Statue "Ah, a visitor most strange has arrived at my step. State the purpose of your passage."
            narrator "The statue gives a malevolent stare."
            Panna "Interesting, that's a new response. Serene! Choose your words carefully! I have an awful premonition about this."

        menu:
            extend ""
            "Investigate the statue.":
                jump investigate
            "Check around for another exit.":
                jump investigate
            "\"We're lost and need a way out of here.\"":
                jump investigate

        label investigate:
            Statue "I see. An exit, you so desire. An exit, I may easily provide. The statue's eyes gives a yellow fluorescent glow."
            Sunela "I don't like this. I've never seen her eyes do that before!"
            Moonga "I'm telling you guys, we need to get rid of it!!"
            Statue "A foreshadowing comment. It appears our thoughts are alike. The statue's eyes shifts to a deep crimson hue."

        menu:
            extend ""
            "\"I've changed my mind. I want to stay here.\"":
                jump worship
            "Bow down and worship the statue.":
                jump worship
            "Have Panna check the manuscript.":
                jump worship
            "Ask it specifically how to leave the cave with your lives still in-tact.":
                jump worship

        label worship:
        Sunela "Good idea Miss Serene!! What does the book say Panna?!"
        Panna "audibly a nervous wreck Y-Yes. I'm already looking. WAIT I see IT. \"Only when its eyes turn deep red, does its heart shine a brilliant blue.\"" 
        Panna "...!" 
        Panna "I understand now! Serene! Take this bracelet!" 
        #Panna tosses a brilliant blue sapphire bracelet.
        narrator "Without hesitation, you slip the bracelet on your wrist. The blue sapphire shimmers against the light being cast from the statue's glowing eyes."  
        Statue "Ah, a strange identity finally revealed. You may pass but heed these words. Upon completion of the full cycle, your return shall be prompt. Leave."
        Serene "Yes. Going! Going very fast! C'mon guys let's go. NOW."
        narrator "As the lot of you scurry out of the cave, you approach a blindingly bright light leading outside."
        stop music
        #- Scene Transition to Outside - ################################################################################

        scene cave5
        play music "apotos.mp3" volume 0.05
        Sunela "We did it!! I knew Serene could do it!!"
        Serene "*Still catching her breath* Wow. That. That was actually kind of fun? Well, minus the whole possibly getting crushed to death thing, but still!"
        Panna "That was purely a stroke of luck; I can't believe it. Well, Miss Serene, I think we owe you an apology."
        Serene "What are you apologizing for?"
        Panna "For this...? All of this? For bringing you here?"
        Sunela "If anything, it's Moonga who should be apologizing!"
        Moonga "Maaaaaan, for what?! I still say we shoulda' just smashed it."
        Serene "It's okay. I mean, I kind of like it here. The air is better, the scenery looks nice, and-is that a castle...?"
        narrator "You point at the busting town ahead, made of an assortment of large structures." 
        Panna "Oh, you mean the capital? It is pretty big. Thankfully we're relatively close. We need to move now though if we want to get back before sunset. "
        Moonga "Aww, man. Can't we just camp out here?"
        Panna "Have you already forgotten that you ate all of the rations. ALL OF IT. How does one even do that. We had enough food for 6 days and you demolished it in two."
        Moonga "Listen! A strong adventurer's gotta' keep their strength up. You wouldn't get it."
        Panna "Technically, the brain needs more energy than your muscles, which is something you evidently lack."
        Sunela "I still have some biscuits mama baked for us!"
        narrator "Panna and Moonga both decline in unison." 
        Moonga "We need your strength at a 100\% Sunela! Keep those biscuits safe."
        "(It sounds like Panna wants to keep going, but Moonga and Sunela need some rest. What should we do?)"

        menu:
            extend ""
            "\"Let's break camp here for tonight.\"":
                jump camp_cave
            "\"Let's keep going. We'll have a warm bed waiting for us back home.\"":
                jump camp_cave

        # -Scene transition to the city of Balenci - #######################################################################

        label camp_cave:
            scene balenci
            camera:
                subpixel True pos (-1, 0) zpos -9.0 zoom 1.0 



            Serene "Internally: We've finally made it. It was a 3-hour walk, but it felt like an eternity. Walking along a dirt trail in heels? Nope. Not great. We don't like that."
            Sunela "We're almost here, Miss Serene! *Sunela looks over to her brothers* Do you think papa will be home when we get there?"
            Moonga "Dunno'. He's always in his office writing stuff."
            Panna "He should be. I believe this manuscript will pique his interest as well."
            "(I wonder what kind of person their father is...? They're lizards...But they talk, and kinda look like kids.)" 
            "(So, would that mean they look like people with tails? Oh, heck no, are they reptilians? Jacob would have a kick out of that.)"
            narrator "Your mind flashes back to a memory of Jacob at the office desperately explaining that Reptilians are alive and live under his house."
            narrator "You laugh out loud, recalling the wild look in his eyes as he shared his story."
            "(Now that I think about it, I haven't really thought of everyone back at the office, huh? I kind of wish they could be here and see this too.)"
            narrator "A familiar wave of dread washes over you as you remember your planned meeting with your boss and HR manager. The sinking feeling in your stomach returns." 
            Serene "Internally: Eh, maybe, except for them. I really don't understand, though." 
            Serene "I was having a mental breakdown just thinking about getting fired, and here I am saving three little kids from an evil statue-and it's fun...?" 
            Panna "We're here."
            Moonga "Yo, old man! *Moonga rests his arms overhead* We're back. You better not be taking a nap again."
            Sunela "Mama we're homeeeee! And we brought a guest with us!!"
            narrator "A distinguished human man with long legs and lanky arms enters the room." 
            narrator "He has a gentle aura about him, his brown eyes full of kindness despite the wearied eyebags underneath." 
            narrator "He seems very upbeat for a man that looks exhausted."
            Professor " Ah, Panna, Moonga, Sunela. It's good to see you back home safe."
            narrator "An older woman, who is also human, gracefully enters the room. Her presence is healing, and you instantly feel at ease around her."
            narrator "She is the living embodiment of a stereotypical mother." 
            Serene "Internally: They're not reptilian? I guess they could still be wearing a costume so they can blend in with people, though."
            Mama "Oh, thank heavens you all came back safe and sound. "
            Professor "I told you, dear, they may look like kids, but they know what they're doing. They were fine."
            Mama "Talent or not, I want my babies here. With us, nice and safe."
            Moonga "*Moonga looks away spitefully* tsk...Whatever. I'm going upstairs. *Moonga stops halfway* Thanks for your help or whatever Serene." 
            Moonga "You're alright...I guess. Later. *Moonga disappears to his room*"
            Mama "Okay kids, get some rest, we'll talk with your friend."
            Sunela "Okay mama! Goodnight papa! Thank you for saving us, Miss Serene!! Uhm, this is for you!! *Sunela hands you a folded piece of scroll paper and scurries upstairs*" 
            # - Serene "decides to look at the scroll later.
            Professor "Good job keeping everyone safe once again, Panna."
            Panna "Thank you, father. Also...we found it."
            Mama "Found what?"
            Professor "It's none of your concern, dear."
            Mama "No, you've put my children in jeopardy time and time again. What did you ask them to do..?"
            Panna "Here. *Panna hands over the scroll*"
            Professor "By the gods I can't believe it...! You found the manuscript?"
            Panna "That's not all. *Panna points to Serene*"
            Professor "! Miss Serene...? Now that I look at her. Your hair and those clothes... From what lands do you represent?"

        menu:
            "Lie.":
                jump professor
            "Explain what happened to you.":
                jump professor
            "Completely ignore the question and ask if he's secretly a lizard.":
                jump professor
            
        label professor:
            Professor "I see...Just like the legends. Panna, excellent work. You summoned her with this?"
            Panna "Correct. Unfortunately, Moonga chanted the wrong spell. She's not a hero."
            Professor "I see...That's quite alright. There will be more opportunities to try the Shimmer ritual at a later date." 
            Professor "Now, for the problem at hand.. Let's see, Miss...Serene was it...? I'm terribly sorry for the circumstances that have unfolded." 
            Professor "We've brought you here against your will, and you've saved my children. I never leave a debt unpaid. Panna?"
            Panna "Yes, father?"
            Professor "Bring the bespoke chalice." 
            Panna "Father, are you sure? What if-"
            Professor "Now, now. *The professor laughs* It's quite alright, I promise."
            narrator "Panna returns with a bright and shiny chalice."
            Professor "Hand that to Miss Serene for me please, Panna."
            narrator "You receive a chalice."
            Serene "Wait, I couldn't. This is too much."
            Professor "No, no by all means. Please take it. The lives of my children are worth so much more than this small cup." 
            Professor "Here. Take this card and follow this map."
            narrator "You receive a map of the town."
            Professor "This will guide you to the shop of one of my associates. Hand the chalice to her. She will know what to do."
            narrator "Upon touching the card, something awakens in your mind."
            "(I can see a shop on the map so vividly. Was it just from touching the card...?)"
            Mama "Thank you once again Miss Serene. Feel free to come back any time. You're always welcome. Alright, Panna. It's time for you go upstairs as well. Hurry on now."
            Panna "As you wish, mother. Thank you for your service, Miss Serene. Until we meet again. *Panna scurries upstairs with the others*"
            Professor "Also, here is my card. This should help you find your way back here." 
            Professor "I will continue where Panna left off in the Manuscripts and find a way for you to get back home. In the meantime, follow the map I gave you." 
            Professor "There, the shop owner, Amara, will take care of you. Until we meet again."
            narrator "You promptly leave the family estate and head to Amara's shop."

            jump chapter2


    # This ends the game.

    
