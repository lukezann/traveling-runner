from bs4 import BeautifulSoup
import pandas as pd
import requests

names = []
hometowns = []

# get request to roster page
html = requests.get('https://ephsports.williams.edu/sports/mens-cross-country/roster').text
soup = BeautifulSoup(html, 'html.parser')

# find all athletes' data contained in lists
athletes = soup.find_all('li', class_='sidearm-roster-player')

# iterate thru and extract relevant info
for ath in athletes:
    name = ath.find('div', class_='sidearm-roster-player-name')
    name = name.find('a').text.strip()
    names.append(name)

    hometown = ath.find('span', class_='sidearm-roster-player-hometown').text.strip()
    hometowns.append(hometown)

# create pandas DataFrame and export to csv
data = {'name' : names,
        'hometown' : hometowns};

df = pd.DataFrame(data)
df.to_csv('hometowns.csv')