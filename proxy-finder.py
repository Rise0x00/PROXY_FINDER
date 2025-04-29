# -*- coding: utf-8 -*-
from time import sleep
import itertools
import threading
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
        print(f'\rОжидайте... {c}', end="")
        sleep(0.1)
    print("")

def main():
    global done
    print(f"{Green} #############")
    print(f"{Green} PROXY FINDER")
    print(f"{Green} #############")

    t = threading.Thread(target=animate)
    t.start()
    sleep(5)
    done = True

    print(f"\n{Purple}---> Найдено следующее.......\n")
    sleep(3)
    print(Blue)

    proxy_domain = "https://free-proxy-list.net"

    try:
        response = requests.get(proxy_domain)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"{Red}Ошибка при получении списка прокси: {e}{Reset}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("div", class_="table-responsive fpl-list")

    if not table:
        print(f"{Red}Таблица с прокси не найдена на странице{Reset}")
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

    print(f" {Grey}Перезапусти скрипт для обновления списка прокси{Reset}")

if __name__ == "__main__":
    main()