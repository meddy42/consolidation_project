import random

#wordbank selection! Guess the sport!
def select_word():
    word_bank = ["golf", "tennis", "soccer", "football", "baseball"]  #wordbank with sports names!
    return random.choice(word_bank)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

# Setting Max attempts to 3
def play_game():
    secret_word = select_word()
    guessed_letters = set()
    guessed_words = set()
    max_attempts = 3
    attempts = 0

#Start playing the game! Players can guess both word and letters!
    print("Hello! You are playing a word guessing game by Medhnaa!")

    while True:
        print("\nWord to guess:", display_word(secret_word, guessed_letters))

        guess = input("Enter a letter or guess the sport: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter!")
            elif guess in secret_word:
                guessed_letters.add(guess)
                print("Correct guess, good job!!")
            else:
                print("Incorrect guess!")
                attempts += 1
        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                print("Congratulations! The word is correct!")
                break
            else:
                print("Incorrect word guess!")
                attempts += 1
                if attempts == max_attempts:
                    print("You've used all your attempts. Game over!")
                    break
        else:
            print("Invalid input. Please enter a single letter or guess the entire word.")

    print("The word was:", secret_word)

#Adding the advanced component- plots
    def plot_scores(scores):
    plt.bar(range(len(scores)), scores.values(), align='center')
    plt.xticks(range(len(scores)), list(scores.keys()))
    plt.xlabel('Players')
    plt.ylabel('Scores')
    plt.title('Final Scores of Word Guessing Game')
    plt.show()
if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    scores = {}
    for i in range(num_players):
        player_name = input(f"Enter the name of player {i+1}: ")
        attempts = play_game()
        scores[player_name] = attempts
    print("Final Scores:", scores)
    plot_scores(scores)
