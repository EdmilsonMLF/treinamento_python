from urllib.parse import urlencode
from urllib.request import Request, urlopen

def unescapeXML(s):
    s = s.replace("&lt", "<")
    s = s.replace("&gt", ">")
    s = s.replace("&amp", "&")
    s = s.replace("&nbsp", " ")
    return s

def unescapeString(s):
    s = s.replace("\\r", '')
    s = s.replace("\\t", '')
    s = s.replace("\\n", '')
    return s

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
#post_fields = {'relaxation': '60320360', 'tipoCEP': 'ALL', 'semelhante': 'N'}
post_fields = {'relaxation': '60761580', 'tipoCEP': 'ALL', 'semelhante': 'N'}

request = Request(url, urlencode(post_fields).encode())
result = urlopen(request).read()
result = str(result)

result = unescapeString(result)
result =bytes(result, "iso-8859-1").decode("unicode_escape")
result = unescapeXML(result)

#print(result)

find = 'CEP:</th>'
posicao = int(result.index(find) + len(find))
result = result[posicao : posicao + 200]

findInicioRua = '<td width="150">'
findFimRua = ' ;</td><td>'
posicaoInicioRua = int(result.index(findInicioRua) + len(findInicioRua))
posicaoFimRua = int(result.index(findFimRua))
#print("posição inico rua {0} e posicao fim rua {1}".format(str(posicaoInicioRua), str(posicaoFimRua)))
logradouro = result[posicaoInicioRua : posicaoFimRua]

findInicioCEP = '<td width="55">'
findFimCEP = '</td></tr></table>'
posicaoInicioCEP = int(result.index(findInicioCEP) + len(findInicioCEP))
posicaoFimCEP = int(result.index(findFimCEP))
#print("posição inico CEP {0} e posicao fim CEP {1}".format(str(posicaoInicioCEP), str(posicaoFimCEP)))
cep = result[posicaoInicioCEP : posicaoFimCEP]

result2 = result[posicaoFimRua + 2 : posicaoInicioCEP]
#print("result 2 {0} ".format(str(result2)))

findInicioBairro = '</td><td>'
findFimBairro = ' ;</td><td>'
posicaoInicioBairro = int(result2.index(findInicioBairro) + len(findInicioBairro))
posicaoFimBairro = int(result2.index(findFimBairro))
#print("posição inicio bairro {0} e posicao fim bairro {1}".format(str(posicaoInicioBairro), str(posicaoFimBairro)))
bairro = result2[posicaoInicioBairro : posicaoFimBairro]


result3 = result2[posicaoFimBairro + 2 : len(result2)]
#print(result3)

findInicioCidade = '</td><td>'
findFimCidade = ' ;</td><td width="55">'
posicaoInicioCidade = int(result3.index(findInicioCidade) + len(findInicioCidade))
posicaoFimCidade = int(result3.index(findFimCidade))
cidade = result3[posicaoInicioCidade : posicaoFimCidade]

#print(result)
print("")
print("Logradouro: {0}".format(logradouro))
print("Bairro: {0}".format(bairro))
print("Cidade: {0}".format(cidade))
print("CEP: {0}".format(cep))
print("")

