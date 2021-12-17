
from finder.BooleanRetrievalSystem import  *
import PySimpleGUI as sg
import os


retrieval_model = BooleanRetrievalSystem()

model_filename = 'model.pkl'
if (os.path.exists(model_filename)) :
    retrieval_model.read_model(model_filename)
else :
    file_name = 'corpus.csv'
    retrieval_model.read_csv(file_name)
    retrieval_model.write_model(model_filename)

sg.theme('DarkAmber') 

layout = [[sg.Text("Insert query")],
            [sg.Input(size = (75,1), key = '-IN-', enable_events = True)],
            [sg.Button('Search'), sg.Button('Clear')],
            [sg.Text('')],
            [sg.Output(size = (75, 10), key = '-OUTPUT-')]]

margins = (200,150)

# Creation of the window
window = sg.Window("Information Retrieval System", layout = layout, margins = margins, finalize = True)

# Event loop
while True:

    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Exit' :
        break      

    if event == 'Search' :
        try :
            retrieved_docs = retrieval_model.search(values['-IN-'])
            window['-OUTPUT-'].update(retrieved_docs)
        except ValueError  as err :
            window['-OUTPUT-'].update(str(err))

    if event == 'Clear' :
        window['-IN-'].update('')
        window['-OUTPUT-'].update('')

window.close()