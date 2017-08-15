print('State abbreviations')
print('You\'ll be given a state.')
print('Choose the correct postal abbreviation for the state. ')

print('Here we go: '+ '\n'*3)

def check_abbr (user_abbr, answer_abbr):
    global score
    user_guessing = True
    guesses = 0
    while user_guessing and guesses <2:  
      if user_abbr.upper() == answer_abbr.upper():
        print('Correct you are!')
        score = score +1
        user_guessing = False
      else:
        if guesses < 1:
          user_abbr = input('Oh noes. Try again.')
        guesses = guesses + 1
    if guesses == 2:
      print('The correct abbreviation is ' + answer_abbr)

score = 0


alabama = input('What is the abbreviation for Alabama?  \n \
A) Ala. B) AL C) Bama D) Aa \n')
check_abbr(alabama, 'B')

alaska = input('What is the abbreviation for Alaska?  \n \
A) Aa B) AL C) AK D) AS \n')
check_abbr(alaska, 'C')

arizona = input('What is the abbreviation for Arizona?  \n \
A) AR B) Zone C) AN D) AZ \n')
check_abbr(arizona, 'D')

arkansas = input('What is the abbreviation for Arkansas?  \n \
A) Ark B) AK C) AR D) AS \n')
check_abbr(arkansas, 'C')


##continue. mix up states or mention that by not mixing them up, could
##users memorize? another need for loops and random


print('Your score: ' + str(score))