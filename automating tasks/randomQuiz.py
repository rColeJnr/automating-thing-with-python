import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 
    'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
    'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 
    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 
    'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 
    'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
    'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 
    'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 
    'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 
    'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}
capitalsItems = list(capitals.items())
states = list(capitals.keys())
#Generate 35 quiz files.
for q in range(35):
    #Create the quiz and answer key files.
    qFile = open('capitalsquiz%s.txt' % (q + 1), 'w')
    answerkeyFile = open('capitalsquiz_answers%s.txt' % (q + 1), 'w')

    #Write out the header for the quiz.
    qFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    qFile.write((' '* 20) + 'State Capitals Quiz (Form %s)' % (q+1))
    qFile.write('\n\n')

    #Shuffle the order of the states.
    random.shuffle(states)

    for i in range(50):
        correctAnswer = capitals[states[i]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #remove the right answer
        wrongAnswers = random.sample(wrongAnswers, 3) # pick 3 random ones

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #Write the questionand answer options to the file
        qFile.write('%s. What is the capital of %s?\n\n' % (i+1, states[i]))
        for a in range(4):
            qFile.write('   %s. %s\n' % ('ABCD'[a], answerOptions[a]))
            qFile.write('\n')

        # write out the answer key to a file.
        answerkeyFile.write('%s. %s\n' % (i+1, 'ABCD'[answerOptions.index(correctAnswer)]))
    qFile.close()
    answerkeyFile.close()
