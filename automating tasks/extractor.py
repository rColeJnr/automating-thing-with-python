import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)?         # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)          # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ #username
    @ #symbol
    [a-zA-Z0-9.-]+ #domain
    (\.[a-zA-Z]{2,4}) #dot.something
)''', re.VERBOSE)

text = str(pyperclip.paste())
print(text)
matches = []
for g in phoneRegex.findall(text):
    phoneNum = '_'.join([g[1], g[3], g[5]])
    if g[8] != '':
        phoneNum += 'x' + g[8]
    matches.append(phoneNum)    

for g in emailRegex.findall(text):
    matches.append(g[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No matchs')