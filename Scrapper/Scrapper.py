from requests import get
from scrapy import Selector
from MyPokedex import *

# Retrieving the site code
url = "https://www.pokemontrash.com/pokedex/liste-pokemon.php#gen7"
response = get(url)
source = None
if response.status_code == 200:
    source = response.text


# Selection of data to scrapped
selector = Selector(text=source)
table = selector.css("div#pokemon > div#section > div#container > div#main > div#content > div > article > "
                         "div#pokedex-list > table.pokedex > tbody > tr").getall()



# For each pokemon which we scraped we add it in bdd
for pokemon in table:
    selector = Selector(text=pokemon)
    number = selector.css("tr > td::text").get()
    name = selector.css("tr > td > strong > a.name::text").get()
    type = selector.css("tr > td > span::text").getall()
    addToBdd(int(number), name, str(type))


# Print in console all the scrapped pokemon
print(getAll())