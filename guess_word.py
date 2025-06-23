import random

word_bank = ["Instagram" , "Whatsapp" , "Linkdin" , "Snapchat" , "Facebook" , "CandyCrush"]

word = random.choice(word_bank)

guessWord = ["_"] * len(word)

attempts = 10

while attempts > 0:
    print("\n Current Word : " + " " .join(guessWord))

    guess = input("Guess a letter : ")

    if guess in word:
        for i in range(len(word)):
            guessWord[i] = guess
        print("Great Guess!")

    else:
        attempts -= 1
        print("Wrong Guess! Attempts left : " + str(attempts))   
        
    if "_" not in guessWord:
     print("\n Congratulations!! You guessed the word : " + word)
     break

    else:
     print("\n You \'ve run out of attempts! The Word was : " + word)
