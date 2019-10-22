import pymorphy2
import natasha
from collections import OrderedDict
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
lines = [
    'тамань', 'пермь','капуста','В Чеченской республике на день рождения ...',
    'Донецкая народная республика провозгласила ...',
    'Российская Федерация в Соединенных Штатах Америки',
    'речь шла о Обьединенных Арабских Эмиратах Соединённые Штаты'
]
extractor = natasha.LocationExtractor()
#for line in ls1:
for line in ls1:
    try:
        matches = extractor(line)
        match = matches[0]
        fact = match.fact.as_json
        #print(line)
        print(dict(fact)['name'])
    except:
        print(end='')

