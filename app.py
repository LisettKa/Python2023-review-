from threading import Thread

from scraper import scrapper_polling
from database import DBAccessor
from web import app as flask_app

if __name__ == '__main__':
    DBAccessor.init_db("data/data.db")

    Thread(target=scrapper_polling, daemon=True).start()

    flask_app.run("0.0.0.0")
