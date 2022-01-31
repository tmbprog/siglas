import docx

#Abre e adiciona o texto numa lista para poder maniputalar as strings. 
def LerDocumento(fileName):
    doc = docx.Document(fileName)
    texto_completo = []
    for paragrafos in doc.paragraphs:
        texto_completo.append(paragrafos.text.replace('.','')) #Replace removendo os pontos para caso de siglas no formato "S.I.G.L.A.S"
    
    return '\n'.join(texto_completo).split() #Join para unir tudo numa única str e poder fazer o split das palavras 

#Procura por combinações de mais de duas letras em caixa alta
def BuscarSiglas(list):
    siglas = []
    for palavras in arquivo:
        if palavras.isupper() and len(palavras) >= 2:
            siglas.append(palavras)
    return siglas

#Remove as siglas repetidas, evita a presença de números e organiza em ordem alfabética
def TratarLista (lista):
    Siglas_Tratada = []
    for i in lista:
        if i not in Siglas_Tratada and i.isalpha():
            Siglas_Tratada.append(i)
    Siglas_Tratada.sort()
    return Siglas_Tratada

#Execução
try:
    arquivo = LerDocumento(input('Nome do arquivo:')+'.docx')
    Siglas = BuscarSiglas(arquivo)
    Siglas = TratarLista(Siglas)


    if len(Siglas) == 0:
        print('Não foram encontradas Siglas no texto')
    else:
        print('SIGLAS encontradas no texto: ')
        for palavras in Siglas:
            print(palavras)
except:
    print('Desculpe, ocorreu um ERRO... Verifique se o arquivo está na mesma pasta que o script e/ou se o nome digitado está correto')

