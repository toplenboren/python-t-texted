import sys
import urwid
import utilitary
from settings import PALETTE


def launch_help():
    if len(sys.argv) == 1:
        utilitary.print_usage()
        return True
    elif sys.argv[1] == '-h':
        utilitary.print_light_help()
        return True
    elif sys.argv[1] == '--help':
        utilitary.print_full_help()
        return True


def main():
    if not launch_help():
        text_editor()
    else:
        return


def text_editor():

    def check_unhandled_input(key):
        if key == 'shift f5':
            save_text(text_url, edit.edit_text)
            raise urwid.ExitMainLoop()

    def on_edit_change(edit, new_edit_text):

        # todo make this f more effective, rn it's o^n
        def get_word_count(text):
            return len(text.split())

        def change_letter_counter():
            raw_letter_count = len(new_edit_text)
            letter_counter.set_text(('Symbols: ' + str(raw_letter_count) +
                                     ' Words: ' + str(get_word_count(new_edit_text))))

        change_letter_counter()

    def open_text(text_url):
        try:
            raw = open(text_url, 'r')
        except FileNotFoundError:
            print("ERROR, File was not found")
            exit(-1)
        msg = raw.read()
        raw.close()
        return msg

    def save_text(text_text_url, text):
        try:
            raw = open(text_text_url, 'w')
        except FileNotFoundError:
            print("ERROR, File was not found")
            exit(-1)
        raw.write(text)
        raw.close()

    def get_text_url():
        return sys.argv[1]

    text_url = get_text_url()

    edit = urwid.Edit(multiline=True)
    edit.edit_text = open_text(text_url)

    text_helper = urwid.Text(('banner', u"A simple text editor"), align='center')
    letter_counter = urwid.Text(u'Symbols count:')
    div = urwid.Divider()
    pile = urwid.Pile([text_helper, div, edit, div, letter_counter])

    edit_window = urwid.Filler(pile, valign='top')

    urwid.connect_signal(edit, 'change', on_edit_change)

    loop = urwid.MainLoop(edit_window, PALETTE, unhandled_input=check_unhandled_input)
    loop.run()


if __name__ == '__main__':
    main()
