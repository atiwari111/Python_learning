#Replace every white-space character with the charcter *:
import re

txt = "The rain in Spain"
x = re.sub("\s", "*", txt) #where \s is used for space finding
print(x)