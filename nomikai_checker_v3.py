import datetime as dt
import PySimpleGUI as sg
# pylint: disable=no-member

img_paths = {
    'nekochan': 'images/nekochan.png',
    'isogashii': 'images/isogashii_woman.png',
    'gaman': 'images/gaman_osake_woman.png',
    'energy': 'images/energy_drink.png'
}
sg.theme('DarkAmber')
nomikai_days = ['Friday', 'Saturday']

def nomikai_kakunin():
    today = dt.datetime.today()
    if today.strftime('%A') in nomikai_days and today.hour < 18:
        message = 'Be patient, the nomikai will come...'
        image = 'gaman'
    elif today.strftime('%A') in nomikai_days and today.hour >= 18:
        message = 'Leave the office ASAP. Nomikai time.'
        image = 'energy'
    elif today.strftime('%A') == 'Sunday':
        message = 'What are you doing? Go and drink!'
        image = 'energy'
    else:
        message = 'Today you must work harder...'
        image = 'isogashii'
    return message, image


# elements in column to be passed to layout
column_to_be_centered = [
    [sg.Text('Nomikai Checker V3',
             font=('Helvetica Bold', 32))],
    [sg.Frame('',
              [[sg.Image(img_paths['nekochan'], key='img', expand_x=True)]],
              pad=(10, 10),
              size=(400, 400),
              border_width=0)],
    [sg.Text('Let\'s check for nomikai...',
             key='msg',
             pad=(0, 20),
             font=('Helvetica', 24))],
    [sg.Button('Kakunin',
               key='btn_bottom',
               size=(10, 1),
               font=('Helvetica', 24))]
]
layout = [
    [sg.VPush()],
    [sg.Push(), sg.Column(column_to_be_centered, element_justification='c'), sg.Push()],
    [sg.VPush()]
]

window = sg.Window('Nomikai Checker', layout, size=(500, 650))

while True:
    event, values = window.read()
    if event == 'btn_bottom':
        if window['btn_bottom'].ButtonText == 'Exit':
            break
        message, image = nomikai_kakunin()
        window['msg'].update(message)
        window['img'].update(img_paths[image])
        window['btn_bottom'].update('Exit')

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()
