import sys
import urwid
import utilitary
from settings import PALETTE


def launch_utilitary_function():
    if len(sys.argv) == 1:
        utilitary.print_usage()
    else:
        argument = sys.argv[1]

        if argument == '-h':
            utilitary.print_light_help()
            return True
        elif argument == '--help':
            utilitary.print_full_help()
            return True
        elif argument == '-s':
            utilitary.setup()
            return True
    return False


def main():
    if not launch_utilitary_function():
        text_editor()
    else:
        return


def text_editor():
    def check_unhandled_input(key):
        if key == 'shift f5':
            save_text(text_url, edit.edit_text)
            raise urwid.ExitMainLoop()
        if key == 'shift f8':
            raise urwid.ExitMainLoop()

    def update_letter_counter(edit, new_edit_text):

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
            raw = open(text_url, 'w+')

        # todo refactor
        try:
            raw2 = open(text_url, 'w')
            raw2.close()
        except PermissionError:
            print("I wouldn't be able to save your data. Please check permissions.")
            exit(1)

        msg = raw.read()
        raw.close()
        return msg

    def save_text(text_url, text):
        raw = open(text_url, 'w')
        raw.write(text)
        raw.close()

    def get_text_url():
        return sys.argv[1]

    text_url = get_text_url()

    edit = urwid.Edit(multiline=True)
    edit.edit_text = open_text(text_url)

    text_banner = urwid.Text("A simple text editor", align='center')
    text_helper = urwid.Text("Shift+f5 -> save, Shift+f8 -> exit")
    letter_counter = urwid.Text('')
    update_letter_counter(edit, edit.edit_text)

    text_pile = urwid.Pile([letter_counter, text_helper])

    urwid.connect_signal(edit, 'change', update_letter_counter)

    header_prep = urwid.AttrMap(text_banner, 'header')
    body_prep = urwid.AttrMap(urwid.Filler(edit, valign='top'), 'body')
    footer_prep = urwid.AttrMap(text_pile, 'footer')

    frame = urwid.Frame(body=body_prep,
                        header=header_prep,
                        footer=footer_prep)

    loop = urwid.MainLoop(frame, PALETTE, unhandled_input=check_unhandled_input, handle_mouse=False)
    loop.run()


if __name__ == '__main__':
    main()
