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
		distancia = sims[1:top+1]
		sal = []
		for d in distancia:
			t = (datos.iloc[d[0]].id, d[1])
			sal.append(t)

		salida.append(sal)


	datos['distancia']=salida

	return datos


def mostrar_mejores(datos,modelo,corpus,id_articulo,top = 10):
	'''
	Calcula y muestra los articulos con menor distancia.
	'''
	#OBTENER INDICE DEL ARTICULO
	indice = datos.loc[datos['id'] == id_articulo].index.tolist()[0]
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