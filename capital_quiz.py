##a simple quiz py3
##no complex logic as it's an example for kids learning py. (so no loop)
##because of the length, a good one to use later to show what looping does

print('Name the capitals!')
print('Instructions:')
print('You will be given a US state.')
print('Give the correct capital to gain a point.')

print('Here we go: '+ '\n'*3)

def check_capital (user_cap, answer_cap):
    ## changes to var seen throughout program
    global score
    user_guessing = True
    guesses = 0
    while user_guessing and guesses <3:  
      if user_cap.lower() == answer_cap.lower():
        print('Correct you are!')
        score = score +1
        user_guessing = False
      else:
        if guesses < 2:
          user_cap = input('Oh noes. Try again.')
        guesses = guesses + 1
    if guesses == 3:
      print('The capital is ' + answer_cap)

score = 0

alabama = input('Alabama > ')
check_capital(alabama, 'montgomery')

alaska = input('Alaska > ')
check_capital(alaska, 'juneau')

arizona = input('Arizona > ')
check_capital(arizona, 'phoenix')

arkansas = input('Arkansas > ')
check_capital(arkansas, 'little rock')

california = input('California > ')
check_capital(california, 'sacramento')

colorado = input('Colorado > ')
check_capital(colorado, 'denver')

connecticut = input('Connecticut > ')
check_capital(connecticut, 'hartford')

delaware = input('Delaware > ')
check_capital(delaware, 'dover')

florida = input('Florida > ')
check_capital(florida, 'tallahassee')

georgia = input('Georgia > ')
check_capital(georgia, 'atlanta')

hawaii = input('Hawaii > ')
check_capital(hawaii, 'honolulu')

idaho = input('Idaho > ')
check_capital(idaho, 'boise')

illinois = input('Illinois > ')
check_capital(illinois, 'springfield')

indiana = input('Indiana > ')
check_capital(indiana, 'indianapolis')

iowa = input('Iowa > ')
check_capital(iowa, 'des moines')

kansas = input('Kansas > ')
check_capital(kansas, 'topeka')

kentucky = input('Kentucky > ')
check_capital(kentucky, 'frankfort')

louisiana = input('Louisiana > ')
check_capital(louisiana, 'baton rouge')

maine = input('Maine > ')
check_capital(maine, 'augusta')

maryland = input('Maryland > ')
check_capital(maryland, 'annapolis')

massachusetts = input('Massachusetts > ')
check_capital(massachusetts, 'boston')

michigan = input('Michigan > ')
check_capital(michigan, 'lansing')

minnesota = input('Minnesota > ')
check_capital(minnesota, 'st. paul')

mississippi = input('Mississippi > ')
check_capital(mississippi, 'jackson')

missouri = input('Missouri > ')
check_capital(missouri, 'jefferson city')

montana = input('Montana > ')
check_capital(montana, 'helena')

nebraska = input('Nebraska > ')
check_capital(nebraska, 'lincoln')

nevada = input('Nevada > ')
check_capital(nevada, 'carson city')

new_hampshire = input('New Hampshire > ')
check_capital(new_hampshire, 'concord')

new_jersey = input('New Jersey > ')
check_capital(new_jersey, 'trenton')

new_mexico = input('New Mexico > ')
check_capital(new_mexico, 'santa fe')

new_york = input('New York > ')
check_capital(new_york, 'albany')

north_carolina = input('North Carolina > ')
check_capital(north_carolina, 'raleigh')

north_dakota = input('North Dakota > ')
check_capital(north_dakota, 'bismark')

ohio = input('Ohio > ')
check_capital(ohio, 'columbus')

oklahoma = input('Oklahoma > ')
check_capital(oklahoma, 'oklahoma city')

oregon = input('Oregon > ')
check_capital(oregon, 'salem')

pennsylvania = input('Pennsylvania > ')
check_capital(pennsylvania, 'harrisburg')

rhode_island = input('Rhode Island > ')
check_capital(rhode_island, 'providence')

south_carolina = input('South Carolina > ')
check_capital(south_carolina, 'columbia')

south_dakota = input('South Dakota  > ')
check_capital(south_dakota, 'pierre')

tennessee = input('Tennessee > ')
check_capital(tennessee, 'nashville')

texas = input('Texas > ')
check_capital(texas, 'austin')

utah = input('Utah > ')
check_capital(utah, 'salt lake city')

vermont = input('Vermont > ')
check_capital(vermont, 'montpelier')

virginia = input('Virginia > ')
check_capital(virginia, 'richmond')

washington = input('Washington > ')
check_capital(washington, 'olympia')

west_virginia = input('West Virginia > ')
check_capital(west_virginia, 'charleston')

wisconsin = input('Wisconsin > ')
check_capital(wisconsin, 'madison')

wyoming = input('Wyoming > ')
check_capital(wyoming, 'cheyenne')

print('Your score: ' + str(score))
