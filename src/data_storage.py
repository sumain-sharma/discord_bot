'''
    Module to perform DB operations
'''

import sqlite3

class DataStorage:
    '''
        Class to store and fetch searched keyword on the google.
    '''

    def __init__(self):
        self.__DB_NAME = 'discord_bot'
        self.__TABLE_NAME = 'google_search_keyword'
        self.__DB_PATH = f'{self.__DB_NAME}.db'
        self.db_con = None

    def __enter__(self):
        self.db_con = sqlite3.connect(self.__DB_PATH)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_con.close()

    def initializing_schema(self):
        '''
            Method to create a DB schema if not exist
        '''
        self.db_con.execute(
            f'''
            CREATE TABLE IF NOT EXISTS {self.__TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user INTEGER NOT NULL,
                keyword VARCHAR2 NOT NULL
            );
            '''
        )

    def save_keyword(self, user, keyword):
        '''
            Method to save the keywords into the DB
        '''
        self.db_con.cursor().execute(
            f'INSERT INTO {self.__TABLE_NAME} (user, keyword) VALUES ({user}, "{keyword}");'
        )
        self.db_con.commit()

    def get_matched_keywords(self, user, keyword):
        '''
            Method to fetch matching data from the DB for a particular keyword
        '''
        cursor = self.db_con.cursor().execute(
            f'SELECT DISTINCT keyword from {self.__TABLE_NAME} where user={user} and keyword LIKE "%{keyword}%";'
        )
        return cursor.fetchall()
