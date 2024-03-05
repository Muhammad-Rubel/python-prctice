import random

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

selected_word = random.choice(words)
letter_list = list(selected_word)

random.shuffle(letter_list)

suffled_word = ''.join(letter_list)

print(f"Shuffled word is: {suffled_word}")

max_attempt = int(3)
count = int(0)

for attempt in range(max_attempt):
  current_guess = str(input("The word is:- "))
  count += 1

  if current_guess == selected_word:
    print("Congratulatins! Your are right")
    break
  else:
    print("Sorry! Your are wrong")

  if count == max_attempt:
    print("Sorry! you have used all credits")

