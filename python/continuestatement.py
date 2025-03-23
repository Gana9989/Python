#Continues statement
candies = 10
for i in range(candies):
    if candies - i == 5:
        print("Only 5 candies left.skipping this turn.")
        continue

    print("Giving a candy to a friend")