from ..


class schedule_url_service:
    def __init__(self):
        self.su_dao = schedule_url_dao()
        self.uh_parser = url_html_parser()

    def add_url_by_name(self, institute, course):
        url = self.uh_parser.get_url_by_name(institute, course)
        self.su_dao.add_row(url, institute, course)
