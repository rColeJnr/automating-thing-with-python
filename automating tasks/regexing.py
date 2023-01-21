import re

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