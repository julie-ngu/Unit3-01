# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program is a guessing game where the user must input the number 5 (the correct number) in order to 
# win

import ui

def check_answer_button_touch_up_inside(sender):
    # This checks if the user's guess was right or wrong
    
    # constants
    CORRECT_NUMBER = 5
    
    # input
    number_entered = int(view['enter_guess_textfield'].text)
    
    # process
    if number_entered == CORRECT_NUMBER:
        #output
        view['answer_label'].text = "Good job!"

view = ui.load_view()
view.present('full_screen')
