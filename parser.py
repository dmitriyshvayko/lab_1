from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mp_mv250"

pr = requests.get(url)

soup = BeautifulSoup(pr.text, "html.parser")


sp_1= []
sp_2= []


per_1 =  soup.findAll('td', class_='titleColumn')

for tag in per_1:
    a = tag.findAll('a')
    for i in a:
        k = i.get_text()
        sp_1.append(k)


per_2 =  soup.findAll('td', class_='ratingColumn imdbRating')

for data in per_2: 
    if data.find('strong'): 
        description = data.get_text('|', strip=True)
        sp_2.append(description)


sl = dict(zip(sp_1, sp_2))

print(sl)   
