from __future__ import unicode_literals

import json
from re import sub

from bs4 import BeautifulSoup
import requests


class AmazonMXScrapper():
    BASE_URL = 'https://www.amazon.com.mx/s/'
    ITEM_DEFINITIONS = [
        {'keywords': ['gtx', '1080'], 'threshold': 10500},
        {'keywords': ['i5', '8600k'], 'threshold': 5000},
        {'keywords': ['i7', '8700k'], 'threshold': 6000},
    ]

    def _match_item(self, item, item_definition):
        has_all_keywords = all(map(lambda k: k in item['title'].lower(), item_definition['keywords']))
        return has_all_keywords and item['price'] <= item_definition['threshold']

    def _parse_price(self, price):
        return float(sub(r'[^\d.]', '', price))

    def _parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='s-item-container'):
            link_element = item.find('a', class_='s-access-detail-page')
            price_element = item.find('span', class_='s-price')
            title_element = item.find('h2', class_='s-access-title')
            if link_element and price_element and title_element:
                yield {
                    'link': link_element['href'],
                    'price': self._parse_price(price_element.text.strip()),
                    'title': title_element.text.strip(),
                }

    def _run_single_item(self, item_definition):
        url = '%s?keywords=%s' % (self.BASE_URL, '+'.join(item_definition['keywords']))
        for item in self._parse(requests.get(url).text):
            if self._match_item(item, item_definition):
                yield item

    def find_items(self):
        for item_definition in self.ITEM_DEFINITIONS:
            for item in self._run_single_item(item_definition):
                yield item

if __name__ == '__main__':
    for item in AmazonMXScrapper().find_items():
        print(json.dumps(item, indent=1))
