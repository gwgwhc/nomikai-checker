import PySimpleGUI as sg
from nomikai_checker import NomikaiChecker


class NomikaiCheckerGUI():
    def __init__(self):
        """ Initialize image paths, NomikaiChecker and window."""
        self.img_paths = {
            'nekochan': 'images/nekochan.png',
            'isogashii': 'images/isogashii_woman.png',
            'gaman': 'images/gaman_osake_woman.png',
            'energy': 'images/energy_drink.png'
        }
        self.checker = NomikaiChecker()  # Initialize NomikaiChecker
        self.window = self.make_window()  # Create the window

    def make_window(self):
        """ Create GUI layout and window. """
        # elements in column to be passed to layout
        column_to_be_centered = [
            [sg.Text('Nomikai Checker V3',
                     font=('Helvetica Bold', 32))],
            [sg.Frame('',
                      [[sg.Image(self.img_paths['nekochan'],
                                 key='img', expand_x=True)]],
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
        # centred layout
        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Column(column_to_be_centered,
                                  element_justification='c'),
             sg.Push()],
            [sg.VPush()]
        ]

        return sg.Window('Nomikai Checker', layout, size=(500, 650))

    def update_ui(self, result_msg, image_key):
        """Update the message, image, and button"""
        self.window['msg'].update(result_msg)
        self.window['img'].update(self.img_paths[image_key])
        self.window['btn_bottom'].update('Exit')

    def handle_event(self):
        """Handle GUI events and updates"""
        while True:
            event, values = self.window.read()

            if event == 'btn_bottom':
                if self.window['btn_bottom'].ButtonText == 'Exit':
                    break  # Exit the loop if 'Exit' button is pressed

                self.process_nomikai_check()

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

        self.window.close()

    def process_nomikai_check(self):
        """Process the logic for checking the nomikai probability and update the UI"""
        today = self.checker.get_datetime()

        # Check if probability to leave early based on the current day
        if today.strftime('%A') in ('Saturday', 'Sunday') and self.checker.check_probability():
            self.update_ui('What are you doing? Go and drink!', 'energy')
        elif self.checker.check_probability():
            self.update_ui('Leave the office ASAP. Nomikai time.', 'energy')
        elif not self.checker.is_before_4pm():
            self.update_ui('Be patient, the nomikai will come...', 'gaman')
        else:
            self.update_ui('Today you must work harder...', 'isogashii')

    def run(self):
        """Run the main event loop for the GUI"""
        self.handle_event()

def test():
    NomikaiCheckerGUI().run()


if __name__ == '__main__':
    test()
