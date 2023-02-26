#1
import re

text = "ab"
pattern = r'a(b*)'

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")

#2
import re

text = "abbb"
pattern = r'a(b{2,3})'

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")

#3
import re

text = "hello_world"
pattern = r'[a-z]+_[a-z]+'

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")
#4
import re

text = "HelloWorld"
pattern = r'[A-Z][a-z]+'

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")
#5
import re

text = "aanythingb"
pattern = r'a.+b$'

match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")
#6
import re

text = "Hello, world. How are you?"
pattern = r'[ ,\.]+'

new_text = re.sub(pattern, ':', text)
print(new_text)
#7
import re

text = "snake_case_string"
pattern = r'_(\w)'

new_text = re.sub(pattern, lambda x: x.group(1).upper(), text)
print(new_text)
#8
import re

text = "SplitThisStringAtUpperCaseLetters"
pattern = r'[A-Z]'

result = re.split(pattern, text)
print(result)
#9
import re

text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
pattern = r'(?<!^)(?=[A-Z])'

new_text = re.sub(pattern, ' ', text)
print(new_text)
#10
import re

text = "CamelCaseString"
pattern = r'(?<!^)(?=[A-Z])'

new_text = re.sub(pattern, '_', text).lower()
print(new_text)
