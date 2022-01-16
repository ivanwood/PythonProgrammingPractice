# this program is a beginner level program that builds on the random function. The point of the program is to generate a random number with a message to the user (like a fortune cookie)
import random  # import random

# randint returns a random number between the given range. Add it to the lucky_number variable.
lucky_number = random.randint(1, 100)

# fortune_num is ranged from 1 and 3 to give us 3 different fotunes with the nubers between 1 - 100
fortune_num = random.randint(1, 3)

fortune_text = " "  # this is the fortune text. It is empty to randomize it.

# if statements will generate fortune text strings.
if fortune_num == 1:
    fortune_text = "You will have a great day!"

if fortune_num == 2:
    fortune_text = "Today will be alright!"

if fortune_num == 3:
    fortune_text = "The frog overlords will take over today"

# use f string with variables to generate numbers and strings.
print(f"{fortune_text}! Your lucky number is: {lucky_number}")
