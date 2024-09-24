
########### Investigate(!) Screen Labels ########################

#This script contains all of the labels used in the "Investigation" screen for Chapter 1. We use the "return()" line at the end of each block.
#(Otherwise, the game will just continue to read the rest of the text down the page, and we don't want that lmao.)
#

##################################
# - "Think" prompts.
label chapter1_think: 
    #camera:
        #subpixel True pos (1878, 652) zpos 1238.0    
     
    #show white
        #subpixel True pos (-0.01, -0.195) 
    with wiperight_black  
    #show Serene 
    if chapter1_status == 0: # Chapter1_Status updates with new dialogue content. Will need to add a variable for when the status has been read.
        if ignore_devon == False:
            "You didn't ignore Devon."
            hide forest with wiperight_black
            $ignore_devon = True
            $chapter1_status += 1
            call screen serene_office_chapter1
            return()
        else:
            "You ignored Devon."
            hide forest with wiperight_black
            $ignore_devon = False
            call screen serene_office_chapter1
            return()
    if chapter1_status == 1:
        "I'm feeling stressed."
        hide forest with wiperight_black
        call screen serene_office_chapter1
        return()

    if chapter1_status == 2:
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
        play sound "SFX/wham.mp3" volume 0.75
        with vpunch
        #stop music fadeout 0.0
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
        with wiperight_black
        
        call screen serene_office_chapter1
        return()   
           

    else:
        "Where am I? The chapter status is neither 0 nor 1."
        $chapter1_status = 0
        hide forest with wiperight_black
        call screen serene_office_chapter1
        return()
    hide forest

##################################
# - "Talk" prompts.
label chapter1_talk: 
    camera:
        subpixel True pos (1878, 652) zpos 1238.0     
    show forest behind Serene:
        subpixel True pos (-0.01, -0.195) 
    with wiperight_black  
    #show Serene 
    if chapter1_status == 0:
        if ignore_devon == False:
            call screen serene_room()
            hide forest with wiperight_black
            $ignore_devon = True
            $chapter1_status += 1
            call screen serene_office_chapter1
            return()
        else:
            call screen serene_room()
            hide forest with wiperight_black
            $ignore_devon = False
            call screen serene_office_chapter1
            return()







    hide forest

