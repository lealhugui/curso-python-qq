from bs4 import BeautifulSoup
import requests


def get_all_links():
    page = requests.get('http://www.google.com')
    if page.status_code != 200:
        raise Exception('eita, deu erro')

    soup = BeautifulSoup(page.text, 'html.parser')
    all_as = soup.find_all('a')
    for a in all_as:
        print(a['href'])



if __name__ == "__main__":
    get_all_links()