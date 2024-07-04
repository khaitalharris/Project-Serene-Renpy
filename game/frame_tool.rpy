################################################################################
##
## Frame Tool by Feniks (feniksdev.itch.io / feniksdev.com) v1.0
##
################################################################################
## This file contains the code and screens for the Frame Tool.
## This tool requires image_tool_common.rpy to work, found on my itch.io.
## https://feniksdev.itch.io/image-tools-for-renpy
## The version of Image Tools for Ren'Py must be at least 1.5.0.
##
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
## Then you can select the Frame Tool button and get started.
## You will be shown the tutorial the first time you use a tool.
## Leave a comment on the tool page on itch.io if you run into any issues!
################################################################################
## VARIABLES
################################################################################
## Persistent ##################################################################
################################################################################
## The last Frame image
default persistent.sprt_frame_img = "sprt_frame_starter"
## The tutorial
default persistent.sprt_tutorial6_shown = False
## Normal ######################################################################
################################################################################
## The name of the image to use for the Frame tool.
default sprt.temp_tag = "sprt_frame_starter"
## The colors used for the resizing UI
default sprt.rect_color = sprt.WHITE
default sprt.bg_color = "#0006"
################################################################################
## IMAGES
################################################################################
## The dotted lines used for extending the resizing rectangle
image sprt_dotted_line_h = Frame(HBox(
    Transform(sprt.CREAM, xysize=(sprt.PADDING, sprt.PADDING)),
    Null(width=sprt.PADDING), spacing=0), 0, 0, 0, 0, tile=True)
image sprt_dotted_line_v = Frame(VBox(
    Transform(sprt.CREAM, xysize=(sprt.PADDING, sprt.PADDING)),
    Null(height=sprt.PADDING), spacing=0), 0, 0, 0, 0, tile=True)
## The starting example image the first time you open the tool
image sprt_frame_starter = Grid(3, 3,
    Window(Text("1", style="sprt_grid2_text"), style="sprt_grid2_frame", background=sprt.RED),
    Window(Text("2", style="sprt_grid2_text"), style="sprt_grid2_frame"),
    Window(Text("3", style="sprt_grid2_text"), style="sprt_grid2_frame", background=sprt.RED),
    Window(Text("4", style="sprt_grid2_text"), style="sprt_grid2_frame"),
    Window(Text("5", style="sprt_grid2_text"), style="sprt_grid2_frame", background=sprt.RED),
    Window(Text("6", style="sprt_grid2_text"), style="sprt_grid2_frame"),
    Window(Text("7", style="sprt_grid2_text"), style="sprt_grid2_frame", background=sprt.RED),
    Window(Text("8", style="sprt_grid2_text"), style="sprt_grid2_frame"),
    Window(Text("9", style="sprt_grid2_text"), style="sprt_grid2_frame", background=sprt.RED),
)
style sprt_grid2_text:
    is sprt_text
    size sprt.BIG_TEXT align (0.5, 0.5)
    color sprt.WHITE outlines [(2, "#000")]
style sprt_grid2_frame:
    xysize (sprt.SPACER*3, sprt.SPACER*3)
    background sprt.ORANGE
## The mouse images used for resizing. Based on some special ASCII characters.
image move = Text("↔", style="sprt_move_cursor")
image left_right_cursor = Text("↔", style="sprt_move_cursor")
image top_bottom_cursor = Text("↕", style="sprt_move_cursor")
image diagonal_cursor1 = Transform("move", rotate=-45, rotate_pad=False)
image diagonal_cursor2 = Transform("move", rotate=45, rotate_pad=False)
image move_cursor = Fixed("left_right_cursor",
    Transform("top_bottom_cursor", align=(0.5, 0.5)), fit_first=True)

style sprt_move_cursor:
    is sprt_text
    font "DejaVuSans.ttf"
    color "#fff"
    outlines [(1, "#000")]
    size sprt.BIG_TEXT
    align (0.5, 0.5)

