
import PySimpleGUI as sg

sg.theme('DarkAmber') 


layout = [[sg.Text("Insert query")],
            [sg.Input(key = '-IN-', enable_events = True)],
            [sg.Button('Search'), sg.Exit()]]

margins = (200,100)

# Create the window
window = sg.Window("Demo", layout = layout, margins = margins, finalize = True)

# The Event Loop
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    if event == 'Search':
        # Update the "output" text element to be the value of "input" element
        #window['-OUTPUT-'].update(values['-IN-'])

        print(values['-IN-'])



window.close()


