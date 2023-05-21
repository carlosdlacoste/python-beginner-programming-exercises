total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
if total > 100:
    response = "Give me your money!"
elif total <= 50:
    response = "You are a poor guy, go away!"
else:
    response = "Buy me some coffee you cheap!"

print(response)
