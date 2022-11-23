def introducere():
    tablou = []
    limita = int(input('Introduceti dimensiunea tabloului: '))
    print('Introduceti elementele')
    for i in range(limita):
        x = int(input())
        tablou.append(x)
    return tablou

lista = introducere()

#printeaza
def tablourec(tablou, element):
    if element == 2*len(tablou) -1:
        return print(tablou[len(tablou) - 1])
    else:
        print(tablou[element-len(tablou)])
        return tablourec(tablou, element+1)
print('Printeaza elementele:')
tablourec(lista,len(lista))
#invers
def tablourec(tablou, element):
    if element == 1:
        return print(tablou[0])
    else:
        print(tablou[element-1])
        return tablourec(tablou, element-1)
print('Printeaza elementele invers:')
tablourec(lista, len(lista))

#suma
def tablourecs(tablou, element):
    if element == 0:
        return print(tablourecs.suma)
    else:
        tablourecs.suma += (tablou[element-1])
        return tablourecs(tablou, element-1)
print('Printeaza suma elementelor:')
tablourecs.suma = 0
tablourecs(lista, len(lista))
#pare
def tablourecsp(tablou, element):
    if (tablou[element - 1]% 2 == 0):
        tablourecsp.suma += (tablou[element-1])
    if element >= 0:
        return tablourecsp(tablou, element-2)
    else:
        return tablourecsp.suma
print('Printeaza suma elementelor pare:')
tablourecsp.suma = 0
print(tablourecsp(lista,len(lista)))
#impare
def tablourecsi(tablou, element):
    if (tablou[element - 1]% 2 != 0):
        tablourecsi.suma += (tablou[element-1])
    if element >= 0:
        return tablourecsi(tablou, element-2)
    else:
        return tablourecsi.suma
print('Printeaza suma elementelor impare:')
tablourecsi.suma = 0
print(tablourecsi(lista,len(lista)))
#afisarepar
def tablourecp(tablou, element):
    if element == 0:
        return 'done'
    if (tablou[element - 1]% 2 == 0):
        print(tablou[element-1])
    return tablourecp(tablou, element-1)
print('Printeaza elementele pare:')
tablourecp(lista,len(lista))
#afisareimpare
def tabloureci(tablou, element):
    if element == 0:
        return 0
    if (tablou[element - 1]% 2 != 0):
        print(tablou[element-1])
    return tabloureci(tablou, element-1)
print('Printeaza elementele impare:')
tabloureci(lista,len(lista))
