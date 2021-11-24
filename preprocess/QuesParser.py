# this is the parser used in our model

# steps:
# 1. separate questions into question and statement
# 2. get the question, procude has_q
# 3. get the statement, produce q_rel
# 
# Definitions of has_q and q_rel
# hasQ():
# qRel():
# parser to be finished before finishing the main optimization part


class QueryParser(object):
    def __init__(self):
        return

    def splitQuery(self, question):
        ques = ""
        rel = ""
        return ques, rel

    def getHasQ(self):
        hasQ = {}
        return hasQ

    def getQRel(self):
        qRel = {}
        return qRel

    def getParserResults(self, questions):
        hasQ = []
        qRel = []
        assert (type(questions) is list), "please wrap questions into a list"
        for question in questions:
            print(question)
            ques, rel = self.splitQuery(question)
            print(ques)
            print(rel)
            hasQ = self.getHasQ()
            qRel = self.getQRel()
            break
        return hasQ, qRel


def moduleTest():
    # retrieve the questions
    ROOT = "/ROOT_dir/"
    listText = "tmp/misc/querylist.txt"
    # # load question
    questions = []
    with open(ROOT+listText, 'r') as tmpQ:
        for line in tmpQ:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            questions.append(currentPlace)
    parser = QueryParser()
    parser.getParserResults(questions)
    return


if __name__ == "__main__":
    moduleTest() 
