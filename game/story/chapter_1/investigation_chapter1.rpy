
# This script contains all of the labels used in the "Investigation" prompt for Chapter 1. We use the "return()" line at the end of each block.
# (Otherwise, the game will just continue to read the rest of the text down the page, and we don't want that lmao.)
##################################
# - "Think" prompts.
label chapter1_think: 
    #camera:
        #subpixel True pos (1878, 652) zpos 1238.0     
    show forest behind Serene
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
        $chapter1_status += 1
        hide forest with wiperight_black
        call screen serene_office_chapter1
        return()

    else:
        "Where am I? The chapter status is neither 0 nor 1."
        $chapter1_status = 0
        hide forest with wiperight_black
        call screen serene_office_chapter1
        return()
    hide forest

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

