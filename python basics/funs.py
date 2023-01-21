import random

def hello(name):
    print(f'Hello {name}')
    return 23

print(hello("Rick"))

def getAnswer(answerNumber):
    print("fk", end='')
    print('some else')

getAnswer(5)

def spam():
    global eggs 
    eggs = 'spam'

    try:
        return 34/0
    except ZeroDivisionError:
        print('It\'s supposed to be a try catch u dumb ass pl')

spam()
eggs = 'global'
print(eggs)