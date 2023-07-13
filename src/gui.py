# REF: https://github.com/PySimpleGUI/PySimpleGUI
import PySimpleGUI as sg
import star_war_char

class GUI:
    def __init__(self):
        self.output=""
        self.input=""
        self.results=[]
        self.column=[]
        self.input_layout=[[sg.Text("Please input character name you want to search:")],
                [sg.Input(key='-INPUT-'),sg.Button('Submit'), sg.Button('Quit')]]
        self.output_layout=[]
        self.count=0
        
    def build(self):
        # Create the window
        window = sg.Window('Star War series - character', self.input_layout,size=(1000, 500))

        # Display and interact with the Window using an Event Loop
        while True:
             # Get evetn and values. values['-INPUT-']
            event, values = window.read()
            # Get user's input
            self.input=values['-INPUT-']            

            # See if user wants to quit or window was closed
            if event == sg.WINDOW_CLOSED or event == 'Quit':
                break

            # See if user wants to submit a task
            if event == 'Submit':
                window.refresh()
                # Start searching only if input is valid
                search_result=[]

                search_result=self.search()

                # Increase the count for key name
                self.count+=1
                    
                #window.extend_layout(window['-FRAME-'],self.output_layout)

                window.close()
                window = sg.Window('Star War series - characters with '+self.input, search_result,size=(1000, 500))

        # Finish up by removing from the screen
        window.close()

    # Search for user's input
    def search(self):
            # Create an object for characters
            chars=star_war_char.Star_war_char()
            # Search for results
            chars.get_chars(self.input)

            # Define a new layout
            output=[[sg.Text("Please input character name you want to search:")],
                [sg.Input(key='-INPUT-'),sg.Button('Submit'), sg.Button('Quit')]]
            
            # Handle no characters back
            if len(chars.name)==0:
                 output.append([sg.Text("Sorry, there is no characters containing "+self.input)])

            # Get all results names in alphabetical order
            rows=[]
            for name in chars.name:
                # Get star ships
                ships=chars.chars[name][0]
                # Get home planet
                home_planet=chars.chars[name][1]
                # Get species
                species=chars.chars[name][2]

                name_layout=[sg.Text("Character Name: "+name,key=name)]
                ships_layout=[sg.Table(values=ships, headings=['Starship Name','Starship Cargo Capacity','Starship class'],justification='left',size=(40,2),key="ship"+name)]
                home_layout=[sg.Table(values=home_planet, headings=['Home Planet Name', 'Home Planet Population', 'Home Planet Climate'],justification='left',size=(40,2),key="home"+name)]
                species_layout=[sg.Table(values=species, headings=['Species Name','Species Language','Species Lifespan'],justification='left',size=(40,2),key="species"+name)]
                
                column=[name_layout,ships_layout,home_layout,species_layout]
                rows+=column

                #for layout in [name_layout,ships_layout,home_layout,species_layout]:
                    #self.output_layout.append(layout)
            output.append([sg.Column(rows, key=str(self.count), scrollable=True,  vertical_scroll_only=True,size=(1000,800))])

            return output
            



'''
column = [
    [sg.Frame(f'AI-{i}', frame(), pad=(0, 0), key=f'FRAME {i}')]
        for i in range(1, 11)
]

[
        [sg.Text('OK:'),         sg.Push(), Text(10)],
        [sg.Text('NG:'),         sg.Push(), Text(10)],
        [sg.Text('Yield Rate:'), sg.Push(), Text(15)],
        [sg.Text('Total:'),      sg.Push(), Text(15)],
    ]
    '''