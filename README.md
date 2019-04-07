# python-t-texted
**@toplenboren**

**EN**

A simple terminal text editor,written during my time at the Uni. 

**Install**

`pip install -r requirements.txt`

**Usage**

`Usage: python main.py [file to edit] or python main.py -s (setup)`

`keys: -h, --help -s (setup)`

**Challengelog:**

*01.04.19:* _first release_

*03.04.19:* _multiline_text_input_ + bugfixes

*08.04.19:* _ui_refactor_ + change_settings + bugfixes

**Documentation**

I use urwid module as the console UI engine. Main.py contain main logic of the program. Settings.py contain PALLETE variable, that stores info about user preferences, such as colors. Utilitary.py contains some utilitary functions. This file was created just to make main.py cleaner. 

________________________________________________________________________________________________________________________________________

**RU**

Реализация текстового редактора с консольным интерфейсом. Матмеховский курс по Питону.

**Установка**

`pip install -r requirements.txt`

**Использование**

`Использование: python main.py [путь к файлу] или python main.py -s (для настройки)`

`поддерживаемые ключи: -h, --help -s (настройки)`

**Путь:**

*01.04.19:* господи, оно работает

*03.04.19:* теперь можно тыкать 'enter' и оно будет вставлять перводы строк. + багфикс

*08.04.19:* переделал ui, тепреь текстовый редактор выглядт как nano, а еще теперь можно менять цвета + багфикс

**Документация**

Использую модуль urwid для вывода консольного интерфейса. В main.py главная логика программы. В settings.py лежат настройки для urwidа (цвета, шрифты, и.т.д). В utilitary.py описаны утилитарные функции. Файл сделан только для того, чтобы чуть почистить main.py
