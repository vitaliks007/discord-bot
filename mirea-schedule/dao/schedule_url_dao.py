import mysql.connector
from mysql.connector import Error


class schedule_url_dao:
    def __init__(self, hostname, user_name, user_password):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=hostname,
                user=user_name,
                passwd=user_password,
                database="schedule_url"
            )
            print("Connection to MySQL DB successful")
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"The error '{e}' occurred")

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def add_row(self, url, institute, course):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS schedule_url.urls ('
                            'url VARCHAR(200) NOT NULL, '
                            'institute VARCHAR(100) NOT NULL, '
                            'course INT UNSIGNED NOT NULL, UNIQUE INDEX id_UNIQUE (url ASC) VISIBLE, PRIMARY KEY ('
                            'url)) '
                            'ENGINE = InnoDB;')
        self.cursor.execute('INSERT INTO urls '
                            'VALUES ("' + url + '", "' + institute + '", ' + str(course) + ');')
        self.connection.commit()

    def drop_table(self):
        self.cursor.execute('DROP TABLE IF EXISTS urls;')
        self.connection.commit()
