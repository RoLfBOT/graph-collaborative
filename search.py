class searchTrie:
    def __init__(self):
        self.rootDict = {}

    def insert(self, word):
        currentDict = self.rootDict

        for letter in word:
            keys = currentDict.keys()
            if(letter not in keys):
                newDict = {}
                currentDict[letter] = newDict
            currentDict = currentDict[letter]

    def search(self, wordToBeSearched):
        if len(wordToBeSearched) != 0:
            if len(self.rootDict) != 0:
                currentDict = self.rootDict
                flag = 0

                for letter in wordToBeSearched:
                    keys = currentDict.keys()
                    if letter in keys:
                        currentDict = currentDict[letter]
                        flag = 1

                    else:
                        flag = 0
                        break

            else:
                print("Search Trie is empty!\n\n")
        else:
            print("Enter valid search string\n\n")
        return flag


            
