import string
import random

secret = [random.choice('ABCDEF') for i in range(4)]

print(secret)
print("4character code selected from A,B,C,D,E and F. ")
print("I may have repeated some. ")
print("Now try and guess what I chose. ")

guess =[]

while list(guess) != secret:
    guess = input("Enter a guess  :  ").upper()
    if len(guess) != 4:
        continue

    print("You guessed",guess)

    compList = zip(secret,guess)

    correctList =[x for x,y in compList if x == y]

    fewLetters = [min(secret.count(j),guess.count(j)) for j in 'ABCDEF']

    print("Number of correct letters is ",len(correctList))
    print("Number of unused letters is ",sum(fewLetters)- len(correctList))

print("YOU GOT THE ANSWE:", secret)