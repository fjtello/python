import pandas as pd
import numpy as np
import pyodbc as odbc
# import time as tm
# import scrapy as sc
import requests as rq
import string as st

from pathlib import Path
from math import floor
# import urllib

import io as os
import webbrowser as wb
# import time
from datetimefunctions import getSecondsBetween
from datetimefunctions import getDateAddingMonths
from datetimefunctions import getTodayAsDatetime
from datetimefunctions import getSecondsSinceEpoch

from requests.auth import HTTPBasicAuth


## initialize objects in db (innecesary at first, but useful to confirm sp's are invoked)
cnx = "Driver={ODBC Driver 13 for SQL Server};Server=(localdb)\MSSQLLocalDB;Database=STOCK;Trusted_Connection=yes;"
cnx = "Driver={ODBC Driver 17 for SQL Server};Server=(localdb)\MSSQLLocalDB;Database=STOCK;Trusted_Connection=yes;"

xml_aemet_mostoles = r"http://www.aemet.es/xml/municipios/localidad_28161.xml"

chrome_path = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"
chrome_path = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

download_path = r"%USERPROFILE%\Downloads"

def save_url_content_into_html_file(par_URLsource, par_Path):
	web_content = rq.get(par_URLsource)
	destiny_file = par_Path.replace(".csv", "_read.html")
	destiny_file = destiny_file.replace("source", "download")	# I know, I know,...

	contenido_destino = web_content.text[:].encode('utf-8').strip().decode('utf-8')

	file_text = os.open(destiny_file, mode='w', encoding='UTF-8')
	file_text.write(contenido_destino)
	file_text.close()

def open_web_page(par_link, par_browserPath):
	wb.get(par_browserPath).open(par_link)

def download_file_into_folder(par_downloadLink, par_browserPath):
	try:
		# segundos transcurridos desde 1971-01-01 00:00:00.000
		periodo_final = getTodayAsDatetime() # hoy
		periodo_inicial = getDateAddingMonths(periodo_final, -2)

		str_periodo_final = str(floor(getSecondsSinceEpoch(periodo_final)))
		str_periodo_inicial = str(floor(getSecondsSinceEpoch(periodo_inicial)))

		par_downloadLink = par_downloadLink.replace("[periodo_inicial]", str_periodo_inicial)
		par_downloadLink = par_downloadLink.replace("[periodo_final]", str_periodo_final)

		print(par_downloadLink)

		wb.get(par_browserPath).open(par_downloadLink)

	except Exception as error:
		print("Error en [download_file_into_folder]")
		print(error)

# deprecated
def download_file_into_folder_os(par_downloadLink, par_Path):
	try:
		content_csv = rq.get(par_downloadLink)
		contenido_destino = str(content_csv.text[:].encode('utf-8').strip()).decode('utf-8')
		file_text = os.open(par_Path, mode='w', encoding='UTF-8')
		file_text.write(contenido_destino)
		file_text.close()

	except Exception as error:
		print("Error en [download_file_into_folder_os]")
		print(error)


try:
	connection = odbc.connect(cnx)
	cursor = connection.cursor()

	# crawl throughout the files to read

	# obtener una tabla como respuesta a una invocacion de procedimiento almacenado
	sp_files_select = "EXEC proc_Files_Select"
	cursor.execute(sp_files_select)
	tabla_files = cursor.fetchall()
	stepNum = 0
	for registro_tabla in tabla_files:
		fld_CodFile = registro_tabla[0]
		fld_Ticker = registro_tabla[1]
		fld_Path = registro_tabla[2]
		fld_URLsource = registro_tabla[3]
		fld_downloadLink = registro_tabla[4]
		fld_downloadedFileName = registro_tabla[5]

		stepNum = stepNum + 1
		print("[{}] Processing data read from: {}\t{}\t{}\t\t{}\t\t{}".format(str(stepNum), fld_CodFile, fld_Ticker, fld_Path, fld_downloadLink, fld_URLsource))

		# save the url content into an html file
		save_url_content_into_html_file(fld_URLsource, fld_Path)

		#web_content = rq.get(fld_URLsource)
		#destiny_file = st.replace(fld_Path, ".csv", "_read.html")
		#contenido_destino = str(web_content.text[:].encode('utf-8').strip()).decode('utf-8')

		#file_text = os.open(destiny_file, mode='w', encoding='UTF-8')
		#file_text.write(contenido_destino)
		#file_text.close()

		# download
		download_file_into_folder(fld_downloadLink, chrome_path)
		# open_web_page(fld_URLsource, chrome_path)
		# guardar el archivo descargado con el nombre indicado en el registro de bd


		# existe el archivo?
		fileToPivot = Path(fld_Path)

		if fileToPivot.is_file():

			# leer el contenido de cada uno de los csvs e incorporarlo a una tabla mediante panda
			#file_content = pd.read_csv(fld_Path, sep=',', names=['Date','Open','High','Low','Close','Adj Close','Volume'])
			file_content = pd.read_csv(fld_Path, sep=',')

			cols_en_dataframe = len(file_content.columns)
			filas_en_dataframe = len(file_content.index)

			# recorrer cada linea del dataframe y guardar los valores
			for index, row in file_content.iterrows():

				fld_csv_date = row[0]
				fld_csv_open = row[1]
				fld_csv_high = row[2]
				fld_csv_low = row[3]
				fld_csv_close = row[4]
				fld_csv_adjclose = row[5]
				fld_csv_volume = row[6]

				ejecutar_insert = True
				if np.isnan(fld_csv_open) or np.isnan(fld_csv_high) or np.isnan(fld_csv_low) or np.isnan(fld_csv_close) or np.isnan(fld_csv_adjclose) or np.isnan(fld_csv_volume):
					ejecutar_insert = False

				# guardar cada registro en la tabla
				if ejecutar_insert:
					sql_sp_insert = "EXEC [STOCK].[dbo].[proc_StockValues_Insert] ?, ?, ?, ?, ?, ?, ?, ?, ?;"
					values_sp_insert = (fld_Ticker, fld_csv_date, fld_csv_open, fld_csv_high, fld_csv_low, fld_csv_close, fld_csv_adjclose, fld_csv_volume, 1)
					cursor.execute(sql_sp_insert, values_sp_insert)
					connection.commit()
		else:
			print("\t File does not exist: {}".format(fld_Path))

	cursor.close()
	connection.close()
except odbc.Error as err:
	print("ODBC.ERROR")
	print(err)
except rq.exceptions.RequestException as err:
	print("REQUEST.ERROR")
	print(err)
except Exception as error:
	print("A general error was found along the process")
	print(error)

print("=================> The process has ended")
