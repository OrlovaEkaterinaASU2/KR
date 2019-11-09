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
#print(ls1)
for word in ls1:
    for p in morph.parse(word):
        is_name = any('Name' in p.tag for p in morph.parse(word))
        exc=['том','из','арен','герой','гора','брюнна','слава','«право']
        if (is_name):
            if (word not in exc):
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
#print(move)
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
        exc1 = ['ростов', 'уста', 'мирный', 'главнокомандовавший', 'билибино', 'тушино','пара','билибин']
        if (dict(fact)['name'] not in exc1):
            print(dict(fact)['name'])
    except:
        print(end='')
# находим координаты
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("Москва")
print((location.latitude, location.longitude))
loc1 = [location.latitude, location.longitude]
location = geolocator.geocode("Париж") # типа франция
print((location.latitude, location.longitude))
loc2 = [location.latitude, location.longitude]
location = geolocator.geocode("Санкт-Петербург")
print((location.latitude, location.longitude))
loc3 = [location.latitude, location.longitude]
location = geolocator.geocode("Вена")  # типа австрия
print((location.latitude, location.longitude))
loc4 = [location.latitude, location.longitude]
location = geolocator.geocode("Браунау-ам-Инн")  # типа австрия
print((location.latitude, location.longitude))
loc5 = [location.latitude, location.longitude]
# отображение на карте
import folium
map = folium.Map(location=loc1, zoom_start = 5)
for coordinates in [loc1,loc2,loc3,loc4,loc5]:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)
folium.PolyLine([loc2,loc1,loc3,loc4,loc5]).add_to(map)
map.save("map2.html")