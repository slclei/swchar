# REF: https://github.com/PySimpleGUI/PySimpleGUI
import PySimpleGUI as sg
import star_war_char

class GUI:
    def __init__(self):
        self.output=""
        self.input=""
        self.results=[]
        pass

    def build(self):
        # Define the window's contents
        layout = [[sg.Text("Please input character name you want to search:")],
                [sg.Input(key='-INPUT-')],
                [sg.Text(size=(40,40), key='-OUTPUT-')],
                [sg.Button('Submit'), sg.Button('Quit')]]

        # Create the window
        window = sg.Window('Star War series - character', layout)

        # Display and interact with the Window using an Event Loop
        while True:
             # Get evetn and values. values['-INPUT-']
            event, values = window.read()
            # Get user's input
            self.input=values['-INPUT-']
            # Start searching
            self.search()

            # See if user wants to quit or window was closed
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break

            # Output a message to the window
            window['-OUTPUT-'].update(self.output)

        # Finish up by removing from the screen
        window.close()

    # Search for user's input
    def search(self):
        # Only start with valid input
        if self.input!="":
            # Create an object for characters
            chars=star_war_char.Star_war_char()
            chars.get_chars(self.input)
            self.output=chars.chars

