
from BooleanRetrievalSystem import *
import PySimpleGUI as sg


file_name = 'out_subset.csv'
retrieval_model = BooleanRetrievalSystem(file_name)
retrieval_model.read_csv()



sg.theme('DarkAmber') 

layout = [[sg.Text("Insert query")],
            [sg.Input(size = (75,1), key = '-IN-', enable_events = True)],
            [sg.Button('Search'), sg.Button('Clear')],
            [sg.Text('')],
            [sg.Text('', key = '-OUTPUT-')]]
            #[sg.Output(size=(75,10), key='-OUTPUT-')]]

margins = (200,150)

# Create the window
window = sg.Window("Demo", layout = layout, margins = margins, finalize = True)

# The Event Loop
while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Exit' :
        break      

    if event == 'Search' :
        try :
            retrieved_docs = retrieval_model.search(values['-IN-'])
            window['-OUTPUT-'].update(retrieved_docs)
        except ValueError  as err:
            window['-OUTPUT-'].update(str(err))
            

    if event == 'Clear' :
        window['-IN-'].update('')
        window['-OUTPUT-'].update('')

window.close()





'''

retrieved_docs = retrieval_model.search('driv*')
print(retrieved_docs)

'''

