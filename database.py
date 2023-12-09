import sqlite3

db_file = ""


def init_db(filename):
    global db_file
    db_file = filename

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS psychics (
                   id INTEGER PRIMARY KEY,
                   name text,
                   watcher real,
                   psychics real,
                   televiewer real
                   )''')
    conn.commit()
    conn.close()


def insert_psychic(name, watcher, psychics, televiewer):
    conn = sqlite3.connect(db_file)
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

    conn.close()


def select_last():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    lasts = cursor.execute('''SELECT *, (watcher + psychics + televiewer) AS total_score FROM psychics 
                           WHERE id IN (SELECT max(id) FROM psychics GROUP BY name)
                           ORDER BY total_score DESC''').fetchall()
    conn.close()
    return lasts
