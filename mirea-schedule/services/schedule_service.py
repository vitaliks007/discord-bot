import os

from dao.schedule_dao import schedule_dao
from utils.excel_parser import excel_parser


class schedule_service:
    def __init__(self):
        self.s_dao = schedule_dao('127.0.0.1', 'root', 'qwerty')
        self.exl_parser = excel_parser()

    def disconnect(self):
        self.s_dao.disconnect()

    def get_day_schedule(self, date, group):


    def add_row_group(self):
        with open('../resources/institutes_courses.txt', 'r', encoding='utf8') as f:
