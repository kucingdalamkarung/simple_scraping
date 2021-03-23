from bs4 import BeautifulSoup
from network import Network


class CategoryScraper:
    def __init__(self, baseUrl):
        self._network = Network(baseUrl)

    def scrape(self):
        statusCode, content = self._network.request()
        furnitures = []
        if statusCode != 200:
            return None

        bs = BeautifulSoup(content, 'html.parser')
        h2_list = bs.find_all('h2')

        for h2 in h2_list:
            span = h2.find('span')
            furniture = span.find('strong').get_text() if span.find(
                'strong') != None else span.get_text()
            furnitures.append(furniture)

        for f in furnitures:
            print(f)
