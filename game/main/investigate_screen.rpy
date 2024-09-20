##############################
# - This screen is used for the "Investigate (!)" mechanic. Includes "Think", "Talk", "Action", and "Explore".
# - Each of these prompts sends the player to a label using the "Call" function. 
# - The Call function will show text, and then return the player to their current conversation.
# - Also disabled the "right-click" to show menu. The code is line 73 of "options.rpy"
# - Good info on Viewports https://lemmasoft.renai.us/forums/viewtopic.php?t=50254


### This is the code for the investigate Screen's Icon. The icon is a chibi version of Serene that the player can click.
### The icon shows an (!) when new interactable things that haven't been clicked yet are available.

screen serene_icon:
    imagebutton:
        xalign 1.0 yalign 2.5
        focus_mask True
        idle "serene_icon" 
        hover "serene_icon_highlighted"
        action Play("audio", "cl_flip_phone.mp3")




### The Investigate screen is what the player uses to interact with the game. There is a seperate version of this screen for each chapter, but I need to streamline the system. 
### Having the same code copied across multiple chapters is a big nono, so working on that next.
screen serene_office:
    on "show" action [Play("audio", "sword_draw.mp3"), mtt.Action(Text(""))]
    
    add "#ffffff7e":
        xysize (0.5, 0.5)
        xalign 1.6
        yalign -25.0
        rotate 30
        at transform:
            subpixel True
            yoffset 10
            #function WaveShader(period=10, amp=5.0, speed=0.005, direction='x')
            parallel:
                xoffset 120
                ease 0.3 xoffset 0
            parallel:
                alpha 0.0
                ease 0.3 alpha 1.0
                

    add "Serene" xalign 1.0 yalign 1.4 at transform:
        xcenter 1.5
        parallel:
            easein_back 0.5 xcenter 0.85
        parallel:
            outline_transform(0, "#0000", 8.0, offset=(0, 0))
            pause 0.3
            easein_back 0.5 outline_transform(0, "#ffffff4f", 8.0, offset=(25, 20))
        parallel:
            text_test(15,10,2.8,2.0)
    #[text_test(15,10,0.8,2.0), outline_transform(10, "#657bd5f8", smoothing= 5.0, mesh_pad=True)]:
        
    vbox:
        yalign 1.35
        xalign 0.8
        spacing -55
        
        textbutton ("Think") style "choice_list":
            xoffset 50
            #action Call("chapter1_think")
            action Call ("chapter_select")
            hovered [SetField(mtt, 'redraw', True)] 
            unhovered SetField(mtt, 'redraw', False)
            at [text_test(15,10,0.8,2.0), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(25)]

        textbutton ("Talk") style "choice_list":
            #action Show("serene_room")
            action Return(1)
            hovered [SetField(mtt, 'redraw', True)]
            unhovered SetField(mtt, 'redraw', False)
            at [text_test(18, 10,1.5,2.8), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(5)]

        textbutton ("Action") style "choice_list":
            action CaptureFocus("investigate_action")
            hovered [SetField(mtt, 'redraw', True)]
            unhovered SetField(mtt, 'redraw', False)
            at [text_test(20,10,1.1,2.4), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(-7)]

        textbutton ("Explore") style "choice_list":
            action Return(3)
            hovered [SetField(mtt, 'redraw', True)]
            unhovered SetField(mtt, 'redraw', False)
            at [text_test(22), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(-20)]
    if GetFocusRect("investigate_action"):
        dismiss action ClearFocus("investigate_action")
        key "mousedown_3" action ClearFocus("investigate_action")
        
        
        nearrect:
            focus "investigate_action"
            #frame:
                #background "black"
            #modal True
            vbox:
                yalign 1.35
                xalign 0.5
                spacing -55
                textbutton ("Encyclopaedia") style "choice_list": 
                    action [ShowMenu(my_encyclopaedia.list_screen, my_encyclopaedia), ClearFocus("investigate_action")]
                    at [text_test(15,10,0.8,2.0), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True)]
                    

                

    add mtt
    on "hide" action Play("audio", "cl_flip_phone.mp3")    


