from requests import get
from scrapy import Selector
from MyPokedex import *

url = "https://www.pokemontrash.com/pokedex/liste-pokemon.php#gen7"
response = get(url)
source = None
if response.status_code == 200:
    source = response.text


selector = Selector(text=source)
table = selector.css("div#pokemon > div#section > div#container > div#main > div#content > div > article > "
                         "div#pokedex-list > table.pokedex > tbody > tr").getall()


for pokemon in table:
    selector = Selector(text=pokemon)
    number = selector.css("tr > td::text").get()
    name = selector.css("tr > td > strong > a.name::text").get()
    type = selector.css("tr > td > span::text").getall()
    addToBdd(int(number), name, str(type))

print(getAll())