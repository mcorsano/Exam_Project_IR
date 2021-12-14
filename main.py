
from BooleanRetrievalSystem import *
import PySimpleGUI as sg



sg.theme('DarkAmber') 


layout = [[sg.Text("Insert query")],
            [sg.Input(size = (50,1), key = '-IN-', enable_events = True)],
            [sg.Output(size=(50,2), key='-OUTPUT-')],
            [sg.Button('Search'), sg.Button('Clear'), sg.Exit()]]

margins = (200,100)

# Create the window
window = sg.Window("Demo", layout = layout, margins = margins, finalize = True)

# The Event Loop
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Exit' :
        break      

    if event == 'Search' :
        file_name = 'out_subset.csv'
        retrieval_model = BooleanRetrievalSystem(file_name)
        retrieved_docs = retrieval_model.search(values['-IN-'])
        window['-OUTPUT-'].update(retrieved_docs)

    if event == 'Clear' :
        window['-IN-'].update('')
        window['-OUTPUT-'].update('')

window.close()





'''
file_name = 'out_subset.csv'
retrieval_model = BooleanRetrievalSystem(file_name)
retrieved_docs = retrieval_model.search('film')
'''


