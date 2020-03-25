import PySimpleGUI as sg
from subprocess import call as execute
from termcolor import cprint
from random import choice
from Helper.consoleHelper import consolePrint

# Theme
sg.theme('DarkAmber')

# For Prints
colors = ('green', 'yellow', 'blue', 'magenta')
color = choice(colors)

# MKFS Built in formatter functions
btrfs = "mkfs.btrfs"
ext2 = "mkfs.ext2"
ext3 = "mkfs.ext3"
ext4 = "mkfs.ext4"
fat32 = "mkfs.vfat"
ntfs = "mkfs.ntfs"
minix = "mkfs.minix"

# SUDO as default super user
superuser = "sudo"


def Format(format_to, device, partition, ):
    execute(f"{superuser} {format_to} /dev/sd{device}{partition}", shell=True)


def confirmation():
    layout = [
        [sg.Text('Are You Sure?', size=(20, 1), justification='center', font=("Helvetica", 16))],
        [sg.T(' ' * 12), sg.Button("Yes"), sg.Button("No")]
    ]

    confirmation_popup = sg.Window('ATTENTION!', layout, default_element_size=(20, 1), grab_anywhere=False)

    while True:
        event, values = confirmation_popup.read()
        if event in ('', None):
            break

        confirmation_popup.close()


def notice():
    layout = [
        [sg.Text('Welcome To Splicer Version 0.1', size=(30, 1),
                 justification='center', font=("Helvetica", 15))],
        [sg.T(' ' * 30), sg.Button("Okay")]
    ]

    notice_windows = sg.Window('Welcome!', layout, default_element_size=(10, 1), grab_anywhere=False)

    while True:
        event, values = notice_windows.read()
        if event in ('', None):
            break

        notice_windows.close()
        cprint("> Running Main-Window", "green")


def main():
    layout = [
        [sg.Text('Format To:')],
        [sg.InputCombo(('btrfs', 'ext2', 'ext3', 'ext4', 'fat32', 'ntfs', 'minix'), size=(20, 1))],

        [sg.Text('Device: /dev/sd?')],
        [sg.InputCombo(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'), size=(20, 1))],

        [sg.Text('Partition: /dev/sdx?')],
        [sg.InputCombo(('1', '2', '3', '4', '5', '6', '7', '8', '9'), size=(20, 1))],

        [sg.Button("FORMAT!"), sg.Button("Exit")]
    ]

    window = sg.Window('Splicer', layout, default_element_size=(40, 1), grab_anywhere=False)
    cprint("Running Notice-Window", "green")
    notice()

    while True:  # Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            cprint("Exiting Application...", "red")
            break
        if event == 'FORMAT!':
            cprint("Running Confirmation-Window", "green")
            confirmation()

    window.close()


consolePrint()
main()
