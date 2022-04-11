from bs4 import BeautifulSoup
import requests as req
import re


class url_html_parser:
    def __init__(self):
        resp = req.get("https://www.mirea.ru/schedule")
        self.soup = BeautifulSoup(resp.text, 'html.parser')

    def get_url_by_name(self, institute, course):
        url = self.soup.find('a', href=re.compile(f".*({institute}_{course}).*")).get('href')
        return url
