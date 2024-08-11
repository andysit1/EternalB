+++
title = "Design Plan - Jarvis.md"
date = "2024-08-08"
+++
## Design UI
Figure out how to change the ui of the conversations, can be quick and dirty

## Structure 

- We want code block blocks to make it easy to set up commands for jarvis to read and handle
- Could use an adapter to handle the command types
  - [Type] [ACTION] 
  - 


## Implementations and Libs
- **Key Word Detection**:
  1.) constant listening -> only save when sentence ends
  2.) or button press
  
- **Hot Key to enable and disable transcription**:
  [GitHub - webNeat/ctrl-keys: A tiny, super fast, typescript library to handle keybindings efficiently.](https://github.com/webNeat/ctrl-keys)
   
  1.) Setup handlers to handle certain commands? Then on handle down we trigger an internal api to active the toggle? The question is do I make it seperate from conversions or directly
  
  2.) Maybe use the tooltip bar? Conversions does not have one, instead lets make it automatically feed a conversion between you and jarvis there!
     -> would be cool and iterative 
     
- **AI-Powered Commands**
    CMD LINE interface?
    - Need a web scrapper -> into summarizer for with highlight llm
    - A way to iterface data from google chrome
    - read screen? command pulse read the screen?
      - gives a user input for help? suggestions as a alert?
  
  ## Other Features
 
 - what if we can get jarvis to send info to google chrome then read it's info and summarize accurate information

## FastAPI Implementation
 - Have a dictionary that can be hashed and saved?
   - handles the bools and flags that we need to know given capabilties dependent on user? -> prob too advance for myself
 - Basic functions that a jarvis should have


1.) first issue to solve : Command Problem

Issue is static questions and prompts. I want llm and jarvis to be flexible as possible to feel like a real person.
 
Command system given prompts to short to simple commands, [input -> output] [cut_image 40x40 -> image]
 
Idea: Mix and Mash key words that combine into powerful commands our fastapi can handle. Use llm to handle the conversion into commands

Formater Agent FORCE to correct KEYWORDS
  on_true -> send_api
  on_false -> recall Formatter agent

## Brainstorm
Maybe base on the blocks we can open source the structure of block.

we have an llm
we have user context ie screen sharing, voice, and copy and past infomration

we have all libraries in javascript
we have logic 
we have a user storage system
