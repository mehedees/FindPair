
class PairFinder:
    def __init__(self, inputArray, target):
        self.inputArray = inputArray
        self.target = target
        self.items = self.inputArray[1:-1]  # stripping square brackets from both end
        self.items = self.items.split(', ')  # getting a string list of the numbers
        self.items = list(map(int, self.items))  # converting to a num string
        self.resultList = []
        
    def findPairs(self):
        for x in self.items:
            for y in self.items:
                diff = x - y
                if diff == target:
                    self.resultList.append([x, y])

        self.resultString = '{0} -> '.format(len(self.resultList))
        for it, pair in enumerate(self.resultList):
            if it == len(self.resultList) - 1:
                self.resultString += '{}'.format(pair)
            else:
                self.resultString += '{}, '.format(pair)
        print(self.resultString)
        



inputArray = input()
target = int(input())
p = PairFinder(inputArray, target)
p.findPairs()




