from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer
import nltk
import re

stopwords = set(nltk.corpus.stopwords.words('portuguese'))
# stopwords.remove('não')
# stopwords.remove('mas')
# stopwords.remove('nem')
stopwords.update(["https", "plotlygraphs", 'não', 'mas', 'nem', 'vc', 'vcs', 'a', 'o', 'na'])


# nltk.download('stopwords')
# nltk.download('rslp')
# nltk.download('punkt')
# nltk.download('wordnet')

wordnet_lemmatizer = WordNetLemmatizer()
tweet_tokenizer = TweetTokenizer()


def RemoveStopWords(instancia):
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

def Stemming(instancia):
    stemmer = nltk.stem.RSLPStemmer()
    palavras = []
    for w in instancia.split():
        palavras.append(stemmer.stem(w))
    return (" ".join(palavras))

def Limpeza_dados(instancia):
    remove = ['.', ';', '-', ':', ')', '(', '_', '@', '!', "?"]
    instancia = re.sub(r"http\S+", "", instancia).lower()
    for item in remove:
        instancia = instancia.replace(item, '')
    return instancia

def Lemmatization(instancia):
  palavras = []
  for w in instancia.split():
    palavras.append(wordnet_lemmatizer.lemmatize(w))
  return (" ".join(palavras))

def To_negation(texto):# PARAR A ADIÇÃO DO NEG EM UM .
    negacoes = ['não','not']
    negacao_detectada = False
    resultado = []
    palavras = texto.split()
    for p in palavras:
        p = p.lower()
        if negacao_detectada == True:
            p = p + '_neg'
        if p in negacoes:
            negacao_detectada = True
        resultado.append(p)
    return (" ".join(resultado))

def Preprocessing_neg(instancia, split=False):
   if split:
       instancia = instancia[0].split('.') 

   stemmer = nltk.stem.RSLPStemmer()
   instancia = Limpeza_dados(instancia)
   instancia = RemoveStopWords(instancia)
   instancia = Lemmatization(instancia)
   instancia = To_negation(instancia)
 
   return instancia

def Preprocessing(instancias):
    lista = []
    for instancia in instancias:
        instancia = Limpeza_dados(instancia)
        instancia = RemoveStopWords(instancia)
        instancia = Lemmatization(instancia)
        lista.append(instancia)

    return lista


def pop_indexs(data, exclud):
    count=0
    for c in sorted(exclud):
        data.pop(c+count)
        count-=1
    return data

def remove_itens_x(data, item, qtd):
    for c in range(qtd):
        data.remove(item)
    return data

#remove_itens_x([1,2,3,1,5,47,8,4,1,31,5,'sd'], 1, 2)

#print(Preprocessing(['teste amiga! dessa função de expliti e tambem:']))