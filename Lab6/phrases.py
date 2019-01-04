#   Erich Eden
#   SY301
#   Dr. Mayberry
#   oneword.py

from bst import*
import sys

#make a bst of all the bad words and phrases
bwTree = TreeSet()

bw = open('badWords.txt', 'r')

badWord = str.strip(bw.readline())
while badWord:
    bwTree.insert(badWord)
    badWord = str.strip(bw.readline())
bw.close()
#######################
#check each word from the book to see if it's in the tree
book = open(sys.argv[1], 'r')
wordlist = []
count = 0
for line in book:
    for word in line.split():
        str.strip(word)
        wordlist.append(word)

for i in range(len(wordlist)):
    phrase = str.strip(wordlist[i])
    if phrase in bwTree:
        print(phrase)
        count += 1
    for j in range (1, 4):
        t = i + j
        if (t >= len(wordlist)):
            t = (len(wordlist) - 1)
        phrase = phrase + " " + str.strip(wordlist[t])

        if phrase in bwTree:
            print(phrase)
            count += 1



book.close()
print("Count: " + str(count))
