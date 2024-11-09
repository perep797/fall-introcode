# import the requests library
import requests
import os

# import beautifulsoup
from bs4 import BeautifulSoup

headers = {'User Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36'} #So the browser doesn't think I'm a bot, I checked what request headers I was sending. A lot of sites will still return a 403 or 400 error. I think they check for cookies and it seemed like too much of a pain to mess with that stuff, but the scraper works on more of them. The user agent may need to be changed depending on what computer is running this program.

response_1 = requests.get("https://www.bbc.com/news/articles/cj0jq134y91o") #Headers here return a 400 error code (malformed request), so I had to remove it
response_2 = requests.get("https://archiveofourown.org/works/60313249", headers=headers)
response_3 = requests.get("https://archiveofourown.org/works/59026102/chapters/150478603", headers=headers)


if response_1.status_code == 200: #Adding error handling so I know what goes wrong, checks for a successful request
   try:
      response_1_html = BeautifulSoup(response_1.text, "html.parser")
      response_1_text = response_1_html.find_all('div', {"data-component": "text-block"}) #targets specific divs which hold main article text, otherwise other subtitles are included in the output. Luckily, all these divs mostly have p tags within them.

      response_1_data = open('response_1.txt', 'w', encoding ='utf-8')
      
      for div in response_1_text: 
         response_1_data.write(div.get_text())
         response_1_data.write("\n") #Uses .get_text to convert results into a string, otherwise I get a TypeError
      
      response_1_data.close() #File has to be closed here, otherwise I get a PermissionError during the checks below

      file_size_1 = os.path.getsize('response_1.txt')

      if (file_size_1 == 0):
         print('File 1 is empty')
         os.remove("response_1.txt") #automatically deletes file if empty
         response_1_data.close()
      else:
         response_1_data.close()

   except UnicodeEncodeError:
          print('File 1 has weird characters') #for encoding errors, I have also gotten a few AssertionErrors but only in super specific cases where the txt file already exists
          os.remove("response_1.txt")
          response_1_data.close()
else:
   print("request_1 unsuccessful, reason:", response_1.status_code)


if response_2.status_code == 200:
   try: 
      response_2_html = BeautifulSoup(response_2.text, "html.parser")

      try: 
         response_2_div = response_2_html.find('div', {"class": "userstuff"}) #This is website dependent, but for AO3 the main div which holds text is called userstuff or userstuff module; this checks for both possible names. If I don't target the div other hidden text is returned, strangely enough.
      except response_2_html == None: 
         response_2_div = response_1_html.find('div', {'class': 'userstuff module'})

      response_2_text = response_2_div.find_all('p') #All p tags within the main text div
      response_2_data = open('response_2.txt', 'w', encoding='utf-8')
      
      for p in response_2_text:
         response_2_data.write(p.get_text())
         response_2_data.write("\n")

      response_2_data.close()

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

if response_3.status_code == 200:
   try: 
      response_3_html = BeautifulSoup(response_3.text, "html.parser")

      try: 
         response_3_div = response_3_html.find('div', {"class": "userstuff"}) #This is website dependent, but for AO3 the main div which holds text is called userstuff or userstuff module; this checks for both possible names. If I don't target the div other hidden text is returned, strangely enough.
      except response_3_html == None: 
         response_3_div = response_3_html.find('div', {'class': 'userstuff module'})

      response_3_text = response_3_div.find_all('p') #All p tags within the main text div
      response_3_data = open('response_3.txt', 'w', encoding='utf-8')
      
      for p in response_3_text:
         response_3_data.write(p.get_text())
         response_3_data.write("\n")

      response_3_data.close()

      file_size_3 = os.path.getsize('response_3.txt')

      if (file_size_3 == 0):
         print('File 3 is empty')
         os.remove("response_3.txt")
         response_3_data.close()
      else:
         response_3_data.close()

   except UnicodeEncodeError:
      print('File 3 has weird characters')
      os.remove("response_3.txt")
      response_3_data.close()
else:
   print("request_3 unsuccessful, reason:", response_3.status_code)

      
