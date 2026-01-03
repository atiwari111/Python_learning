#Problem: Given a string, find the first non-repeated character.

word = str("solso")

for i in word:
    if word.count(i)==1:
        
        print("non repeated charcter is :",i)
        break
