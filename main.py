import sys
import urwid
import utilitary
from settings import PALETTE

selection_buffer = ""


class Buffer:

    data = ""
    buffer_type = 0
    start_ind = 0
    finish_ind = 0

    def add(self, char):
        self.data = char + self.data

    def add_to_the_back(self, char):
        self.data += char

    def remove(self):
        if len(self.data) > 0:
            self.data = self.data[0:len(self.data) - 1]
            if len(self.data) == 0:
                self.buffer_type = 0
        else:
            raise Exception("REMOVE FROM EMPTY BUFFER.")

    def show(self):
        return self.data


class TextEditor:

    def launch(self):

        buffer = Buffer()

        def select(direction):
            if direction == 'left':
                current_cursor_pos = edit.edit_pos
                if buffer.buffer_type != 1:
                    if current_cursor_pos - 1 >= 0:
                        buffer.add(edit.edit_text[current_cursor_pos-1])
                        #todo
                        edit.set_edit_pos(current_cursor_pos-1)
                        update_buffer_show()
                        buffer.buffer_type = -1
                else:
                    buffer.remove()
                    edit.set_edit_pos(current_cursor_pos - 1)
                    update_buffer_show()

            if direction == 'right':
                current_cursor_pos = edit.edit_pos
                if buffer.buffer_type != -1:
                    if current_cursor_pos + 1 < len(edit.edit_text):
                        buffer.add_to_the_back(edit.edit_text[current_cursor_pos+1])
                        #todo
                        edit.set_edit_pos(current_cursor_pos+1)
                        update_buffer_show()
                        buffer.buffer_type = 1
                else:
                    buffer.remove()
                    edit.set_edit_pos(current_cursor_pos + 1)
                    update_buffer_show()
            pass

        def check_unhandled_input(key):
            if key == 'shift f5':
                save_text(text_url, edit.edit_text)
                raise urwid.ExitMainLoop()
            elif key == 'shift f6':
                save_text(text_url, buffer)
                raise urwid.ExitMainLoop()
            elif key == 'shift f8':
                select('left')
            elif key == 'shift f9':
                select('right')

        def update_buffer_show():
            original = letter_counter.text.split('Buffer')[0]
            letter_counter.set_text(original + 'Buffer: ' + str(buffer.show()))

        def update_letter_counter(edit, new_edit_text):

            # todo make this f more effective, rn it's o^n
            def get_word_count(text):
                return len(text.split())

            def change_letter_counter():
                raw_letter_count = len(new_edit_text)
                letter_counter.set_text(('Symbols: ' + str(raw_letter_count) +
                                         ' Words: ' + str(get_word_count(new_edit_text))))
                update_buffer_show()
            change_letter_counter()

        def open_text(text_url):

            global buffer

            try:
                raw = open(text_url, 'r')
            except FileNotFoundError:
                raw = open(text_url, 'w+')

            msg = raw.read()
            buffer = msg
            raw.close()

            # todo refactor
            try:
                raw2 = open(text_url, 'w')
                raw2.close()
            except PermissionError:
                print("I wouldn't be able to save your data. Please check permissions.")
                exit(1)

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
        update_buffer_show()

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


def launch_utilitary_function():
    if len(sys.argv) == 1:
        utilitary.print_usage()
        return True
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
        ted = TextEditor()
        ted.launch()
    else:
        return


if __name__ == '__main__':
    main()
