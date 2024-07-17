################################################################################
##
## Image Tint Tool by Feniks (feniksdev.itch.io / feniksdev.com)
##
################################################################################
## This file contains code for an image tinting tool, designed to work
## alongside Image Tools, found here:
## https://feniksdev.itch.io/image-tools-for-renpy
##
## The files in Image Tools for Ren'Py are *required* in order for this code
## to work.
## This tool also requires the Color Picker code, which can be found here:
## https://feniksdev.itch.io/color-picker-for-renpy
## If you use these tools during development, credit me as Feniks @ feniksdev.com
##
## This tool is designed to be used during development only, and should be
## excluded from a proper build. The code to do so is included with this file.
##
## It also has a visual component, and includes in-game tutorials you can
## go through to learn how to use the tools.
## To access the tools, simply make yourself a button (probably on the main
## menu) that goes to the main tool screen, image_tools:
##
# textbutton "Image Tools" action ShowMenu("image_tools")
##
## Then you can select a tool and get started. You will be shown the tutorial
## the first time you use a tool.
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################
## VARIABLES
################################################################################
## Persistent ##################################################################
################################################################################
## The current background
default 5 persistent.sprt_bg = ""
## The saved background tags
default persistent.sprt_bg_tags = [ ]
## Tints associated with each background
default persistent.sprt_bg_tint_dict = dict()
## The starting position of the draggable picker
default 40 persistent.sprt_picker_xpos = config.screen_width-sprt.PICKER_FRAME_SIZE
default 40 persistent.sprt_picker_ypos = sprt.SPACER*3
## The tutorial variable
default persistent.sprt_tutorial4_shown = False
## Normal ######################################################################
################################################################################
## The last valid background
default sprt.last_valid_bg = None
## The current saturation slider value
default sprt.saturation = 1.0
## The current contrast slider value
default sprt.contrast = 1.0

################################################################################
## CONSTANTS
################################################################################
## The size of the colour picker. This is a percentage of the screen size,
## and it is square.
define sprt.PICKER_SIZE = min(
    int(config.screen_width*0.5),
    int(config.screen_height*0.5)
)
## The width of the picker bars.
define sprt.PICKER_BAR_WIDTH = int(sprt.PICKER_SIZE*0.09)
## The width of the swatch
define sprt.SWATCH_WIDTH = int(sprt.PICKER_SIZE/4)
## The width of the frame holding the picker and associated bars
define 30 sprt.PICKER_FRAME_SIZE = (sprt.PICKER_SIZE+sprt.PADDING*36
    +sprt.PICKER_BAR_WIDTH
    +sprt.SWATCH_WIDTH)

