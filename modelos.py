import gensim
from gensim.utils import simple_preprocess

def generar_corpus(datos,columna,estar_minimo,estar_maximo):
	diccionario = gensim.corpora.Dictionary(datos[columna])

	# filtramos las palabras más raras o demasiado frecuentes
	#	no_below: en cuantos documentos esta al menos
	#	no_above: esta, no en mas del 80% de los documentos
	diccionario.filter_extremes(no_below=estar_minimo, no_above = estar_maximo)

	# Cada documento se transformará en una bolsa de palabras
	# con las frecuencias de aparición
	corpus = [diccionario.doc2bow(doc) for doc in datos[columna]]

	return diccionario, corpus


def entrenar(diccionario,corpus,n_topicos,n_art_entrenamiento):
	
	#ENTRENAR EL MODELO
	#LDA MODEL
	# num_topics: número de tópicos. Para este tutorial extraeremos 50 tópicos.
	# random_state: parámetro para controlar la aleatoriedad del 
	# 			  proceso de entrenamiento y que nos devuelva siempre los mismos resultados.
	# chunksize: número de documentos que será utilizado en cada pasada de entrenamiento.
	# passes: número de pasadas por el corpus durante el entrenamiento.
	# alpha: representa la densidad de tópicos por documento.
	#  	   Un mayor valor de este parámetro implica que los documentos estén compuestos de más tópicos.
	#        En este caso, fijamos el valor en auto.
	lda = gensim.models.LdaModel(corpus=corpus, id2word=diccionario, 
				   num_topics=n_topicos, random_state=42, 
				   chunksize=n_art_entrenamiento, passes=8, alpha='auto')
	return lda


def topicos_obtenidos(modelo, num_palabras, num_topics):
	return modelo.print_topics(num_words=num_palabras, num_topics=num_topics)