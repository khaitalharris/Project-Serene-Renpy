##############################################################################
# Portrait Engine
##############################################################################
      
##############################################################################
# Portrait class

init python:
    import random   
    class Portrait(renpy.Displayable):
        def __init__(self, name, express="neutral", eyes=None, mouth=None, speaker=None, **args):
            super(Portrait, self).__init__(**args)
            # Values
            self.speaker = speaker if speaker != None else name
            self.ec  = None
            self.mc = None
            self.eyes = None
            self.mouth = None
            # Get filenames
            # Base
            prefix = ("images/char/%s/" % name)
            self.base = ("%s%s_base.png" % (prefix, express))
            # Eyes
            # If eyes are not unique, use expression, if expression n/a, use neutral.
            if eyes:
                if len(eyes) >= 3:
                    self.eyes = ("%s%s_eyes.png" % (prefix, eyes[2]))
                else:
                    self.eyes = ("%s%s_eyes.png" % (prefix, express))  
                if not renpy.loadable(self.eyes):
                    self.eyes = ("%sneutral_eyes.png" % prefix)
                # Give custom idle frame (static)
                self.eyes_idle = ("%s%s_eyes.png" % (prefix, eyes[3])) if len(eyes) == 4 else None
                # Send co-ordinates
                self.ec = (eyes[0], eyes[1])
            # Mouth
            # If mouth is not unique, use expression, if expression n/a, use neutral.
            if mouth:
                if len(mouth) >= 3:
                    self.mouth = ("%s%s_mouth.png" % (prefix, mouth[2]))
                else:
                    self.mouth = ("%s%s_mouth.png" % (prefix, express))
                if not renpy.loadable(self.mouth):
                    self.mouth = ("%sneutral_mouth.png" % prefix)
                # Give custom idle frame
                self.mouth_idle = ("%s%s_mouth_i.png" % (prefix, mouth[3])) if len(mouth) == 4 else None
                # Send co-ordinates
                self.mc = (mouth[0], mouth[1])
            # Blink timer
            self.blink_time = random.choice([3.3, 3.6, 4.3, 4.5])
            
        def render(self, width, height, st, at):
            # Get base
            portrait = Image(self.base)
            # Draw base
            portrait_render = renpy.render(portrait, width, height, st, at)
            # Eyes
            if self.ec is not None:
                # Get size
                ed = renpy.render(Image(self.eyes), width, height, 0, 0).get_size()
                # Render
                if self.eyes_idle:
                    eyes = renpy.render(DynamicDisplayable(self.static, self.eyes_idle), width, height, 0, 0)
                    portrait_render.blit(eyes, (self.ec[0], self.ec[1]))
                else:
                    eyes = renpy.render(DynamicDisplayable(self.redraw_eyes, ed), width, height, st, at)
                    portrait_render.blit(eyes, (self.ec[0], self.ec[1]))
            # Mouth
            if self.mc is not None:
                # Get size
                md = renpy.render(Image(self.mouth), width, height, 0, 0).get_size()
                # Render
                if speaking == self.speaker and speaking != None:
                    mouth = renpy.render(DynamicDisplayable(self.redraw_mouth, md), width, height, st, at)
                    portrait_render.blit(mouth, (self.mc[0], self.mc[1]))
                elif self.mouth_idle:
                    mouth = renpy.render(DynamicDisplayable(self.static, self.mouth_idle), width, height, 0, 0)
                    portrait_render.blit(mouth, (self.mc[0], self.mc[1]))                
                else:
                    mouth = renpy.render(im.Crop(self.mouth, (0, 0, md[0], md[1]/3)), width, height, 0, 0)
                    portrait_render.blit(mouth, (self.mc[0], self.mc[1]))
            # Return the render.
            flatten = renpy.render(Flatten(portrait), width, height, st, at)
            return flatten

        def redraw_eyes(self, st, at, d):
            # Set frames
            i = self.eyes
            w = d[0]
            f = d[1]/3
            opened =        im.Crop(i, (0, 0, w, f))
            half_opened =   im.Crop(i, (0, f, w, f))
            closed =        im.Crop(i, (0, f*2, w, f))
            # Draw frames as per this timing
            p = self.blink_time
            time = st % p
            if time > (p - .1):
                return half_opened, 0.05
            elif time > (p - .2):
                return closed, 0.05
            elif time > (p - .3):
                return half_opened, 0.05
            else:
                return opened, 0.05
    
        def redraw_mouth(self, st, at, d):
            # Set frames
            i = self.mouth
            w = d[0]
            f = d[1]/3
            closed =        im.Crop(i, (0, 0, w, f))
            half_opened =   im.Crop(i, (0, f, w, f))
            opened =        im.Crop(i, (0, f*2, w, f))
            # Draw frames as per this timing
            time = st % .4
            if time < .1:
                return half_opened, 0.1
            elif time < .2:
                return opened, 0.1
            elif time < .3:
                return half_opened, 0.1
            else:
                return closed, 0.1   
                
        def static(self, st, at, i):
            return Image(i), 0.05

##############################################################################
# Text blip + speaker template system

init -5 python:
    # Character template
    def CharTemplate(name=None, quote=True, mode=None, file=None, speaker=None, **args):
        if quote:
            return Character(name, what_prefix=u"\"", what_suffix="\"", who_prefix=u"", who_suffix="", ctc="continimg", ctc_pause="continimg", ctc_timedpause=Null(), kind=mode, callback=text_effect(file, speaker), **args)
        else:
            return Character(name, ctc="continimg", ctc_pause="continimg", ctc_timedpause=Null(), kind=mode, **args)
    
    # Text blip and speaker set
    def text_effect(file, speaker, event, **args):
        if event == "show_done":
            pass
            if file and _preferences.text_cps != 0:
                renpy.music.play(file, channel="text")
        elif event == "slow_done" or event == "end":
            speaking = None
            renpy.music.stop(channel="text")
        renpy.invoke_in_new_context(speaker_curry(speaker, event))
        #
    text_effect = renpy.curry(text_effect)

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
        
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker_curry = renpy.curry(speaker_callback)

