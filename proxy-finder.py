# -*- coding: utf-8 -*-
import time
import itertools
import threading
import sys
import requests
from bs4 import BeautifulSoup

Green = "\033[1;33m"
Blue = "\033[1;34m"
Grey = "\033[1;30m"
Reset = "\033[0m"
Red = "\033[1;31m"
Purple = "\033[0;35m"

done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rWAIT A MOMENT I WILL DO IT QUICKLY ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('')

def main():
    print(" " + Green + "   #############")
    print(" " + Green + "   PROXY FINDER")
    print(" " + Green + "   #############")

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(10)
    global done
    done = True

    print(Purple + "---> I FOUND THESE.......\n")
    time.sleep(3)

    print(Blue)

    proxy_domain = "https://free-proxy-list.net"

    try:
        response = requests.get(proxy_domain)
        response.raise_for_status()
    except requests.RequestException as e:
        print(Red + "Ошибка при получении списка прокси: " + str(e) + Reset)
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("div", class_="table-responsive fpl-list")

    if not table:
        print(Red + "Таблица с прокси не найдена на странице." + Reset)
        return

    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) < 5:
            continue
        ip = columns[0].get_text(strip=True)
        port = columns[1].get_text(strip=True)
        country = columns[3].get_text(strip=True)
        anonymity = columns[4].get_text(strip=True)
        print(f"{ip}:{port}\t{country:20}\t{anonymity:10}")

    print(" " + Grey + "JUST RUN ME ANYTIME, I WILL REFRESH PROXY LIST" + Reset)

if __name__ == "__main__":
    main()