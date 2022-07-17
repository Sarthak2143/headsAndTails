# Calculating the number of heads and tails for
# multiple times to study about random.choice for two
# elements and getting the probablity according to
# the result.

from random import choice
# head -> 1
# tail -> 0
num = int(input("Enter the number of rounds: "))
if num%2 != 0:
    print("Choose an even number for fair competition.")
    exit()

heads = 0
tails = 0
data = [0,1]

for i in range(num):
    guess = choice(data)
    if guess == 0:
        tails += 1
    elif guess == 1:
        heads += 1

print(num, "times.")
print(heads, "heads.")
print("Probablity of getting head:", round((heads/num)*100,2))
print(tails, "tails.")        
print("Probablity of getting tail:", round((tails/num)*100,2))

print(int(abs(num/2 - heads)), "times unfair.")
