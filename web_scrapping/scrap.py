from bs4 import BeautifulSoup
import requests
import csv

"""
Web Scrapping Example: List of Top rated bollwood film on IMDB and created CSV file of film(name, rate, and starring) 
"""
url= "https://www.imdb.com/india/top-rated-indian-movies/"
response= requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

names = soup.find_all('td', {'class':'titleColumn'})
film_name=[]
film_actor=[]
for name in names:
    film_name.append(name.a.text)
    film_actor.append(name.a['title'])



names = soup.find_all('td', {'class':'imdbRating'})
film_ratng=[]
for name in names:
    film_ratng.append(name.strong.text)

    
data= zip(film_name, film_ratng, film_actor)
# for x in data:
#     print(x)


filename = 'web_scrapping/top250bollywood.csv'
with open(filename, 'w') as f: 
    csv_out=csv.writer(f)
    csv_out.writerow(['name','rating', 'actor'])
    for row in data:
        csv_out.writerow(row)

    print("done")