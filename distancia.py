from gensim import similarities

#PARA GUARDAR
#index.save('ml.index')
#index = similarities.MatrixSimilarity.load('ml.index')

def agregar_distancia(datos,top,modelo,corpus):
	similares = similarities.MatrixSimilarity(modelo[corpus])

	salida = []
	for indice in range(len(datos)):
		art1 = datos.iloc[indice]
		art1_corpus = corpus[indice]
		art1_modelo = modelo[art1_corpus]

		sims = similares[art1_modelo]

		sims = sorted(enumerate(sims), key=lambda item: -item[1])
		salida.append(sims[:top])

	datos['distancia']=salida

	return datos


def mostrar_mejores(datos,modelo,corpus,indice,top = 10):
	'''
	Calcula y muestra los articulos con menor distancia.
	'''
	similares = similarities.MatrixSimilarity(modelo[corpus])
	art1 = datos.iloc[indice]
	art1_corpus = corpus[indice]
	art1_modelo = modelo[art1_corpus]

	sims = similares[art1_modelo]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])

	print(art1.abstract)
	print("--------ASBTRACT---------------")
	for doc_position, doc_score in sims[:top]:
	    print(doc_score, datos.iloc[doc_position].titulo)
	    print("---------------------")