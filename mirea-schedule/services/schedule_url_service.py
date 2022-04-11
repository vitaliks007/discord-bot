from dao.schedule_url_dao import schedule_url_dao
from utils.url_html_parser import url_html_parser


class schedule_url_service:
    def __init__(self):
        self.su_dao = schedule_url_dao('127.0.0.1', 'root', 'qwerty')
        self.uh_parser = url_html_parser()

    def add_url_by_name(self, institute, course):
        url = self.uh_parser.get_url_by_name(institute, course)
        self.su_dao.add_row(url, institute, course)


sc = schedule_url_service()
sc.add_url_by_name('ИИТ', 2)
