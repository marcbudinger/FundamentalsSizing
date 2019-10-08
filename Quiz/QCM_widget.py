import ipywidgets as widgets
import sys
from IPython.display import display
from IPython.display import clear_output
import pandas

out = widgets.Output()

def create_multipleChoice_widget(description, options, correct_answer):
    
    options = [x for x in options if str(x) != 'nan']
    
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)      
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "True" + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "False" + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="Submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

def quiz(number, file):
    f = pandas.read_excel(file)
    Q=create_multipleChoice_widget(f.iloc[number-1][0],f.iloc[number-1][1:7].values.tolist(),f.iloc[number-1][7])
    display(Q)
    