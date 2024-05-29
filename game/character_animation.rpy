# CTC Indicator Animation
image ctc_blink:
    "gui/ctc_stars.png"
    xpos 0.70 ypos 0.85
    xanchor 1.0 yanchor 1.0
    parallel:
        alpha 0
        ease 2.5 alpha 1.0
        ease 2.5 alpha 0
        repeat
    parallel:
        #around (.5, .5) 
        subpixel True
        #alignaround (.5, .5) 
        #xalign .5 yalign .5
        rotate_pad False
        transform_anchor False
        rotate 0
        linear 20 rotate 360
        #linear 10 clockwise radius 360 #5 seconds, 360 degrees
        repeat  
    
image ctc_blink_serene:  
    "gui/ctc_stars_serene.png"
    xpos 0.85 ypos 1.0
    xanchor 1.0 yanchor 1.0
    parallel:
        alpha 0
        ease 2.5 alpha 1.0
        ease 2.5 alpha 0
        repeat
    parallel:
        subpixel True
        rotate_pad False
        transform_anchor False
        rotate 0
        linear 20 rotate 360
        repeat  

image continimg:
        Text("→")
        alpha 0.0
        linear 0.1 alpha 1.0
        pause 0.5
        linear 0.1 alpha 0.0
        pause 0.5
        repeat
     



# "Walk" Animation
transform hop(linear):
    ypos 0.5
    linear 0.5 ypos 0.45
    linear 0.5 ypos 0.5
    repeat

transform flip:
    xzoom -1.0

transform exit_left:
    linear 2.0 xalign -5


# Blob's "blinking" Animation
image npc1_eyes_normal:
    "npc1_eyes.png"
    choice: 
        pause 3
    choice:
        pause 6
    choice: 
        pause 4
    "eye_closed.png"
    pause 0.1
    "eye_half.png"
    pause 0.1
    repeat


transform hbounce:
    ease .06 xoffset 24
    ease .06 xoffset 0
    ease .05 xoffset 20
    ease .05 xoffset 0
    ease .04 xoffset 16
    ease .04 xoffset 0
    ease .03 xoffset 12
    ease .03 xoffset 0
    ease .02 xoffset 8
    ease .02 xoffset 0
    ease .01 xoffset 4
    ease .01 xoffset 0
    ease .01 xoffset 0


# Slide-show anaimation.
transform slide_position:
    xpos 0.5
    ypos 390
    xanchor 0.5
    yanchor 0.5
    size (1800, 750)
    fit "contain"

screen slide_sequence(): #Use "call screen slide_sequence" to use.
    default current_slide = 1
    timer 1 action SetScreenVariable("current_slide", 2)
    timer 2 action SetScreenVariable("current_slide", 3)
    timer 3 action Return(True)

    if current_slide is 1:   
        add Image("images/slide1.png"):
            at slide_position
    elif current_slide is 2:
        add Image("images/slide2.png"):
            at slide_position
    elif current_slide is 3:
        add Image("images/slide3.png"):
            at slide_position

    textbutton "[[ Skip ]":
        action Return(True)
        xalign 0.5
        yalign 0.85