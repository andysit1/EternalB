+++
title = "design plan.md"
date = "2024-08-21"
+++
# Mission:
Have a tui app that can render out the clip position that we want.

# Options
- .txt read a .txt file that we cache and handle the processing 
	- this is pretty easy to addon
	- a lot of references online ie logmerger or toolong
- from mem, probably a bad idea since these files are so long
# Features
Side Features
- file drop -> low 
	- creates an folder setup for this file
	- holds the users info

Main Features I want.
- open video from table
- regenerate a video by padding 20 secs 
	- should refill the table with new data...
- delete video given x command on table


These features are in ttui 
- we need to have a parse class to read a line of data and figure out the best case of usage
	- for now we just add dict and make it so people can add their own  
	- maybe follow the obsidian-to-hugo repo for their structure?
- types of input
	- can pipe into it
	- can copy and paste path to it
- add sorting -> added in ttui
	- DataTable has a built in function for this so I can just use that

# Approach
- we should just pull a txt file over from one of our testing documents and use it as a demo before doing the pipeline
- build out the features of tui app
