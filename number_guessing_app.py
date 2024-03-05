import random
import sys

lower_number = int(input("Please enter the lower number "))
upper_number = int(input("Please enter the upper number "))

generated_number = random.randint(lower_number, upper_number)

max_attempt = int(3)
count = int(0)
user_input = int(0)

for num in range(lower_number, upper_number + 1):
  user_input = int(input("Please enter a number "))
  count += 1

  if user_input == generated_number:
    print("Congratulations! You have guessed the number")
    sys.exit()
  elif user_input < generated_number:
    print("Your guess is too low")
  elif user_input > generated_number:
    print("Your guess is too high")

    if(count < max_attempt):
      break
      


if count == max_attempt:
  print(f"Sorry, you have reached the maximum number of attempts. The number was {generated_number}")










