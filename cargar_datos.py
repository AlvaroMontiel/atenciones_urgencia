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

    ruta = 'D:\\Datasets\\atenciones_urgencias\\hcc_2019\\AU-S-Mixto-S1.xls'
    html = pd.read_html(ruta)
    print(html)

    años = [2019, 2020, 2021, 2022]
    lista_archivos = list()





