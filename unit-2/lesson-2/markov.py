import markovify

text_1 = open("response_1.txt", encoding='utf-8').read()
text_2 = open("response_2.txt", encoding='utf-8').read()

model_1 = markovify.Text(text_1)
model_2 = markovify.Text(text_2)

model_combo = markovify.combine([model_2, model_1]) #Documentation says this method of combining puts more weight on model_1, idk how to makeit equal

paragraph = ""

for i in range(10):
    paragraph += str(model_combo.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")

#Output: Rather, the objection goes, we must say that t is past, present, and future. Turns out, I was barely even there. I should get a sense of such an argument. That is, she will deny that it was up against my ear. For our purposes it is always true that there are some non-present objects. And for another thing, as I haven’t seen my parents in months. All such objects are spread out in space-time. I quit so fast I was too embarrassed to face them. Here is an example of such talk, if there really are no non-present objects? For example, when we say that time really passes.

#Output: The 3D/4D Controversy Bibliography Academic Tools How to cite this entry. I got locked out of nowhere, in, say, 1900. He got on my couch in my dinosaur-print pyjamas. For discussion of the main topics in the same two lines over and over. The question of whether there could not be in the eye. That is, she will deny that it is always true that only present objects exist. Thus, according to this line, there are some non-present objects. It was like a badass. Is such a period, we would not believe this story. For discussion of the display toilets.

#I thought it'd be funny to combine some philosophy blog post about time and more informal sounding FML posts (its some website I bookmarked a long time ago where people post stupid things that happened to them, or that they did to themselves)

#Maybe for unit 2 I could combine formal and informal texts from online? I could compare the writing from bigger social media platforms (idk if the scraping would work on these though), and smaller ones. Or I could find older blog posts/social media and compare it to newer ones?