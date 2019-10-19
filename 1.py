import pymorphy2
morph = pymorphy2.MorphAnalyzer()
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
