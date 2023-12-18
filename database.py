import sqlite3


class DBAccessor:
    db_file = ""

    @staticmethod
    def init_db(filename):

        DBAccessor.db_file = filename

        with sqlite3.connect(DBAccessor.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS psychics (
                        id INTEGER PRIMARY KEY,
                        name text,
                        watcher real,
                        psychics real,
                        televiewer real
                        )''')
            conn.commit()

    def insert_psychic(self, name, watcher, psychics, televiewer):
        
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            existed = cursor.execute("SELECT id FROM psychics "
                                    "WHERE name = ? AND watcher = ? AND psychics = ? AND televiewer = ?",
                                    (name, watcher, psychics, televiewer)).fetchall()

            if not existed:
                cursor.execute('''INSERT INTO psychics 
                            (name, watcher, psychics, televiewer)
                            VALUES (?, ?, ?, ?)''',
                            (name, watcher, psychics, televiewer))

                conn.commit()


    def select_last(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()

            lasts = cursor.execute('''SELECT *, (watcher + psychics + televiewer) AS total_score FROM psychics 
                                WHERE id IN (SELECT max(id) FROM psychics GROUP BY name)
                                ORDER BY total_score DESC''').fetchall()

        return lasts
