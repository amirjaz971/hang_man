import random

words=['python','water','pizza','computer','canada','engineer','banana','lion','tiger','cat','food','animal','inception','mushroom','english']
answers=[]
answered_answers=[]
open=True
won_count=0
lost_count=0
while open:
    
    
    print('1.Play')
    print('2.Exit')
    print('3.Results')
    print('4.About game')
    
    choose=input('Choose the action:')
    if choose=='2':
        print('exiting....')
        open=False
    elif choose=='1':
        word_guess=[]
        guessed_letters=[]
        counter=7

        word=list(random.choice(words))

        for i in range(len(word)):
            word_guess.append('-')
           

        while counter>0:
            print(f'you have {counter} attends')
            print(word_guess)
    
    
            if word_guess==word:
                won_count+=1
                answered=''
                for i in word_guess:
                    answered+=i
                    
                answered_answers.append(answered)
                print('You won!')
                break
            letter_guess=input('Guess the letter:')
            
            if len(letter_guess)==1 and letter_guess.isalpha():
             
                
                
             if letter_guess.lower() not in word:
                if letter_guess.lower() not in guessed_letters:
                    
                    print('Wrong guess!')
                    counter-=1
                else:
                    print('You have already chosen this letter!')    
             else:
    
                if letter_guess.lower() in word_guess:
                    print('You have already chosen this letter!')
                else:
            
                    print('Correct guess!')
            
                    index=0
            
        
                    for j in word:
                
                        if j==letter_guess.lower():
                            word_guess[index]=j
                    
                        index+=1    
                    
             guessed_letters.append(letter_guess.lower())
            else:
                print('Enter one letter only!')
                print("Try again")        
                            
        else:
            lost_count+=1
            print('You lost!')

        answer=''
        for i in word:
            answer+=i

        print('The word is',answer)
        answers.append(answer)
    
    elif choose=='3':
        print(f'Answers={answers}')
        print(f'answered answers={answered_answers}')
        print('Wins:',won_count)
        print('Loses:',lost_count)
    
    elif choose=='4':
        print('In Hangman you guess a word letter by letter. There is a maximum of seven wrong guesses. Each wrong guess will incrementally draw a figure of a man being hung.')
    else:
        print('Wrong comand!')