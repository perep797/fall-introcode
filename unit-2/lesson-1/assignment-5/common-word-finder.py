import io

with io.open('solaris.txt', encoding = "utf8") as Solaris: #was having trouble opening the .txt file, issues with io.word wrapper or something? Solution online said to import that module, there was also some decoding problem so I had to specify 
    dictionary = list(Solaris) #converts text document into a list

avoid_words = ['the',"The", 'I', "he", "He", "his", "His", "they", 'and', 'of', 'a', 'at', "as", 'in', 'to', "was", "my", "me", ".", ","] #list of words to avoid 
other_words = {} #contains key value pairs in order of appearnace in text, (At:2) where 2 is the value and At is the key

for line in dictionary: #line is necessary for converting the list into a string
    for word in line.split(): #splits the line (or lines) into items
        if word in avoid_words:
            continue #tells loop to ignore items in the avoid_words list
        if word in other_words:
            other_words[word] = other_words[word] + 1 #For every instance of a word from the text that isn't in the avoid_words list, 1 will be added to that word's value 

        else:
            other_words[word] = 1 #If there is only one instance of that word the number will reflect that and the loop ends there

allPairs = iter((other_words.items())) #all pairs is some iteration object? Encoded weirdly, I think it allows the items in other_words to be sorted through
firstPair = next(allPairs) #first pair is the first pair in the list of key value pairs (not invariably, you could probably put firstPair[1] and it would equal the second item)

mostFrequent = firstPair[0] #mostFrequent now equals the the key (and not value, or both) of the first item in the list
for word in other_words: #for a word in the other words dictionary
    if other_words[word] > other_words[mostFrequent]: #if the value of a word is greater than the current most frequent word, it replaces it 
        mostFrequent = word


# I know you can use sorted(), but I wanted to come up with a loop that uses a counter for the ten most common words

# i = 0
# while i <= 10:
#     for word in other_words:
#         if other_words[word] > other_words[mostFrequent]:
#             i = i + 1
#             mostFrequent = word
#             print(mostFrequent)

#Ok for some reason this loop only prints 6 words (from least to most frequent within the top 10 I think), and after that the computer gets stuck? It doesn't finish the loop and I am not sure why. I shortened the list of words to avoid but that wasn't the issue (I thought all the other words after might appear once). The counter works properly when I ask it to print i in the loop, but for some reason it just stops after 6???

# ten_mostFrequent = []
# list_count = len(ten_mostFrequent)
# print(len(ten_mostFrequent))
# while list_count <= 10:
#     for word in other_words:
#         if other_words[word] > other_words[mostFrequent]:
#             mostFrequent = word
#             ten_mostFrequent.append(mostFrequent)

# print(ten_mostFrequent)

#This loop just causes my computer to calculate something indefinitely, it never finishes the loop and prints. It doesn't even return an error or empty line so I can't tell what's wrong. I know that len(ten_mostFrequent) is an integer and starts off at 0, so maybe something goes wrong when things are added to the list? I am not sure....

print(" \n \nThe most frequent word is:", mostFrequent, "\n \nit appears", other_words[mostFrequent], "times!!!")
#result: The most frequent word is: had, it appears 31 times!!!