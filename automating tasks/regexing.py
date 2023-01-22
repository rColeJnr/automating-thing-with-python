import re

def allThis():
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

    mo = phoneNumRegex.search('My number is 415-444-4545.')
    print('Phone number found: '+ mo.group())


    phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

    mo = phoneNumRegex.search('My number is 415-444-4545.')
    print('Phone number found: '+ mo.group(1))
    print('Phone number found: '+ mo.group(2))

    areaCode, mainNumber = mo.groups()

    phoneNumRegex = re.compile(r'(\(\d{3})\)-(\d{3}-\d{4})')

    mo = phoneNumRegex.search('My number is (415)-444-4545.')
    print(f'Phone number found: {mo.groups()}')

    areaCode, mainNumber = mo.groups()

    # Pipe | used to match expressiong,
    pipeRegex = re.compile(r'Batman|Tina Fey')
    mo1 = pipeRegex.search('Batman and Tina Fey bitch.')
    print(mo1.group())

    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo = batRegex.search('Batman or Batmobile')
    print(mo.group())

    batRegex = re.compile(r'Bat(wo)?man')
    #will match batman or batwoman

    batRegex = re.compile(r'Bat(wo)*man')
    mo3 = batRegex.search('The Adventures of Batwowowowoman')
    # it matches batman, woman and batwowowowman

    # Match one or more with plus
    batRegex = re.compile((r'Bat(wo)+man'))
    mo1 = batRegex.search('The Adventures of Batwoman')

#Matching specific repetitions with curly brackets
''' (Ha){3} is the same as (ha)(ha)(ha)
    (ha){3,5} same as ha ah (ah) or (ha)(ha)(ha)(ha)(ha)
    it matches 3 to 5 ha, doesnt match ha
'''

# Greedy and nongreedy matching
'''
    Python’s regular expressions are greedy by default, which means that in
ambiguous situations they will match the longest string possible. The non-
greedy version of the curly brackets, which matches the shortest string pos-
sible, has the closing curly bracket followed by a question mark.
'''

def greedyNonGreedy():
    greedyRegex = re.compile(r'(Ha){3,5}')
    mo1 = greedyRegex.search("HaHaHaHa ha hahahahaha")
    print(mo1.group())

    nonGreddy = re.compile(r'(Ha){3,5}?')
    mo2 = nonGreddy.search('HaHaHaHaHa')
    print(mo2.group())


'''
    While search() will return a match object of the first matched text
    finall() will return the string of every match
    '''
def findAll():
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.findall("cell: 435-894-4333 and work: 344-948-7833")
    print(mo)

'''
To summarize what the findall() method returns, remember the
following:
When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d,
the method findall() returns a list of string matches, such as ['415-555-
9999', '212-555-0000'].
When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\
d\d\d), the method findall() returns a list of tuples of strings (one string
for each group), such as [('415', '555', '1122'), ('212', '555', '0000')].
'''

#Character Classes
'''

    /d any numeric 0-9
    /D any character that isnot a numeric from 0-9

    \w Any letter, numeric digit, or the underscore character
        (matching word characters)
    /W any character that is not a letter, num or underscore
    \s Any space, tab or newLine
    \S any char that is not space, tab or \n
'''
# Making ur own classes
# You can define ur own char class using []

def vowels():
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    mo = vowelRegex.findall('Roboco eats boby food, BABY FOOD')
    print(mo)

    ''' You can also include ranges of chars by using hyphen '''
    rangeRegex = re.compile(r'a-zA-Zo-9')

    ''' ^ negative character class.
        matches all chars that are not in the char class
    '''

    consonatRegex = re.compile(r'[^aeiouAEIOU]')
    mo = consonatRegex.findall('Roboco eats boby food, BABY FOOD')
    print(mo)

vowels()

#The Caret and dollar sign chars
''' ^ at the start of regex indicates that a match must occur at the beggining
of the searched text. Likewise, $ indicates that the string must end with
this regex pattern. and you use ^ $ to indicate that the entire string must
match the regex
'''

#The Wildcard char and Don-Star
''' . Will match amy char except for a newline'''
def wildcard():
    atRegex = re.compile(r'.at')
    print(atRegex.findall('The cat and the hat at the sat dancat'))
    # matches cat, hat, at, sat, cat

    nameRegex= re.compile(r'First name: (.*) Last name: (.*)')
    mo = nameRegex.findall('First name: Al Last name: Alshujean')
    print(mo)
    ''' The dot-star uses greedy mode: It will always try to match as much text as
possible. To match any and all text in a nongreedy fashion, use the dot, star,
and question mark (.*?). Like with curly brackets, the question mark tells
Python to match in a nongreedy way.
'''
    newlineRegex = re.compile('.*', re.DOTALL)
    # matches everything including \n and the text that follows 

#Review of Regex symbols
''' 
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character,
respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.
'''

# Case insensitive matching
''' pass @param re.IGNORECASE or re.I '''

# replacing strings
'''
The sub() method for Regex objects is
passed two arguments. The first argument is a string to replace any matches.
The second is the string for the regular expression. The sub() method returns
a string with the substitutions applied.
'''
def subbing():
    nameRegex = re.compile(r'Rick \w+')
    mo = nameRegex.sub("Awesome", 'Rick is awesomingly going for his future')
    print(mo)

    namesRegex = re.compile(r'Rick (\w)\w+', re.I)
    mo = namesRegex.sub(r"\1***", 'Rick rick is Rick awesomingly going for his rick future')
    print(mo)

subbing()