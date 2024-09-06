+++
title = "thebjorn pydebs.md"
date = "2024-08-30"
+++
### core overview

python (pulls data of packaging) -> structure in graph with python code(uses dependency graph structure depgraph2dot.py ) -> output graph (ses [Graphviz](https://www.graphviz.org/) which as the dot which dot.py handles)

pydebs is a graph that holds the import data through package names using site.getusersitepackages() and site.getsitepackages(). 

data -> json
packages aka the class Source can be too far from out entrypoint. 

dot.py -> is used to run commands with Graphviz dot command

### Conditions
- Hotspots
	- conditions
		- number lines of code
		- flow of logic
		- number of times side file is imported
		- bargraphs?
	- we can do a ascii parser
	- change pydeps for imports
- 

### Context

Key Words
- Dotting
- depgraph vs py2depgraph aka dependency graph
- import op-code

Structure
- At it's core it's a graph data structure filled with data from finding imports by looking for import-opcode

>pydeps finds imports by looking for import-opcodes in python bytecodes (think .pyc files). Therefore, only imported files will be found (ie. pydeps will not look at files in your directory that are not imported).>

Entry
Input

Bacon Algo Scoring
- https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon

Output
Opcode Loading?

### Snippets

```python
def find_package_names():
    # initialize with well-known packages that don't seem to have a top_level.txt
    res = {
        'yaml': 'PyYAML',
        'Crypto': 'pycrypto',
    }
    site_package_dirs = [site.getusersitepackages()]
    site_package_dirs += site.getsitepackages()

    for site_packages in reversed(site_package_dirs):
        if not os.path.isdir(site_packages):
            continue

        for pth in os.listdir(site_packages):
            top_level_fname = _find_top_level_file(site_packages, pth)
            if top_level_fname is None:
                continue

            pkgname = _extract_pkg_name(pth)

            if not os.path.exists(top_level_fname):
                if pkgname not in res.values():
                    print("ERR:", pth, 'has not top_level.txt')
                continue

            with open(top_level_fname) as fp:
                modnames = fp.read().split()

            for modname in modnames:
                modname = modname.replace('/', '.')
                if modname.startswith(r'win32\lib'):
                    modname = modname.rsplit('\\')[1]
                res[modname] = pkgname

    return res

```

Top Level