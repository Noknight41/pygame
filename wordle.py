from termcolor import colored

class game:
    def __init__(self):
        self.live = 5
    
    def convert(self, string):
        list1 = []
        list1[:0] = string
        return list1
    
    def generateWord(self):
        # Randomize word
        word = "hello";
        # Assign 
        self.word = self.convert(word)
    
    def checkAnswer(self, answer):
        ans = self.convert(answer.lower())
        if ans == self.word:
            return [(x, 2) for x in ans]
        else:
            letgo = []
            remain = self.word[:] # Shallow Copy
            for i in ans:
                if i in remain:
                    if ans.index(i) == self.word.index(i):
                        letgo = letgo + [(i, 2)]
                    else:
                        letgo = letgo + [(i, 1)]
                    remain.pop(remain.index(i))
                else:
                    letgo = letgo + [("-", 0)]
            return letgo
    
    def printAnswer(self, result):
        for i in result:
            if i[1] == 0:
                print(i[0])
            elif i[1] == 1:
                print(colored(i[0],'yellow'))
            else:
                print(colored(i[0],'green'))
                  
    def run(self):
        self.generateWord()
        

g = game()
g.run()
g.printAnswer(g.checkAnswer("yolos"))
g.printAnswer(g.checkAnswer("hello"))
    
    