import sys
import urwid
from settings import PALETTE


def exit_on_enter(key):
    if key == 'enter':
        save_text('try.txt', edit.edit_text)
        raise urwid.ExitMainLoop()


def on_edit_change(edit, new_edit_text):
    letter_counter.set_text(('Symbols: %s' % len(new_edit_text)))


def open_text(url):
    raw = open(url, 'r')
    msg = raw.read()
    raw.close()
    return msg


def save_text(url, text):
    raw = open(url, 'w')
    raw.write(text)
    raw.close()


url = sys.argv[1]

edit = urwid.Edit()
edit.edit_text = open_text(url)

text_helper = urwid.Text(('banner', u"A simple text editor"), align='center')
letter_counter = urwid.Text(u'Symbols count:')
div = urwid.Divider()
pile = urwid.Pile([text_helper, div, edit, div, letter_counter])
top = urwid.Filler(pile, valign='top')

urwid.connect_signal(edit, 'change', on_edit_change)

loop = urwid.MainLoop( top, PALETTE , unhandled_input=exit_on_enter)
loop.run()