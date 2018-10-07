TeX Todoer
----------

A very simple tool to display TODOs in multi-file TeX documents. Takes a path and either displays all TeX documents it can find, or just one specified.

Prints a list of chapters, sections, subsections, subsubsections and TODOs.

TODOs must be of the form %TODO.

Works in Python 3.5.

Syntax
------

`python main.py [PATH] [-so|-to] [-s filename]`

`[PATH]` - Path to root of TeX document.

`-so` - Displays filenames, sections, subsections and TODOs only.

`-to` - Displays filenames and TODOs only.

`-s filename` - Just displays TODOs for one file, at `[PATH]filename`.
