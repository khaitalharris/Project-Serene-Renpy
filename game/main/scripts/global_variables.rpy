
########### Global Chapter Status Variable ########################
#This variable is used to keep track of what overall chapter the player is currently in. 
#This is the first logic gate that tells Renpy which individual Chapterx_status to follow.

default chapter_status = 0 # Keeps track of overall chapter progress.

##########################################################################################################

########### Individual Chapter Status Variables ##################

#Each chapter's variable keeps track of where in the chapter the player is currently in.
#Each chapter status variable will work with other logic statements to determine what the player can do or speak to during a given chapter.
#I'm foreseeing waaaay too many variables being needed, so goal is to learn some python code that can help streamline this. 
#The encyclopaedia code has a great system for notifying renpy when the player has "seen" an entry. Can we refactor this to work with in-game events here? 
#(Will need to clean up this code in the future with a better method.)

default chapter1_status = 0 # Keeps track of story progress in chapter 1. This variable is used in the "investigation_chapter1" script.
default chapter2_status = 0
default chapter3_status = 0
default chapter4_status = 0
default chapter5_status = 0
default chapter6_status = 0
default chapter7_status = 0
default chapter8_status = 0
default chapter9_status = 0
default chapter10_status = 0

##########################################################################################################