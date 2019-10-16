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
