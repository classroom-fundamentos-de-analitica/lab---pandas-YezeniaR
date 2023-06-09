"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd 

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    nombre_archivo = "tbl0.tsv"
    df = pd.read_csv(nombre_archivo, sep='\t')

    cantidad_filas = df.shape[0]

    return cantidad_filas


def pregunta_02():
    nombre_archivo = "tbl0.tsv"
    df = pd.read_csv(nombre_archivo, delimiter='\t')

    cantidad_columnas = len(df.columns)

    return cantidad_columnas
  

def pregunta_03():
    nombre_archivo = "tbl0.tsv"
    df = pd.read_csv(nombre_archivo, delimiter='\t')
    
    conteo = df['_c1'].value_counts().sort_index()
    
    return conteo


def pregunta_04():
    nombre_archivo = "tbl0.tsv"
    df = pd.read_csv(nombre_archivo, delimiter='\t')

    promedio_por_letra = df.groupby('_c1')['_c2'].mean()

    return promedio_por_letra


def pregunta_05():
    nombre_archivo = "tbl0.tsv"
    df = pd.read_csv(nombre_archivo, sep='\t')

    resultado = df.groupby('_c1')['_c2'].max()

    return resultado


def pregunta_06():
    nombre_archivo = "tbl1.tsv"
    df = pd.read_csv(nombre_archivo, delimiter='\t')

    valores_unicos = sorted(df['_c4'].str.upper().unique())

    return valores_unicos


def pregunta_07():
    nombre_archivo = "tbl0.tsv"
    data = pd.read_csv(nombre_archivo, delimiter='\t')

    suma_por_letra = data.groupby('_c1')['_c2'].sum()

    return suma_por_letra


def pregunta_08():
    nombre_archivo = "tbl0.tsv"
    df = pd.read_csv(nombre_archivo, delimiter='\t')

    df['suma'] = df['_c0'] + df['_c2']

    return df


def pregunta_09():
    nombre_archivo = "tbl0.tsv"
    df = pd.read_csv(nombre_archivo, delimiter='\t')

    df['year'] = pd.to_datetime(df['_c3'], errors='coerce').dt.year

    df = df.dropna(subset=['year'])

    df['year'] = df['year'].astype(int)

    return df


def pregunta_10():
    archivo = "tbl0.tsv"
    df = pd.read_csv(archivo, sep='\t')

    df['_c2'] = df['_c2'].astype(int)
    df = df.sort_values(by='_c2')

    tabla = df.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, x))).reset_index()

    return tabla



def pregunta_11():
    archivo = "tbl1.tsv"
    df = pd.read_csv(archivo, sep='\t')

    tabla = df.groupby('_c0')['_c4'].apply(lambda x: ','.join(sorted(x))).reset_index()

    return tabla



def pregunta_12():
    archivo = "tbl2.tsv"
    df = pd.read_csv(archivo, sep='\t')

    df_agrupado = df.groupby('_c0').apply(lambda x: ','.join([f"{a}:{b}" for a, b in sorted(zip(x['_c5a'], x['_c5b']))]))

    df_resultado = pd.DataFrame({'_c0': df_agrupado.index, '_c5': df_agrupado.values})

    return df_resultado


def pregunta_13():
    archivo1 = "tbl2.tsv"
    archivo = "tbl0.tsv"
    df_tbl0 = pd.read_csv(archivo, sep='\t')
    df_tbl2 = pd.read_csv(archivo1, sep='\t')
    
    df_merge = pd.merge(df_tbl0, df_tbl2, left_on='_c0', right_on='_c0')
    resultado = df_merge.groupby('_c1')['_c5b'].sum()
    
    return resultado
