# adapted from https://www.decontextualize.com/teaching/rwet/n-grams-and-markov-chains/

# WE ALREADY WROTE CODE FOR FINDING OUT HOW MANY TIMES A WORD APPEARS IN A TEXT FILE!


### HERE IS KIRSTEN'S SOLUTION, WITH SIGRID'S SCRAPED TEXT FILE:::::::
# create file variable (this file should already have text inside of it)
file = open("small_text.txt" , "r")
# create empty dictionary


word_counts = {}

for line in file:
    # for each word in each line
    # .split() very helpful! 
    # it takes a string and splits it into more substrings! 
    # so splits a sentence into its individual words essentially
    for word in line.split():
    #### if word is in word_counts, add 1 to frequency
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        
        ##### else word is not in word_counts, add to word count as only 1
        else:
            word_counts[word] = 1 

   
# print(word_counts)


# # HERE IS BEIMNET'S SOLUTION FOR ORDERING THE DICTIONARY:::::
# sorted_keys = sorted(word_counts, key=word_counts.get)
# sorted_keys.reverse()
# print(sorted_keys)

# # AND HER SOLUTION FOR SKIPPING OVER CERTAIN WORDS::::::::
# skip = ['THE', 'AND']

# filtered_words = []

# for word in sorted_keys: # Iterate through sorted keys
#     if word in skip: # Check if word exists in skip list
#         continue # If it exists, continue
#     else:
#         filtered_words.append(word) # If it doesn't exist, add to list

# print(filtered_words)
