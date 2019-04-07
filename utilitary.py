import settings

def print_usage():
    print("Usage: python3 main.py [path to the text file]")
    print("-h or --help for additional info")


#todo
def print_light_help():
    print("Shift + f5 = save file \nShift + f8 = exit WO saving")


#todo
def print_full_help():
    print("Shift + f5 = save file "
          "\nShift + f8 = exit WO saving "
          "\nPlease note, that this program is set up to automatically create files,"
          " if provided text file doesn't exist")


def setup():
    print("Avainable settings:")
    print("1. theme:")
    setting = input("Please specify a setting you want to change: *1")

    if setting == '1':
        print('Available variants: \n1. Marine (blue) \n2. Royal Red (red)')
        user_inp = input("Please specify a value you want to set: *1")
        color_settings = ['dark blue', 'dark_red']
        try:
            settings.color_misc = color_settings[int(user_inp) - 1]
        except Exception:
            print("Please choose valid settings.")
            exit(2)
