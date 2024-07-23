##########################################################################################

default time_day = "Morning"
default sleep_early = True

default transition_is_playing = False

screen walking_transition():
    add "walk_transition"
    
screen choice_time():
    frame:
        xalign 0.5
        yalign 0.5
        background "black"
        vbox:
            textbutton "Time: [time_day]":
                action CaptureFocus("choice")
            textbutton "Done":
                action Return(True)
    if GetFocusRect("choice"):
        dismiss action ClearFocus("choice")
        nearrect:
            focus "choice"
            frame:
                background "black"
                modal True
                vbox:
                    textbutton "Morning" action [SetVariable("time_day", "Morning"), ClearFocus("choice")]
                    textbutton "Afternoon" action [SetVariable("time_day", "Afternoon"), ClearFocus("choice")]
                    textbutton "Night" action [SetVariable("time_day", "Night"), ClearFocus("choice")]

#Menu that pops up at night. Options for going to bed, scheduling counselings, and checking mail.
screen serene_room():
    modal True
    frame:
        align(0.0, 0.0)
        xsize 1920
        ysize 1080

        background "#ffffff00"
        #background "serene_room.png"
        
        vbox:
            yalign 0.5
            xalign 0.25
            spacing 100
            at transform:
                outline_transform(3, "#ffffff", mesh_pad=True)
                
            
            textbutton ("Schedule") style "word_list":
                yalign 0.2
                action CaptureFocus("date")
            textbutton ("Mail") style "word_list":
                action CaptureFocus("letters")
            textbutton ("Glossary") style "word_list":
                action CaptureFocus("info")
            textbutton ("Sleep") style "word_list":
                action CaptureFocus("progress")
    if GetFocusRect("date"):
        dismiss action ClearFocus("date")
        nearrect:
            focus "date"
            frame:
                modal True
                vbox:
                    textbutton "Counseling": 
                        action CaptureFocus("counseling")
                    textbutton "Calendar" action [Call("achievement_popup"), ClearFocus("date")]
                        #action CaptureFocus("calendar")
                    textbutton "Close":
                        action  ClearFocus("date")
    elif GetFocusRect("letters"):
        dismiss action ClearFocus("letters")
        nearrect:
            focus "letters"
            frame:
                at gotachievement    
                xalign 0.5 yalign 0.5
                modal True
                vbox:
                    textbutton "Close":
                        action ClearFocus("letters")
    elif GetFocusRect("info"):
        dismiss action ClearFocus("info")
        nearrect:
            focus "info"
            frame:
                modal True
                vbox:
                    textbutton "Close":
                        action ClearFocus("info")
    elif GetFocusRect("progress"):
        dismiss action ClearFocus("progress")
        nearrect:
            focus "progress"
            frame:
                modal True
                vbox:
                    textbutton "Go to Sleep" action [ClearFocus("progress"), Call("day_progression")]
                        
                    textbutton "Close":
                        action ClearFocus("progress")

##############################################################################################################
# Time of Day Screens for the Day Display. Displays Morning, Afternoon, and Evening. Will still need an early morning display.
screen DayDisplay:
    zorder 1
    #add "overlay3.png"
    add "wavy_overlay"
    if time_day == "Morning":
            add "morning_time" at transform:
                outline_transform(3, "#ffffffff", mesh_pad=True)
                subpixel True
                blur 50.0

    elif time_day == "Afternoon":
            add "morning_time"  at transform:
                outline_transform(4, "#0077ff6b", mesh_pad=True)
                subpixel True
                blur 50.0
    elif time_day == "Evening":
            add "night_time"
    vbox:
            ypos 0 xpos 10
            at transform:
                #outline_transform(4, "#ffffff", mesh_pad=True)
                glow_outline(5, "#ffffffff", num_passes=30, power=1, mesh_pad=True)
                subpixel True
            text "{=date_s}[calDate.month]" + "/" + "[calDate.day]{/=date_s}" ypos 18 
            text "{=date_r}[store.stringweekday]{/=date_r}" ypos 5 xpos -3#"[calendar.day_name[calDate.day]]"
    vbox:
            ypos 100
            at transform:
                outline_transform(3, "#ffffff", mesh_pad=True)
            text ("[gt.day_part]") style "day_part"
                

