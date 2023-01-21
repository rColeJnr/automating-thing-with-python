#! python3

import pyperclip

# TODO: sepaate the lines

text = pyperclip.paste()

lines = text.split('\n')
for l in range(len(lines)):
    lines[l] = '* ' + lines[l]

text = '\n'.join(lines)
pyperclip.copy(text)
print(pyperclip.paste())