################################################################################
## FUNCTIONS
################################################################################
init -80 python in sprt:
    import pygame
    from store import ColorizeMatrix, Text, DynamicDisplayable, Frame, Fixed
    from store import SetScreenVariable, Null

    class Make9Patch(renpy.Displayable):
        """
        A CDD which allows the player to adjust a rectangle over an image.

        Attributes:
        -----------
        image : Displayable
            The image which is being turned into a Frame.
        original_image : Displayable
            The original image file, as a string (not Displayable).
        ren_size : tuple
            The size of the render area.
        preview : ResizeImage
            A ResizeImage object used to preview the Frame.
        top_left_corner : tuple
            An (x, y) tuple of where the top left corner of the image is based
            on its zoom level.
        width : int
            The width of the image (automatically calculated).
        height : int
            The height of the image (automatically calculated).
        dragging : bool
            Whether the player is currently dragging the Frame rectangle.
        which_edge : string
            The edge the player was closest to when dragging.
        last_edge : string
            The last active edge; used to move the rectangle with the arrow keys.
        drag_touchdown : tuple
            The position where the player touched the screen when dragging.
            Helps so the rectangle doesn't go off-screen.
        left, right, top, bottom : int
            The border on that side for the Frame.
        x : int
            The current x coordinate of the mouse.
        y : int
            The current y coordinate of the mouse.
        zoom : float
            The zoom level of the image.
        """
        ## How close the player has to be to the edge for it to be draggable
        CROP_SENSITIVITY = 0.02
        def __init__(self, image, *args, **kwargs):
            super(Make9Patch, self).__init__(*args, **kwargs)

            self.image = renpy.easy.displayable(image)
            self.original_image = image

            self.width = None
            self.height = None
            self.ren_size = (round(config.screen_width*0.5),
                round(config.screen_height*0.75))
            self.top_left_corner = (0, 0)

            self.dragging = False
            self.which_edge = None
            self.last_edge = None
            self.drag_touchdown = None

            if kwargs.get('start_coords', None) is not None:
                start_coords = kwargs.get('start_coords', None)
                self.left = start_coords[0]
                self.top = start_coords[1]
                self.right = self.left + start_coords[2]
                self.bottom = self.top + start_coords[3]
            else:
                self.left = 0
                self.right = 0
                self.top = 0
                self.bottom = 0

            self.x = 0
            self.y = 0
            self._zoom = 1.0
            self.tile = False
            self.symmetrical = False
            self.lock_symmetrical = False
            self.preview = None

            self.images_for_prediction = [
                self.image,
                renpy.get_registered_image('left_right_cursor'),
                renpy.get_registered_image('top_bottom_cursor'),
                renpy.get_registered_image('diagonal_cursor1'),
                renpy.get_registered_image('diagonal_cursor2'),
                renpy.get_registered_image('move_cursor'),
            ]

        def per_interact(self):
            renpy.redraw(self, 0)
            super(Make9Patch, self).per_interact()

        def visit(self):
            return self.images_for_prediction

        def cycle_tile(self):
            """Cycle through the values for tile."""

            if not self.tile:
                self.tile = True
            elif self.tile == "integer":
                self.tile = False
            else:
                self.tile = "integer"

        @property
        def printout(self):
            """Return a string of the Frame() for this displayable."""
            if not self.width:
                return "Frame(\"{}\", 0, 0, 0, 0)".format(
                    self.original_image)

            left, top, right, bottom = self.frame_tuple

            ## Prettily print the xpadding and ypadding if it's symmetrical
            if left == right and top == bottom:
                numbers = ', '.join([str(left), str(top)])
            else:
                numbers = ', '.join([str(x) for x in (left, top, right, bottom)])
            tile = "\"integer\"" if self.tile == "integer" else self.tile

            return "Frame(\"{}\", {}{})".format(
                self.original_image, numbers,
                ", tile={}".format(tile) if self.tile else "")

        def real_time_frame(self, st, at):
            """Return the printout as a DynamicDisplayable."""
            return Text(self.printout, style="sprt_text"), 0.1

        @property
        def real_printout(self):
            return DynamicDisplayable(self.real_time_frame)

        def copy_to_clipboard(self):
            """Copy the Frame to the clipboard."""
            copy_to_clipboard(self.printout)

        @property
        def frame_tuple(self):
            """
            Returns a tuple of (left, top, right, bottom), suitable for Frame.
            """
            return (self.left, self.top, self.right, self.bottom)

        def get_frame(self, st, at):
            """Return the Frame image created by this displayable."""
            if self.left is not None and self.width is not None:
                return Frame(self.image, *self.frame_tuple, tile=self.tile), 0.1
            else:
                return Frame(self.image, 0, 0, tile=self.tile), 0.1

        @property
        def zoom(self):
            return self._zoom

        @zoom.setter
        def zoom(self, value):
            value = max(min(value, 6.0), 0.25)
            ## Adjust the top left corner based on the new zoom level
            ren_width, ren_height = self.ren_size
            self.top_left_corner = (int(ren_width/2. - (self.width*value)/2.),
                                    int(ren_height/2. - (self.height*value)/2.))
            self._zoom = value
            return

        @property
        def frame(self):
            """Return the Frame displayable in real time."""
            return DynamicDisplayable(self.get_frame)

        def make_rect(self, left, top, right, bottom, include_dots=True):
            """
            Create a resizing rectangle around the image.

            Parameters:
            -----------
            left, top, right, bottom : int
                The coordinates of the rectangle.
            include_dots : bool
                Whether to include the dotted lines extending out from the
                rectangle.
            """
            if self.which_edge in ("left", "right"):
                mouse_img = Transform("left_right_cursor",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge in ("top", "bottom"):
                mouse_img = Transform("top_bottom_cursor",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge in ("top left", "bottom right"):
                ## Diagonal from top left to bottom right
                mouse_img = Transform("diagonal_cursor2",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge in ("top right", "bottom left"):
                ## Diagonal from top right to bottom left
                mouse_img = Transform("diagonal_cursor1",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            elif self.which_edge == "move":
                ## Moving the whole image at once
                mouse_img = Transform("move_cursor",
                    pos=(self.x, self.y), anchor=(0.5, 0.5))
            else:
                ## Not within the valid event area
                mouse_img = Null()

            line_colors = [rect_color]*4
            if self.last_edge == "left":
                line_colors[0] = YELLOW
            elif self.last_edge == "top":
                line_colors[1] = YELLOW
            elif self.last_edge == "right":
                line_colors[2] = YELLOW
            elif self.last_edge == "bottom":
                line_colors[3] = YELLOW

            rect_width = sprt.PADDING
            ## The rectangle
            rect = Fixed(
                ## Top + Bottom
                Transform(line_colors[1], ysize=rect_width, xsize=right-left,
                    ypos=top, xpos=left),
                Transform(line_colors[3], ysize=rect_width, xsize=right-left,
                    ypos=bottom-rect_width, xpos=left),
                ## Left + Right
                Transform(line_colors[0], xsize=rect_width, ysize=bottom-top,
                    xpos=left, ypos=top),
                Transform(line_colors[2], xsize=rect_width, ysize=bottom-top,
                    xpos=right-rect_width, ypos=top),
                xysize=self.ren_size,
            )

            resize_rect = Transform(rect_color, xysize=(13, 13), anchor=(0.5, 0.5))

            ## The extra dotted lines
            if include_dots:
                dotted = Fixed(
                    ## Top + Bottom
                    Transform("sprt_dotted_line_h", ysize=rect_width,
                        xsize=self.ren_size[0], ypos=top,
                        matrixcolor=ColorizeMatrix(rect_color, line_colors[1])),
                    Transform("sprt_dotted_line_h", ysize=rect_width,
                        xsize=self.ren_size[0], ypos=bottom-rect_width,
                        matrixcolor=ColorizeMatrix(rect_color, line_colors[3])),
                    ## Left + Right
                    Transform("sprt_dotted_line_v", xsize=rect_width,
                        ysize=self.ren_size[1], xpos=left,
                        matrixcolor=ColorizeMatrix(rect_color, line_colors[0])),
                    Transform("sprt_dotted_line_v", xsize=rect_width,
                        ysize=self.ren_size[1], xpos=right-rect_width,
                        matrixcolor=ColorizeMatrix(rect_color, line_colors[2])),
                    xysize=self.ren_size,
                )
            else:
                dotted = Null()

            ret = Fixed(
                dotted,
                rect,
                ## Some squares around the rectangle to make it clear that it's
                ## for resizing
                Transform(resize_rect, xpos=left, ypos=top,
                    xoffset=rect_width//2, yoffset=rect_width//2),
                Transform(resize_rect, xpos=left, ypos=bottom,
                    xoffset=rect_width//2, yoffset=-rect_width//2),
                Transform(resize_rect, xpos=right, ypos=top,
                    xoffset=-rect_width//2, yoffset=rect_width//2),
                Transform(resize_rect, xpos=right, ypos=bottom,
                    xoffset=-rect_width//2, yoffset=-rect_width//2),
                Transform(resize_rect, xpos=round((right-left)/2.0+left),
                    ypos=top, xoffset=rect_width//2,
                    yoffset=rect_width//2),
                Transform(resize_rect, xpos=round((right-left)/2.0+left),
                    ypos=bottom, xoffset=rect_width//2,
                    yoffset=-rect_width//2),
                Transform(resize_rect, xpos=right,
                    ypos=round((bottom-top)/2.0+top),
                    xoffset=-rect_width//2, yoffset=-rect_width//2),
                Transform(resize_rect, xpos=left,
                    ypos=round((bottom-top)/2.0+top),
                    xoffset=rect_width//2, yoffset=-rect_width//2),
                ## The resizing arrows, if applicable
                mouse_img,
                xysize=self.ren_size
            )
            return ret

        def rectangle(self):
            """
            Return the resizing rectangle and any mouse images which should be
            rendered under the cursor.
            """
            ## Determine the coordinates of the borders.
            tlcx, tlcy = self.top_left_corner
            left = round((self.left*self._zoom) + tlcx)
            right = round(tlcx + self.width*self._zoom - (self.right*self._zoom))
            top = round((self.top*self._zoom) + tlcy)
            bottom = round(tlcy + self.height*self._zoom - (self.bottom*self._zoom))
            return self.make_rect(left, top, right, bottom, True)

        def render(self, width, height, st, at):
            """Render the crop rectangle to the screen."""

            ren_width, ren_height = self.ren_size

            if self.width is None:
                ## Get the image dimensions so we know where the top left
                ## corner is when resizing.
                ren = renpy.render(self.image, width, height, st, at)
                self.width = int(ren.width)
                self.height = int(ren.height)
                ren_width, ren_height = self.ren_size
                self.top_left_corner = (int(ren_width/2. - (self.width*self._zoom)/2.),
                                        int(ren_height/2. - (self.height*self._zoom)/2.))
                renpy.restart_interaction()

            ## Create the initial render
            r = renpy.Render(ren_width, ren_height)

            rect = self.rectangle()
            img = Fixed(Transform(construct_frame(RED, bg_color),
                    xysize=(ren_width, ren_height)),
                Transform(self.image, xpos=int(self.top_left_corner[0]),
                    ypos=int(self.top_left_corner[1]), zoom=self._zoom),
                rect, xysize=(ren_width, ren_height))

            ## Render the rectangle and any mouse images under the cursor
            ren = renpy.render(img, self.width, self.height, st, at)
            r.blit(ren, (0, 0))
            ## Ensure none of our lines go out of bounds.
            rv = r.subsurface((0, 0, ren_width, ren_height), focus=True)
            ## If there's a preview, it should be updated when this is.
            if self.preview:
                renpy.redraw(self.preview, 0)
            return rv

        def get_edge(self, x, y):
            """Return which edge(s) this point is near."""
            left = False
            right = False
            top = False
            bottom = False

            width, height = self.ren_size
            exact_sensitivity = (int(self.CROP_SENSITIVITY*width),
                                int(self.CROP_SENSITIVITY*height))

            within_xbounds = (-exact_sensitivity[0] < x
                < width+exact_sensitivity[0])
            within_ybounds = (-exact_sensitivity[1] < y
                < height+exact_sensitivity[1])

            tlcx, tlcy = self.top_left_corner
            _left = round((self.left*self._zoom) + tlcx)
            _right = round(tlcx + self.width*self._zoom - (self.right*self._zoom))
            _top = round((self.top*self._zoom) + tlcy)
            _bottom = round(tlcy + self.height*self._zoom - (self.bottom*self._zoom))
            ## CROP_SENSITIVITY is so you don't have to be exactly at
            ## the edge for it to consider you able to drag from that edge
            if (_left-exact_sensitivity[0] < x
                    < _left+exact_sensitivity[0]):
                left = True
            elif (_right-exact_sensitivity[0] < x
                    < _right+exact_sensitivity[0]):
                right = True
            if (_top+exact_sensitivity[1] > y
                    > _top-exact_sensitivity[1]):
                top = True
            elif (_bottom+exact_sensitivity[1] > y
                    > _bottom-exact_sensitivity[1]):
                bottom = True

            ## Check for combos near the corners
            if left and top:
                return "top left"
            elif left and bottom:
                return "bottom left"
            elif right and top:
                return "top right"
            elif right and bottom:
                return "bottom right"
            ## Regular edges
            elif left:
                return "left"
            elif right:
                return "right"
            elif top:
                return "top"
            elif bottom:
                return "bottom"
            ## Somewhere in the middle for moving
            elif _left < x < _right and _top < y < _bottom:
                return "move"
            else:
                return None

        def restrict_crop_areas(self):
            """
            Ensure the padding numbers don't overlap one another or go out of
            bounds.
            """
            self.left = max(min(self.left, self.width-self.right), 0)
            self.right = max(min(self.right, self.width-self.left), 0)
            self.top = max(min(self.top, self.height-self.bottom), 0)
            self.bottom = max(min(self.bottom, self.height-self.top), 0)

        def event(self, ev, x, y, st):
            """
            The event method for the crop rectangle. Listens for mouse button
            down, up, and movement events to detect clicking and dragging.
            """
            x = int(x)
            y = int(y)
            self.x = x
            self.y = y
            tlcx, tlcy = self.top_left_corner

            ## Make x/y relative to the image dimensions
            width, height = self.ren_size

            in_range = (0 <= x < width and 0 <= y < height)

            if in_range and renpy.map_event(ev, "viewport_wheelup"):
                ## Zoom in
                self.zoom += 0.25
                renpy.redraw(self, 0)
                renpy.restart_interaction()
                raise renpy.IgnoreEvent()
            elif in_range and renpy.map_event(ev, "viewport_wheeldown"):
                ## Zoom out
                self.zoom -= 0.25
                renpy.redraw(self, 0)
                renpy.restart_interaction()
                raise renpy.IgnoreEvent()

            exact_sensitivity = (int(self.CROP_SENSITIVITY*width),
                                int(self.CROP_SENSITIVITY*height))

            within_xbounds = (-exact_sensitivity[0] < self.x
                < width+exact_sensitivity[0])
            within_ybounds = (-exact_sensitivity[1] < self.y
                < height+exact_sensitivity[1])

            if not (within_xbounds and within_ybounds):
                ## Out of bounds; stop dragging and de-select active edge.
                if self.which_edge is not None:
                    self.which_edge = None
                    self.last_edge = None
                ## Stop dragging
                self.dragging = False
                self.drag_touchdown = None
                renpy.redraw(self, 0)
                return
            ## Make sure whichever edge is being hovered, that it's still active
            elif not self.dragging and self.which_edge is not None:
                current_edge = self.get_edge(x, y)
                if current_edge != self.which_edge:
                    self.which_edge = current_edge
                    if self.which_edge not in (None, "move"):
                        self.last_edge = self.which_edge
                    renpy.redraw(self, 0)
                    return

            ####################################################################
            ## Deal with symmetricality
            if (pygame.key.get_mods() & pygame.KMOD_ALT) and not self.symmetrical:
                self.symmetrical = True
            elif not (pygame.key.get_mods() & pygame.KMOD_ALT) and self.symmetrical:
                self.symmetrical = False
            if self.lock_symmetrical:
                self.symmetrical = True

            ## Dragging the mouse around
            if (ev.type == pygame.MOUSEMOTION and self.dragging
                    and self.which_edge is not None):

                if self.which_edge == "move":
                    # Moving the whole thing around
                    if x < self.drag_touchdown[0]:
                        # Moving it left
                        left = (self.original_crop[0] + x
                            - self.drag_touchdown[0])
                        left = max(0, left)
                        # Adjust the right side to keep the width the same
                        right = left + (self.original_crop[2]
                            - self.original_crop[0])
                    else:
                        # Moving it right
                        right = (self.original_crop[2] + x
                            - self.drag_touchdown[0])
                        right = min(self.ren_size[0], right)
                        # Adjust the left side to keep the width the same
                        left = right - (self.original_crop[2]
                            - self.original_crop[0])
                    if y < self.drag_touchdown[1]:
                        # Moving it up
                        top = (self.original_crop[1] + y
                            - self.drag_touchdown[1])
                        top = max(0, top)
                        # Adjust the bottom side to keep the height the same
                        bottom = top + (self.original_crop[3]
                            - self.original_crop[1])
                    else:
                        # Moving it down
                        bottom = (self.original_crop[3] + y
                            - self.drag_touchdown[1])
                        bottom = min(self.ren_size[1], bottom)
                        # Adjust the top side to keep the height the same
                        top = bottom - (self.original_crop[3]
                            - self.original_crop[1])

                    ## Turn them back to their usual coordinates
                    self.left = round((left - tlcx)/self._zoom)
                    self.right = round((tlcx+self.width*self._zoom-right)/self._zoom)
                    self.top = round((top - tlcy)/self._zoom)
                    self.bottom = round((tlcy+self.height*self._zoom-bottom)/self._zoom)

                    renpy.redraw(self, 0)
                    return

                ## Move the edge. Don't allow it to be completely
                ## 0 width/height though or you can't see the area
                if "left" in self.which_edge:
                    self.left = round((x-tlcx)/self._zoom)
                    if self.symmetrical:
                        self.right = self.left
                elif "right" in self.which_edge:
                    self.right = round((tlcx+self.width*self._zoom-x)/self._zoom)
                    if self.symmetrical:
                        self.left = self.right
                if "top" in self.which_edge:
                    self.top = round((y-tlcy)/self._zoom)
                    if self.symmetrical:
                        self.bottom = self.top
                elif "bottom" in self.which_edge:
                    self.bottom = round((tlcy+self.height*self._zoom-y)/self._zoom)
                    if self.symmetrical:
                        self.top = self.bottom
                self.restrict_crop_areas()
                renpy.redraw(self, 0)
                return

            ## Moving the mouse around but not dragging; add icon to show
            ## that they CAN drag it
            elif ev.type == pygame.MOUSEMOTION and not self.dragging:
                ## Is it close to an edge?
                self.which_edge = self.get_edge(x, y)
                renpy.redraw(self, 0)
                return

            ## Pressing down to start a drag
            elif (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1
                    and not self.dragging):
                self.dragging = True
                ## Is it close to an edge?
                self.which_edge = self.get_edge(x, y)
                if self.which_edge not in (None, "move"):
                    self.last_edge = self.which_edge
                ## Only let them drag the whole thing around if it's within
                ## the crop area
                if (self.which_edge == "move"):
                    ## Can move the whole thing from the center
                    self.drag_touchdown = (x, y)
                    self.original_crop = (
                        tlcx+round(self.left*self._zoom),
                        tlcy+round(self.top*self._zoom),
                        tlcx+round(self.width*self._zoom - self.right*self._zoom),
                        tlcy+round(self.height*self._zoom - self.bottom*self._zoom))
                else:
                    self.drag_touchdown = None
                renpy.redraw(self, 0)
                ## Eat this mouse click
                if in_range:
                    raise renpy.IgnoreEvent()

            ## Releasing the mouse button to end the drag
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.dragging = False
                self.drag_touchdown = None
                renpy.redraw(self, 0)
                return

            elif ev.type == pygame.KEYDOWN and self.last_edge:
                ## Perhaps a keydown event; move it one pixel
                if ev.key == pygame.K_LEFT:
                    if self.last_edge == "left":
                        self.left -= 1
                        if self.symmetrical:
                            self.right = self.left
                    elif self.last_edge == "right":
                        self.right += 1
                        if self.symmetrical:
                            self.left = self.right
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                elif ev.key == pygame.K_RIGHT:
                    if self.last_edge == "left":
                        self.left += 1
                        if self.symmetrical:
                            self.right = self.left
                    elif self.last_edge == "right":
                        self.right -= 1
                        if self.symmetrical:
                            self.left = self.right
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                elif ev.key == pygame.K_UP:
                    if self.last_edge == "top":
                        self.top -= 1
                        if self.symmetrical:
                            self.bottom = self.top
                    elif self.last_edge == "bottom":
                        self.bottom += 1
                        if self.symmetrical:
                            self.top = self.bottom
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                elif ev.key == pygame.K_DOWN:
                    if self.last_edge == "top":
                        self.top += 1
                        if self.symmetrical:
                            self.bottom = self.top
                    elif self.last_edge == "bottom":
                        self.bottom -= 1
                        if self.symmetrical:
                            self.top = self.bottom
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
            return

    class ResizeImage(Make9Patch):
        """
        A CDD which allows the player to adjust a rectangle over an image.
        Designed to work in concert with Make9Patch.

        Attributes:
        -----------
        image : Make9Patch
            The Frame which is being resized.
        ren_size : tuple
            The size of the render area.
        top_left_corner : tuple
            An (x, y) tuple of where the top left corner of the image is based
            on its zoom level.
        dragging : bool
            Whether the player is currently dragging the resizing rectangle.
        which_edge : string
            The edge the player was closest to when dragging.
        last_edge : string
            The last active edge; used to move the rectangle with the arrow keys.
        drag_touchdown : tuple
            The position where the player touched the screen when dragging.
            Helps so the crop doesn't go off-screen.
        left : float
            The x coordinate of the left edge of the resizing rectangle.
        right : float
            The x coordinate of the right edge of the resizing rectangle.
        top : float
            The y coordinate of the top edge of the resizing rectangle.
        bottom : float
            The y coordinate of the bottom edge of the resizing rectangle.
        x : int
            The current x coordinate of the mouse.
        y : int
            The current y coordinate of the mouse.
        mode : string
            Whether the player is adjusting the frame borders or the padding.
        frame_numbers : tuple
            The corner coordinates before the player started adjusting the
            padding.
        padding_numbers : tuple
            The last padding numbers used for this displayable.
        show_text : bool
            Whether to show the text for the padding numbers.
        zoom : float
            The zoom level of this displayable.
        """
        ## How close the player has to be to the edge for it to be draggable
        CROP_SENSITIVITY = 0.05
        ## Extra padding around the image for resizing, so you can see the
        ## edges of the image.
        PADDING = int(min(config.screen_width, config.screen_height) * 0.02)

        def __init__(self, *args, **kwargs):
            kwargs['start_coords'] = (0.15, 0.15, 0.7, 0.7)
            super(ResizeImage, self).__init__(*args, **kwargs)
            self.image.preview = self
            self.frame_numbers = None
            self.padding_numbers = (0, 0, 0, 0)
            self.mode = "frame"
            self.show_text = False
            self.width = self.ren_size[0]
            self.height = self.ren_size[1]

        @property
        def crop_tuple(self):
            """
            Returns a tuple of (x, y, width, height), suitable for crop
            rectangles or areas.
            """
            return (self.left, self.top, self.right-self.left,
                self.bottom-self.top)

        def rectangle(self):
            """
            Return the crop rectangle and any mouse images which should be
            rendered under the cursor.
            """
            ren_width, ren_height = self.ren_size
            left = round(self.left*ren_width)
            right = round(self.right*ren_width)
            top = round(self.top*ren_height)
            bottom = round(self.bottom*ren_height)
            if self.mode == "frame":
                return self.make_rect(left, top, right, bottom, False)
            else:
                return self.make_rect(left, top, right, bottom, True)

        @property
        def zoom(self):
            return self._zoom

        @zoom.setter
        def zoom(self, value):
            value = max(min(value, 6.0), 0.25)
            self._zoom = value
            renpy.redraw(self, 0)

        def toggle_mode(self):
            """Toggle the mode between frame and padding."""
            if self.mode == "frame":
                self.frame_numbers = self.frame_tuple
                self.mode = "padding"
                self.show_text = True
                if self.padding_numbers:
                    w = (self.right-self.left)*self.ren_size[0]
                    h = (self.bottom-self.top)*self.ren_size[1]
                    tlcx = self.left*self.ren_size[0]
                    tlcy = self.top*self.ren_size[1]
                    left, top, right, bottom = [x*self._zoom for x in self.padding_numbers]
                    self.left = (tlcx + left) / float(self.ren_size[0])
                    self.top = (tlcy + top) / float(self.ren_size[1])
                    self.right = (tlcx + w - right) / float(self.ren_size[0])
                    self.bottom = (tlcy + h - bottom) / float(self.ren_size[1])
            else:
                self.padding_numbers = self.padding_tuple
                self.mode = "frame"
                if self.frame_numbers:
                    self.left, self.top, self.right, self.bottom = self.frame_numbers

        @property
        def printable_padding(self):
            """
            Return a pretty string of the padding numbers for this displayable.
            """
            if self.padding_numbers or self.mode == "padding":
                if self.mode == "padding":
                    numbers = self.padding_tuple
                else:
                    numbers = self.padding_numbers
                numbers = [str(round(x-self.PADDING)) for x in numbers]
                if numbers[0]==numbers[2] and numbers[1]==numbers[3]:
                    return "padding ({})".format(', '.join(numbers[:2]))
                else:
                    return "padding ({})".format(', '.join(numbers))
            else:
                return ""

        def copy_to_clipboard(self):
            """Copy the padding numbers to the clipboard."""
            pp = self.printable_padding
            if not pp:
                renpy.notify("No padding to copy")
                return
            copy_to_clipboard(pp)

        def print_padding_fn(self, st, at):
            """Real-time display of the padding numbers."""
            return Text(self.printable_padding, style="sprt_text"), 0.1

        @property
        def printable_padding_dd(self):
            return DynamicDisplayable(self.print_padding_fn)

        @property
        def padding_tuple(self):
            """
            Returns a tuple of (left, top, right, bottom), suitable for padding.
            """
            left, top, right, bottom = self.frame_tuple
            w = self.frame_numbers[2]-self.frame_numbers[0]
            h = self.frame_numbers[3]-self.frame_numbers[1]
            ren_width, ren_height = self.ren_size
            width = (w*ren_width)
            height = (h*ren_height)

            tlcx = self.frame_numbers[0]*ren_width
            tlcy = self.frame_numbers[1]*ren_height

            left, top, right, bottom = (self.left*ren_width,
                self.top*ren_height, self.right*ren_width, self.bottom*ren_height)
            left = left - tlcx
            top = top - tlcy
            right = (tlcx+width) - right
            bottom = (tlcy+height) - bottom
            ## Convert for zoom
            left = round(left / self._zoom)
            top = round(top / self._zoom)
            right = round(right / self._zoom)
            bottom = round(bottom / self._zoom)
            return (left, top, right, bottom)

        def render(self, width, height, st, at):
            """Render the resizing rectangle to the screen."""

            ## Create the initial render
            ren_width, ren_height = self.ren_size
            r = renpy.Render(ren_width, ren_height)
            if self.mode == "frame":
                self.top_left_corner = (self.left*ren_width, self.top*ren_height)
            else:
                self.top_left_corner = (self.frame_numbers[0]*ren_width,
                    self.frame_numbers[1]*ren_height)

            if self.mode == "frame":
                w = self.right-self.left
                h = self.bottom-self.top
            else:
                w = self.frame_numbers[2]-self.frame_numbers[0]
                h = self.frame_numbers[3]-self.frame_numbers[1]

            left, top, right, bottom = self.image.frame_tuple
            ## Multiply by zoom
            left = round(left * self._zoom)
            top = round(top * self._zoom)
            right = round(right * self._zoom)
            bottom = round(bottom * self._zoom)

            the_frame = Frame(Transform(self.image.image, zoom=self.zoom),
                left, top, right, bottom, tile=self.image.tile)

            if self.mode == "padding" or (self.show_text and self.padding_numbers):
                ## Has padding numbers
                if self.mode == "padding":
                    left, top, right, bottom = self.padding_tuple
                else:
                    left, top, right, bottom = self.padding_numbers
                ## Multiply by zoom
                left = round(left * self._zoom)
                top = round(top * self._zoom)
                right = round(right * self._zoom)
                bottom = round(bottom * self._zoom)
                pads = (left, top, right, bottom)
                ## Figure out the size of the inside
                inner_width = int(w*ren_width - left - right)
                inner_height = int(h*ren_height - top - bottom)
                ## Render out a bunch of lorem ipsum text
                lorem = "Lorem ipsum dolor sit amet, consect etur adi piscing elit, sed do eiusmod tempor incidi dunt ut labore et dolore magna aliqua. Turpis egestas maecenas pharetra convallis. Id interdum velit laoreet id donec ultrices tinci dunt arcu non. Elit pellen tesque habitant morbi tristique. Pellen tesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio. Vivamus at augue eget arcu dictum. Sit amet cursus sit amet dictum. Vel eros donec ac odio tempor orci dapibus. Arcu ac tortor dignissim convallis aenean et tortor. Nibh mauris cursus mattis molestie a iaculis. "
                ## Better word breaking so it fills the line
                lorem = ''.join(["{}{}".format(x, "\u200B" if x != " " else "") for x in lorem])
                num_lorem = 1
                while True:
                    txt = Text(lorem*num_lorem, style="text",
                        color="#FFF", outlines=[(1, "#000")], xmaximum=inner_width)
                    if renpy.render(txt, inner_width, inner_height, st, at).height > inner_height:
                        break
                    num_lorem += 1
                inset = Fixed(txt, style='empty',
                    xysize=(inner_width, inner_height)).render(ren_width, ren_height, st, at)
                inset = inset.subsurface((0, 0, inner_width, inner_height), focus=True)
                inset_pos = (self.top_left_corner[0]+left, self.top_left_corner[1]+top)
            else:
                pads = (0, 0)
                inset = None

            rect = self.rectangle()
            img = Fixed(Transform(construct_frame(RED, bg_color),
                    xysize=(ren_width, ren_height)),
                Transform(the_frame,
                    xpos=int(self.top_left_corner[0])+self.PADDING,
                    ypos=int(self.top_left_corner[1])+self.PADDING,
                    xysize=(int(w*ren_width)-self.PADDING*2,
                        int(h*ren_height)-self.PADDING*2)),
                rect, xysize=(ren_width, ren_height))

            ## Render the rectangle and any little mouse images under the cursor
            ren = renpy.render(img, ren_width, ren_height, st, at)
            r.blit(ren, (0, 0))
            if inset:
                r.blit(inset, inset_pos)
            rv = r.subsurface((0, 0, ren_width, ren_height), focus=True)
            renpy.redraw(self, 0)
            return rv

        def get_edge(self, x, y):
            """Return which edge(s) this point is near."""
            left = False
            right = False
            top = False
            bottom = False

            within_xbounds = (-self.CROP_SENSITIVITY+self.left < x
                < self.CROP_SENSITIVITY+self.right)
            within_ybounds = (-self.CROP_SENSITIVITY+self.top < y
                < self.CROP_SENSITIVITY+self.bottom)

            ## CROP_SENSITIVITY is so you don't have to be exactly at
            ## the edge for it to consider you able to drag from that edge
            if (self.left-self.CROP_SENSITIVITY < x
                    < self.left+self.CROP_SENSITIVITY):
                if within_ybounds:
                    left = True
            if (self.right-self.CROP_SENSITIVITY < x
                    < self.right+self.CROP_SENSITIVITY):
                if within_ybounds:
                    right = True
            if (self.top+self.CROP_SENSITIVITY > y
                    > self.top-self.CROP_SENSITIVITY):
                if within_xbounds:
                    top = True
            if (self.bottom+self.CROP_SENSITIVITY > y
                    > self.bottom-self.CROP_SENSITIVITY):
                if within_xbounds:
                    bottom = True

            ## Check for combos near the corners
            if left and top:
                return "top left"
            elif left and bottom:
                return "bottom left"
            elif right and top:
                return "top right"
            elif right and bottom:
                return "bottom right"
            ## Regular edges
            elif left:
                return "left"
            elif right:
                return "right"
            elif top:
                return "top"
            elif bottom:
                return "bottom"
            ## Somewhere in the middle for moving
            elif self.left < x < self.right and self.top < y < self.bottom:
                return "move"
            else:
                return None

        def event(self, ev, x, y, st):
            """
            The event method for the crop rectangle. Listens for mouse button
            down, up, and movement events to detect clicking and dragging.
            """
            self.x = int(x)
            self.y = int(y)

            ## Make x/y relative to the image dimensions
            width, height = self.ren_size

            in_range = (0 <= x < width and 0 <= y < height)

            if in_range and renpy.map_event(ev, "viewport_wheelup"):
                ## Zoom in
                self.zoom += 0.25
                renpy.redraw(self, 0)
                renpy.restart_interaction()
                raise renpy.IgnoreEvent()
            elif in_range and renpy.map_event(ev, "viewport_wheeldown"):
                ## Zoom out
                self.zoom -= 0.25
                renpy.redraw(self, 0)
                renpy.restart_interaction()
                raise renpy.IgnoreEvent()

            x = x / width
            y = y / height

            exact_sensitivity = (int(self.CROP_SENSITIVITY*width),
                                int(self.CROP_SENSITIVITY*height))

            within_xbounds = (-exact_sensitivity[0] < self.x
                < width+exact_sensitivity[0])
            within_ybounds = (-exact_sensitivity[1] < self.y
                < height+exact_sensitivity[1])

            if not (within_xbounds and within_ybounds):
                ## Out of bounds; stop dragging and de-select active edge.
                if self.which_edge is not None:
                    self.which_edge = None
                    self.last_edge = None
                ## Stop dragging
                self.dragging = False
                self.drag_touchdown = None
                renpy.redraw(self, 0)
                return
            ## Make sure whichever edge is being hovered, that it's still active
            elif not self.dragging and self.which_edge is not None:
                current_edge = self.get_edge(x, y)
                if current_edge != self.which_edge:
                    self.which_edge = current_edge
                    if self.which_edge not in (None, "move"):
                        self.last_edge = self.which_edge
                    renpy.redraw(self, 0)
                    return

            ####################################################################
            ## Dragging the mouse around
            if (ev.type == pygame.MOUSEMOTION and self.dragging
                    and self.which_edge is not None):

                if self.which_edge == "move":
                    # Moving the whole thing around
                    if x - self.drag_touchdown[0] < 0:
                        # Moving it left
                        self.left = (self.original_crop[0] + x
                            - self.drag_touchdown[0])
                        self.left = max(0.0, self.left)
                        # Adjust the right side to keep the width the same
                        self.right = self.left + (self.original_crop[2]
                            - self.original_crop[0])
                    else:
                        # Moving it right
                        self.right = (self.original_crop[2] + x
                            - self.drag_touchdown[0])
                        self.right = min(1.0, self.right)
                        # Adjust the left side to keep the width the same
                        self.left = self.right - (self.original_crop[2]
                            - self.original_crop[0])

                    if y - self.drag_touchdown[1] < 0:
                        # Moving it up
                        self.top = (self.original_crop[1] + y
                            - self.drag_touchdown[1])
                        self.top = max(0.0, self.top)
                        # Adjust the bottom side to keep the height the same
                        self.bottom = self.top + (self.original_crop[3]
                            - self.original_crop[1])
                    else:
                        # Moving it down
                        self.bottom = (self.original_crop[3] + y
                            - self.drag_touchdown[1])
                        self.bottom = min(1.0, self.bottom)
                        # Adjust the top side to keep the height the same
                        self.top = self.bottom - (self.original_crop[3]
                            - self.original_crop[1])

                    renpy.redraw(self, 0)
                    return

                ## Move the edge. Don't allow it to be completely
                ## 0 width/height though or you can't see the area
                if "left" in self.which_edge:
                    self.left = min(x, self.right)
                if "right" in self.which_edge:
                    self.right = max(x, self.left)
                if "top" in self.which_edge:
                    self.top = min(y, self.bottom)
                if "bottom" in self.which_edge:
                    self.bottom = max(y, self.top)
                self.restrict_crop_areas()
                renpy.redraw(self, 0)
                return

            ## Moving the mouse around but not dragging; add icon to show
            ## that they CAN drag it
            elif ev.type == pygame.MOUSEMOTION and not self.dragging:
                ## Is it close to an edge?
                old_edge = self.which_edge
                self.which_edge = self.get_edge(x, y)
                renpy.redraw(self, 0)
                return

            ## Pressing down to start a drag
            elif (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1
                    and not self.dragging):
                self.dragging = True
                ## Is it close to an edge?
                self.which_edge = self.get_edge(x, y)
                if self.which_edge not in (None, "move"):
                    self.last_edge = self.which_edge
                ## Only let them drag the whole thing around if it's within
                ## the crop area
                if (self.which_edge == "move"):
                    ## Can move the whole thing from the center
                    self.drag_touchdown = (x, y)
                    self.original_crop = (self.left, self.top,
                                        self.right, self.bottom)
                else:
                    self.drag_touchdown = None
                renpy.redraw(self, 0)
                ## Eat this mouse click
                if in_range:
                    raise renpy.IgnoreEvent()

            ## Releasing the mouse button to end the drag
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.dragging = False
                self.drag_touchdown = None
                renpy.redraw(self, 0)
                return

            elif ev.type == pygame.KEYDOWN and self.last_edge:
                ## Perhaps a keydown event; move it the equivalent of
                ## one pixel
                one_pixel_x = self._zoom / self.ren_size[0]
                one_pixel_y = self._zoom / self.ren_size[1]
                if ev.key == pygame.K_LEFT:
                    if self.last_edge == "left":
                        self.left -= one_pixel_x
                    elif self.last_edge == "right":
                        self.right -= one_pixel_x
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                elif ev.key == pygame.K_RIGHT:
                    if self.last_edge == "left":
                        self.left += one_pixel_x
                    elif self.last_edge == "right":
                        self.right += one_pixel_x
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                elif ev.key == pygame.K_UP:
                    if self.last_edge == "top":
                        self.top -= one_pixel_y
                    elif self.last_edge == "bottom":
                        self.bottom -= one_pixel_y
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
                elif ev.key == pygame.K_DOWN:
                    if self.last_edge == "top":
                        self.top += one_pixel_y
                    elif self.last_edge == "bottom":
                        self.bottom += one_pixel_y
                    renpy.redraw(self, 0)
                    raise renpy.IgnoreEvent()
            return

    def set_frame_image(s):
        """
        A callback used on the Frame tool to make sure the image is set only
        when a valid input is given.

        Parameters:
        -----------
        s : string
            The name of the image to check.
        """
        global persistent
        ## Is this a valid image?
        if renpy.get_registered_image(s):
            pass
        elif renpy.loadable(s):
            pass
        elif renpy.loadable("images/" + s):
            pass
        else:
            return

        new_patch = Make9Patch(s)
        ri = ResizeImage(new_patch)
        persistent.sprt_frame_img = s
        renpy.run(SetScreenVariable("frame_tool", new_patch))
        renpy.run(SetScreenVariable("frame_preview", ri))

    def change_frame_ui_colors():
        """
        Change the colors of the frame tool UI.
        """
        global rect_color, bg_color
        if rect_color == WHITE:
            rect_color = PINK
            bg_color = CREAM
        else:
            rect_color = WHITE
            bg_color = "#0006"


################################################################################
## SCREENS
################################################################################
screen frame_tool():
    tag menu

    ## Ensure the user sees the tutorial the first time they open this screen
    if not persistent.sprt_tutorial6_shown:
        on 'replace' action ShowMenu("sprt_tutorial6")
        on 'show' action ShowMenu("sprt_tutorial6")

    ## The displayable with the crop square and the image
    default frame_tool = sprt.Make9Patch(persistent.sprt_frame_img)
    default frame_preview = sprt.ResizeImage(frame_tool)
    default sprt_img_input = SpecialInputValue(sprt, 'temp_tag',
        set_callback=sprt.set_frame_image,
        starting_value=persistent.sprt_frame_img)

    add sprt.GRAY

    ## The tag input
    frame:
        style_prefix 'sprt_small'
        xpos sprt.MENU_SIZE+sprt.SPACER*2
        has hbox
        text "Image:" style 'sprt_text' yalign 0.5
        button:
            style_prefix 'sprt_input'
            key_events True xminimum sprt.SPACER*7 xmaximum 0.42
            selected renpy.get_editable_input_value() == (sprt_img_input, True)
            action sprt_img_input.Toggle()
            input value sprt_img_input copypaste True
        textbutton "Clear":
            sensitive sprt.temp_tag
            action SetField(sprt, "temp_tag", "")

    ## Copy to clipboard buttons
    hbox:
        style_prefix 'sprt_small' xalign 1.0 yalign 0.0
        textbutton "Flip UI Colors" action Function(sprt.change_frame_ui_colors)
        textbutton "Copy Frame" action Function(frame_tool.copy_to_clipboard)
        textbutton "Copy Padding" action Function(frame_preview.copy_to_clipboard)

    vbox:
        align (0.5, 1.0) order_reverse True spacing sprt.PADDING*2
        ## The buttons + frame and padding printouts
        side "l r c":
            style_prefix 'sprt_small' yalign 0.0 spacing sprt.PADDING
            hbox:
                spacing sprt.PADDING*2 yalign 1.0
                textbutton "Tile: {}".format(frame_tool.tile):
                    action Function(frame_tool.cycle_tile)
                textbutton "Lock Symmetrical" style_prefix 'sprt_frame_tool_check':
                    action ToggleField(frame_tool, "lock_symmetrical")
            hbox:
                spacing sprt.PADDING*2 yalign 1.0
                textbutton "Adjust {}".format("Padding" if frame_preview.mode == "frame" else "Borders"):
                    action Function(frame_preview.toggle_mode)
                textbutton "Show Text" style_prefix 'sprt_frame_tool_check':
                    sensitive (frame_preview.mode != "padding")
                    action ToggleField(frame_preview, "show_text")
            frame:
                style_prefix 'sprt_frame_info'
                has vbox
                add frame_tool.real_printout xalign 0.5
                add frame_preview.printable_padding_dd xalign 0.5

        hbox:
            style_prefix 'sprt_frame_tools'
            fixed:
                xysize frame_tool.ren_size
                ## The image with the rectangle for cropping
                add frame_tool
                text "Frame Adjustment"
            ## A preview box
            fixed:
                xysize frame_tool.ren_size
                add frame_preview
                text "Preview"

        fixed:
            fit_first "height" xfill True style 'empty'
            fixed:
                style_prefix 'sprt_zoom'
                xsize 0.45 yalign 1.0
                bar value FieldValue(frame_tool, 'zoom', 5.75, offset=0.25, step=0.25)
                text "Zoom {:.2f}".format(frame_tool.zoom)
            fixed:
                style_prefix 'sprt_zoom'
                xsize 0.45 yalign 1.0 xalign 1.0
                bar value FieldValue(frame_preview, 'zoom', 5.75, offset=0.25, step=0.25)
                text "Zoom {:.2f}".format(frame_preview.zoom)

    use hamburger_menu():
        style_prefix 'hamburger'
        textbutton _("Return") action Return()
        textbutton "How to Use" action ShowMenu("sprt_tutorial6")

################################################################################
## STYLES
################################################################################
style sprt_frame_info_frame:
    is empty
    xalign 0.5 yalign 1.0 xfill True
    padding (sprt.PADDING, sprt.PADDING)
    background sprt.construct_frame(sprt.CREAM, "#21212dc9", 2)
style sprt_frame_info_vbox:
    is empty
    xalign 0.5

style sprt_frame_tools_hbox:
    is empty
    align (0.5, 0.5) order_reverse True spacing 0
style sprt_frame_tools_text:
    is sprt_text
    outlines [(1, "#000", 0, 0)] yalign 1.0

style sprt_frame_tool_check_button:
    is empty
    left_padding sprt.SPACER+sprt.PADDING
    yalign 0.5
    background sprt.construct_checkbox(sprt.RED, inside="#000d",
        width=sprt.PADDING, box_size=(sprt.SPACER, sprt.SPACER), checked=False)
    selected_background sprt.construct_checkbox(sprt.RED, inside="#000d",
        width=sprt.PADDING, box_size=(sprt.SPACER, sprt.SPACER), checked=True)
style sprt_frame_tool_check_button_text:
    is sprt_small_button_text
    hover_color sprt.ORANGE
    insensitive_outlines [(1, "#000")]
    insensitive_color "#888"

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
init 30 python in sprt:
    tut6 = Tutorial(
        TutorialText("intro", "Welcome to the Frame Tool!",
        "This tool provides a visual way to get the border and padding numbers for a Frame displayable.",
        "For more information on the Frame displayable, you can check out my tutorial {a=https://feniksdev.com/how-to-make-resizeable-backgrounds-in-renpy-with-frame/}How to make Resizeable Backgrounds in Ren'Py with Frame{/a}",
        "This tutorial will show you how to use the tool.",
        xalign=0.5),
        TutorialText("image1", "Enter an Image",
        "First, you need to type an image path into the input box in the top left corner.",
        "(This is just a tutorial so you can't type anything here, now!)",
        "This can be a full image path, like \"gui/frame.png\", or it can be an auto-defined or user-defined image name like just \"bubble\" if you've got \"bubble.webp\" in the images folder or declared \"image bubble\" in your script somewhere.",
        xalign=1.0, xsize=config.screen_width//2),
        TutorialText("image2", "Enter an Image 2",
        "The image in the tool area below won't change until you provide a valid image name, so double-check your spelling and image paths if you're having trouble.",
        "The \"Clear\" button will remove all text in the input.",
        xalign=1.0, xsize=config.screen_width//2),
        TutorialText("left1", "The Tool",
        "Once you've entered an image, it'll appear in the left side of the tool area. There is a resizing rectangle around it that you can click and drag.",
        "If the colours are hard to see, you can click \"Flip UI Colors\" in the top right corner to change them.",
        "You can also zoom in and out of the image using the zoom bar at the bottom, or by hovering over the left tool area and using the mouse wheel.",
        "Scrolling won't affect the final image; it's just for you to better see the area you're working with.",
        xalign=1.0, xsize=config.screen_width//2),
        TutorialText("left2", "The Tool 2",
        "You can drag the edges of the rectangle to adjust the borders of the Frame displayable. You'll see a preview of the results on the right side of the screen.",
        "If you hold down ALT while dragging, you can adjust the borders symmetrically. You can also toggle symmetrical dragging on and off by clicking the \"Lock Symmetrical\" button above the left tool area.",
        "The last edge you highlighted will be shown in yellow. If an edge is highlighted in yellow, you can use the arrow keys to move it one pixel at a time (this is adjusted according to the zoom level).",
        "You can use this for extra precision when adjusting the borders.",
        xalign=1.0, xsize=config.screen_width//2),
        TutorialText("left3", "The Tool 3",
        "The other button above the left side of the screen lets you toggle tiling on and off.",
        "It cycles through False (no tiling), True (tiling), and \"integer\" (\"whole number\" tiling).",
        "You'll see these changes reflected in the right side preview also, as well as in the printout in the middle.",
        xalign=1.0, xsize=config.screen_width//2),
        TutorialText("right1", "The Preview Area",
        "On the right side of the screen is the preview area. It'll show the changes as you adjust your image borders on the left side.",
        "There is also a resizing rectangle on this side of the screen, and a zoom bar. Use the zoom bar to zoom in on your preview image. As with the left side, you can also hover over the right side and use the scroll wheel to zoom in and out.",
        xalign=0.0, xsize=config.screen_width//2),
        TutorialText("right2", "The Preview Area 2",
        "When you resize the image on the right side, you'll be able to see how your Frame displayable looks at different sizes to check if you have the right border numbers.",
        "As with the left side, you can also use the arrow keys to nudge the active resize edge, if you're hovering over the right side of the screen.",
        xalign=0.0, xsize=config.screen_width//2),
        TutorialText("right3", "Adjusting Padding",
        "The right side of the screen also lets you preview how the Frame displayable will react to text, and adjust the padding.",
        "You can toggle between adjusting the padding and the borders by clicking the \"Adjust Padding\" button above the right side of the screen.",
        "When adjusting the padding, you'll see text fill the inside of your image. You can use the resizing rectangle to adjust the text area, and the padding numbers will update accordingly.",
        "When you switch back to adjusting the borders, the text will continue to show. You can hide it again by toggling the \"Show Text\" button at the top right.",
        xalign=0.0, xsize=config.screen_width//2),
        TutorialText("copy1", "Copying the Results",
        "When you've finished getting your border numbers, you can copy them to the clipboard with the \"Copy Frame\" button in the top right.",
        "You can then paste the Frame displayable into your script as needed.",
        "You can also copy the padding numbers by clicking the \"Copy Padding\" button. The default formatting is as a style property.",
        xalign=0.0),

        TutorialText("conclusion", "Conclusion",
        "And that's everything! I hope this helped you learn how to use the frame tool, and that it helps you during development.",
        "To view this tutorial again, click the three lines in the top left corner and select \"How to Use\".",
        "If you run into any problems or have questions, feel free to leave a comment on itch.io.",
        "You can find more of my Ren'Py tools at {a=https://feniksdev.itch.io/}feniksdev.itch.io{/a}.",
        xalign=0.5)
    )

screen sprt_tutorial6():
    tag menu
    on 'show' action SetField(persistent, 'sprt_tutorial6_shown', True)
    on 'replace' action SetField(persistent, 'sprt_tutorial6_shown', True)

    default step = 0

    add sprt.GRAY

    ############################################ Duplicate code
    use frame_tool()
    ############################################

    if sprt.tut6.tut(step).id in ("intro", "conclusion"):
        add Transform(sprt.GRAY, alpha=0.9)
    elif sprt.tut6.before_id("right1", step):
        add Transform(sprt.GRAY, alpha=0.9) xsize 0.5 xalign 1.0
    else:
        add Transform(sprt.GRAY, alpha=0.9) xsize 0.5 xalign 0.0

    if sprt.tut6.tut(step).id in ("image1", "image2"):
        add Transform(sprt.GRAY, alpha=0.9) ysize 0.9 yalign 1.0
    elif sprt.tut6.tut(step).id == "conclusion":
        pass
    elif sprt.tut6.before_id("right1", step):
        add Transform(sprt.GRAY, alpha=0.9) ysize 0.1 yalign 0.0

    if sprt.tut6.tut(step).id == "copy1":
        add Transform(sprt.GRAY, alpha=0.9) ysize 0.9 yalign 1.0 xalign 1.0
    elif sprt.tut6.tut(step).id == "conclusion":
        pass
    elif sprt.tut6.after_id("left3", step):
        add Transform(sprt.GRAY, alpha=0.9) ysize 0.1 yalign 0.0 xalign 1.0

    ## Click anywhere to continue
    dismiss action If(step < sprt.tut6.length-1, SetScreenVariable("step", step+1), ShowMenu("frame_tool"))
    key 'dismiss' action If(step < sprt.tut6.length-1, SetScreenVariable("step", step+1), ShowMenu("frame_tool"))
    ## Esc or right-click to exit the tutorial
    key 'game_menu' action ShowMenu("frame_tool")
    ## Rollback to see the previous step
    key 'rollback' action SetScreenVariable("step", max(step-1, 0))

    use sprt_tutorial_text(sprt.tut6, step, None)

################################################################################
## Code to remove these files for a distributed game. Do not remove.
init python:
    build.classify("**frame_tool.rpy", None)
    build.classify("**frame_tool.rpyc", None)
################################################################################