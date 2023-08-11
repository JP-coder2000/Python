height = int(input('Whats your height? (in cm WITHOUT THE .) '))
credits = float(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
    answer = "Enjoy the ride!"
elif height >= 137 and credits < 10:
    answer = "You don't have enough credits"
elif height < 137 and credits >= 10:
    answer = "You are not tall enough to ride"
else:
    answer = "Your are neither tall enough or have the credits necessary"

print(answer)