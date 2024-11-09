import markovify

text_1 = open("response_1.txt", encoding='utf-8').read()
text_2 = open("response_2.txt", encoding='utf-8').read()
text_3 = open("response_3.txt", encoding='utf-8').read()

model_1 = markovify.Text(text_1)
model_2 = markovify.Text(text_2)
model_3 = markovify.Text(text_3)

model_combo = markovify.combine([model_1, model_2, model_3], [0.6, 0.2, 0.2]) 

list_sentences = []

for i in range(35): #returns 35 sentences instead of 10 for the word count
    one_sentence = str(model_combo.make_short_sentence(120)) #limits to a minimum of 100 characters instead of 80
    if one_sentence not in list_sentences:
        list_sentences.append(one_sentence) #Avoids repeating sentences, some sentences are still similar though

paragraph = " ".join(list_sentences) #Turns list into one string, separated by a space

# print("\n")
# print(paragraph)
# print("\n")

text_file = open('my_essay2.txt', 'w', encoding ='utf-8') #adds generated essay to a file
text_file.write(paragraph)
text_file.close

