from dao.schedule_url_dao import schedule_url_dao
from utils.url_html_parser import url_html_parser


class schedule_url_service:
    def __init__(self):
        self.su_dao = schedule_url_dao('127.0.0.1', 'root', 'qwerty')
        self.uh_parser = url_html_parser()

    def disconnect(self):
        self.su_dao.disconnect()

    def add_url_by_name(self, institute, course):
        url = self.uh_parser.get_url_by_name(institute, course)
        self.su_dao.add_row(url, institute, course)

    def fill_table(self):
        self.su_dao.drop_table()
        with open('../resources/institutes_courses.txt', 'r', encoding='utf8') as f:
            institutes_courses = [institute_course.strip().split(',') for institute_course in f.readlines()]
            for institute, course in institutes_courses:
                course = int(course)
                for i in range(1, course + 1):
                    try:
                        self.add_url_by_name(institute, i)
                    except TypeError:
                        print(institute + ' ' + str(course))


sc = schedule_url_service()
sc.fill_table()
sc.disconnect()
