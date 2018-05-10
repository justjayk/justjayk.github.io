import urllib.request as urllib2
from bs4 import BeautifulSoup
import requests

website = "https://www.pokemon.com/us/play-pokemon/leaderboards/op/api/"
r = requests.get(website)
soup = BeautifulSoup(r.text, "json.parser")