style date_s is text:
        color "#657CD5"
        size 70
        font "CelticKnots-Bq55.ttf"

style date_r is text:
        color "#657CD5"
        size 40
        line_spacing 100
        #bold True
        font "CelticKnots-Bq55.ttf"

style word_list is button:
    background "#ffff0000"              # transparent

style word_list_text is text:
    size 45
    hover_color "#23cbd1"             # Teal
    color "#657CD5"                  # blurple

style day_part is text:
    size 25
    bold True
    #font "GaldienRounded.otf"
    color "#657CD5"            

##############################################################################################################
#Transforms and Labels for the Time Screens and transitions.
        
# Achievement Animation
transform gotachievement:
    on show:
        zoom 0.0
        easein 0.2 zoom 1.0
    on hide:
        easeout 0.2 zoom 0.0

# Achievement Pop-up
screen achievementpopupscreen():
    frame:
        at gotachievement   
        xalign 0.5 yalign 0.5
        vbox:
            text "This is a place-holder screen for a Calendar."
            text " - The calendar will show birthdays and holidays."
            text " - It also allows you to schedule Counseling Sessions."

# Call Function for Achievement
label achievement_popup:
    show screen achievementpopupscreen
    pause
    hide screen achievementpopupscreen
    return

label day_progression:
    hide screen DayDisplay
    call calendar(1)
    $ store.theweekday += 1
    if [sleep_early] == True:
        $ gt.alter(sleep=1)
    else:
        $ gt.alter(sleep=1, steps=1)
    show screen DayDisplay
    with dissolve 
    return

define wiperight = CropMove(0.5, "wiperight")

define wiperight_black = MultipleTransition([
    False, wiperight,
    "black", Pause(3.5),
    "walk_transition", dissolve,
    "black", dissolve,
    True])

define walking_man = ComposeTransition(wiperight_black, before=None, after=None)

image morning_time:
    #contains:
    contains:
        "images/sun_small.png"
        xpos 140
        ypos -25
        xysize(90, 90)
        subpixel True
        rotate_pad True
        transform_anchor True
        parallel:
            rotate 0
            linear 200 rotate 360
            repeat  


image night_time:
    contains:
        "images/moon_small.png" 
        xpos 0
        ypos 0
        xysize(200,200)
        subpixel True
        rotate_pad True

image wavy_overlay:
    contains:
        "overlay4_base.png"
        xysize(0.7, 0.7)
        xpos -65 #xpos -75
        ypos -20 #ypos -20
    
        #function WaveShader(period=50, amp=0.5, speed=0.015, direction='x')
        function WaveShader(period=50, amp=2, speed=0.015, direction='x')
    #function WaveShader(period=10, amp=5.0, speed=0.1, direction='x', double="x")
    contains:
        "overlay_tri_gold.png"
        xysize(0.7, 0.7)
        xpos -30 #xpos -75
        ypos -30 #ypos -20
        #glow_outline(25, "#ff833588", num_passes=30, power=10)


image royal = Frame("pattern", 0, 0, tile=True)
#padding (203, 411, 215, 411)
image walk_transition:
    contains:
        "black" with wiperight
        #pause 2.0
    contains:
        parallel:
            subpixel True
            "person" with dissolve
            yrotate 180
            xalign -0.5
            yalign 1.0
            linear 4.0 xalign 1.5
        parallel:
            subpixel True
            hop2
    contains:
        parallel:
            subpixel True
            "person" with dissolve
            yrotate 0
            xalign 1.5
            yalign 1.0
            linear 7.0 xalign -0.5
        parallel:
            subpixel True
            hop2
    contains:
        parallel:
            subpixel True
            "person" with dissolve
            yrotate 0
            xalign 1.5
            yalign 1.0
            linear 7.0 xalign -0.5
        parallel:
            subpixel True
            hop2


transform hop2(linear):
    yalign 1.0
    linear 0.5 yalign 1.1
    linear 0.5 yalign 1.0
    repeat

layeredimage person:
    always: 
        "npc1.png"
    always:
        "mouth_closed.png"