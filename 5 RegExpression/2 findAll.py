#Return an empty list if no match was found:

import re

txt = "The is goin to east"

x = re.findall("west",txt)
print(x)