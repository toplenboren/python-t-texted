# python-t-texted
**@toplenboren**

**EN**

A simple terminal text editor,written during my time at the Uni. 

**Usage**

`requires urwid for console UI`

`Usage: python main.py [file to edit]`
`keys: -h, --help`

**Challengelog:**

*01.04.19:* _first release_

*03.04.19:* _multiline_text_input_ + bugfixes

**Documentation**

I use urwid module as the console UI engine. Main.py contain main logic of the program. Settings.py contain PALLETE variable, that stores info about user preferences, such as colors. Utilitary.py contains text info for launch_help() function in main.py. This file was created just to make main.py cleaner. 

________________________________________________________________________________________________________________________________________

**RU**

Реализация текстового редактора с консольным интерфейсом. Матмеховский курс по Питону.

**Использование**

`требуется модуль urwid для UI`

`Использование: python main.py [путь к файлу]`
`поддерживаемые ключи: -h, --help`

**Challengelog:**

*01.04.19:* господи, оно работает

*03.04.19:* теперь можно тыкать 'enter' и оно будет вставлять перводы строк. + багфикс

**Документация**

Использую модуль urwid для вывода консольного интерфейса. В main.py главная логика программы. В settings.py лежат настройки для urwidа (цвета, шрифты, и.т.д). В utilitary.py описаны функции вывода помощи. Файл сделан только для того, чтобы чуть почистить main.py
