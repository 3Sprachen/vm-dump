#   Erich Eden
#   SY301
#   Dr. Mayberry
#   oneword.py

from bst import*
import sys
#make a bst of all the bad words
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
count = 0
for line in book:
    for word in line.split():
        str.strip(word)
        if word in bwTree:
            print(word)
            count += 1


book.close()
print("Count: " + str(count))
