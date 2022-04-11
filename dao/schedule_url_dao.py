import mysql.connector
from mysql.connector import Error


class schedule_url_dao:
    def __init__(self):
        self.connection = None

    def create_connection(self, host_name, user_name, user_password):
        try:
            self.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database="schedule_url"
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    def add_row(self, url, institute, course):
        cursor = self.connection.cursor()
        cursor.execute("INSERT urls(url, institute, course)"
                       "VALUES ('" + url + "', '" + institute + "', " + course + ");")
