from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_regions(links=False):
    with urlopen("http://mosopen.ru/regions") as f:
        soup = BeautifulSoup(f, 'html.parser')
    districts_div = soup.find(id="regions_by_districts")

    res = []
    for p in districts_div.find_all('p'):
        regions = []
        for link in p.find_all('a'):
            lnk = link.get('href')
            if "district" in lnk:
                cur_district = link.contents[0]
            else:
                if not links:
                    regions.append(link.contents[0])
                else:
                    regions.append(lnk)
        res.append((cur_district, regions))
    return res


def get_streets(region_link, links=False):
    res = []
    with urlopen(''.join([region_link, '/streets'])) as f:
        soup = BeautifulSoup(f, 'html.parser')
    streets_div = soup.find_all("div", class_="double_part")
    for part in streets_div:
        for link in part.find_all('a'):
            lnk = link.get('href')
            cont = link.contents[0]
            if not links:
                res.append(cont)
            else:
                res.append(lnk)
    return res


def get_houses(street_link):
    res = []

    with urlopen(street_link) as f:
        soup = BeautifulSoup(f, 'html.parser')

    for p in soup.body.find_all('p'):
        if "Список домов" in p.contents[0]:
            for link in p.find_all('a'):
                cont = link.contents[0]
                res.append(cont.replace('\xa0', ' '))
    return res
