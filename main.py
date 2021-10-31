import datetime
import json
import random

class Result:
    def __init__(self, player_name, attempts, secret, date, wrong_guesses):
        self.player_name = player_name
        self.attempts = attempts
        self.secret = secret
        self.date = date
        self.wrong_guesses = wrong_guesses

name = input("Please enter your name: ")
secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

for score_dict in new_score_list:
    print(str("User {0} took {1} attempts with the secret number {2} on {3} \nAll the wrong guesses: {4}".format(score_dict["name"], score_dict["attempts"], score_dict.get("secret"), score_dict.get("date"), score_dict["wrong_guesses"])))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    if guess == secret:
        score_list.append(Result(player_name=name, attempts=attempts, secret=secret, date=str(datetime.datetime.now()), wrong_guesses=wrong_guesses).__dict__)
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guesses.append(guess)
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guesses.append(guess)
