#BREAK STATEMENT
candies = 10
for i in range(candies):
    print("Giving candy to a friend!")
    if candies - i == 5:
        print("Only 5 candies left stop in distrubution")
        break
print(candies)
