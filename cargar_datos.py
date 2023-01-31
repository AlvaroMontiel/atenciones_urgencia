def crea_dataframe(html):
  html = html
  df = pd.DataFrame()
  for i in html:
    df = df.append(i.loc[4:28], ignore_index=True, sort=None)
  df = df.rename(columns = {0:"Consulta", 1:"Total"}).fillna(0)
  df = df.drop(df.loc[df.Consulta.str.contains('TOTAL'), :].index)
  df = df.drop(df.loc[df.Consulta.str.contains('Covid-19'), :].index)
  df['Total'] = df['Total'].astype('int32')
  df.reset_index(inplace=True, drop=True)

  return df


if __name__ == '__main__':

    import pandas as pd
    import os

    # html = pd.read_html("AU-S-Mixto-S1.xls")

    años = [2019, 2020, 2021, 2022]
    lista_archivos = list()

    contador = 0
    for i in años:
        archivo = "hra_"+str(i)
        ruta =  "/Users/alvaro/Documents/Data_Science/datasets/atenciones_urgencias/afta/hospital/hra/"+archivo
        archivos = os.listdir(ruta)
        archivos.sort()
        lista_archivos.append(archivos)
        contador += 1

    archivos_dict = dict(zip(años, lista_archivos))

    lista_establecimientos = ["hra", "mejillones", ]



