import urwid
import sys

buffer = ""

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class TextField(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return super(TextField, self).keypress(size,key)
        self.original_widget = urwid.Text(
            u"Saved some data: \n %s \n symbols" % len(edit.edit_text)
        )
        buffer = edit.edit_text


palette = [('I say', 'default,bold', 'default', 'bold'),('bg', 'black', 'dark blue')]

edit = urwid.Edit()
edit.edit_text = "Try to edit me"
editboy = TextField(edit)

text_helper = urwid.Text(u"A simple text editor")
letter_counter = urwid.Text(u'Symbols count:')
div = urwid.Divider()
pile = urwid.Pile([text_helper, div, edit, div, letter_counter])
top = urwid.Filler(pile, valign='top')


def on_editboy_change(edit, new_edit_text):
    letter_counter.set_text(('Symbols: %s' % len(new_edit_text)))

urwid.connect_signal(edit,'change', on_editboy_change)

loop = urwid.MainLoop(top, palette, unhandled_input=exit_on_q)
loop.run()