################################################################################
## FUNCTIONS
################################################################################
init -80 python in sprt:

    from renpy.store import TintMatrix, SaturationMatrix, Fixed, Text, Function
    from renpy.store import DynamicDisplayable, ContrastMatrix, SetScreenVariable

    def record_picker_drag_pos(drags, drop):
        """
        Remember where the box with the colour picker was dragged to.

        Parameters:
        -----------
        drags : Drag[]
            A list of Drag objects (which will contain one Drag, the window).
        drop : Drag
            The Drag object that was dropped onto; this will always be None
            since there are no drop targets.
        """
        if not drags:
            return
        drag = drags[0]
        persistent.sprt_picker_xpos = drag.x
        persistent.sprt_picker_ypos = drag.y

    def tint_img(st, at, img, picker, sat, contrast):
        """
        Return a tinted image based on the picker's colour.
        Used for a DynamicDisplayable.
        """
        saturation = getattr(sprt, sat)
        contrast = getattr(sprt, contrast)
        return Transform(img,
            matrixcolor=(TintMatrix(picker.color)
                *SaturationMatrix(saturation)
                *ContrastMatrix(contrast))), 0.01

    def check_bg(s):
        """
        Ensure the entered background tag is valid. If not,
        return an appropriate image.

        Parameters:
        -----------
        s : str
            The background tag to check.
        """
        global last_valid_bg
        if renpy.get_registered_image(s) is not None:
            last_valid_bg = s
            return s
        elif renpy.loadable(s):
            last_valid_bg = s
            return s
        elif last_valid_bg is not None:
            return last_valid_bg
        else:
            return "image_not_found"

    def save_image_tint(picker):
        """
        Save the current tint of the image.

        Parameters:
        -----------
        picker : ColorPicker
            The colour picker the tint is derived from.
        """
        global saturation, persistent, contrast
        persistent.sprt_bg_tint_dict[
            persistent.sprt_bg] = (picker.color, saturation, contrast)

    def set_up_tint(bg, picker):
        """
        Set up the tint picker with the current tint.
        """
        global persistent, saturation, contrast
        col, sat, con = persistent.sprt_bg_tint_dict.get(bg, ("#fff", 1.0, 1.0))
        picker.set_color(col)
        contrast = con
        saturation = sat

    def copy_matrix_to_clipboard(picker):
        """
        Copy the current tint matrix to the clipboard to be pasted into a
        matrixcolor argument.
        """
        global saturation, contrast

        ret = "TintMatrix(\"{}\")*SaturationMatrix({:.4f})*ContrastMatrix({:.4f})".format(
            picker.color.hexcode, saturation, contrast)
        copy_to_clipboard(ret)

    def check_tint_who_c(dev_who, picker):
        """
        A callback used by the input for persistent.sprt_who which confirms
        if the input is a valid image name or not, and applies the
        tint system to it if so.
        """
        global persistent, last_valid_image

        if not dev_who:
            return "image_not_found"

        def set_up_image_tint(img, tg, picker):
            renpy.run([Function(retrieve_xyinitial, tg),
            SetScreenVariable("tinted_image",
                DynamicDisplayable(tint_img,
                img=get_image(img, save_last_image=True), picker=picker,
                sat="saturation",
                contrast="contrast"))])

        tag, attrs = get_tag_attrs(dev_who, '')
        attrs = ' '.join(attrs)
        img = "{} {}".format(tag, attrs).strip()

        result = renpy.can_show(img)

        if result is not None:
            last_valid_image = ' '.join(result)
            set_up_image_tint(last_valid_image, dev_who, picker)
            return last_valid_image

        result = renpy.get_registered_image(dev_who)
        if result is not None:
            last_valid_image = dev_who
            set_up_image_tint(last_valid_image, dev_who, picker)
            return img

        if last_valid_image is not None:
            set_up_image_tint(last_valid_image, None, picker)
            return last_valid_image
        return "image_not_found"

    def picker_color(st, at, picker, xsize=100, ysize=100):
        """
        A DynamicDisplayable function to update the colour picker swatch.

        Parameters:
        -----------
        picker : ColorPicker
            The picker this swatch is made from.
        xsize : int
            The width of the swatch.
        ysize : int
            The height of the swatch.
        """
        return Transform(picker.color, xysize=(xsize, ysize)), 0.01

    def picker_hexcode(st, at, picker):
        """
        A brief DynamicDisplayable demonstration of how to display color
        information in real-time.
        """
        return Fixed(Text(picker.color.hexcode, style='sprt_text'),
            xsize=SWATCH_WIDTH, yfit=True), 0.01


    check_tint_who = renpy.curry(check_tint_who_c)

