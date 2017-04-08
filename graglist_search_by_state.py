from bs4 import BeautifulSoup
import requests

def findCities(state_name):
    base_url = "craigslist.org/search/mcy?s=1"
    url = "https://geo.craigslist.org/iso/us/" + str(state_name)
    cities = []
    full_url = []
    source_code = requests.get(url)
    plain_text = source_code.text
    html_contents = BeautifulSoup(str(BeautifulSoup(plain_text).findAll('ul', {'class': 'height6 geo-site-list'})))

    for city in html_contents.findAll('a'):
        cities.append(city.text.replace(" ", "").split("/")[0])
        print(city)
    for city in cities:
        if city=="southwestTX":
            city = "bigbend"
        elif city=="deepeasttexas":
            city = "nacogdoches"
        full_url.append('https://'+city+'.'+base_url)
    return full_url


def search_graglist(url_list):
    for url in url_list:
        page_count = 1
        while(page_count <= 1200):
            try:
                source_code = requests.get(url)
            except:
                page_count += 120
                continue
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text)
            for link in soup.findAll('a', {'class': 'result-title'}):
                title = link.string
                if 'suzuki' in title:
                    newurl = str(url)
                    print("Title:", title)
                    print("Url: ", newurl.replace('/search/mcy?s='+str(page_count),link.get('href')))
            newurl = str(url)
            url = newurl.replace(str(page_count),str(page_count+120))
            page_count += 120

url = findCities("tx")
search_graglist(url)