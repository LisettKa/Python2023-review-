import logging
import time

import requests
import re
from bs4 import BeautifulSoup
import json

from database import DBAccessor

url = "https://bitva-silnejshih.tnt-online.ru"


def scrapper_polling():
    while True:
        try:
            html = requests.get(url)
            soup = BeautifulSoup(html.content, 'lxml')
            script = soup.find_all('script')[8].text

            string = re.findall(r"let response = .+'\)", script)[0]
            string = string.lstrip("let response = JSON.parse('")
            string = string.rstrip("')")
            string = string.encode().decode("unicode_escape")

            data = json.loads(string)

            chart = data['chart']
            for value in chart.values():
                person = value[0]
                name = person['name']
                watcher = person['votesList']['1']['value']
                psychics = person['votesList']['2']['value']
                televiewer = person['votesList']['3']['value']
                DBAccessor().insert_psychic(name, watcher, psychics, televiewer)

            logging.info("Parsed successfully")
        except Exception:
            logging.exception("Undefined error")

        time.sleep(60 * 60)