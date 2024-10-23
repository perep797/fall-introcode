# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

cla_response = requests.get("https://www.newschool.edu/lang/code-as-a-liberal-art/")
phil_response = requests.get("https://www.newschool.edu/lang/philosophy/")

# print(response.text[:500])

cla_soup_html = BeautifulSoup(cla_response.text, "html.parser")
phil_soup_html = BeautifulSoup(phil_response.text, "html.parser")

cla_soup_text = cla_soup_html.get_text()
phil_soup_text = phil_soup_html.get_text()

cla_data = open('newschool-cla.txt', 'w')
cla_data.write(cla_soup_text)
cla_data.close()

phil_data = open('newschool-phil.txt', 'w')
phil_data.write(phil_soup_text)
phil_data.close()


def getTitles(soupdata):  
  titles = soupdata.select("h2")
  if titles:
    for t in titles:
      print(t.text)
      
print("CLA........")
getTitles(cla_soup_html)
print("Philosophy.........")
getTitles(phil_soup_html)