import random
"""

responses = [
    "Yes",
    "No",
    "Maybe",
    "It is certain",
    "Ask again later",
    "Outlook not so good",
    "Definitely",
    "Cannot predict now",
    "Most likely",
    "Don't count on it"
]

response = random.choice(responses)
print(response)
"""

num = random.randint(1, 9)

if num == 1:
    answer = "Yes."
elif num == 2:
    answer = "No."
elif num == 3:
    answer = "Without a doubt."
elif num == 4:
    answer = "Reply hazy, try again."
elif num == 5:
    answer = "Ask again later."
elif num == 6:
    answer = "Better not tell you now."
elif num == 7:
    answer = "My sources say no."
elif num == 8:
    answer = "Outlook not so good."
elif num == 9:
    answer = "Very doubtful."
else:
    answer = "error"

question = input('Question: ')
print(answer)

