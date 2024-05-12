##############################################################################
# Styles

style h:
    color "#ddc600"
    
style hyperlink_text:
    color "#ddc600"
    underline True
    
style nvl_window:
    background              "nvlbg"
    xpadding 0 ypadding 32
    xsize 936 xalign 0.5
    yfill True
    box_spacing             18
    
style nvl_label:
    text_align              0.0
    
style nvl_vbox:
    yalign 0.0
    
image nvlbg = Solid("#0008", xysize=(1280,720), xalign=0.5, yalign=0.5)

##############################################################################
# Transitions

init -14:          
    #
    image continimg:
        Text("→")
        alpha 0.0
        linear 0.1 alpha 1.0
        pause 0.5
        linear 0.1 alpha 0.0
        pause 0.5
        repeat
        
    # General Transforms
    transform char_anchor:
        anchor(0.5, 0.32)
    transform left:
        char_anchor
        pos(0.33, 0.5)
    transform center:
        char_anchor
        pos(0.5, 0.5)
    transform right:
        char_anchor
        pos(0.66, 0.5)

    transform close:
        yanchor(0.27)
        zoom 0.86
    transform away:
        yanchor(0.40)
        zoom 0.45
    transform med:
        char_anchor
        zoom 0.6
    transform far:
        yanchor(0.48)
        zoom 0.36
        
    # Portrait transition
    transform char_fade:
        on show:
            alpha 0.0
            linear 0.4 alpha 1.0
        on replace:
            linear 0.4 alpha 1.0
        on hide, replaced:
            linear 0.4 alpha 0.0
            
            