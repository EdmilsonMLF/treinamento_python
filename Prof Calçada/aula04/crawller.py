import urllib.request

content = urllib.request.urlopen("https://dolarhoje.com").read()
content = str(content)
find = '<input type="text" id="nacional" value="'
posicao = int(content.index(find) + len(find))
dolar = content[posicao : posicao +4]


content = urllib.request.urlopen("https://dolarhoje.com/euro-hoje").read()
content = str(content)
find = '<input type="text" id="nacional" value="'
posicao = int(content.index(find) + len(find))
euro = content[posicao : posicao +4]

content = urllib.request.urlopen("https://www.climadobrasil.com.br/estado-do-ceara/fortaleza").read()
content = str(content)
find = '<span class="m_table_weather_day_max_temp"><span data-temp="'
posicao = int(content.index(find) + len(find))
maxima = content[posicao : posicao +2]

find = '<span class="m_table_weather_day_min_temp"><span data-temp="'
posicao = int(content.index(find) + len(find))
minima = content[posicao : posicao +2]

print("Dollar: " + dolar)
print("Euro: " + euro)
print("Temp. Máxima: " + maxima)
print("Temp. Mínima: " + minima)