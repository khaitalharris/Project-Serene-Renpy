screen serene_office:
    on "show" action [Play("audio", "sword_draw.mp3"), mtt.Action(Text(""))]
    
    default x_movement = 30
    default y_movement = 10
    default x_speed = 1.3
    default y_speed = 2.5
    vbox:
        
        yalign 0.5
        xalign 0.20
        spacing -50
        
        textbutton ("Think") style "choice_list":
            xoffset 50
            action Call("chapter1_think")
            hovered [SetField(mtt, 'redraw', True)] 
            unhovered SetField(mtt, 'redraw', False)
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

    add mtt
    on "hide" action Play("audio", "cl_flip_phone.mp3")    

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

transform rotate_text(rotation):
    rotate (rotation)
style choice_list_text is text:
    size 100
    hover_color "#23cbd1f3"             # Teal
    color "#657bd5f8"                  # blurple
    #bold True
    font "FRAMDCN.ttf"

style choice_list is button:
    background "#ffff0000"  