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
                cur_district = lnk
            else:
                if not links:
                    regions.append(lnk)
                else:
                    regions.append(lnk)
        res.append(regions)
    return res

print(get_regions())