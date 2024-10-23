import random
import pprint


# # STEP 1 
# # Open a text file (of your choosing), set all characters to lower class, and split up each word to make an array of the entire text, print the text variable to see what it looks like and to make sure it work
# # # # //////////////////////////////////////////////////
text = open("4-text-small.txt").read().lower().split()

# # print(text)
# # # # //////////////////////////////////////////////////


# STEP 2 
# make an empty dictionary, all the words and their next possible words will go in here
# # # //////////////////////////////////////////////////
markovDictionary = {}	
# # # # //////////////////////////////////////////////////



# # STEP 5
# # this function is called on below in the for loop for our text
# # this function is called getIndexForWord, and it takes two arguments, which we pass in below in the for loop
# # # //////////////////////////////////////////////////
def getIndexForWord(word, nextPossibleWordsAmount): 
    # # receive the current word, and the amount of next possible words
    indexes = []

    # # for each word (w) in the text, assign it to a number
    for i, w in enumerate(text):
        # # check if it (w) is equal to the word passed in from our for loop
        if w == word:
            # # if it is equal, append the index (assigned number) of this word to the indexes list
            indexes.append(i)
    
    # # return the indexes of the next possible words
    return indexes[nextPossibleWordsAmount]
# # # //////////////////////////////////////////////////



# # # //////////////////////////////////////////////////
# # # //////////////////////////////////////////////////
# # STEP 3 add words to the dictionary 
# # each word in the text will become a key, 
# # the value for each key will be set as a list of the next possible words

totalWords = len(text)
for word in text:
    # # if the word is not yet in the dictionary, 
    # # add it as a key value pair
    # # the word is the key, the value is a list of next possible words
    # # to start we set the list as empty, words will be added to it later
    if not word in markovDictionary:
        markovDictionary[word] = []

    # # as we loop through the text
    # # we can get the position of the word by using .index()
    # # if the position is more than the amount of totalWords
    # # so the index of "To" is 0, "be" is 1, "or" is 2 "not" is 3 and so on...
    # # stop the loop!
    if text.index(word) == (totalWords - 1): break


    # # STEP 4 add the possible words list to the each word
    # # get the amount of possible words for each word
    # # for example, for the word be, the key-value pair looks like this:
    # # {'be', ['or', 'that]} so the amount of next possible words is equal to 2

    nextPossibleWordsAmount = len(markovDictionary[word]) 
    textIndex = getIndexForWord(word, nextPossibleWordsAmount)
    if word == text[(totalWords - 1)]:
        continue
    else:
        nextWord = text[textIndex + 1]
        markovDictionary[word].append(nextWord)


# use pretty print library to see dictionary more clearly
pprint.pprint(markovDictionary)   
# # //////////////////////////////////////////////////







# # //////////////////////////////////////////////////
# #  STEP 6, first make sure STEPS 1-5 are working, you should be able to print the markovdictionary and see a list of all of the words with their possible next words
# #  now we can GENERATE THE TEXT by CHOOSING A RANDOM WORD from THE POSSIBLE WORDS LIST FOR 10 WORDS at a time

# # set the current word to a placeholder, the first word in the text
chosenWord = random.choice(text)

generatedText = []

# # generate a 10 word sentence
for i in range(10):
    if chosenWord == text[(totalWords - 1)]:
        chosenWord = text[0]
    else:
        generatedText.append(chosenWord)
        nextWord = random.choice(markovDictionary[chosenWord])
        chosenWord = nextWord

# # join the generatedText array into a printable sentence
finalPrintOut = " ".join(generatedText)

print("\n\n\n")
print(finalPrintOut)
print("\n\n\n")
