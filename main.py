#ELiMINAR WARNING
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

#PROPIOS
import carga
import limpiar
import modelos
import random
import time
import distancia
import graficos
import puntajes

#ABRIR EL PRE-FILTRADO
articulos = carga.abrir('procesados.xlsx')


#ABRIR Y FILTRAR IDIOMAS Y GUARDAR
#datos_excel = carga.abrir('datos.xlsx')
#datos_csv = carga.abrir_csv('datos2.csv')
#articulos = carga.unir(datos_excel,datos_csv)
#articulos = limpiar.filtrar_vacios(articulos,columna='abstract')
#articulos = limpiar.sacar_idioma_abstract(articulos,columna='abstract')
#articulos = limpiar.filtrar_idioma(articulos,columna='abstract')
#carga.guardar_df(articulos,'procesados.xlsx')


#SEPARAR 2 MODELOS
df_abstract = carga.separar(articulos,'abstract')
df_key_titulo = carga.separar(articulos,'titulo','keywords')

#LIMPIAR
df_abstract = limpiar.limpiar(df_abstract, 'abstract')
df_key_titulo = limpiar.limpiar(df_key_titulo, 'titulo','keywords')


#TOKENIZAR (AGREGA COLUMNA DE TOKENS)
df_abstract = limpiar.tokenizar(df_abstract,'abstract')
df_key_titulo = limpiar.tokenizar(df_key_titulo, 'titulo','keywords')
#STOPWORDS
df_abstract = limpiar.filtrar_stopwords(df_abstract,columna = 'tokens')
df_key_titulo = limpiar.filtrar_stopwords(df_key_titulo,columna = 'tokens')
#STEMMING
df_abstract = limpiar.stemmear(df_abstract,columna='tokens')
df_key_titulo = limpiar.stemmear(df_key_titulo,columna='tokens')


################################################################
#OBTENER CORPUS Y DICCIONARIO
ESTAR_MINIMO_EN = 2
ESTAR_MAXIMO_EN = 0.8
#8 o 11es el mejor segun choerencia
TOPICOS_BUSCADOS = 8
N_X_ENTRENAMIENTO = 200

dicc_abstract,corpus_abstract = modelos.generar_corpus(datos=df_abstract, columna='tokens', 
												estar_minimo = ESTAR_MINIMO_EN, estar_maximo = ESTAR_MAXIMO_EN)
dicc_key_titulos,corpus_key_titulo = modelos.generar_corpus(datos=df_key_titulo, columna='tokens', 
												estar_minimo = ESTAR_MINIMO_EN, estar_maximo = ESTAR_MAXIMO_EN)


#ENTRENAR MODELOS LDA
modelo_abstract = modelos.entrenar(diccionario = dicc_abstract, corpus =corpus_abstract,
									 n_topicos=TOPICOS_BUSCADOS,n_art_entrenamiento=N_X_ENTRENAMIENTO)

modelo_key_titulo = modelos.entrenar(diccionario = dicc_key_titulos, corpus =corpus_key_titulo,
									 n_topicos=TOPICOS_BUSCADOS,n_art_entrenamiento=N_X_ENTRENAMIENTO)

#GRAFICAR LACHOERENCIA
LIMITE_TOPICOS = 20
#puntajes.graficar_choerencia(dicc_abstract,corpus_abstract,df_abstract['tokens'],LIMITE_TOPICOS)


#CALCULAR Y AGREGAR LA DISTANCIA DE CADA ARTICULO A LOS DEMAS
TOP_MEJORES = 10
#df_abstract = distancia.agregar_distancia(df_abstract,top = TOP_MEJORES,modelo = modelo_abstract,corpus=corpus_abstract)

#CALCULAR Y MOSTRAR TOP ARTICULOS MAS RELACIONADOS AL SELECCIONADO
INDICE = 64
TOP_MEJORES = 10
distancia.mostrar_mejores(articulos,modelo_abstract,corpus_abstract,INDICE,TOP_MEJORES)

#GRAFICAR TOPICOS DE UN ARTICULO
#indice = 96 o 106
INDICE = 96
#graficos.grafico_gaby(articulos,modelo_abstract,INDICE,corpus_abstract)




