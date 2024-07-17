screen serene_office_chapter1:
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
        
    
    default x_movement = 30
    default y_movement = 10
    default x_speed = 1.3
    default y_speed = 2.5
    vbox:
        yalign 1.35
        xalign 0.8
        spacing -55
        
        textbutton ("Think") style "choice_list":
            xoffset 50
            action Call("chapter1_think")
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
            action Return(2)
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