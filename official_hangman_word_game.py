import random
position = []
bad_suggestion = 10
secret_word_list = []
view_word_list = []
words_list = ["bycycle", "blanket", "refrigerator", "biology", "microscope",
              "triangle", "computer", "cucumbers", "steak", "truck"]


def random_word():                            # select random word
    secret_word = random.choice(words_list)
    return secret_word


def format_secret_word():    # format random word into a secret-view word
    word = secret_word
    hidden_letter = ""
    for i in range(1, len(word)-1):
        hidden_letter += "_"
    view_word = word[0] + hidden_letter + word[len(word) - 1]
    return view_word


player_name = input("Please, enter your name: ")
print(f"Hi {player_name}, let`s play Hangman!!!!!!")   # player name can contain any characters

secret_word = random_word()
view_word = format_secret_word()


print(f"The word that you have to guess is {view_word} !")
for i in secret_word:                            # convert word in list
    secret_word_list.append(i)
for i in view_word:
    view_word_list.append(i)


while view_word != secret_word:
    suggestion = input("Please, make a suggestion for letter: ").lower()
    if suggestion.isalpha() is True and len(suggestion) == 1:
        if suggestion in secret_word:
            for i in range(len(secret_word_list)):
                if suggestion == secret_word_list[i]:
                    position.append(i)

            for i in position:
                view_word_list.pop(i)
                view_word_list.insert(i, suggestion)
            whole_word = "".join(view_word_list)
            view_word = whole_word
            position.clear()
            print(f"Good job ! Keep going : {view_word}")
        else:
            bad_suggestion -= 1
            if bad_suggestion == 0:
                print(f"Ooooooh No, you lost the game , the word was - {secret_word} !!!!")
                break
            elif 1 <= bad_suggestion <= 3:
                print(f"Be careful , you have only {bad_suggestion} tries!")
            else:
                print(f"Wrong suggestions that last : {bad_suggestion}")
    else:
        print("You have to write a letter and it should be only one per suggestion !")


if view_word == secret_word:
    print(f"Congratulations !!!!!! YOU WIN !!!!!!!")