#This is a list of chapters for the Investigate screen to use. The Investigate screen directs to chapter select, and based on the variable that is active, directs them to the spot.
label chapter_select:
    if chapter_status == 1:
        jump chapter1_think
    if chapter_status == 2:
        jump chapter2_think
    if chapter_status == 3:
        jump chapter3_think
    if chapter_status == 4:
        jump chapter4_think
    if chapter_status == 5:
        jump chapter5_think
    

## Leaving this here as a example of the old version of the screen.
screen serene_office_example:
    ## Play audio of "ShING!" when the screen slides in. The "mtt.Action" bit of code is used to get rid of any tool-tip text that might show up from previous screens ##
    on "show" action [Play("audio", "sword_draw.mp3"), mtt.Action(Text(""))]
    
    ## How fast and from what direction the screen slides in ##
    default x_movement = 30
    default y_movement = 10
    default x_speed = 1.3
    default y_speed = 2.5
    vbox:
        ## This section has the text that flies in when the screen shows up ##
        yalign 0.5
        xalign 0.20
        spacing -50
        
        ## Each textbutton is a different "prompt" that pops up in the screen. ##
        ## The Player can click each button, which directs the player to the next screen, or returns them to the main game. ##
        textbutton ("Think") style "choice_list":
            xoffset 50
            ## The "Call" action directs the player to a label. The label is full of variable checks, and shows dialogue from the section the player is on ##
            action Call("chapter1_think")
            hovered [SetField(mtt, 'redraw', True)] 
            unhovered SetField(mtt, 'redraw', False)
            ## Contains the "floating" animation and text outline used for the text button ##
            at [text_test(15,10,0.8,2.0), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(25)]

        textbutton ("Talk") style "choice_list":
            action Return(2)
            hovered [SetField(mtt, 'redraw', True)]
            unhovered SetField(mtt, 'redraw', False)
            at [text_test(18, 10,1.5,2.8), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(5)]

        textbutton ("Action") style "choice_list":
            action Return(3)
            hovered [SetField(mtt, 'redraw', True)]
            unhovered SetField(mtt, 'redraw', False)
            at [text_test(20,10,1.1,2.4), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(-7)]

        textbutton ("Explore") style "choice_list":
            action Return(3)
            hovered [SetField(mtt, 'redraw', True)]
            unhovered SetField(mtt, 'redraw', False)
            at [text_test(22), outline_transform(10, "#ffffff4f", smoothing= 5.0, mesh_pad=True), rotate_text(-20)]

    add mtt #Tooltip
    on "hide" action Play("audio", "cl_flip_phone.mp3") #Plays this SFX when the screen disappears   

# Gives the parameters for the floating text animations. The values added in parenthesis of the "text_test" function changes the movement and speed values.
transform text_test(x_movement, y_movement=10, x_speed=1.3, y_speed=2.5):
    subpixel True
    yoffset 10
    parallel:
        xoffset 120
        ease 0.3 xoffset 0
    parallel:
        alpha 0.0
        ease 0.3 alpha 1.0
    pause 0.1   
    parallel:
        ease x_speed xoffset x_movement
        ease x_speed xoffset 0
        repeat
    parallel:
        ease y_speed yoffset 0
        ease y_speed yoffset y_movement
        repeat
image white:
    "#00000027"
    blur 25.0

transform rotate_text(rotation):
    rotate (rotation)
style choice_list_text is text:
    size 100
    hover_color "#23cbd1f3"             # Teal
    color "#657bd5f8"                  # blurple
    #bold True
    font "FRAMDCN.ttf"

style menu_list_text is text:
    size 50
    hover_color "#23cbd1f3"                # blurple
    color "#ffffffff"                  # white
    bold True
    #bold True
    #font "FRAMDCN.ttf"

style choice_list is button:
    background "#ffff0000"  