################################################################################
## SCREENS
################################################################################
screen tinting_tool():
    tag menu

    ## The picker itself
    default picker = ColorPicker(sprt.PICKER_SIZE, sprt.PICKER_SIZE,
        persistent.sprt_bg_tint_dict.get(
            persistent.sprt_bg, ("#fff", 1.0, 1.0))[0])
    ## The input values for the character name and attributes
    default sprt_who_input = SpecialInputValue(persistent, 'sprt_who',
        set_callback=sprt.check_tint_who(picker=picker),
        enter_callback=sprt.save_xyinitial)
    default bg_input = SpecialInputValue(persistent, 'sprt_bg',
        set_callback=sprt.check_bg)
    ## The preview swatch. Needs to be provided the picker variable from above.
    ## You can specify its size as well.
    default picker_swatch = DynamicDisplayable(sprt.picker_color, picker=picker,
        xsize=int(sprt.PICKER_SIZE/7), ysize=int(sprt.PICKER_SIZE/7))
    ## The hexcode of the current colour. Demonstrates updating the picker
    ## colour information in real-time.
    default picker_hex = DynamicDisplayable(sprt.picker_hexcode, picker=picker)
    default tinted_image = DynamicDisplayable(sprt.tint_img,
        img=sprt.get_image(persistent.sprt_who, True), picker=picker,
        sat="saturation", contrast="contrast")
    ## True if the tint is currently being applied to the image
    default tint_applied = True

    on 'show' action [SetField(sprt, 'saturation',
        persistent.sprt_bg_tint_dict.get(
        persistent.sprt_bg, ("#fff", 1.0, 1.0))[1]),
        SetField(sprt, 'contrast',
            persistent.sprt_bg_tint_dict.get(
            persistent.sprt_bg, ("#fff", 1.0, 1.0))[2]),
        If(not persistent.sprt_tutorial4_shown,
            ShowMenu("sprt_tutorial4"))]
    on 'replace' action [SetField(sprt, 'saturation',
        persistent.sprt_bg_tint_dict.get(
        persistent.sprt_bg, ("#fff", 1.0, 1.0))[1]),
        SetField(sprt, 'contrast',
            persistent.sprt_bg_tint_dict.get(
            persistent.sprt_bg, ("#fff", 1.0, 1.0))[2]),
        If(not persistent.sprt_tutorial4_shown,
            ShowMenu("sprt_tutorial4"))]
    ## Ensure coordinates are saved so you don't have to reposition
    ## the image each time the tool is used.
    on 'replaced' action [Function(sprt.save_xyinitial),
        Function(sprt.save_image_tint, picker)]

    add sprt.check_bg(persistent.sprt_bg):
        xysize (config.screen_width, config.screen_height) fit "contain"

    use sprt_viewport(tinted=tint_applied):# id "sprt_viewport":
        if tint_applied:
            add tinted_image:
                align (0.5, 0.5) zoom persistent.sprt_zoom_dict.setdefault(
                    persistent.sprt_who, 1.0)

    hbox:
        style_prefix 'sprt_copy'
        textbutton "Turn tint {}".format("off" if tint_applied else "on"):
            action [Function(sprt.save_image_tint, picker),
                    ToggleScreenVariable("tint_applied")]
        textbutton "Hide UI" action [Function(sprt.save_xyinitial),
            Function(sprt.save_image_tint, picker),
            ShowMenu("tint_preview", img=tinted_image)]
        textbutton "Copy Matrix":
            action [Function(sprt.save_image_tint, picker),
                Function(sprt.copy_matrix_to_clipboard, picker)]

    drag:
        id 'text_attr_drag'
        draggable True drag_handle (0, 0, 1.0, sprt.SPACER*2)
        dragged sprt.record_picker_drag_pos
        xpos persistent.sprt_picker_xpos
        ypos persistent.sprt_picker_ypos
        frame:
            style_prefix 'sprt_drag'
            xsize sprt.PICKER_FRAME_SIZE
            has vbox
            spacing sprt.PADDING*2 xalign 0.5
            frame:
                style 'sprt_drag_label'
                text "(Drag to move)"
            frame:
                background None padding (0, 0) style 'empty'
                modal True align (0.5, 0.5)
                has hbox
                style_prefix 'sprt_color'
                frame:
                    has fixed
                    ## A vertical bar which lets you change the hue of the picker.
                    vbar value FieldValue(picker, "hue_rotation", 1.0)

                ## The picker itself
                vbox:
                    spacing sprt.PADDING*3
                    frame:
                        has fixed
                        add picker
                    frame:
                        style_prefix 'sprt_color'
                        has fixed
                        bar value FieldValue(sprt, "saturation", 1.0)
                    frame:
                        style_prefix 'sprt_color'
                        has fixed
                        bar value FieldValue(sprt, "contrast", 5.0):
                            style 'sprt_contrast_bar'
                vbox:
                    xsize sprt.SWATCH_WIDTH spacing 10
                    ## The swatch
                    frame:
                        has fixed
                        add picker_swatch
                    add picker_hex ## The DynamicDisplayable from earlier
                    ## These update when the mouse button is released
                    ## since they aren't a dynamic displayable
                    text "R: [picker.color.rgb[0]:.2f]"
                    text "G: [picker.color.rgb[1]:.2f]"
                    text "B: [picker.color.rgb[2]:.2f]"
                    textbutton "S: [sprt.saturation:.2f]":
                        action SetField(sprt, "saturation", 1.0)
                    textbutton "C: [sprt.contrast:.2f]":
                        action SetField(sprt, "contrast", 1.0)


    ## Dim the background behind the input button when it's active
    if (renpy.get_editable_input_value() == (sprt_who_input, True)
            or renpy.get_editable_input_value() == (bg_input, True)):
        add sprt.GRAY alpha 0.7
        dismiss action sprt_who_input.Disable()

    ## The tag input
    vbox:
        xanchor 0.0 yanchor 0.0 spacing sprt.PADDING*2
        xpos sprt.MENU_SIZE+sprt.SPACER*2
        frame:
            style_prefix 'sprt_small'
            if renpy.get_editable_input_value() == (bg_input, True):
                foreground Transform(sprt.GRAY, alpha=0.7)
            has hbox
            textbutton "Tag:" action CaptureFocus("tag_drop")
            button:
                style_prefix 'sprt_input'
                key_events True
                selected renpy.get_editable_input_value() == (sprt_who_input, True)
                action [sprt_who_input.Toggle(),
                    Function(sprt.save_xyinitial),
                    Function(sprt.save_image_tint, picker),
                    ## Ensure we don't have attribute conflicts
                    If(not sprt_who_input.editable,
                    [SetField(sprt, "what", ""),
                    SetField(sprt, "swap_attr", "")])]
                input value sprt_who_input allow sprt.INPUT_ALLOW
            textbutton "Clear":
                sensitive persistent.sprt_who
                action [SetField(persistent, "sprt_who", ""),
                        ## Also clear the attributes associated with them
                        SetField(sprt, "what", ""),
                        Function(sprt.save_xyinitial),
                        Function(sprt.save_image_tint, picker),
                        SetField(sprt, "swap_attr", "")]
            textbutton "Save":
                sensitive (persistent.sprt_who
                    and persistent.sprt_who not in persistent.sprt_tags)
                action [AddToSet(persistent.sprt_tags, persistent.sprt_who),
                    Function(sprt.save_xyinitial),
                    Function(sprt.save_image_tint, picker),
                    Notify("Saved!")]
        frame:
            style_prefix 'sprt_small' xalign 0.5
            if renpy.get_editable_input_value() == (sprt_who_input, True):
                foreground Transform(sprt.GRAY, alpha=0.7)
            has hbox
            textbutton "BG:" action CaptureFocus("bg_drop")
            button:
                style_prefix 'sprt_input'
                key_events True
                action bg_input.Toggle()
                input value bg_input allow sprt.INPUT_ALLOW
            textbutton "Clear":
                sensitive persistent.sprt_who
                action [Function(sprt.save_image_tint, picker),
                    SetField(persistent, "sprt_bg", "")]
            textbutton "Save":
                sensitive (persistent.sprt_bg != sprt.GRAY
                    and persistent.sprt_bg
                    and persistent.sprt_bg not in persistent.sprt_bg_tags)
                action [AddToSet(persistent.sprt_bg_tags, persistent.sprt_bg),
                    Function(sprt.save_xyinitial),
                    Function(sprt.save_image_tint, picker),
                    Notify("Saved!")]

    if GetFocusRect("tag_drop"):
        add sprt.GRAY alpha 0.7
        dismiss action ClearFocus("tag_drop")
        nearrect:
            focus "tag_drop"
            frame:
                modal True style_prefix 'sprt_drop'
                has vbox
                for tg in sorted(persistent.sprt_tags):
                    hbox:
                        textbutton tg:
                            yalign 0.5 text_yalign 0.5
                            action [SetField(sprt, "what", ""),
                                SetField(sprt, "swap_attr", ""),
                                Function(sprt.save_xyinitial),
                                Function(sprt.retrieve_xyinitial, tg),
                                SetField(persistent, "sprt_who", tg),
                                SetScreenVariable("tinted_image",
                                    DynamicDisplayable(sprt.tint_img,
                                        img=sprt.get_image(tg),
                                        picker=picker, sat="saturation",
                                        contrast="contrast")),
                                ClearFocus("tag_drop")]
                        textbutton "(Remove)" size_group None:
                            background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                            hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                            action [RemoveFromSet(persistent.sprt_tags, tg)]

    elif GetFocusRect("bg_drop"):
        add sprt.GRAY alpha 0.7
        dismiss action ClearFocus("bg_drop")
        nearrect:
            focus "bg_drop"
            frame:
                modal True style_prefix 'sprt_drop'
                has vbox
                for tg in sorted(persistent.sprt_bg_tags):
                    hbox:
                        textbutton tg:
                            yalign 0.5 text_yalign 0.5
                            action [Function(sprt.save_image_tint, picker),
                                Function(sprt.set_up_tint, tg, picker),
                                SetField(persistent, "sprt_bg", tg),
                                ClearFocus("bg_drop")]
                        textbutton "(Remove)" size_group None:
                            background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                            hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                            action [RemoveFromSet(persistent.sprt_bg_tags, tg)]

    use hamburger_menu():
        style_prefix 'hamburger'
        textbutton _("Return") action Return()
        textbutton "How to Use" action ShowMenu("sprt_tutorial4")

