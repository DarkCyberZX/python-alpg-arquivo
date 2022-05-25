with open("file",encoding="utf-8") as file:
    data = file.readline()
    datasplit = data.split()
    lista_maiorpalavra = []
    z = 0
    y = 0
    contar_palavras = data.replace(" ","")
    list_a = []
    list_e = []
    list_i = []
    list_o = []
    list_u = []


    for x in datasplit:
        lista_maiorpalavra.append(len(datasplit[z]))
        z += 1
        if len(lista_maiorpalavra) > 5:
            lista_maiorpalavra.remove(min(lista_maiorpalavra))

    lista_maiorpalavra.sort(reverse=True)
    for x in data:
        if data[y] == "a":
            list_a.append(1)

        elif data[y] == "e":
            list_e.append(1)

        elif data [y] == "i":
            list_i.append(1)

        elif data [y] == "o":
            list_o.append(1)

        elif data [y] == "u":
            list_u.append(1)

        y += 1


    print(f"o numero de palavras é {len(contar_palavras)}")
    print(f"As maiores palavras tem respectivamente {lista_maiorpalavra} letras")
    if sum(list_a) > sum(list_e) or sum(list_i) or sum(list_o) or sum(list_u) :
        print(f"A vogal que mais aparece e a letra A aparecendo {sum(list_a)} vezes  ")

    elif sum(list_e) > sum(list_a) or sum(list_i) or sum(list_o) or sum(list_u) :
        print(f"A vogal que mais aparece e a letra E aparecendo {sum(list_e)} vezes  ")

    elif sum(list_i) > sum(list_a) or sum(list_e) or sum(list_o) or sum(list_u) :
        print(f"A vogal que mais aparece e a letra I aparecendo {sum(list_i)} vezes  ")

    elif sum(list_o) > sum(list_a) or sum(list_e) or sum(list_i) or sum(list_u) :
        print(f"A vogal que mais aparece e a letra O aparecendo {sum(list_o)} vezes  ")

    elif sum(list_u) > sum(list_a) or sum(list_e) or sum(list_i) or sum(list_o) :
        print(f"A vogal que mais aparece e a letra O aparecendo {sum(list_o)} vezes  ")

with open("file",encoding="utf-8") as file:
    newdata = file.readlines()
    linhas = 0
    for x in newdata:
        try:
            index = newdata[linhas].index("ção")
            print(f"ção aparece na {linhas + 1} linha")
            break

        except:
            linhas += 1
            pass



