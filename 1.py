import pymorphy2
import natasha
from collections import OrderedDict
import geocoder
#блок для поиски имен
morph = pymorphy2.MorphAnalyzer()
ls1=list()
with open('1.txt') as f:
    ls = []
    for line in f:
        lst = line.split()
        words = []
        for word in lst:
            p = morph.parse(word)[0]  # делаем разбор
            words.append(p.normal_form)
        ls.append(words)
for i in ls:
    ls1 = i
print(ls1)
for word in ls1:
    for p in morph.parse(word):
        is_name = any('Name' in p.tag for p in morph.parse(word))
        if (is_name):
            print(word)
with open('2.txt') as movement:  # приводим передвижения в нормальную форму
    ls2 = []
    for line in movement:
        lst2 = line.split()
        words2 = []
        for word in lst2:
            p = morph.parse(word)[0]  # делаем разбор
            words2.append(p.normal_form)
        ls2.append(words2)
for i in ls2:
    move = i
print(move)
# блок для поиска городов
lines = [
    'тамань', 'пермь','капуста','В Чеченской республике на день рождения ...',
    'Донецкая народная республика провозгласила ...',
    'Российская Федерация в Соединенных Штатах Америки',
    'речь шла о Обьединенных Арабских Эмиратах Соединённые Штаты'
]
extractor = natasha.LocationExtractor()
for line in ls1:
    try:
        matches = extractor(line)
        match = matches[0]
        fact = match.fact.as_json
        print(dict(fact)['name'])
    except:
        print(end='')
# находим координаты
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Пермь")
print((location.latitude, location.longitude))
loc1 = [location.latitude, location.longitude]
location = geolocator.geocode("Москва")
print((location.latitude, location.longitude))
loc2 = [location.latitude, location.longitude]
# отображение на карте
'''import matplotlib.pylab as plt
import mpl_toolkits
mpl_toolkits.__path__.append('/usr/lib/pymodules/python2.7/mpl_toolkits/')
from mpl_toolkits.basemap import Basemap
lat = [66.297,66.299,66.298,66.295,66.301,66.304,66.288,66.289,66.286,66.289]
lon = [33.640,33.660,33.690,33.747,33.829,33.908,33.891,33.839,33.781,33.740]
m = Basemap(projection='merc', llcrnrlat=66.22, urcrnrlat=66.37, \
            llcrnrlon=33.60, urcrnrlon=34, resolution='f')
figsize(10, 15)

x, y = m(lon, lat)

m.drawcoastlines()
m.fillcontinents(color='gray', lake_color='white')
m.drawmapboundary(fill_color='white')
m.drawparallels(np.arange(66.22, 66.37, .04), labels=[1, 0, 0, 0], fontsize=14)
m.drawmeridians(np.arange(33.60, 34., .1), labels=[0, 0, 0, 1], fontsize=14)

m.scatter(x, y, 20, marker='o', color='k')
plt.title("Location of the measurement points", fontsize=14)
plt.show()'''