## A screen to display the image against the background without the
## additional UI elements
screen tint_preview(img):

    tag menu

    add sprt.check_bg(persistent.sprt_bg):
        xysize (config.screen_width, config.screen_height) fit "contain"

    use sprt_viewport(tinted=True) id "sprt_viewport":
        add img:
            align (0.5, 0.5) zoom persistent.sprt_zoom_dict.setdefault(
                persistent.sprt_who, 1.0)

    use hamburger_menu():
        style_prefix 'hamburger'
        textbutton "Show UI":
            action [Function(sprt.save_xyinitial),
                ShowMenu("tinting_tool")]
    key 'game_menu' action [Function(sprt.save_xyinitial),
            ShowMenu("tinting_tool")]

################################################################################
## STYLES
################################################################################
style sprt_color_hbox:
    spacing sprt.PADDING*3 xalign 0.5 yalign 0.5
style sprt_color_fixed:
    fit_first True
style sprt_color_vbar:
    xysize (sprt.PICKER_BAR_WIDTH, sprt.PICKER_SIZE)
    base_bar At(Transform("#000",
            xysize=(sprt.PICKER_BAR_WIDTH, sprt.PICKER_SIZE)),
        spectrum(horizontal=False))
    thumb Transform("selector_bg", xysize=(sprt.PICKER_BAR_WIDTH, sprt.PADDING*4))
    thumb_offset sprt.PADDING*2
