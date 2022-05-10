#TERCEROS
from googletrans import Translator
import re
from nltk.tokenize import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def separar_idioma(texto):
	'''
	Saca la parte en ingles
	'''
	if texto.find('||')>0:
		x = texto.split('||')
		return x[0]
	return texto

def sacar_idioma_abstract(datos,columna):
	datos[columna] = datos[columna].apply(separar_idioma)
	return datos

def es_ingles(texto):
	'''
	Verifica el idioma del texto
	'''
	y = Translator()
	return y.translate(texto).src == 'en'

def filtrar_idioma(datos,columna):	
	ingles = datos[(datos[columna].apply(es_ingles))].index
	datos.drop(ingles,inplace=True)
	return datos

def filtrar_vacios(datos,columna):
	'''
	Elimina articulos sin abstract
	'''
	datos.dropna(subset = [columna], inplace=True)
	return datos

def limpiar(datos,*args):
	'''
	Limpia el texto de las columnas pasadas como parametro
	'''
	for col in args:
		datos[col] = datos[col].apply(limpiar_texto)
	return datos

def tokenizar(datos,*args):
	'''
	Genera los tokens de las columnas pasadas como parametro
	y los agrega en una nueva columna llamada: tokens
	'''
	tokenizer = ToktokTokenizer()
	if len(args)>1:
		datos['tokens'] = datos[list(args)].apply(' '.join, axis=1)
		datos['tokens'] = datos['tokens'].apply(tokenizer.tokenize)
	else:
		datos['tokens'] = datos[args[0]].apply(tokenizer.tokenize)
	return datos


def filtrar_stopwords(datos,columna):
	'''
	Elimina las palabras comunes
	'''
	datos["tokens"] = datos.tokens.apply(stopwords_digitos)
	return datos

def stemmear(datos,columna):
	'''
	Stemm de los tokens
	'''
	datos[columna] = datos[columna].apply(stem_palabras)
	return datos

###############################################################################
#FUNCIONES PARA SERIES
def limpiar_texto(texto):
	"""
	Función para realizar la limpieza de un texto dado.
	"""
	# Eliminamos los caracteres especiales
	texto = re.sub(r'\W', ' ', str(texto))
	# Eliminado las palabras que tengo un solo caracter
	texto = re.sub(r'\s+[a-zA-Z]\s+', ' ', texto)
	# Sustituir los espacios en blanco en uno solo
	texto = re.sub(r'\s+', ' ', texto, flags=re.I)
	#Eliminar retorno de excel
	texto = texto.replace('_x000D_',' ')
	# Convertimos textos a minusculas
	texto = texto.lower()

	return texto

def stopwords_digitos(tokens):
	STOP_WORDS = stopwords.words("spanish")
	STOP_WORDS.extend(['proyecto', 'desarrollo', 'analisis', 'estudio', 'presenta', 'trabajo','análisis'])
	STOP_WORDS = set(STOP_WORDS)
	return [token for token in tokens if token not in STOP_WORDS 
			and not token.isdigit()]

def stem_palabras(tokens):
	stemmer = SnowballStemmer("spanish")
	return [stemmer.stem(token) for token in tokens]