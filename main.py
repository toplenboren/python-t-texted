import sys
import urwid
from settings import PALETTE


def exit_on_enter(key):
    if key == 'enter':
        save_text(url, edit.edit_text)
        raise urwid.ExitMainLoop()


def on_edit_change(edit, new_edit_text):

    #todo make this f more effective, rn it's o^n
    def get_word_count(text):
        return len(text.split())


    raw_letter_count = len(new_edit_text)
    letter_counter.set_text(('Symbols: ' + str(raw_letter_count) + 
                             ' Words: ' + str(get_word_count(new_edit_text))))


def open_text(url):
    try:
        raw = open(url, 'r')
    except FileNotFoundError:
        print("ERROR, File was not found")
        exit(-1)
    msg = raw.read()
    raw.close()
    return msg


def save_text(url, text):
    try:
        raw = open(url, 'w')
    except FileNotFoundError:
        print("ERROR, File was not found")
        exit(-1)
    raw.write(text)
    raw.close()


def print_usage():
    print("Usage: python3 main.py [path to the text file]")
    print("-h or --help for additional info")


def print_light_help():
    print("light help")


def print_full_help():
    print("full_help")


def launch_help():
    if len(sys.argv) == 1:
        print_usage()
        return True
    elif sys.argv[1] == '-h':
        print_light_help()
        return True
    elif sys.argv[1] == '--help':
        print_full_help()
        return True





def text_editor():
    url = sys.argv[1]

    edit = urwid.Edit()
    edit.edit_text = open_text(url)

    text_helper = urwid.Text(('banner', u"A simple text editor"), align='center')
    letter_counter = urwid.Text(u'Symbols count:')
    div = urwid.Divider()
    pile = urwid.Pile([text_helper, div, edit, div, letter_counter])
    edit_window = urwid.Filler(pile, valign='top')

    urwid.connect_signal(edit, 'change', on_edit_change)

    loop = urwid.MainLoop(edit_window, PALETTE, unhandled_input=exit_on_enter)
    loop.run()
