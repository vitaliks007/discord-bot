import mysql.connector
from mysql.connector import Error


class schedule_dao:
    def __init__(self, hostname, user_name, user_password):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=hostname,
                user=user_name,
                passwd=user_password,
                database="schedule"
            )
            print("Connection to MySQL DB successful")
            self.cursor = self.connection.cursor(buffered=True)
        except Error as e:
            print(f"The error '{e}' occurred")

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def add_row_group(self, group, institute, course):
        self.create_table()
        self.cursor.execute('INSERT INTO groups '
                            'VALUES ("' + group + '", "' + institute + '", ' + str(course) + ');')
        self.connection.commit()

    def add_row_subject(self, date, subject, cabinet, teacher, s_format, group, subgroup):
        self.create_table()
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('INSERT INTO subjects '
                            'VALUES ("' + date + '", "' + subject + '", ' + str(cabinet)
                            + '", ' + teacher + '", ' + s_format + '", ' + group + '", ' + str(subgroup) + ');')
        self.connection.commit()

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS `mydb`.`groups` ('
                            '`group` VARCHAR(45) NOT NULL,'
                            '`institute` VARCHAR(45) NOT NULL,'
                            '`course` INT NOT NULL,'
                            'UNIQUE INDEX `group_UNIQUE` (`group` ASC) VISIBLE,'
                            'PRIMARY KEY (`group`))')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS `mydb`.`subjects` ('
                            '`date` DATETIME NOT NULL,'
                            '`subject` VARCHAR(45) NOT NULL,'
                            '`cabinet` INT NULL,'
                            '`teacher` VARCHAR(45) NULL,'
                            '`format` VARCHAR(45) NOT NULL,'
                            '`group` VARCHAR(45) NOT NULL,'
                            '`subgroup` INT NOT NULL,'
                            'PRIMARY KEY (`date`, `subject`, `group`, `subgroup`),'
                            'INDEX `fk_subjects_groups_idx` (`group` ASC) VISIBLE,'
                            'CONSTRAINT `fk_subjects_groups`'
                            'FOREIGN KEY (`group`)'
                            'REFERENCES `mydb`.`groups` (`group`)'
                            'ON DELETE NO ACTION'
                            'ON UPDATE NO ACTION)')
        self.connection.commit()
