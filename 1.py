import pymorphy2
import geocoder
import natasha
from collections import OrderedDict
morph = pymorphy2.MorphAnalyzer()
#_________передвижение
with open('2.txt') as movement: # ключевые слова передвижения
    lst2 = []
    for line in movement:
        lst2 = line.split()
print(lst2)
phileasfogg = {}
k=0
with open('Верн Жюль. Вокруг света в восемьдесят дней - royallib.com.txt') as f:
    ls = list() # запишем весь текст разбитый на слова
    for line in f:
        lst = line.split()
        words = [] # слова из одной строки
        for word in lst:
            p = morph.parse(word)[0]  # делаем разбор
            words.append(p.normal_form)
        ls += words
for i in range(len(ls)-1):
    for move in lst2:
        if ls[i] == move:
            ls1 = ls[i-25:i+25]
            p1 = False
            p2 = False
            for j in range(len(ls1)-1):
                p = morph.parse(ls1[j])[0]
                if ('Name' in p.tag) and ((p.normal_form == 'филеасу') or (p.normal_form == 'фогга')):
                    p1 = True
                elif ('Geox' in p.tag):
                    p2 = True
                    g = [ls1[j]]
            if p1 == True and p2 == True:
                phileasfogg[k] = g
                k += 1
location1= []
from geopy.geocoders import Nominatim
for key in phileasfogg.keys():
    if key != 0 or key != 1:
        try:
            phileasfogg[key]
            geolocator = Nominatim(user_agent="specify_your_app_name_here")
            location = geolocator.geocode(phileasfogg[key])
            location1 += [list([location.latitude, location.longitude])]
            phileasfogg[key].append([location.latitude, location.longitude])
        except:
            phileasfogg[key] = ['no']
    else:
        phileasfogg[key] = ['No']
for key in phileasfogg.keys():
    print(phileasfogg[key])
location1.insert(0,[51.5073219, -0.1276474]) # координаты лондона
location1.append([51.5073219, -0.1276474])
print(location1)
location1.remove([22.34921555, 114.185797810004]) # "ошибка" алгоритма
#отображение на карте
import folium
map = folium.Map(location=[51.5073219, -0.1276474], zoom_start = 5)
for coordinates in location1:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)
folium.PolyLine([location1]).add_to(map)
map.save("map2.html")
