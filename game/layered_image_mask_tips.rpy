################################################################################
## An expansion of LayeredImageProxy to support AlphaMask, foregrounds,
## and backgrounds.
## If you use this code in your project,
## please credit me as Feniks @ feniksdev.com
## Also consider tossing me a ko-fi @ https://ko-fi.com/fen
################################################################################
##
## TIPS AND TRICKS
##
################################################################################
## If you use the same mask for multiple sprites, you can make a dictionary
## to quickly apply them to multiple sprites:
##
# define CUTIN_MASK = dict(
#     mask="sprite_mask.png",
#     foreground="sprite_mask_frame.png",
#     background="sprite_bg.png"
# )
# image alice cutin = LayeredImageMask("alice",
#     Transform(crop=(220, 30, 564, 953)),
#     **CUTIN_MASK
# )
##
## The Transform can be included in the dictionary as well if it's the
## same for every sprite:
##
# define CUTIN_MASK = dict(
#     transform=Transform(crop=(220, 30, 564, 953)),
#     mask="sprite_mask.png",
#     foreground="sprite_mask_frame.png",
#     background="sprite_bg.png"
# )
# image alice cutin = LayeredImageMask("alice", **CUTIN_MASK)
##
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**layered_image_mask_tips.rpy", None)
    build.classify("**layered_image_mask_tips.rpyc", "archive")
################################################################################
## And finally, if you'd like to automate the declaration of masked sprite
## cut-ins, here is some code to apply it to all your existing layered images:
##
## Low init order so this happens after all other image declarations
init 9999 python:
    ## This is the attribute name that will cause the LayeredImageMask version
    ## of the layered image to be displayed (e.g. `show eileen cutin`).
    ## Change this to whatever you like.
    MASK_ATTRIBUTE = "cutin"
    ## These are the transform properties that will be applied to the
    ## LayeredImage to create the LayeredImageMask. In particular, the image
    ## paths need to be correct. Change these to suit your needs.
    MASK_PROPERTIES = dict(
        ## You can add a transform property in here, e.g.
        # transform=Transform(zoom=1.3),
        mask="sprite_mask.png",
        ## Optionally, you can add a foreground and/or background
        foreground="sprite_mask_frame.png",
        background="sprite_bg.png",
        ## You can also add positional or size properties to apply to
        ## the final window displayable, if desired
        ## e.g.
        align=(1.0, 0.0)
    )

    ## If your sprites occasionally (or always) have different crop position
    ## needs, then you can use this dictionary to specify them. If a tag is
    ## not found in this dictionary, it will use the None key's values, so
    ## set that up to the numbers you need. The last two numbers of the crop
    ## should be the size of the mask image, and the first two numbers will
    ## adjust the position of the mask image.
    ## If you have layered images with multiple tags, such as
    ## `layeredimage alice front:`, then you can add a specific key with
    ## all those tags, e.g. "alice front" : (220, 30, 564, 953),
    ## OR you can just add an entry for "alice" and it will use that if it
    ## is available.
    MASK_CROP_DICT = {
        None : (0, 0, 564, 953),
        "alice" : (280, 530, 564, 953),
        ## Add more keys here e.g.
        # "bob" : (230, 0, 564, 953),
    }


    ## After all images have been defined, declare the LayeredImageMasks.
    ## We don't want to re-look at images we newly defined, so this takes a
    ## snapshot of the image list to loop over.
    renp_list = list(renpy.list_images())
    for k in renp_list:
        ## Is it a LayeredImage?
        reg = renpy.get_registered_image(k)

        if isinstance(reg, LayeredImage) or isinstance(reg, LayeredImageProxy):
            ## Update the transform property with the crop
            trans = MASK_PROPERTIES.get('transform', None) or [ ]
            if not isinstance(trans, list):
                trans = [ trans ]
            ## Grab the first tag as a possible fallback
            try:
                tag = k.split()[0]
            except Exception as e:
                tag = k

            ## Add in the crop
            trans.append(Transform(crop=MASK_CROP_DICT.get(
                k, MASK_CROP_DICT.get(tag, MASK_CROP_DICT[None]))))

            properties = MASK_PROPERTIES.copy()
            properties['transform'] = trans

            ## Declare a new image, with the mask attribute
            renpy.image(k + ' ' + MASK_ATTRIBUTE,
                LayeredImageMask(k, **properties))

    ## When the above code is done running, if you had `layeredimage bob front`
    ## and MASK_ATTRIBUTE is "cutin", then you can do `show bob front cutin`.
    ## Similarly, if you had a LayeredImageProxy to apply tints or zooms onto
    ## the sprite, just add the MASK_ATTRIBUTE to the list of attributes when
    ## you show the sprite and it will receive the cutin mask and bg/fg e.g.
    ## `show bob front sunset closeup cutin`

    ############################################################################
    ## These functions allows the cutins to override regular default transforms,
    ## so they can be more easily positioned. If you don't want this behaviour,
    ## you can delete the lines marked with ## OPTIONAL - FOR TRANSFORMS
    ##
    ## They can also add a layer for cutins, so they aren't affected by things
    ## like camera movement on the master layer.
    ## If this isn't important to you, you can set CUTIN_LAYER = None
    ##
    ## And if you need neither the custom cutin layer nor the custom cutin
    ## transforms, then you can remove everything below this line.
    ##
    ## NOTE FOR <7.6 / <8.1 VERSIONS:
    ## If you're not using 7.6/8.1 or later, or you've disabled sticky
    ## layers, you will need to include the MASK_ATTRIBUTE every time
    ## you show or hide a cutin so that those lines are passed to the
    ## cutin layer (e.g. it can't just be `hide eileen` it must be
    ## `hide eileen cutin`). This is unnecessary if you're on a version
    ## with sticky layers.
    CUTIN_LAYER = "cutins"
    if CUTIN_LAYER:
        renpy.add_layer(CUTIN_LAYER, above="master", menu_clear=False)

    def cutin_show(name, at_list=[], layer=None, *args, **kwargs):
        if not isinstance(name, tuple):
            tname = tuple(name.split())
        else:
            tname = name

        ## OPTIONAL - FOR TRANSFORMS (delete below here if unneeded)
        if store.MASK_ATTRIBUTE in tname and not at_list:
            at_list = [null_transform]
        ## END OF OPTIONAL - FOR TRANSFORMS

        if store.MASK_ATTRIBUTE in tname:
            layer = store.CUTIN_LAYER or layer
        return OG_SHOW(name, at_list, layer, *args, **kwargs)

    OG_SHOW = config.show
    config.show = cutin_show

    ## This ensures you can hide cutins without needing to specify the layer
    def cutin_hide(name, layer=None, *args, **kwargs):
        if not isinstance(name, tuple):
            tname = tuple(name.split())
        else:
            tname = name
        if store.MASK_ATTRIBUTE in tname:
            layer = store.CUTIN_LAYER or layer
        return OG_HIDE(name, layer, *args, **kwargs)

    OG_HIDE = config.hide
    config.hide = cutin_hide

    ## Similarly, this clears the cutin layer when you clear the master layer
    def cutin_scene(layer='master'):
        if store.CUTIN_LAYER:
            OG_SCENE(store.CUTIN_LAYER)
        OG_SCENE(layer)

    OG_SCENE = config.scene
    config.scene = cutin_scene

## OPTIONAL - FOR TRANSFORMS (delete below here if unneeded)
transform null_transform():
    pass
## END OF OPTIONAL - FOR TRANSFORMS