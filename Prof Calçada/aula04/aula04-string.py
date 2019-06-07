texto = "Um texto qualquer"
posicao = texto.index("t")
print(posicao)

#tam = len("qua")

resultado = texto[posicao:posicao + 5]
print(resultado)

resultado2 = texto[posicao:len(texto)]
print(resultado2)