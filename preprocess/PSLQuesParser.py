# this file rephase how the old pslqa model process the question


def getAnswersByType(question, answersByType):
    question = question.lower()
    colorQs = {'what color', 'what is the color of'}
    for colorQ in colorQs:
        if question.startswith(colorQ):
            return answersByType['color']
    locQs = {'where'}
    for locQ in locQs:
        if question.startswith(locQ):
            answers = answersByType['location']
            answers.extend(answersByType['entity'])
            answers.extend(answersByType['animal'])
            return answers
    humanQs = {'who'}
    for humanQ in humanQs:
        if question.startswith(humanQ):
            answers = answersByType['human']
            answers.extend(answersByType['entity'])
            answers.extend(answersByType['animal'])
            return answers
    return None


def parseQuestion(questions):
    for question in questions:
        if question.startswith("how ") \
            or question.startswith("can you") \
            or question.startswith("could ") \
            or question.startswith("has ") \
            or question.startswith("none of the above "):
            continue
        # next classify questions into 3 types (color, location, people)
        # for SN, since the question is simple, he directly use the hard 
        # code to parse the question


        # answers = getAnswersByType(question, answersByType)
        # reducePossibleAnswers()


if __name__ == "__main__":
    questions = ['how are you']
    parseQuestion(questions)    
