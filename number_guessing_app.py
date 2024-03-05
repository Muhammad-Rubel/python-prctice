import random
import sys

lower_num = int(input("Enter the lower number: "))
upper_num = int(input("Enter the upper number: "))

generated_num = random.randint(lower_num, upper_num)

max_attempt = int(3)
count = int(0)

for attempt in range(max_attempt):
  current_guess = int(input("Guess the number: "))
  count +=1

  if current_guess == generated_num:
    print("Congratulations! You have guessed the number")
    sys.exit()
  elif current_guess < generated_num:
    print("Your guess is too low")
  elif current_guess > generated_num:
    print("Your guess is too high")


if count == max_attempt:
  print(f"Sorry, you have reached the maximum number of attempts. The number was {generated_num}")