style sprt_color_bar:
    xysize (sprt.PICKER_SIZE, sprt.PICKER_BAR_WIDTH)
    base_bar At(Transform("#000",
            xysize=(sprt.PICKER_SIZE, sprt.PICKER_BAR_WIDTH)),
        color_picker("#f00", "#f00", "#888", "#888"))
    thumb Transform("selector_bg", xysize=(sprt.PADDING*4, sprt.PICKER_BAR_WIDTH))
    thumb_offset sprt.PADDING*2
style sprt_contrast_bar:
    is sprt_color_bar
    base_bar At(Transform("#000",
            xysize=(sprt.PICKER_SIZE, sprt.PICKER_BAR_WIDTH)),
        color_picker("#fff", "#fff", "#000", "#000"))
style sprt_color_frame:
    background sprt.construct_frame("#fff", "#0000")
    padding (sprt.PADDING, sprt.PADDING)
style sprt_color_text:
    is sprt_text
style sprt_color_button_text:
    is sprt_text
    hover_color sprt.ORANGE
    insensitive_color sprt.WHITE
    idle_color sprt.CREAM
    underline True

################################################################################
## TUTORIAL
################################################################################
## Note that this is coded in a pretty specific way due to the flexibility
## of the tool. It's not meant to be a good example of how to code a screen,
## in particular due to the repeated code. Normally it would be easier to
## have images showing highlighted areas of the screen, which isn't possible
## here due to how the tool adapts to different projects + I didn't want to
## include unnecessary images in the tool.
################################################################################
init 40 python in sprt:
    ## A special way of declaring the tutorial text in order to make it easy
    ## to add or remove text without having to change the code.
    tut4 = Tutorial(
        TutorialText("intro", "Welcome to the Image Tinting Tool!",
        "Have you ever wanted to tint your images so they blend in with your backgrounds better? Matching your characters to your backgrounds can help them feel like part of their environment. This tinting tool will help you do that.",
        "This tutorial will show you how to use the tool to create image tint matrices.",
        xalign=0.5),
        TutorialText("tag1", "Entering an Image Tag",
        "The first thing you need to do is type an image tag in the input box beside the \"Tag\" button.",
        "(This is just a tutorial so you can't type anything here, now!)",
        "This can be be any image tag, but it's usually a character name like \"eileen\", or sometimes a multi-word tag like \"side mc\" or \"bg\" for backgrounds.",
        "The \"Clear\" button will remove all text in the tag field.",
        xalign=1.0, background="#000e"),
        TutorialText("tag2", "Saving an Image Tag",
        "You can also save tags to quickly access later with the \"Save\" button.",
        "Tags that you've saved can be accessed by clicking the \"Tag\" text to the left of the input box.",
        "This will show a dropdown of all the tags you've saved. Click \"(Remove)\" to remove a saved tag from this list, or click the tag itself to switch to it.",
        "Clicking on a tag or anywhere outside of the dropdown will close the dropdown.",
        xalign=1.0, background="#000e"),
        TutorialText("tag3", "Entering a Background Tag",
        "For comparing while tinting, you can also enter a background image tag in the box labelled \"BG\".",
        "This is to help you get a better idea of how your image blends in with the background.",
        "As with image tags, there is a \"Clear\" button to remove the current background, and a \"Save\" button to save a background tag so you can select it from the dropdown later.",
        xalign=1.0, background="#000e"),
        TutorialText("moving_img", "Moving the Image",
        "After entering an image tag, you can move the image around by clicking and dragging it.",
        "If you can't find your image, use the \"Re-center\" button to center it.",
        "If the game can't find your image, you'll see a big red square with some text on it.",
        xalign=1.0, background="#000e"),
        TutorialText("moving_img2", "Moving the Image 2",
        "The slider in the bottom left lets you zoom the image in and out so you can more easily compare it to the background. You can also use the mouse wheel to zoom in and out.",
        xalign=1.0, background="#000e"),
        TutorialText("tint1", "Picking a Tint",
        "On the right side of the screen is a colour picker. You can grab this code separately on {a=https://feniksdev.itch.io/}feniksdev.itch.io{/a}.",
        "You will click and drag around the central square to pick a colour and see it applied as a tint to your image.",
        "You can also click and drag the full window around by dragging the top part.",
        xsize=config.screen_width-sprt.PICKER_FRAME_SIZE-sprt.SPACER),
        TutorialText("tint2", "Picking a Tint 2",
        "There are three sliders: The vertical slider on the left adjusts the hue of the colour picker. For example, you might want a more blue colour for a nighttime background, or a more red one for a sunset.",
        "The red horizontal slider on the bottom adjusts the saturation of the tint. The left side is fully desaturated (grayscale) and the right side is fully saturated.",
        "This can be useful to help blend colours more, especially for nighttime and gloomy weather backgrounds.",
        "The bottommost horizontal slider adjusts the contrast of the image. The left side is zero contrast (all gray) and the farther right the slider, the more contrast there is. 1.0 is default contrast.",
        xsize=config.screen_width-sprt.PICKER_FRAME_SIZE-sprt.SPACER),
        TutorialText("tint3", "Picking a Tint 3",
        "You'll also notice some information to the right of the colour picker. This shows a hex code of the tint, as well as the RGB values and S for the Saturation.",
        "The RGB values will only update once you stop dragging the colour picker, but the hex code, saturation, and contrast will update as you adjust the picker or sliders.",
        "There isn't a brightness slider, but that's because the farther down in the colour picker you move the indicator, the darker the final image will be, resulting in the same effect.",
        xsize=config.screen_width-sprt.PICKER_FRAME_SIZE-sprt.SPACER),
        TutorialText("tint3b", "Picking a Tint 4",
        "You can also click on the \"S\" to reset the saturation to the default (1.0) or the \"C\" to reset the contrast to the default (1.0).",
        "This is especially useful for the contrast, which can slide both above and below the default value of 1.0.",
        xsize=config.screen_width-sprt.PICKER_FRAME_SIZE-sprt.SPACER),
        TutorialText("tint4", "Viewing the Tint",
        "At the top right of the screen are three buttons. The first one is \"Turn tint off\". Click this to toggle the tint on and off.",
        "This will help you get a better idea of how the tint is affecting the colours of your regular image.",
        xsize=config.screen_width-sprt.PICKER_FRAME_SIZE-sprt.SPACER),
        TutorialText("tint5", "Viewing the Tint 2",
        "The \"Hide UI\" button will toggle most of the UI off so you can see more of your image compared to the background.",
        "You can still click and drag and zoom in and out of your image while the UI is hidden.",
        "Right-clicking or pressing ESC will show the UI again, or you can use the menu button in the top-left corner.",
        xsize=config.screen_width-sprt.PICKER_FRAME_SIZE-sprt.SPACER),
        TutorialText("tint6", "Saving the Tint",
        "Once you're happy with the tint, click \"Copy Matrix\" in the top right corner to copy the tint matrix to the clipboard.",
        "This will come in a form that looks something like {b}TintMatrix(\"#7474be\") * SaturationMatrix(0.7934) * ContrastMatrix(1.000){/b}. You should use this alongside the {b}matrixcolor{/b} property of a Transform.",
        "You can look up {b}matrixcolor{/b} in the Ren'Py docs for more information.",
        xsize=config.screen_width-sprt.PICKER_FRAME_SIZE-sprt.SPACER),
        TutorialText("conclusion", "Conclusion",
        "And that's everything! I hope this tutorial helped you learn how to use the tinting tool, and that it helps you during development.",
        "To view this tutorial again, click the three lines in the top left corner and select \"How to Use\".",
        "If you run into any problems or have questions, feel free to leave a comment on itch.io.",
        "You can find more of my Ren'Py tools at {a=https://feniksdev.itch.io/}feniksdev.itch.io{/a}.",
        xalign=0.5)
    )

