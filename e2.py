from urllib import request
from urllib.error import URLError

lpo = ['cabrón','caca','carajo','lambon','coño','puto','bobo']

def verificar_web(url):
    try:
        f=request.urlopen(url)
    except:
        return ('la url' + url + 'no existe')
    else:
        aux= f.read()
        contenido= aux.split()
        palabras_encontradas=[]
        cantidad_po=0
        for l in lpo:
            for con in contenido:
                if l in con.decode():
                    palabras_encontradas.append(l)
                    
        return palabras_encontradas




url='https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print("\n....................................")
print('Informe del contenido de la página web')
print(verificar_web(url))
print('Cantidad de palabras encontradas: ',len(verificar_web(url)))
print("....................................")