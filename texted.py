# Copyright: Toplenboren, 18.03.2019
import os

def get_os():
    pass


def print_main_menu():
    print("O - open file, S - save file, E - edit file")


def clear_colsole():
    os.system('cls')


def edit_file():
    pass


def open_file():
    pass


def save_file():
    pass


def create_file():
    pass


def file_opened():
    pass


def re_render():
    clear_colsole()
    print_main_menu()


def main():
    print_main_menu()

    print()
    user_command = input("Please input your command")
    print()

    if user_command == "O":
        open_file()
    elif user_command == 'N':
        create_file()
    elif user_command == "E":
        if file_opened():
            edit_file()
    elif user_command == "S":
        if file_opened():
            save_file()

    return 0

main()
