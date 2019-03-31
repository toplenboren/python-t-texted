import urwid


def exit_on_enter(key):
    if key == 'enter':
        save_text('try.txt', edit.edit_text)
        raise urwid.ExitMainLoop()


class TextField(urwid.Filler):

    def keypress(self, size, key):
        if key != 'enter':
            return super(TextField, self).keypress(size,key)
        edit.edit_text+='\n'
        self.original_widget = urwid.Text(
            u"Saved some data: \n %s \n symbols" % len(edit.edit_text)
        )


def open_text(url):
    raw = open(url, 'r')
    msg = raw.read()
    raw.close()
    return msg


def save_text(url, text):
    raw = open(url, 'w')
    raw.write(text)
    raw.close()


palette = [('bg', 'black', 'dark blue'),('banner', 'bold', 'white'  )]

edit = urwid.Edit()
edit.edit_text = open_text('try.txt')
editboy = TextField(edit)

text_helper = urwid.Text(('banner', u"A simple text editor"), align='center')
letter_counter = urwid.Text(u'Symbols count:')
div = urwid.Divider()
pile = urwid.Pile([text_helper, div, edit, div, letter_counter])
top = urwid.Filler(pile, valign='top')


def on_editboy_change(edit, new_edit_text):
    letter_counter.set_text(('Symbols: %s' % len(new_edit_text)))

urwid.connect_signal(edit,'change', on_editboy_change)

loop = urwid.MainLoop(top, palette, unhandled_input=exit_on_enter)
loop.run()
