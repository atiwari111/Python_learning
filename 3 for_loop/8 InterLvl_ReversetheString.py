#reverse the string
word ="python"
revers_word ="" #This will store the reversed result. yet its empty.

for ch in word: #Loop picks one character at a time from "python". Stores it in variable ch
                
    revers_word= ch + revers_word # ch take each letter plus variable reverse_word in each itration

print(revers_word)