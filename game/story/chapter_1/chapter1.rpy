
# - This is the main script for Chapter 1 of Project Serene. Includes the code for an opening Splashscreen, and the variable for Encyclopaedia. 
# - (I'll move both of these into a seperate script later.)

#######################################

$ Encyclopaedia = True # Will probably delete later. Testing out the "Encyclopaedia" script.
default mtt = MouseTooltip(Text(""), padding={"x": 10, "y": -10}) # - Testing out a function where a message prompt appears when you hover over stuff.
#######################################
label splashscreen:
    scene black
    with Pause(2)
    #play ambience "Ocean.mp3" volume 0.5
    play sound "Ocean.mp3" volume 0.5 loop 
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

#########################################
# - Main storyline progression starts here. 𝔅𝔩𝔲𝔢 ℌ𝔬𝔯𝔦𝔷𝔬𝔫

label start:
        #jump outline_test
        label chapter1: # - calDate is setting up today's date for the "Time" screen. "store.theweekday" sets up the day of the week. We hide the quickmenu.
        $ calDate = calDate.replace(second=10, hour=12, minute=30, day=15, month=4, year=2018)
        $ store.theweekday = 5
        $ quick_menu = False
        $ chapter_status = 1
        stop music
        scene black
        call screen tooltip_test # - The screen for the message prompt.
        show screen DayDisplay
        call calendar(1)
        $ store.theweekday += 1
        show text "Monday, April 16th." with fade
        with Pause(3)
        hide text with fade
        stop ambience
        stop sound fadeout 0.5
        window hide 
        play music"butterfly.mp3" volume 0.1
        camera:
            perspective True
        #camera at parallax
        scene office2 with fade
        #show screen DayDisplay
        play ambience "office.mp3" loop volume 0.5
        $ quick_menu = True

        # after all choices have been seen game will automatically resume here
        narrator "The fading sunlight streams through the office windows." 
        narrator "The warm, 4 P.M. glow slowly losing its battle to the cold, fluorescent lights." 
        narrator "You hear muffled chatter around your cubicle."            
        
        #show npc1 at left, flip   
        show npc1_name at left:
            yrotate 180.0 
        camera:
            pos (250, 750) zoom 2.0 
        $ lipsync(npc1, "Coworker1.wav", "Did you see the look on Patrick's face after that meeting?")
        show npc2_name at right
        camera:
            subpixel True 
            pos (250, 750) zoom 2.0 
            ease 0.3 pos (1500, 751) zoom 2.0 
        #with Pause(1.10)
        #camera:
            #pos (1500, 751) zoom 2.0 
        $ lipsync(npc2, "Coworker2.wav", "Yeah...Today's gonna' be rough...") # - We have to use the lipsync variable here for the mouth flaps to work in sync with audio.
        pause 0.1
        show npc2_name: 
            parallel:
                hop
            parallel:
                linear 7.5 xalign 0.0
        show npc1_name at left: 
            #pause 0.8
            #flip
            parallel:
                hop
            parallel:
                linear 7.5 xalign 0.0     
        play sound "SFX/type_in.mp3" loop volume 0.05
        scene 
        camera:
            subpixel True pos (1878, 652) zpos 1238.0 
        show cubicle2
        show cubicle2:
            subpixel True blur 6.0
        show cubicle1
        show Serene:
            subpixel True pos (0.3, 0.1) matrixtransform ScaleMatrix(1.95, 1.95, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
            blur 0.0 
        narrator "Feelings of dread wash over you. You continue typing, trying to focus on the computer screen while keeping your composure." 
        pause 0.1
        show Devon behind cubicle1:
            subpixel True xpos 1404 
            ypos -0.05 
            ease 1.04 ypos -0.34 
        with Pause(1.14)
        show Devon behind cubicle1:
            pos (1404, -0.34)     
        narrator "A man peaks over the cubicle."
        $ renpy.say("", "A man peaks over the cubicle.", interact=False)
        call screen serene_office
        
        menu annoying_devon1 (screen = "choice_return") :
                narrator "A man peaks over the cubicle." 
                "Finish typing your e-mail.":
                    jump ignore_devon
                "Stop working and talk to your coworker.":
                    $ renpy.notify("You've unlocked: Context (!)")
                    pause(1.5)
                    $ wall_break = True
                    jump ignore_devon

        hide npc1
        hide npc1_name
        hide npc2 
        narrator "You see, your coworker, Devon, hovers over you like a lost puppy." 
        narrator "Devon was hired a month before you, but he gloms onto you like an imprinted duckling for some reason."
        jump see_devon

        label see_devon: # - Delete this label later if no longer useful.
            
            Devon "Hey, Serene!"
            extend " Can I borrow your pen real fast?"
            Devon "I think I dropped it somewhere on my way back here."
        

        label ignore_devon:       
            Devon "Hey, Serene!"
            extend " Can I borrow your pen real fast?"
            Devon "I think I dropped it somewhere on my way back here."
            Devon "..."
            Devon "......"
            Devon "............!"
            Devon "What's up? {w=2.0}You look worried.{w=1.0} Is it about the lay-offs...?" 
            
            #narrator "Your keyboard's keystrokes grow louder in an attempt to drown out his sorry attempt at consoling you."
            camera:
                linear 10.0 ypos 300 zpos 900 

            show Serene:
                subpixel True 
                blur 0.0 
                linear 6.0 blur 4 
            show cubicle1:
                subpixel True
                blur 0.0
                linear 6.0 blur 4
           
            #show Devon grimace
            narrator "Ever eager to step on eggshells, Devon delves into an unsolicited therapy session." 
            play sound "SFX/type_in.mp3" volume 0.2 loop
            narrator "So you type, louder and more deliberate, keystrokes firing out in an attempt to ignore this nonsense." 
            narrator "Devon does not relent."
            #show Devon neutral
            Devon "You'll be alright. I mean, they already fired like five people in our department, what are the odds they'd keep going? "
            stop sound
            narrator "You abruptly stop typing, and without turning your head, you shift your gaze to meet Devon's."
            #show Devon grimace
            show Devon smile
            narrator "He's looking at you with his signature smile." 
            #show Devon neutral
            narrator " His bright attitude is almost blinding sometimes." 

            camera:
                subpixel True 
                ease 2.0 pos (1950, 1035) zpos 1314.0 


            show Serene:
                linear 2 blur 0.0

            show cubicle1:
                linear 2 blur 0.0

            narrator "You take a deep breath before summoning the patience to respond."
            play sound "SFX/chair_with_wheels.mp3"
            

            window hide
            camera:
                subpixel True pos (1950, 495) zpos 1114.0 
            show Serene:
                subpixel True 
                ypos 0.0 yrotate 0.0 
                linear 0.61 ypos -0.12 yrotate 207.0 
            with Pause(0.71)
            show Serene mad:
                ypos -0.12 yrotate 207.0 
            window show

            Serene "Devon, I appreciate you but please. I just—" 
            #show office with hpunch 
            play sound "SFX/crash.mp3" volume 0.5
            with hpunch
            stop music fadeout 0.0
            
            pause 2.0
            narrator "You are suddenly interrupted by an authoritative voice booming over your cubicle."
            show Devon surprise 
            show Serene curious:
                ease 0.4 ypos -0.12 yrotate 0 blur 0.0
            
            Devon "Op!" 
            
            show Devon behind cubicle1:
                subpixel True xpos 1404 
                ypos -0.34 
                ease 0.6 ypos -0.05 
            with Pause(1.14)

            narrator "Devon ducks and quickly scurries back to his side of the cubicle." 

            Manager "Serene... Can you meet me at the corner office in five minutes?"

            Serene "Y-yes. I'll be right there."

            narrator "The Manager walks back down the hallway, escorting an emotional, laid-off employee with security in tow." 
            narrator "Their cries linger in the stale office air like forlorn dissonance."   
            play music "beneath_mask.mp3" volume 0.1
            show Serene normal:
                ease 0.4 ypos 0 
            narrator "You sit blankly at your desk." 
            narrator "It feels like all the blood has drained from your body, your hands are like icicles." 
            se "(I hate this.  I hate this. I hate this. I hate this feeling. I HATE this.)" 
            show Serene:
                yrotate 180
            #Serene breathes in and exhales deeply
            Serene "Just breathe.  Just. Breathe." 
            play sound "SFX/phone_notif.mp3" volume 0.5
            pause(2.0)
            narrator "Your Phone chimes in your pocket. You've received a new message."
            $ renpy.say("", "Your Phone chimes in your pocket. You've received a new message.", interact=False)
            call screen serene_office_chapter1
            #Serene reaches for Phone.
            play sound "SFX/confirm.mp3" volume 0.5
            show Serene curious
            pause(1.5)
            Phone " Unknown Number - Principality of Balenci"
            
            narrator "Puzzled, you swipe on the notification to read the message." 
            
            Phone " A Shimmer request has been initiated. Reply (Y) to accept." 

            #Serene Internally:
            se "(Principality of Balenci...? {w=1.0} What is this...?{w=1.0} A scam...?)"
            play sound "SFX/phone_down.mp3"
            pause(1)
            show Serene normal smile
            narrator "Shaking your head you set your Phone down before laughing cathartically." 
        
            #Devon yells from across the cubicle
            Devon "That's right Serene! You're finally listening to what I've been telling you!!" 
            show Serene curious meh
            Devon "You just need a positive attitude, and everything will be-" 
            Devon "Oh whats up...?" 
            Devon "You're on the Phone?!" 
            show Serene ugh mouth_X
            Devon "Keep my voice down?!"
            Devon "Oh, my fault I...!" 
            
            narrator "Devon's voice starts to fade as if he is moving further and further away." 
            
            #Serene Internally:
            show Serene normal
            se "(...Okay, yeah. Never mind. I'm over it today.)"
            menu:
                extend "" 
                "Reply to the message.":
                    $ chapter1_status = 2
                    pause(1.5)
                "Get ready for your meeting with the manager.":
                    $ renpy.notify("You've unlocked: Context (!)")
                    pause(1.5)
                    $ wall_break = True
            narrator "You pick up your Phone, and without hesitating you reply (Y)."

            Phone "Thank you for your response. It appears that you are in an unsatisfactory location." 
            Phone "Please relocate to an area away from other people."

            narrator "You look at the message in bewilderment." 
            
            #Serene Internally:
            show Serene curious mouth_X
            se "(Huh. That's a new one. No Nigerian prince to give money to?)"
            show Serene curious smile
            #Serene begins to laugh
            se "(I'm so dumb.)" 
            
            Phone " Shimmer will commence in 10 seconds."
            show Serene normal mouth_X
            se "(For a second there, I was really hoping something was going to happen...)"
            
            narrator "A flash of sparkling bright white light comes across the room and envelopes the world around you."
            
            Serene "Okay, I spoke too soon; I guess I'm just dying." 
            
            Phone "Shimmer will commence in 5 seconds."
            
            #Reality begins to warp**
            
            Serene "Surprisingly, I'm okay with this."

            #########################################################################################
            #The screen fades out from white to black.
            
            show cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            
            camera:
                subpixel True pos (1896, 1080) zpos 1217.0 


            stop ambience 
            
            play ambience "ambience/cave.mp3" loop volume 0.5
            play music "cake.mp3" volume 0.05
            
            show Moonga at flip with dissolve:
                xalign -0.2 yalign 1.0
                easein 1.0 xalign 0.2 


                
            Moonga "Wait look! Something's happening!"
            show Sunela at flip:
                xalign -0.2 yalign 1.2
                easein 1.0 xalign 0.0 
            Sunela "SEE! I TOLD YOU!!"
            show Panna:
                xalign 1.5 yalign 1.0
                easein 1.0 xalign 1.0 
            Panna "Both of you...Relax."
            #A ring of small flames materializes around you.
            
            Moonga "Aww man. Lame, it's just a girl."
            
            Sunela "HEY! Girls can be heroes too! I wonder what kind of powers she has." 
            Sunela "The book said they can do all kinds of stuff!"
            
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            show Serene:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
                xalign 0.5 yalign 1.0

            
            show cave6:
                blur 6.0
            camera:
                subpixel True pos (0, 0) zpos -100.0 zoom 1.0
                ease 10.0 zpos -300.0
            show Serene:
                subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 468.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 


            narrator "You stand in the middle of a bizarre, glowing circle." 
            narrator "As the flames dissipate, your eyes are drawn to three small figures standing around you." 
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            camera:
                subpixel True pos (1896, 1080) zpos 1217.0 zoom 2.0
            show Moonga at flip:
                xalign 0.2 yalign 1.0
            show Sunela at flip:
                xalign 0.0 yalign 1.2
            show Panna:
                xalign 1.0 yalign 1.0
            narrator "Three children in identical lizard suits stand before you." 
            $ renpy.say("", "Three children in identical lizard suits stand before you.", interact=False) # renpy.say keeps the dialogue in place after calling a screen.
            $ chapter1_status = 2
            call screen serene_office_chapter1 
            play sound "SFX/wham.mp3" volume 0.75
            with vpunch
            stop music fadeout 0.0
            pause(0.5)
            narrator "Wait."
            
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blur 6.0
            show Serene:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
                xalign 0.5 yalign 1.0
            camera:
                subpixel True pos (0, 0) zpos -100.0 zoom 1.0
            show Serene:
                subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 468.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
            narrator "You rub your eyes in attempt to clear your vision. You look at the three small figures again."
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blur 6.0
            camera:
                subpixel True pos (4000, 2500) zpos 1217.0 zoom 3.0
            show Moonga at flip:
                xalign 0.5 yalign 1.0
            show Sunela at flip:
                xalign 0.3 yalign 1.2
            show Panna:
                xalign 0.85 yalign 1.0
            #Serene Internally
            se "(Those aren't costumes...)" 
            se "(Those are children...but they're {i}lizards{/i}?)"
            se "(That can't be right. Where {i}am I{/i}?)"

            Moonga "Hey Lady! {w=1.0}Do something cool...{w=2.0}like casting light magic out of your eyes or something."

            narrator "The angry lizard continues to stare at you with demanding impression."

            Panna "Let me see the book again. I'm certain we casted the spell incorrectly."
            show Moonga at flip:
                xalign 0.5 yalign 1.0
                parallel:
                    yalign 1.0
                    linear 0.5 yalign 0.75
                    linear 0.5 yalign 1.0
                    linear 0.5 yalign 0.75
                    linear 0.5 yalign 1.0

                parallel:
                    easein 3.0 xalign 0.65

            pause 1.5
            Sunela "Uhm. Excuse me, Miss, are you our hero?"

            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blur 6.0
            show Serene:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
                xalign 0.5 yalign 1.0
            camera:
                subpixel True pos (0, 0) zpos 0.0 zoom 1.0
            show Serene:
                subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 468.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
            
            narrator "Shakily, you manage to stand up and attempt to find your footing."
            
            Serene "Where am I...?"
            
            show black behind Serene with dissolve
            hide cave6
            narrator "You briefly regain your composure before reality and time seemingly shifts and warps around you."
            play sound "SFX/ai_voice.mp3" loop
            
            narrator "An advanced human-like AI echoes through the forefront of your mind." 
            
            Phone "Shimmer complete. Arrived at Destination: Principality of Balenci."
            
            narrator "Alarmed, you look around the cave frantically trying to discern where the voice was coming from."

            show Serene curious:
                yrotate 180
                pause 1.0
                yrotate 0
                pause 1.0
                yrotate 180
            
            se "(Am I having auditory hallunications? What is a Shimmer...? Does this have anything to do with that text earlier?!)"
            
            Phone "Good morning, Serene. The time is now 8:53 am."
            
            narrator "You look up at the cave ceiling, the rock walls cascade into the shadows, pooling around the centre like a dark lake." 

            show Serene mad:
                yrotate 0
            
            Serene "You're not just a voice in my head, right? Please tell me I'm not going any crazier than I already am." 
            
            Phone "Query received:{w=2.0} Activating \"Internal Audio Mode.\" {w=1.5}Tachypnea and rapid heart rate detected." 
            show Serene curious:
                yrotate 180
            Phone "It appears you are under distress." 
            Phone "Warning:{w=2.0} Battery life at 10\%. {w=2.0}Switching to Low Power Mode."

            
            se "(Internal audio mode?  Low battery...? I knew this voice was familiar. {w=2.0}Is this my {i}phone{/i}?)"
            
            Phone "Query received:{w=2.0} This is the only phone signed into your account. {w=2.5}Powering down."
            stop sound 
            
            #Time resumes.
            show Serene curious:
                yrotate 0
                pause 1.0
                yrotate 180
                pause 1.0
                yrotate 0
            
            Serene "You can read my thoughts?! {w=1}This doesn't make any sense...! {w=2}Uh, power... on!"
            show cave6 behind Serene with dissolve:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blur 6.0

            pause 2.0
            
            narrator "An awkward silence pierces the cave." 

            pause 2.0

            show Serene normal 
            
            narrator"The silence seems to elevate the atmospheric sounds of your surroundings." 
            narrator "The metronome of recurrent drips echoes through the cave." 
            
            play music "music/chill_vibe.mp3" volume 0.3
            Moonga "\"{i}Power on? {/i}\""
            #Moonga laughs hysterically 
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blur 6.0
            camera:
                subpixel True pos (4000, 2500) zpos 1217.0 zoom 3.0
            show Moonga at flip:
                xalign 0.65 yalign 1.0
            show Sunela at flip:
                xalign 0.3 yalign 1.2
            show Panna:
                xalign 0.85 yalign 1.0
            Moonga "Maaaan. She can't even cast any spells either. {w=1.5}She just keeps talking to herself."
            show Moonga:
                yrotate 180
                ease 0.5 yrotate 0
                parallel:
                    yalign 1.0
                    linear 0.5 yalign 0.75
                    linear 0.5 yalign 1.0
                    linear 0.5 yalign 0.75
                    linear 0.5 yalign 1.0
                    repeat

                parallel:
                    easein 10.0 xalign -0.2

            show Panna:
                yrotate 0
                parallel:
                    yalign 1.0
                    linear 0.5 yalign 0.75
                    linear 0.5 yalign 1.0
                    linear 0.5 yalign 0.75
                    linear 0.5 yalign 1.0
                    repeat

                parallel:
                    easein 10.0 xalign -0.2
            Sunela "Uhm... Miss...?"
            show Sunela at flip:
                xalign 0.3 yalign 1.2
                parallel:
                    yalign 1.2
                    linear 0.3 yalign 0.95
                    linear 0.3 yalign 1.2
                    linear 0.3 yalign 0.95
                    linear 0.3 yalign 1.2

                parallel:
                    easein 2.0 xalign 0.45
            
            narrator "You spin your heels and turn around to face Sunela."
        
        
        menu sunela_intro:
            extend ""
            "\"Where am I?\"":
                jump proceed
            "\"Oh, I'm Serene. What's your name?\"":
                jump proceed
            "Pretend to be a hero.":
                jump proceed   
            "\"Why do I hear a British man narrating everything in my head?\"" if wall_break: 
                jump proceed

    
        label proceed:
            Sunela "Uh, uhm. I'm Sunela, Miss Serene!! These two are my big brothers {w=2.0}Panna and Moonga!" 
            hide Sunela

            show cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) blur 6.0
            camera:
                subpixel True pos (2850, 2500)

            show Moonga:
                yrotate 0
                xalign 0.2 yalign 1.0

            show Panna:
                yrotate 180
                xalign 0.0 yalign 1.0

            narrator "Moonga fixes their gaze on you, looking mildly disappointed before introducing themself."
            show Moonga:
                ease 0.5 yrotate 180 
            Moonga "...Nice to meet you, ma'am."
            show Moonga:
                ease 0.35 yrotate 0
          
            narrator "Without lifting his head, Panna looks up from his book. He corrects his wide framed glasses before introducing himself." 
        
            Panna "Yes. Hello." 
            Panna "Anyway, Moonga, take a look at this line here. We did the wrong spell."
            Moonga "Whaaaaaat? For real? How was I supposed to know?"
            Panna "How many times have I told you-"
            Panna "Read the manuscripts. {w=1.0}{i}Slowly.{/i}"
            narrator "Panna and Moonga continue to drone on..." 
            hide Moonga
            hide Panna
            camera:
                subpixel True pos (4000, 2500) zpos 1217.0 zoom 3.0
            show Sunela:
                yrotate 180
                yalign 1.2 xalign 0.45
            Sunela "There's so much I need to tell you Miss Serene!! Uhm...uh..."
        menu:
            extend ""
            "Encourage Sunela.":
                jump proceed2 
            "\"...\"":
                jump proceed2
            "Ask Sunela to calm down.":
                jump proceed2   

        label proceed2:
            camera:
                subpixel True pos (2850, 2500)
            
            hide Sunela

            show Moonga:
                yrotate 0
                xalign 0.2 yalign 1.0

            show Panna:
                yrotate 180
                xalign 0.0 yalign 1.0


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
            show Moonga:
                ease 0.5 yrotate 180 
            Moonga "The dumb thing won't let us out until we answer the riddle, but it doesn't make any sense at all!" 
            Moonga "That's why we needed a hero so they could smash it!"
            hide Moonga
            hide Panna
            camera:
                subpixel True pos (4000, 2500) zpos 1217.0 zoom 3.0
            show Sunela:
                yrotate 180
                yalign 1.2 xalign 0.5
            show Panna:
                yrotate 180
                parallel:
                    yalign 1.0
                    linear 0.5 yalign 0.85
                    linear 0.5 yalign 1.0
                    linear 0.5 yalign 0.85
                    linear 0.5 yalign 1.0
                    linear 0.5 yalign 0.85
                    linear 0.5 yalign 1.0
                    linear 0.5 yalign 0.85
                    linear 0.5 yalign 1.0
                parallel:
                    ease 4.2 xalign 0.3
            Sunela "But the uh simula-watcha-ma-call-it isn't a bad guy!! It's just lonely and wants a friend!"

            Panna "Regardless...This poses a problem. We don't exactly have enough food to stay down here much longer. We need a plan."

            show Sunela:
                ease 0.5 yrotate 0

            Sunela "Oh!! I know!! Miss Serene can talk to it! She's really smart, I know she can figure it out!"
            camera:
                subpixel True pos (2850, 2500)
            
            hide Sunela
            hide Panna

            show Moonga:
                yrotate 180
                xalign 0.2 yalign 1.0
            Moonga "Yeah, right. Like she could figure it out. The riddle is so dumb." 
            Moonga "Let's just send her back and summon a {i}REAL{/i} hero. {w=2.0}Then we can just ask {i}HIM{/i} to smash it."
            hide Moonga
            camera:
                subpixel True pos (4000, 2500) zpos 1217.0 zoom 3.0
            show Sunela:
                yrotate 180
                yalign 1.2 xalign 0.5
            show Panna:
                yrotate 180
                yalign 1.0 xalign 0.3
                ease 0.5 yrotate 0
            Panna "Unfortunately, Miss Serene is all we've got for now." 
            Panna "I need more time to find a way to send her back."
            show Panna:
                ease 0.5 yrotate 180
            show Sunela:
                xalign 0.5 yalign 1.2
                parallel:
                    yalign 1.2
                    linear 0.3 yalign 0.95
                    linear 0.3 yalign 1.2
                    linear 0.3 yalign 0.95
                    linear 0.3 yalign 1.2

                parallel:
                    easein 2.0 xalign 0.55
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
            stop music
            
            scene scrolling_cave 
            camera:
                subpixel True pos (0, -0) zpos 0.0 zoom 1.01 

            show Moonga:
                xalign 0.1
                yrotate 180
                parallel:
                    yalign 1.2
                    linear 0.6 yalign 0.95
                    linear 0.6 yalign 1.2
                    linear 0.6 yalign 0.95
                    linear 0.6 yalign 1.2
                    repeat

            show Panna:
                xalign 0.3
                yrotate 180
                parallel:
                    yalign 1.2
                    linear 0.5 yalign 0.95
                    linear 0.5 yalign 1.2
                    linear 0.5 yalign 0.95
                    linear 0.5 yalign 1.2
                    repeat

            show Sunela:
                xalign 0.5
                yrotate 180
                parallel:
                    yalign 1.4
                    linear 0.45 yalign 1.15
                    linear 0.45 yalign 1.4
                    linear 0.45 yalign 1.15
                    linear 0.45 yalign 1.4
                    repeat

            show Serene behind Sunela:
                xalign 0.7
                yrotate 180
                parallel:
                    yalign 1.4
                    linear 0.6  yalign 1.2
                    linear 0.6 yalign 1.4
                    repeat
            play music "fe_mystery.mp3" volume 0.2           
            with fade
            narrator "The team walks further, their footsteps uneven and sounding like soft thuds against the cave floor."
            Sunela "There it is! The sim moo laba laba!!"
            #Panna notably unamused
            Panna "It's {i}Simulacrum.{/i}"
            Moonga "Well, it's about to sim moo la crumble after I'm done with it." 
            Moonga "Can we just not waste our time talking and move on?"
    
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
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            
            camera:
                subpixel True pos (3840, 2160) zpos 600.0 zoom 3.0


            
            with fade
            narrator "The statue opens its eyes, its gaze seemingly piercing through you. "
            Statue "Ah, a visitor most strange has arrived at my step. State the purpose of your passage."
            narrator "The statue gives a malevolent stare."
            camera:
                subpixel True pos (1780, 2160) zpos 600.0 zoom 3.0
            show Serene:
                xalign 0.35
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180
            
            show Sunela behind Serene:
                xalign 0.25
                yalign 1.8
                yalign 1.9
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180

            show Panna:
                xalign 0.15
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180

            show Moonga:
                xalign 0.05
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180

            Panna "Interesting, that's a new response...{w=1.5}Wait, Serene!" 
            Panna "Choose your words carefully! I have an awful premonition about this."
            $ renpy.say("Panna", "Choose your words carefully! I have an awful premonition about this.", interact=False) # renpy.say keeps the dialogue in place after calling a screen.
            $ chapter_status = 3
            call screen serene_office 

        menu (screen = "choice_return"):
            Panna "Choose your words carefully! I have an awful premonition about this."
            "Investigate the statue.":
                jump investigate
            "Check around for another exit.":
                jump investigate
            "\"We're lost and need a way out of here.\"":
                jump investigate

        label investigate:
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            camera:
                subpixel True pos (3840, 2160) zpos 600.0 zoom 3.0
            Statue "I see. An exit, you so desire. An exit, I may easily provide." 
            narrator "The statue's eyes gives a yellow fluorescent glow."
            camera:
                subpixel True pos (1780, 2160) zpos 600.0 zoom 3.0
            show Serene:
                xalign 0.35
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180
            
            show Sunela behind Serene:
                xalign 0.25
                yalign 1.8
                yalign 1.9
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180

            show Panna:
                xalign 0.15
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180

            show Moonga:
                xalign 0.05
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180
            Sunela "I don't like this. I've never seen its eyes do that before!"
            Moonga "I'm telling you guys, we need to get rid of it!!"
            scene cave6:
                subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            camera:
                subpixel True pos (3840, 2160) zpos 600.0 zoom 3.0
            Statue "A foreshadowing comment. It appears our thoughts are alike."
            narrator "The statue's eyes shifts to a deep crimson hue."

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
            camera:
                subpixel True pos (1780, 2160) zpos 600.0 zoom 3.0
            show Serene:
                xalign 0.35
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180
            show Sunela behind Serene:
                xalign 0.25
                yalign 1.8
                yalign 1.9
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180

            show Panna:
                xalign 0.15
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180

            show Moonga:
                xalign 0.05
                yalign 1.8
                subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
                yrotate 180
        Sunela "Good idea Miss Serene!! What does the book say Panna?!"
        #Panna audibly a nervous wreck
        Panna "Y-Yes. I'm already looking. {w=0.8}Wait...{w=0.8}I see it...! {w=2.0}\"Only when its eyes turn deep red, does its heart shine a brilliant blue.\"" 
        Panna "...!" 
        Panna "I understand now!{w=1} Serene! {w=0.5}Take this bracelet!" 
        #Panna tosses a brilliant blue sapphire bracelet.
        narrator "Without hesitation, you slip the bracelet on your wrist." 
        narrator "The blue sapphire shimmers against the light being cast from the statue's glowing eyes."  
        scene cave6:
            subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.33)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        camera:
            subpixel True pos (3840, 2160) zpos 600.0 zoom 3.0
        Statue "Ah, a strange identity finally revealed..." 
        Statue "You may pass...{w=1.5}But heed these words;" 
        Statue "Upon completion of the full cycle, your return shall be prompt." 
        Statue "Now leave."
        camera:
            subpixel True pos (1780, 2160) zpos 600.0 zoom 3.0
        show Serene:
            xalign 0.35
            yalign 1.8
            subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
            yrotate 180
        show Sunela behind Serene:
            xalign 0.25
            yalign 1.8
            yalign 1.9
            subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
            yrotate 180
        show Panna:
            xalign 0.15
            yalign 1.8
            subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
            yrotate 180
        show Moonga:
            xalign 0.05
            yalign 1.8
            subpixel True matrixtransform ScaleMatrix(0.5, 0.5, 1.0)
            yrotate 180
        Serene "Absolutely understood! {w=1.0} Leaving, leaving, leaving, thank you so much..! {w=2.0}"
        scene cave_exit
        camera:
            subpixel True pos (0, 0) zpos 0.0 zoom 1.0
        narrator "As the lot of you scurry out of the cave, you approach a blindingly bright light leading outside."
        stop music
        stop ambience
        #- Scene Transition to Outside - ################################################################################

        scene cave5      
        camera:
            subpixel True xpos 3100 zpos 785.0 ypos 2484 zoom 3.0
        with fade
        play ambience "ambience/windy_ambience.mp3" volume 0.4
        play music "apotos.mp3" volume 0.1
        Sunela "We did it!! I knew Serene could do it!!"
        #*Still catching her breath* 
        Serene "Wow. That. That was actually kind of fun?" 
        Serene "Well, minus the whole possibly getting crushed to death thing, but still!"
        Panna "That was purely a stroke of luck; I can't believe it. Miss Serene, I think we owe you an apology."
        Serene "What are you apologizing for?"
        Panna "For this...? All of this? For bringing you here?"
        Sunela "If anything, it's Moonga who should be apologizing!"
        Moonga "Maaaaaan, for what?! I still say we shoulda' just smashed it."
        Serene "It's okay. I mean, I kind of like it here. The air is better, the scenery looks nice, and-"
        stop music
        Serene "Wait is that a castle...?"
        narrator "You point at the bustling town ahead, made of an assortment of large structures." 
        Panna "Oh, you mean the capital? Thankfully we're relatively close." 
        Panna "We need to move now though if we want to get back before sunset. "
        #Moonga snickers
        play music "music/chill_vibe.mp3" volume 0.3
        Moonga "Can't we just camp out here?"
        Panna "Have you already forgotten that you ate all of the rations? ALL OF IT." 
        Panna "How does one even do that. We had enough food for 6 days and you demolished it in two."
        Moonga "Listen! A strong adventurer's gotta' keep their strength up. You wouldn't get it."
        Panna "Technically, the brain needs more energy than your muscles, which is something you evidently lack."
        Sunela "I still have some biscuits mama baked for us!"
        narrator "Panna and Moonga both decline in unison." 
        Moonga "We need your strength at a 100\% Sunela! Keep those biscuits safe."
        se "(It sounds like Panna wants to keep going, but Moonga and Sunela need some rest. What should we do?)"

        menu:
            extend ""
            "\"Let's break camp here for tonight.\"":
                jump camp_cave
            "\"Let's keep going. We'll have a warm bed waiting for us back home.\"":
                jump camp_cave

        # -Scene transition to the city of Balenci - #######################################################################

        label camp_cave:
            scene forest
            camera:
                subpixel True pos (-1, 0) zpos -9.0 zoom 1.0 
            with fade
            se "(We're almost there. It was a 3-hour walk, but it felt like an eternity.)" 
            se "(Walking along a dirt trail in heels? Nope. Not great. We don't like that.)"
            Sunela "We're almost here, Miss Serene!" 
            # Sunela looks over to her brothers
            Sunela "Do you think papa will be home when we get there?"
            Moonga "Dunno'. He's always in his office writing stuff."
            Panna "He should be. I believe this manuscript will pique his interest as well."
            se "(I wonder what kind of person their father is...?{w=2.0} They're lizards...{w=1.0}But they talk, {w=0.5}and kinda look like kids.)" 
            se "(So, would that mean they look like people with tails...?{w=2.0} {i}Are they reptilians...?!{/i} {w=2.0}Jacob would have a kick out of that.)"
            #Robb has a funny recording about the reptillians mocking Jacob's voice. Keeping a note for later.####
            narrator "Your mind flashes back to a memory of Jacob at the office desperately explaining that Reptilians are alive and live under his house."
            narrator "You laugh out loud, recalling the wild look in his eyes as he shared his story."
            se "(Now that I think about it, I haven't really thought of everyone back at the office, huh?)" 
            se "(I kind of wish they could be here and see this too.)"
            narrator "A familiar wave of dread washes over you as you remember your planned meeting with your boss and HR manager." 
            narrator "The sinking feeling in your stomach returns." 
            se "(Eh, maybe, except for them.)" 
            se "(I really don't understand, though.)" 
            se "(I was having a mental breakdown just thinking about getting fired...)" 
            se "(Now here I am saving three little kids from an evil statue-{w=2.0}{i}and it's fun...?{/i})" 
            stop music
            scene professor_house3
            Panna "We're here."
            Moonga "Yo, old man!" 
            #*Moonga rests his arms overhead* 
            Moonga "We're back. You better not be taking a nap again."
            Sunela "Mama we're homeeeee! And we brought a guest with us!!"
            stop ambience
            scene professor_inside
            play music "music/persona_chill.mp3" volume 0.05
            play ambience "ambience/old_house.mp3" volume 0.1
            play audio "fireplace.mp3" volume 0.1
            narrator "A distinguished human man with long legs and lanky arms enters the room." 
            narrator "He has a gentle aura about him, his brown eyes full of kindness despite the wearied eyebags underneath." 
            narrator "He seems very upbeat for a man that looks exhausted."
            Professor " Ah, Panna, Moonga, Sunela. It's good to see you back home safe."
            narrator "An older woman, who is also human, gracefully enters the room." 
            narrator "Her presence is healing, and you instantly feel at ease around her."
            narrator "She is the living embodiment of a stereotypical mother." 
            se "(Huh. So they're {i}not{/i} reptilian...?{w=2.0} Maybe it's just a costume...?)"
            Mama "Oh, thank heavens you all came back safe and sound. "
            Professor "I told you, dear, they may look like kids, but they know what they're doing. They were fine."
            Mama "Talent or not, I want my babies here. With us, nice and safe."
            #*Moonga looks away spitefully*
            Moonga "tsk...Whatever. I'm going upstairs." 
            #*Moonga stops halfway* 
            Moonga "Thanks for your help or whatever \"Miss Sardine.\"" 
            Moonga "You're alright...{w=0.5}I guess."
            Moonga "Later." 
            #*Moonga disappears to his room*
            Mama "Okay kids, get some rest, we'll talk with your friend."
            Sunela "Okay mama! Goodnight papa! Thank you for saving us, Miss Serene!!" 
            Sunela "Uhm, this is for you!!" 
            $ renpy.notify("You've unlocked: Context (!)")
            extend "{w=2.0}" 
            show text "Sunela handed you a folded scroll...Maybe you can look at it later?" with dissolve
            pause(5)
            hide text with fade
            #*Sunela hands you a folded piece of scroll paper and scurries upstairs*
            # - Serene "decides to look at the scroll later.
            Professor "Good job keeping everyone safe once again, Panna."
            Panna "Thank you, father. Also...we found it."
            Mama "Found what?"
            Professor "It's none of your concern, dear."
            Mama "No, you've put my children in jeopardy time and time again. {w=2.5}What did you ask them to do..?"
            Panna "Here." 
            # *Panna hands over the scroll*
            Professor "By the gods I can't believe it...! You found the manuscript?"
            Panna "That's not all." 
            #*Panna points to Serene*
            Professor "...({b}{i}! {/b}{/i})" 
            Professor "{i}Miss Serene...?{/i}{w=2.0} Now that I look at her..." 
            Professor "{i}Your hair and those clothes...{/i}{w=2.0} From what lands do you represent?"

        menu:
            extend ""
            "Lie.":
                jump professor
            "Explain what happened to you.":
                jump professor
            "Completely ignore the question and ask if he's secretly a lizard.":
                jump professor
            
        label professor:
            Professor "I see...Just like the legends." 
            Professor "Panna, excellent work. You summoned her with {i}this?{i}"
            Panna "Correct. Unfortunately, Moonga chanted the wrong spell. She's not a hero."
            Professor "I see...That's quite alright.{w=2.0} There will be more opportunities to try the Shimmer ritual at a later date." 
            Professor "Now, for the problem at hand...{w=2.0} Let's see...{w=1} Miss...{w=1}{i}Serene was it...?{/i}" 
            Professor "I'm terribly sorry for the circumstances that have unfolded." 
            Professor "We've brought you here against your will, {i}and{/i} you've saved my children." 
            Professor "I never leave a debt unpaid.{w=2} Panna?"
            Panna "Yes, father?"
            Professor "Bring the bespoke chalice." 
            Panna "Father, are you sure? What if-"
            Professor "Now, now." 
            #*The professor laughs* 
            Professor "It's quite alright, I promise."
            narrator "Panna returns with a bright and shiny chalice."
            Professor "Hand that to Miss Serene for me please, Panna."
            narrator "You receive a chalice."
            $ renpy.notify("You've unlocked: Context (!)")
            extend ""
            pause(0.5)
            Serene "Wait, I couldn't. This is too much."
            Professor "No, no by all means. Please take it." 
            Professor "The lives of my children are worth so much more than this small cup." 
            Professor "Here. Take this card and follow this map."
            narrator "You receive a map of the town."
            $ renpy.notify("You've unlocked: Context (!)")
            extend ""
            pause(0.5)
            Professor "This will guide you to the shop of one of my associates. Hand the chalice to her. She will know what to do."
            narrator "Upon touching the card, something awakens in your mind."
            se "(I can see a shop on the map so vividly. {w=2.0} Was it just from touching the card...?)"
            Mama "Thank you once again, Miss Serene. Feel free to come back any time." 
            Mama "Alright, Panna. It's time for you to go upstairs as well. Hurry on now."
            Panna "As you wish, mother. Thank you for your service, Miss Serene." 
            Panna "Until we meet again." 
            # *Panna scurries upstairs with the others*
            Professor "Also, here is my card."
            $ renpy.notify("You've unlocked: Context (!)")
            extend ""
            pause(1.5)
            Professor "This should help you find your way back here." 
            Professor "I will continue where Panna left off in the Manuscripts and find a way for you to get back home." 
            Professor "In the meantime, follow the map I gave you." 
            Professor "Talk to the shop owner,  {color=#f00}Amara{/color}. She will take good care of you." 
            Professor "Until we meet again."
            narrator "You promptly leave the family estate and head to Amara's shop."
            stop ambience
            stop music
            show black with fade
            show text "End Chapter 1." with dissolve
            pause 

            jump chapter2

    
