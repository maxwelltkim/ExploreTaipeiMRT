# ******v2 notes**********
# 1. start using functions for line selection (if they want to play again) and stop randomizing
# 2. ignore lower case for now, too difficult, get it working first then add functionality
# 3. Next functionality 1. accounting for lowercase input
#                       2. allowing player to choose the same line, but a new stop
#                       3. incorporating names to the lines
from random import randint

mrt_lines_and_stops = {'Brown': list(range(1, 25)), 'Red': list(range(2, 29)), 'Green': list(range(1, 20)),
                       'Orange (Luzhou)': list(range(50, 55)), 'Orange (Huilong)': list(range(1, 22)),
                       'Blue': list(range(1, 23)), 'Yellow': list(range(7, 21))}
# this is a dictionary containing the names of the lines, and then the number of stops they have

mrt_lines = []  # this is a list that will take the appropriate line from the mrt_lines_and_stops dictionary
for key, value in mrt_lines_and_stops.items():
    mrt_lines.append(key)

def ask_for_line():
    user_choice = str(input(
        'Which line would you like to ride today: ')).title()  # adding this Title thing allows you take lowercase inputs
    if user_choice not in mrt_lines:
        print('Sorry. That is not a valid choice, please try again"')
        ask_for_line()
    else:
        global line_choice
        line_choice = user_choice

def randomize_stop(line_choice):  # once a line has been selected, this will randomly select a stop on that line
    low = mrt_lines_and_stops[line_choice][0]
    high = mrt_lines_and_stops[line_choice][-1]
    stop = randint(low, high)
    print('Okay! Today you\'ll take the ' + line_choice + ' line all the way to stop number ' + str(
            stop) + '. Have a great day!')
    want_to_play_again()

def play_again():  # this function runs the line choice and selection again
    print('Sure thing, here is the list of lines again ' + str(mrt_lines))
    ask_for_line()

def want_to_play_again():  #this function asks if user wants to play again
    restart = input('If you\'re not happy with your choice, would you like to try again? (Y/N): ')
    if restart == 'Y' or restart == 'y':
        play_again()
    if restart == 'N' or restart == 'n':
        print('Okay, have fun on your adventure today!')
        exit()

print('Welcome to your Taipei exploration game! Not sure what adventure you\'d like to take today? Let me help!')
print('Please choose an MRT line from the following list: ' + str(mrt_lines))

ask_for_line()
randomize_stop(line_choice)
want_to_play_again()
