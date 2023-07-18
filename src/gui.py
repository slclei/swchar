'''
This is the GUI class to build a gui for this application.
It has parameters to store user's input, layout for configuration gui.
API:
GUI.build(): make window for gui, record user's input, pass input to GUI.search() and use the returned layout to make new window to display results
GUI.search(): pass user's input to and get result from Star_warChar class, return a new layout to display results.
'''


# REF: https://github.com/PySimpleGUI/PySimpleGUI
import PySimpleGUI as sg
import star_war_char

class GUI:
    def __init__(self):
        # output is used to record output in gui
        self.output=""
        # input is used to record user's input from gui
        self.input=""
        # input_layout is used to configure layout from start point
        self.input_layout=[[sg.Text("Please input character name you want to search:")],
                [sg.Input(key='-INPUT-'),sg.Button('Submit'), sg.Button('Quit')]]
        # count is used as key of different layouts generated from different user's inputs
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

                # Make new windown with new layout generated with user's input and search result
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
                output.append([sg.Text("Sorry, there is no characters containing: "+self.input)])
                return output
            
            # Handle error if an error is produced from searching
            if chars.error!="":
                output.append([sg.Text("Sorry, there is an error: "+chars.error)])
                return output

            # Get all results names in alphabetical order
            rows=[]
            for name in chars.name:
                # Get star ships
                ships=chars.chars[name][0]
                # Get home planet
                home_planet=chars.chars[name][1]
                # Get species
                species=chars.chars[name][2]

                # Configure layouts for different sections
                name_layout=[sg.Text("Character Name: "+name,key=name)]
                ships_layout=[sg.Table(values=ships, headings=['Starship Name','Starship Cargo Capacity','Starship class'],justification='left',size=(40,2),key="ship"+name)]
                home_layout=[sg.Table(values=home_planet, headings=['Home Planet Name', 'Home Planet Population', 'Home Planet Climate'],justification='left',size=(40,2),key="home"+name)]
                species_layout=[sg.Table(values=species, headings=['Species Name','Species Language','Species Lifespan'],justification='left',size=(40,2),key="species"+name)]
                
                # Configure column for making window later
                column=[name_layout,ships_layout,home_layout,species_layout]
                rows+=column

            # Configure layout with columns
            output.append([sg.Column(rows, key=str(self.count), scrollable=True,  vertical_scroll_only=True,size=(1000,800))])

            return output
            
