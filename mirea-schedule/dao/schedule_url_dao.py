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
            self.cursor = self.connection.cursor(buffered=True)
        except Error as e:
            print(f"The error '{e}' occurred")

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS `schedule_url`.`institutes` ('
                            '  `institute` VARCHAR(100) NOT NULL,'
                            '  `group_start` VARCHAR(1) NOT NULL,'
                            '  PRIMARY KEY (`institute`));')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS `schedule_url`.`urls` ('
                            '  `url` VARCHAR(200) NOT NULL,'
                            '  `institute` VARCHAR(100) NOT NULL,'
                            '  `course` INT UNSIGNED NOT NULL,'
                            '  UNIQUE INDEX `id_UNIQUE` (`url` ASC) VISIBLE,'
                            '  PRIMARY KEY (`url`),'
                            '  INDEX `fk_urls_institutes_idx` (`institute` ASC) VISIBLE,'
                            '  CONSTRAINT `fk_urls_institutes`'
                            '    FOREIGN KEY (`institute`)'
                            '    REFERENCES `schedule_url`.`institutes` (`institute`)'
                            '    ON DELETE NO ACTION'
                            '    ON UPDATE NO ACTION);')
        self.connection.commit()

    def add_institute(self, institute, group_start):
        self.create_table()
        self.cursor.execute('INSERT INTO institutes '
                            'VALUES ("' + institute + '", "' + group_start + '");')
        self.connection.commit()

    def add_row(self, url, institute, course):
        self.create_table()
        self.cursor.execute('INSERT INTO urls '
                            'VALUES ("' + url + '", "' + institute + '", ' + str(course) + ');')
        self.connection.commit()

    def drop_table_urls(self):
        self.cursor.execute('DROP TABLE IF EXISTS urls;')
        self.connection.commit()

    def drop_table_institutes(self):
        self.cursor.execute('DROP TABLE IF EXISTS institutes;')
        self.connection.commit()

    def get_url_by_group_start(self, group_start, course):
        course = str(course)
        self.cursor.execute('SELECT url '
                            'FROM urls '
                            'INNER JOIN institutes ON urls.institute = institutes.institute '
                            f'WHERE group_start = "{group_start}" AND course = {course};')
        self.connection.commit()
        return self.cursor.fetchone()
