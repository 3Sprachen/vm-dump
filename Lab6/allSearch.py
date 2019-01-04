#   Erich Eden
#   SY301
#   Dr. Mayberry
#   allSearch.py

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
#check each word from each book to see if it's in the tree
for s in range (1, len(sys.argv)):
    book = open(sys.argv[s], 'r')
    wordlist = []
    count = 0
    for line in book:
        for word in line.split():
            str.strip(word)
            wordlist.append(word)

    for i in range(len(wordlist)):
        phrase = str.strip(wordlist[i])
        if phrase in bwTree:

            count += 1
        for j in range (1, 4):
            t = i + j
            if (t >= len(wordlist)):
                t = (len(wordlist) - 1)
            phrase = phrase + " " + str.strip(wordlist[t])

            if phrase in bwTree:

                count += 1



    book.close()
    print(str(sys.argv[s]) + " Count: " + str(count))
