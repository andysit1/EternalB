+++
title = "textual - learning.md"
date = "2024-08-20"
+++
#textual 

copy from my daily notes

will slowly add stuff here as a more central location for my notes.

[2024-08-20]({{< ref "2024-08-20" >}})
- textual
	- reactive
		- _descriptor protocol_ -> 
			- auto refreshing 
			- var() from textual.reactive wont causes refreshes
			- built in validates_
			- built in watch_ 
				- check watch01.py for example
	- dev tools
		- super useful
			- allows for double consoles (textual console)
			- from textual import log or TextualHandler with logger()
	- workers
		- `on_worker_state_changed`
		- -- dev shows the lifetime of workers
		- can you decorates for workers as well to auto generate them
	
	- uses id to handle conditions of apps
	
	- widgets
		- mini apps responsible for an area of the screen
		- loading indicator 
			- replaces wigets for a loading icon when generating data
			- (useful for me)
		- base
			- each widget has
			- on_mount
		- Static 
			- Just content with base widget classes
		
	- message_pump.py
		- very important lib cause the entire textual console is just this file. look into! 
