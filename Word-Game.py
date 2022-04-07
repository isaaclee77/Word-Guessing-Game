magicword = 'Mississippi'
list_word = list(magicword)
lives = 7
correctletters = []
wrongletters = []
guessedletters = []

for char in magicword:
    correctletters.append('_')

print("".join(correctletters))

while lives > 0:
    print(f'You have {str(lives)} lives remaining')

    guess = input('Pick a letter ')
    
    if len(guess) > 1:              #Guess is a word
        if guess == magicword:
            print('You win')
            break
        else:                         #Guess is incorrect
            lives = lives -1
            print('Incorrect guess')

    else:                             #Guess is a letter
        
        letterinword = False
        for i in range(len(magicword)):
            if guess == magicword[i]:
                letterinword = True
                correctletters[i] = guess

#True if letter is correct
    if letterinword:
        print('That letter is in the word')
    else:
        lives = lives - 1
        print('Wrong Letter')
    print("".join(correctletters))
    guessedletters.append(guess)

if lives == 0:
    print('No more lives')