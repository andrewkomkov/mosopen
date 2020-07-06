import mosopen
import time

regions = ['http://mosopen.ru/region/tverskoj',
           'http://mosopen.ru/region/meshchanskij',
           'http://mosopen.ru/region/marina_roshcha']

neighbour_regions = ['http://mosopen.ru/region/arbat',
                     'http://mosopen.ru/region/presnenskij',
                     'http://mosopen.ru/region/krasnoselskij',
                     'http://mosopen.ru/region/basmannyj',
                     'http://mosopen.ru/region/savelovskij',
                     'http://mosopen.ru/region/alekseevskij',
                     'http://mosopen.ru/region/begovoj',
                     'http://mosopen.ru/region/butyrskij]']


for region in neighbour_regions:
    print(str(list(filter(lambda s: s.split(' ')[-1], mosopen.get_streets(region)))).replace(',',''))
    #print(str(list(filter(lambda s: s.split(' ')[-1] == 'шоссе', mosopen.get_streets(region)))).replace(',', ''))
    time.sleep(1)