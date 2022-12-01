import re

s = 'wewe , wewew3 , wewe. sdfsd ... ,bruno ,, bruno  bruno'
wordList = re.sub("[^\w]", " ",s).split()
wordListSet = set(wordList)
for i in set(wordListSet):
    print([i, wordList.count(i)])
