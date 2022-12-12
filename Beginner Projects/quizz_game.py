def game_start():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guess)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print(f"Your score is: {score}%")

def continue_playing():
    response = input("Play again? (yes or no) ")
    response = response.upper()
    if response == 'YES':
        return True
    else:
        return False

questions = {
"Quanto é meia dúzia? ": "A",
"Que campeão de lol é um rato? ": "C",
"Kapimba? ": "B",
"Resposta para o universo? ": "D",
"Melhor MMORPG? ": "B"
}

options = [["A. 6", "B. 12", "C. 39", "D. Sei lá porra"],
["A. Darius", "B. Karthus", "C. TEEMO", "D. Twitch gigachad"],
["A. Piu", "B. Kapomba", "C. Jurema", "D. Cachorro"],
["A. E = mc²", "B. Sei nem que dia é hoje", "C. Deus que fez", "D. 42"],
["A. WoW OMEGALUL", "B. FFXIV", "C. Priston", "D. O que é MMORPG?"]]

game_start()

while continue_playing():
    game_start()

print("Game ended!")