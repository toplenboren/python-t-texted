# python-t-texted
**@toplenboren**

A simple terminal text editor,written during my time at the Uni. 

**Usage**

`requires urwid for console UI`

`Usage: python main.py [file to edit]`
`keys: -h, --help`

**Challengelog:**

*01.04.19:* _first release_

*03.04.19:* _multiline_text_input_ + bugfixes

**Documentation**

I use urwid module as the console UI engine. Main.py contain main logic of the program. Settings.py contain PALLETE variable, that stores info about user preferences, such as colors. Utilitary.py contains text info for launch_help() function in main.py. This file was created just to make main.py more clean. 
