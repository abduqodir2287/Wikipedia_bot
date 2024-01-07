import sqlite3


class Wiki_helperDB:
    def __init__(self, dbname='tech.db'):
        self.dbname = dbname
        self.tabname = ''
        self.conn = sqlite3.connect(self.dbname)

    def setup(self, tabname='custom'):
            """
            create table for database
            :param tabname: base name
            :return: default table name id, username
            """
            self.tabname = tabname
            sql = f"""
                CREATE TABLE IF NOT EXISTS {tabname}(
                      "id"  INTEGER PRIMARY KEY AUTOINCREMENT,
                      "userID" INTEGER,
                      "username"  TEXT
                    );"""

            self.conn.execute(sql)

    def add_item(self, userID: int, username: str):

        sql = f"""INSERT INTO "{self.tabname}" (userID, username)
            VALUES (?, ?);"""
        data = (userID, username)
        self.conn.execute(sql, data)
        self.conn.commit()


    def delete_item(self, id):
        sql = f"""DELETE FROM {self.tabname} where id=={id};"""
        self.conn.execute(sql)
        self.conn.commit()

    def select_item(self):
        sql = f"""SELECT * FROM {self.tabname};"""
        return self.conn.execute(sql).fetchall()

    def update_item(self, id, username):
        sql = f"""UPDATE {self.tabname} SET 
                username={username}, 
                WHERE id={id};"""

        self.conn.execute(sql)
        self.conn.commit()

    def log_out(self):
        self.conn.close()
