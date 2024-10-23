# import the requests library
import requests
import os
import io
import random

# import beautifulsoup
from bs4 import BeautifulSoup

response_1 = requests.get("https://genius.com/Taylor-swift-fortnight-lyrics")
response_2 = requests.get("https://www.fmylife.com/Miscellaneous_26")
#With most sites I get weird UnicodeEncodeErrors... :( Even on Wikipedia and Wikihow/some .edu sites

# print(response.text[:500])

if response_1.status_code == 200: #adding error handling so I know what goes wrong
   try:
      response_1_html = BeautifulSoup(response_1.text, "html.parser")

      response_1_text = response_1_html.get_text()

      response_1_data = open('response_3.txt', 'w', encoding ='utf-8') #So the UnicodeEncodingErrors I was getting were mostly bc of the Windows Terminal having a small set of default characters it displays which kept triggering the warning (and also making empty text files), for some reason this fixes it? Perhaps bc it converts it to utf-8 before it starts writing in the file...
      response_1_data.write(response_1_text)

      file_size_1 = os.path.getsize('response_3.txt')

      if (file_size_1 == 0):
         print('File 1 is empty')
         os.remove("response_3.txt") #automatically deletes file if empty
         response_1_data.close()
      else:
         response_1_data.close()

   except UnicodeEncodeError:
          print('File 1 has weird characters')
          os.remove("response_3.txt")
          response_1_data.close()
else:
   print("request_1 unsuccessful, reason:", response_1.status_code)


if response_2.status_code == 200:
   try: 
      response_2_html = BeautifulSoup(response_2.text, "html.parser")

      response_2_text = response_2_html.get_text()

      response_2_data = open('response_2.txt', 'w', encoding='utf-8')
      response_2_data.write(response_2_text)

      file_size_2 = os.path.getsize('response_2.txt')

      if (file_size_2 == 0):
       print('File 2 is empty')
       os.remove("response_2.txt")
       response_2_data.close()
      else:
        response_2_data.close()

   except UnicodeEncodeError:
      print('File 2 has weird characters')
      os.remove("response_2.txt")
      response_2_data.close()
else:
   print("request_2 unsuccessful, reason:", response_2.status_code)

# with io.open('response_1.txt', encoding = "utf8") as response_1_file: 
#     dictionary = list(response_1_file)

# avoid_words = ['the',"The", 'I', "he", "He", "his", "His", "it", "is", "that", "they", 'and', 'of', 'a', 'A', 'at', "as", 'in', 'to', "was", "my", "me", ".", ","] #list of words to avoid 
# other_words = {} 

# for line in dictionary: 
#     for word in line.split(): 
#         if word in avoid_words:
#             continue 
#         if word in other_words:
#             other_words[word] = other_words[word] + 1  

#         else:
#             other_words[word] = 1 
# allPairs = iter((other_words.items())) 
# firstPair = next(allPairs) 

# mostFrequent = firstPair[0] 
# for word in other_words: 
#     if other_words[word] > other_words[mostFrequent]: 
#         mostFrequent = word
# print(mostFrequent, "is the most frequent word in file 1!")

# ten_mostFrequent = []
# list_count = len(ten_mostFrequent)

# while list_count < 10:
#     mostFrequent = firstPair[0]
#     for word in other_words:
#         if other_words[word] > other_words[mostFrequent] and word not in ten_mostFrequent:
#             mostFrequent = word
#     ten_mostFrequent.append(mostFrequent)  
#     list_count = len(ten_mostFrequent)
# print("The 10 most frequent words in file 1 are:", ten_mostFrequent)
# print(random.sample(word))
# time is the most frequent word in file 1!
# The 10 most frequent words in file 1 are: ['time', 'be', 'for', 'there', 'are', 'have', 'this', 'not', 'with', 'on']

# def getTitles(soupdata):  
#  titles = soupdata.select("h2")
#  if titles:
#     for t in titles:
#         print(t.text)
      
# print("Response 1........")
# getTitles(response_1_html)
# print("Response 2.........")
# getTitles(response_2_html)