+++
title = "Command List.md"
date = "2024-08-08"
+++
## Command List
 - list of services we can do with command prompt
 
I want.
* custom
  * pipelines on_start commands for projects -> run test cases and return ideas how to fix
    * hard hard
    
* Open Application
* Open directory 
* Open coding project
  * directory + env startup
  This can be possible by subprocessing with fastapi or calling an async function

* Image processing vs opencv?
  * can handle masking and information processing

* Pull
  * Activity Watch Stuff
    * generate a report of times and charts
  * Better google search and summarize 
 
* Process
  * Handle data processing with python libraries 


## Snippets
```
import subprocess

from fastapi import FastAPI

app = FastAPI()

def runandget():
    myprocess = subprocess.run(["ls"], stdout=subprocess.PIPE)
    thoutput = myprocess.stdout.decode('utf-8')
    return thoutput

@app.post("/doit")
def dothis():
    resultfunc = runandget()
    return {"result": resultfunc}
```

## Subprocess 
> The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:
> 

pipes and return codes
>  *input* argument is passed to [`Popen.communicate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate "subprocess.Popen.communicate") and thus to the subprocess’s stdin. If used it must be a byte sequence, or a string if *encoding* or *errors* is specified or *text* is true. 
>

byte sequenene or string?
utf-8 = byte sequence '.decode('utf-8')' is important


*Popen Class*
Class that handles all the piping in, out, err, and communicate of files.
