color_misc = 'dark_blue'

def set_palette(color_misc):
    return [('header', 'white', color_misc),
            ('footer', 'white', color_misc),
            ('body', 'black', 'white')]

PALETTE = set_palette(color_misc)
