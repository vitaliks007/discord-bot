import os

from dao.schedule_url_dao import schedule_url_dao
from utils.url_html_parser import url_html_parser
import wget


class schedule_url_service:
    def __init__(self):
        self.su_dao = schedule_url_dao('127.0.0.1', 'root', 'qwerty')
        self.uh_parser = url_html_parser()

    def disconnect(self):
        self.su_dao.disconnect()

    def add_url_by_name(self, institute, course):
        url = self.uh_parser.get_url_by_name(institute, course)
        self.su_dao.add_row(url, institute, course)

    def download_by_group(self, group, course):
        url = self.su_dao.get_url_by_group_start(group[0], course)[0]
        path = '../resources'
        filename = path + '/' + os.path.basename(url)
        if os.path.exists(filename):
            os.remove(filename)
        wget.download(url, path)

    def fill_table_institutes(self):
        self.su_dao.drop_table_urls()
        self.su_dao.drop_table_institutes()
        with open('../resources/institutes_courses.txt', 'r', encoding='utf8') as f:
            institutes_courses = [institute_course.strip().split(',') for institute_course in f.readlines()]
            for institute, course, group_start in institutes_courses:
                self.su_dao.add_institute(institute, group_start)

    def fill_table_urls(self):
        self.su_dao.drop_table_urls()
        with open('../resources/institutes_courses.txt', 'r', encoding='utf8') as f:
            institutes_courses = [institute_course.strip().split(',') for institute_course in f.readlines()]
            for institute, course, group_start in institutes_courses:
                course = int(course)
                for i in range(1, course + 1):
                    try:
                        self.add_url_by_name(institute, i)
                    except TypeError:
                        print('TypeError in url: ' + institute + ' ' + str(course))


sc = schedule_url_service()
sc.fill_table_institutes()
sc.fill_table_urls()
sc.download_by_group("ИКБО", 1)
sc.disconnect()
