import pandas as pd
pd.options.mode.chained_assignment = None
import limpiar

def abrir(name):
	path = f'datos/{name}'
	archivo = pd.ExcelFile(path)
	df = pd.read_excel(archivo, "datos")
	return df

def separar(datos,*args):
	index = list(args)
	index.append('id')
	df = datos[index]
	return df

def abrir_csv(name):
	path = f'datos/{name}'
	c1="dc.description.abstract[es_ES]"
	c2="dc.subject[es_ES]"
	c3="dc.title[es_ES]"
	datos = pd.read_csv(path)
	salida = datos[['id',c1,c2,c3]]
	salida = salida.rename(columns={c1:'abstract',c2:'keywords',c3:'titulo'})
	return salida


def unir(datos1,datos2):
	salida = datos1.append(datos2)
	return salida

def guardar_df(datos,name):
	path = f'datos/{name}'
	datos.to_excel(path,sheet_name="datos",index=False)

def unir_y_guardar(df1,df2):
	salida = pd.merge(df1,df2, on = 'id')
	salida.head()
	guardar_df(salida,'salida.xlsx')


'''
def test(datos):
	col = datos['abstract']
	c=0
	for t in col:
		if type(t) == str:
			if t.find('||')>0:
				x = t.split('||')
				print(x[0])
				print(x[1])

	print(c)
		

a = abrir('datos.xlsx')
d2 = separar(a,'abstract')
test(a)
'''