from bs4 import BeautifulSoup
import requests as req
import re


class url_html_parser:
    def __init__(self):
        resp = req.get("https://www.mirea.ru/schedule")
        self.soup = BeautifulSoup(resp.text, 'html.parser')

    def get_url_by_name(self, institute, course):
        root = self.soup.find('a', text=institute).parent.parent.find_all_next('div')[1]
        root = root.find('b', text='Расписание занятий:').parent
        root = root.find_next_sibling('div')
        while root.find('b', text='Расписание зачетно-экзаменационной сессии:') is None:
            root = root.find_next_sibling('div')
            if (root.find('div',
                          text='\n											    %d курс'
                               '											' % course) is not None):
                return root.find('a').get('href')


        # divs = root.find_all('a', href=re.compile('.*(^((?!экз).)*$).*'))
        # for el in divs:
        #     pre_root = el.find('div',
        #                        text='\n											    %d курс'
        #                             '											' % course)
        #     if pre_root is not None:
        #         root = pre_root
        # root = BeautifulSoup(root, 'html.parser')
        # url = root.parent.parent.get('href')
        # return url
