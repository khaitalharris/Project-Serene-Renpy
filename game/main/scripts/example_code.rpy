##### - CHOICE MENU VARIATION EXAMPLES -  #####

## The dialogue choices disappear after the player views them 
    #$ menuset = set()
    #menu .nextQuestion:
        #set menuset
        #"choice 1":
            #narrator "There are more choices to see."
            #jump .nextQuestion

        #"choice 2":
            #narrator "Ah, yes of course. The second choice is the one you select, alas there is more to see..."
            #jump .nextQuestion

        #"choice 3":
            #narrator "Did you pick this choice last? I'd pray you did, otherwise we shall see each other oncemore..."
            #jump .nextQuestion
    #$ menuset = set()*/
## ------------------------------------------------------ ##

## Specifying the type of screen to use after typing "menu" changes its appearance.
    #menu annoying_devon1 (screen = "choice_return") : # "choice_return" shows the "return" button as a seperate choice.
            #narrator "A man peaks over the cubicle." 
            #"Finish typing your e-mail.":
                #jump ignore_devon
            #"Stop working and talk to your coworker.":
                #$ renpy.notify("You've unlocked: Context (!)") # Shows a banner with the following text.
                #pause(1.5)
                #$ wall_break = True # A variable used to show a special dialogue choice later on in the game.
                #jump ignore_devon
#(screen = "choice_return") : # "choice_return" shows the "return" button as a seperate choice.
#(screen = "grid_choice", cols = 3, rows = 1) : #  shows the choices in a grid format.
## ------------------------------------------------------ ##

#######################################################

##### - DISABLE ROLL-BACK - #####
# - We can temporarily stop the roll-back feature by using:
#label start:
#    "Dialogue 1"
#    "Dialogue 2"
#    "Dialogue 3"
#    $ config.rollback_enabled = False
#    "Dialogue 4"
#    "Dialogue 5"
#    $ renpy.block_rollback()
#    $ config.rollback_enabled = True
#   "Dialogue 6"
#   "Dialogue 7"
# "So basically the player can roll back to 1 as late as 3. They can't roll back at all after that until they get to 7."
# "The "block rollback" line serves to purge the history of 4 and 5." https://www.reddit.com/r/RenPy/comments/qaxfh0/is_it_possible_to_disable_rollback_for_a_portion/

###########################################################

#### - ADD CHARACTERS TO NOTEBOOK - ####
# Source: https://www.reddit.com/r/RenPy/comments/u32a4u/an_efficient_way_to_display_information_about/
#init python:
    #class Relationship (store.object):
        #def __init__(self, name, description, age='?', orientation='?', haveMet=False, info_screen=False):
            #self.name = name
            #self.description = description
            #self.age = age
            #self.orientation = orientation
            #self.haveMet = haveMet
            #self.info_screen = info_screen #Add this part into the class.

#####################################################

#label start:
    #python:
        # Just create a list and append things to it.
        #Char = [] 
        # This is Char[0]
        #Char.append(Relationship("Jane","A very nice girl.", "?", "?", False, "jane_relationship_info")
        # This is Char[1]
        #Char.append(Relationship("John","A very nice guy.", "?", "?", False, "john_relationship_info")
        # And so on.

    #call screen k_relationship_list

#screen k_relationship_list():
    #vbox:
        #box_wrap True
        #xminimum 580
        #xmaximum 580
        #xpos 0.22
        #ypos 0.2
        #xanchor 0
        #yanchor 0
            #for i in Char:
                #if i.haveMet:    
                    #textbutton "{b}{size=40}[i.name]{/size}{/b}":
                        #action ToggleScreen(i.info_screen)

#screen jane_relationship_info():
    # Code here.

#screen john_relationship_info():
    # Code here.