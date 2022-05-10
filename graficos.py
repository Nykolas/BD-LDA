from gensim.matutils import jensen_shannon
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import pandas as pd


def grafico_gaby(datos,modelo,indice,corpus):

	art1 = datos.iloc[indice]
	art1_corpus = corpus[indice]
	art1_modelo = modelo[art1_corpus]
	# Indices de los topicos mas significativos
	dist_indices = [topico[0] for topico in modelo[art1_corpus]]
	# Contribución de los topicos mas significativos
	dist_contrib = [topico[1] for topico in modelo[art1_corpus]]


	distribucion_topicos = pd.DataFrame({'Topico':dist_indices,'Contribucion':dist_contrib })
	distribucion_topicos.sort_values('Contribucion', ascending=False, inplace=True)
	ax = distribucion_topicos.plot.bar(y='Contribucion',x='Topico', rot=0, color="orange",
										 title = 'Tópicos mas importantes' + str(indice))

	

	print("#############  TOPICOS #################")
	for ind, topico in distribucion_topicos.iterrows():
			print("*** Tópico: " + str(int(topico.Topico)) + " ***")
			palabras = [palabra[0] for palabra in modelo.show_topic(
					topicid=int(topico.Topico),topn=20)]
			palabras = ', '.join(palabras)
			print(palabras, "\n")
	plt.show()