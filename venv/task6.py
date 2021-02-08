wrd = input("Please enter a word")
rvs = wrd[: :-1]
print(rvs)
if wrd ==rvs:
    print("This word is a palindrone")
else:
    print("This word is not a palindrone")