screen sprt_tutorial4():

    tag menu

    on 'show' action SetField(persistent, 'sprt_tutorial4_shown', True)
    on 'replace' action SetField(persistent, 'sprt_tutorial4_shown', True)
    default step = 0

    default picker = ColorPicker(sprt.PICKER_SIZE, sprt.PICKER_SIZE, "#c13232")
    default picker_swatch = DynamicDisplayable(sprt.picker_color, picker=picker,
        xsize=int(sprt.PICKER_SIZE/7), ysize=int(sprt.PICKER_SIZE/7))
    default picker_hex = DynamicDisplayable(sprt.picker_hexcode, picker=picker)

    add sprt.GRAY

    add Placeholder() xcenter 0.25 yanchor 0.6 ypos 1.0 zoom 1.5 matrixcolor BrightnessMatrix(0.3)
    use sprt_viewport(demonstration=True)

    if sprt.tut4.after_id("moving_img2", step):
        add sprt.GRAY alpha 0.9

    frame:
        background None padding (0, 0) style 'sprt_copy_hbox'
        if sprt.tut4.tut(step).id in ("tint2", "tint3"):
            foreground Transform(sprt.GRAY, alpha=0.9)
        has hbox
        style_prefix 'sprt_copy'
        textbutton "Turn tint off" action NullAction():
            if sprt.tut4.tut(step).id != "tint4":
                foreground Transform(sprt.GRAY, alpha=0.9)
        textbutton "Hide UI" action NullAction():
            if sprt.tut4.tut(step).id != "tint5":
                foreground Transform(sprt.GRAY, alpha=0.9)
        textbutton "Copy Matrix" action NullAction():
            if sprt.tut4.tut(step).id != "tint6":
                foreground Transform(sprt.GRAY, alpha=0.9)

    frame:
        padding (0, 0)
        xpos config.screen_width-sprt.PICKER_FRAME_SIZE
        ypos sprt.SPACER*3 anchor (0.0, 0.0)
        if not sprt.tut4.between_ids("tint1", "tint3b", step):
            foreground Transform(sprt.GRAY, alpha=0.9)
        frame:
            style_prefix 'sprt_drag'
            xsize sprt.PICKER_FRAME_SIZE
            has vbox
            spacing sprt.PADDING*2 xalign 0.5
            frame:
                style 'sprt_drag_label'
                text "(Drag to move)"
            frame:
                background None padding (0, 0) style 'empty'
                modal True align (0.5, 0.5)
                has hbox
                style_prefix 'sprt_color'
                frame:
                    if sprt.tut4.between_ids("tint3", "tint3b", step):
                        foreground Transform(sprt.GRAY, alpha=0.9)
                    has fixed
                    ## A vertical bar which lets you change the hue of the picker.
                    vbar value FieldValue(picker, "hue_rotation", 1.0)

                vbox:
                    spacing sprt.PADDING*3
                    frame:
                        if sprt.tut4.after_id("tint1", step):
                            foreground Transform(sprt.GRAY, alpha=0.9)
                        has fixed
                        add picker
                    frame:
                        style_prefix 'sprt_color'
                        if sprt.tut4.between_ids("tint3", "tint3b", step):
                            foreground Transform(sprt.GRAY, alpha=0.9)
                        has fixed
                        bar value FieldValue(sprt, "saturation", 1.0)
                    frame:
                        style_prefix 'sprt_color'
                        if sprt.tut4.between_ids("tint3", "tint3b", step):
                            foreground Transform(sprt.GRAY, alpha=0.9)
                        has fixed
                        bar value FieldValue(sprt, "contrast", 5.0):
                            style 'sprt_contrast_bar'
                vbox:
                    xsize sprt.SWATCH_WIDTH spacing 10
                    ## The swatch
                    frame:
                        if sprt.tut4.tut(step).id == "tint2":
                            foreground Transform(sprt.GRAY, alpha=0.9)
                        has fixed
                        add picker_swatch
                    add picker_hex ## The DynamicDisplayable from earlier
                    ## These update when the mouse button is released
                    ## since they aren't a dynamic displayable
                    text "R: [picker.color.rgb[0]:.2f]"
                    text "G: [picker.color.rgb[1]:.2f]"
                    text "B: [picker.color.rgb[2]:.2f]"
                    textbutton "S: [sprt.saturation:.2f]" action NullAction()
                    textbutton "C: [sprt.contrast:.2f]" action NullAction()

    if sprt.tut4.before_id("moving_img", step):
        add sprt.GRAY alpha 0.9

    ## The tag input
    vbox:
        xanchor 0.0 yanchor 0.0 spacing sprt.PADDING*2
        xpos sprt.MENU_SIZE+sprt.SPACER*2
        frame:
            style_prefix 'sprt_small'
            if not sprt.tut4.between_ids("tag1", "tag2", step):
                foreground Transform(sprt.GRAY, alpha=0.9)
            has hbox
            textbutton "Tag:" action NullAction():
                if sprt.tut4.tut(step).id == "tag1":
                    foreground Transform(sprt.GRAY, alpha=0.9)
            button:
                style_prefix 'sprt_input'
                key_events True
                action NullAction()
                if sprt.tut4.tut(step).id == "tag2":
                    foreground Transform(sprt.GRAY, alpha=0.9)
                text "eileen" style 'sprt_input_input'
            textbutton "Clear" action NullAction():
                if sprt.tut4.tut(step).id == "tag2":
                    foreground Transform(sprt.GRAY, alpha=0.9)
            textbutton "Save" action NullAction():
                if sprt.tut4.tut(step).id == "tag1":
                    foreground Transform(sprt.GRAY, alpha=0.9)
        frame:
            style_prefix 'sprt_small' xalign 0.5
            if not sprt.tut4.between_ids("tag3", "tag3", step):
                foreground Transform(sprt.GRAY, alpha=0.9)
            has hbox
            textbutton "BG:" action NullAction()
            button:
                style_prefix 'sprt_input'
                key_events True
                action NullAction()
                text "bg park_night" style "sprt_input_input"
            textbutton "Clear":
                action NullAction()
            textbutton "Save":
                action NullAction()

    if sprt.tut4.tut(step).id == "tag2":
        frame:
            modal True style_prefix 'sprt_drop'
            xpos sprt.MENU_SIZE+sprt.SPACER*2
            ypos sprt.MENU_SIZE+sprt.SPACER*2
            has vbox
            for tg in ("ashwin", "side mc", "xia", "zoran"):
                hbox:
                    textbutton tg:
                        yalign 0.5 text_yalign 0.5
                        action NullAction()
                    textbutton "(Remove)" size_group None:
                        background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                        hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                        action NullAction()

    elif sprt.tut4.tut(step).id == "tag3":
        frame:
            modal True style_prefix 'sprt_drop'
            xpos sprt.MENU_SIZE+sprt.SPACER*2
            ypos sprt.MENU_SIZE+sprt.SPACER*4
            has vbox
            for tg in ("bg beach_morning", "bg beach_night", "bg beach_sunset",
                    "bg restaurant", ):
                hbox:
                    textbutton tg:
                        yalign 0.5 text_yalign 0.5
                        action NullAction()
                    textbutton "(Remove)" size_group None:
                        background sprt.construct_frame(sprt.RED, sprt.MAROON, sprt.PADDING)
                        hover_background sprt.construct_frame(sprt.MAROON, sprt.RED, sprt.PADDING)
                        action NullAction()

    if sprt.tut4.tut(step).id in ("intro", "conclusion"):
        use hamburger_menu()

    if sprt.tut4.tut(step).id == "intro":
        add sprt.GRAY alpha 0.9

    use sprt_tutorial_text(sprt.tut4, step, "tinting_tool")

    text sprt.tut4.tut(step).id align (1.0, 1.0)

################################################################################
## Code to remove these files for a distributed game. Do not remove.
init python:
    build.classify("**image_tint_tool.rpy", None)
    build.classify("**image_tint_tool.rpyc", None)
################################################################################