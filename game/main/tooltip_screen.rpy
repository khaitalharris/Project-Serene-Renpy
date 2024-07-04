init -1500 python:

    class MouseTooltip(Tooltip, renpy.Displayable):
        """A Tooltip whose x/y position follows the mouse's."""
        action = Action

        def __init__(self, default, padding=None, *args, **kwargs):
            super(renpy.Displayable, self).__init__(*args, **kwargs)

            self.default = default
            self.value = default

            self.padding = padding or {}
            self.pad_x = self.padding.get('x', 0)
            self.pad_y = self.padding.get('y', 0)

            self.x = 0
            self.y = 0

            self._redraw = False

        @property
        def redraw(self):
            return self._redraw

        @redraw.setter
        def redraw(self, new_value):
            self._redraw = new_value
            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            # Only Text() displayables have a size method
            try:
                w, h = self.value.size()

            except AttributeError:
                child_render = renpy.render(self.value, width, height, st, at)
                w, h = child_render.get_size()

            render = renpy.Render(w, h)
            render.place(self.value, x=self.x + self.pad_x, y=self.y + self.pad_y)
            return render

        def event(self, ev, x, y, st):
            self.x = x
            self.y = y

            if self.redraw:
                renpy.redraw(self, 0)

            # Pass the event to our child
            return self.value.event(ev, x, y, st)
    
screen tooltip_test:
    on "show" action Play("audio", "choice_show.mp3")
    default time_delay = 0.1
    vbox:
        yalign 0.5
        xalign 0.25
        spacing 100
        text "What number do you desire?":
            at transform:
                glow_outline(100, "#ff833588", num_passes=30, power=0.5)

        textbutton "One.":
            action Return(1)
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("The loneliest number."))] 
            unhovered SetField(mtt, 'redraw', False)
            at animated_button_show(0 * time_delay)

        textbutton "Two.":
            action Return(2)
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Is what it takes."))]
            unhovered SetField(mtt, 'redraw', False)
            at animated_button_show(1 * time_delay)

        textbutton "Three.":
            action Return(3)
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("A crowd."))]
            unhovered SetField(mtt, 'redraw', False)
            at animated_button_show(2 * time_delay)

        textbutton "Hearts.":
            action Return(3)
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Image("images/sun_small.png"))]
            unhovered SetField(mtt, 'redraw', False)
            at animated_button_show(3 * time_delay)

    add mtt
    on "hide" action Play("audio", "cl_flip_phone.mp3")