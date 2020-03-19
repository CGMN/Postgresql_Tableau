# -*- coding: utf-8 -*-
## Python code generated with wxFormBuilder (version Nov  1 2019)
import wx
import wx.xrc
import sys

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Interfaz de apoyo para Tableau", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 900,-1 ), wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		style=wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL
		log=self.m_textCtrl4 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, style=style )
		self.m_textCtrl4.SetMinSize( wx.Size( -1,220 ) )

		bSizer9.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )

		sys.stdout=log

		self.m_panel5.SetSizer( bSizer9 )
		self.m_panel5.Layout()
		bSizer5.Add( self.m_panel5, 1, wx.ALL|wx.EXPAND, 5 )

		self.SetSizer( bSizer5 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.Dotacion = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.Dotacion, wx.ID_ANY, u"Creación", wx.EmptyString, wx.ITEM_NORMAL )
		cd=self.Dotacion.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.Dotacion, wx.ID_ANY, u"Subida", wx.EmptyString, wx.ITEM_NORMAL )
		sd=self.Dotacion.Append( self.m_menuItem3 )

		self.m_menu1.AppendSubMenu( self.Dotacion, u"Dotación" )

		self.ModPresupuestaria = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.ModPresupuestaria, wx.ID_ANY, u"Creación", wx.EmptyString, wx.ITEM_NORMAL )
		cm=self.ModPresupuestaria.Append( self.m_menuItem4 )

		self.m_menuItem9 = wx.MenuItem( self.ModPresupuestaria, wx.ID_ANY, u"Subida", wx.EmptyString, wx.ITEM_NORMAL )
		sm=self.ModPresupuestaria.Append( self.m_menuItem9 )

		self.m_menu1.AppendSubMenu( self.ModPresupuestaria, u"Mod. Presupuestaria" )

		self.Cupos = wx.Menu()
		self.m_menuItem10 = wx.MenuItem( self.Cupos, wx.ID_ANY, u"Creación", wx.EmptyString, wx.ITEM_NORMAL )
		cc=self.Cupos.Append( self.m_menuItem10 )

		self.m_menuItem11 = wx.MenuItem( self.Cupos, wx.ID_ANY, u"Subida", wx.EmptyString, wx.ITEM_NORMAL )
		sc=self.Cupos.Append( self.m_menuItem11 )

		self.m_menu1.AppendSubMenu( self.Cupos, u"Cupos" )

		self.Sigfe = wx.Menu()
		self.m_menuItem14 = wx.MenuItem( self.Sigfe, wx.ID_ANY, u"Borrar carga del año", wx.EmptyString, wx.ITEM_NORMAL )
		bs=self.Sigfe.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.Sigfe, wx.ID_ANY, u"Cargar año", wx.EmptyString, wx.ITEM_NORMAL )
		cs=self.Sigfe.Append( self.m_menuItem15 )

		self.m_menu1.AppendSubMenu( self.Sigfe, u"Sigfe" )

		self.Respaldos = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"Tabla Cupos", wx.EmptyString, wx.ITEM_NORMAL )
		tc=self.Respaldos.Append( self.m_menuItem5 )

		self.m_menuItem6 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"Tabla Presupuesto", wx.EmptyString, wx.ITEM_NORMAL )
		tp=self.Respaldos.Append( self.m_menuItem6 )

		self.m_menuItem7 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"Tabla Sigfe", wx.EmptyString, wx.ITEM_NORMAL )
		ts=self.Respaldos.Append( self.m_menuItem7 )

		self.m_menuItem8 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"Base completa", wx.EmptyString, wx.ITEM_NORMAL )
		bc=self.Respaldos.Append( self.m_menuItem8 )

		self.m_menu1.AppendSubMenu( self.Respaldos, u"Respaldos" )

		self.ActualizacionesdeEstado = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.ActualizacionesdeEstado, wx.ID_ANY, u"Cambiar a Tomado de Razón", wx.EmptyString, wx.ITEM_NORMAL )
		tr=self.ActualizacionesdeEstado.Append( self.m_menuItem12 )

		self.m_menu1.AppendSubMenu( self.ActualizacionesdeEstado, u"Actualizaciones de Estado" )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )

		self.Centre( wx.BOTH )

		#Eventos
		self.Bind(wx.EVT_MENU, self.CreacionDotacion,cd)
		self.Bind(wx.EVT_MENU, self.SubidaDotacion,sd)
		self.Bind(wx.EVT_MENU, self.CreacionModificacion,cm)
		self.Bind(wx.EVT_MENU, self.SubidaModificacion,sm)
		self.Bind(wx.EVT_MENU, self.CreacionCupos,cc)
		self.Bind(wx.EVT_MENU, self.SubidaCupos,sc)
		self.Bind(wx.EVT_MENU, self.BorrarSigfe,bs)
		self.Bind(wx.EVT_MENU, self.CargarSigfe,cs)
		self.Bind(wx.EVT_MENU, self.TablaCupos,tc)
		self.Bind(wx.EVT_MENU, self.TablaPresupuesto,tp)
		self.Bind(wx.EVT_MENU, self.TablaSigfe,ts)
		self.Bind(wx.EVT_MENU, self.BaseCompleta,bc)
		self.Bind(wx.EVT_MENU, self.TomaRazon,tr)

	def CreacionDotacion(self, event):#OK
		self.new = Creacion_Dotacion()
		self.new.Show()

	def SubidaDotacion(self,event):#OK
		import time
		self.new = Subida_Dotacion()
		self.new.Show()

	def CreacionModificacion(self,event):
		self.new = Creacion_Modificacion()
		self.new.Show()

	def SubidaModificacion(self,event):
		print ("Subida modificacion")

	def CreacionCupos(self,event):
		print ("Creacion Cupos")

	def SubidaCupos(self,event):
		print ("Subida Cupos")

	def BorrarSigfe(self,event):
		print ("Borrar Sigfe")

	def CargarSigfe(self,event):
		print ("Cargar Sigfe")

	def TablaCupos(self,event):#OK
		import os
		os.chdir('C:/Program Files/PostgreSQL/10/bin') #ojo con las / en lugar de \
		os.startfile("bat_respaldo_cupos.bat")

	def TablaPresupuesto(self,event):#OK
		import os
		os.chdir('C:/Program Files/PostgreSQL/10/bin') #ojo con las / en lugar de \
		os.startfile("bat_respaldo_presupuesto.bat")

	def TablaSigfe(self,event):#OK
		import os
		os.chdir('C:/Program Files/PostgreSQL/10/bin') #ojo con las / en lugar de \
		os.startfile("bat_respaldo_sigfe.bat")

	def BaseCompleta(self,event):#OK
		import os
		os.chdir('C:/Program Files/PostgreSQL/10/bin') #ojo con las / en lugar de \
		os.startfile("bat_respaldo_base.bat")

	def TomaRazon(self,event):
		print ("Toma Razon")

	def __del__( self ):
		pass

class Creacion_Dotacion(wx.Frame): #Pantalla para pedir datos de creacio dotacion y seleccionar archivo

	def __init__(self):

		import os
		"""Constructor"""
		wx.Frame.__init__(self, None, title="Ingrese datos",pos=(600,300),size=(300,200))
		panel = wx.Panel(self)

		self.currentDirectory = os.getcwd()

		my_sizer = wx.BoxSizer(wx.VERTICAL)

		openFileDlgBtn = wx.Button(panel, label="Seleccionar Archivo", pos=(30,120))
		openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
		my_sizer.Add(openFileDlgBtn, 0, wx.ALL|wx.CENTER, 5)

		lbl = wx.StaticText(panel, label="Año en números:")
		my_sizer.Add(lbl, 0, wx.ALL, 5)

		self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		my_sizer.Add(self.txt, 0, wx.ALL, 5)

		lbl2 = wx.StaticText(panel, label="Mes (use minusculas):")
		my_sizer.Add(lbl2, 0, wx.ALL, 5)


		self.txt2 = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
		self.txt2.SetFocus()
		self.txt2.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		my_sizer.Add(self.txt2, 0, wx.ALL, 5)


		panel.SetSizer(my_sizer)
		self.Show()

	#----------------------------------------------------------------------
	def OnEnter(self, event): #Aqui va el programa de creacion dotacion
		import os
		anio = self.txt.GetValue()
		mes = self.txt2.GetValue()
		self.Destroy()

		try:
			anio=int(float(anio))
			import csv
			import pandas as pd
			import numpy as np
			import re

			#la entrada es archivo con cod ss, cod establ, glosa y valor
			#convertirlo a formato de subida

			# para agrupar, se debe escribir agrupor y luego tab

			#lectura y preparación (OK)
			#<inicio #

			print("")
			print("leyendo base\n")

			# el archivo debería tener este formato: Cod SS, Cod Estab, Glosa,Valor,
			#importa el orden, no el nombre
			dfdot = pd.read_excel(str(path[0]))

			dfdot.loc[0, "SS"] = ""
			dfdot.loc[0, "Establ"] = ""
			dfdot.loc[0, "Cod Dipres"] = ""

			#</fin #

			#uso de diccionarios (OK)
			#<inicio #

			# diccionarios
			df1 = pd.read_excel("C:/Users/cmarinn/Google Drive/Python/Programa Revision/Tableau/Postgresql_Tableau/Estandarización.xlsx",
			                    sheet_name="SS y Establ QV a Tableau")
			df2 = pd.read_excel("C:/Users/cmarinn/Google Drive/Python/Programa Revision/Tableau/Postgresql_Tableau/Estandarización.xlsx",
			 					sheet_name="Glosas QV a Tableau")
			cabeceras1 = (list(df1))  # lista con las cabeceras
			cabeceras2 = (list(df2))  # lista con las cabeceras

			diccio_SS = {}  # crea el diccionario de cod servicio:servicio de salud
			for i in range(0, len(df1)):
			    diccio_SS[df1.loc[i, str(cabeceras1[0])]
			                 ] = df1.loc[i, str(cabeceras1[2])]

			diccio_codDipres = {} #diccionario cod ss: cod dipres
			for i in range(0, len(df1)):
			    diccio_codDipres[df1.loc[i, str(cabeceras1[0])]
			                     ] = df1.loc[i, str(cabeceras1[1])]

			diccio_establ = {}  # diccionario cod establ:nombre establ logra
			for i in range(0, len(df1)):
			    diccio_establ[df1.loc[i, str(cabeceras1[8])]
			                  ] = df1.loc[i, str(cabeceras1[9])]

			#uso de los diccionarios
			dfdot[dfdot.columns[4]].update(dfdot[dfdot.columns[0]].map(
			    diccio_SS))  # cod ss - servicio de salud

			dfdot[dfdot.columns[5]].update(dfdot[dfdot.columns[1]].map(
			    diccio_establ))  # cod establ - establ

			dfdot[dfdot.columns[6]].update(dfdot[dfdot.columns[0]].map(
			    diccio_codDipres))  # cod ss - cod dipres
			#</fin #

			#llevar los datos de dotacion al formato (OK)
			#<inicio #

			df_formato = pd.read_excel("C:/Users/cmarinn/Google Drive/Python/Programa Revision/Tableau/Postgresql_Tableau/FORMATO DOTACION.xlsx")

			df_formato[['CÓDIGO SIRH DEL SERVICIO DE SALUD', 'CÓDIGO SIRH DEL ESTABLECIMIENTO',
			            'Glosa', 'Devengado Moneda Año Estudio (2019)', ' Institucion Logra', 'Establecimiento Logra',
			            'CÓDIGO DIPRES DEL SERVICIO DE SALUD']] = dfdot[[dfdot.columns[0], dfdot.columns[1], dfdot.columns[2], dfdot.columns[3],
			                                                            'SS', 'Establ', 'Cod Dipres']]

			df_formato['año '] = anio
			df_formato['mes'] = mes
			df_formato.fillna(0, inplace=True)

			#</fin #

			#grabar archivo (OK)
			#<inicio #

			#lo grabo en la carpeta del programa y en la carpeta desde donde se buscó el archivo de origen
			df_formato.to_csv('dotacion_para_subir.csv', encoding='latin1',
			                  index=False, header=False)
			df_formato.to_csv('C:/Users/cmarinn/Google Drive/Python/Programa Revision/Tableau/Postgresql_Tableau/dotacion_para_subir.csv', encoding='latin1',
			                  index=False, header=False)

			print ('Archivo grabado con',len(df_formato),"filas")

			#</fin #

		except:
		 	print ("Debe ingresar un número entero")

	def onOpenFile(self, event):#Aqui se selecciona el archivo
	#Create and show the Open FileDialog
		wildcard = "All files (*.*)|*.*"
		dlg = wx.FileDialog(self, message="Elegir el archivo",
		defaultDir=self.currentDirectory, defaultFile="",
		wildcard=wildcard, style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
		)
		if dlg.ShowModal() == wx.ID_OK:
			global path
			path = dlg.GetPaths()
		dlg.Destroy()

class Subida_Dotacion(wx.Frame): #Pantalla para pedir datos de subida dotacion

	def __init__(self):

		import os
		"""Constructor"""
		wx.Frame.__init__(self, None, title="Confirme",pos=(600,300),size=(550,200))
		panel = wx.Panel(self)

		self.currentDirectory = os.getcwd()

		my_sizer = wx.BoxSizer(wx.VERTICAL)


		lbl = wx.StaticText(panel, label='''¿Está seguro que desea subir el archivo 'dotacion_para_subir.csv' a la tabla new_cupos_est?,\n Responda SI o NO:''')
		my_sizer.Add(lbl, 0, wx.ALL, 5)

		self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter1)
		my_sizer.Add(self.txt, 0, wx.ALL, 5)


		panel.SetSizer(my_sizer)
		self.Show()

	#----------------------------------------------------------------------
	def OnEnter1(self, event): #Aqui va el programa de subida dotacion
		import os
		import psycopg2
		respuesta = self.txt.GetValue()
		self.Destroy()
		try:
			connection = psycopg2.connect(user="admin", password="admin",
			                          host="localhost", port="5432", database="Gestion_RRHH")
			cursor = connection.cursor()
			# Print PostgreSQL Connection properties
			#print (connection.get_dsn_parameters(),"\n")
			print ("\nSe ha conectado satisfactoriamente a la base de datos","\n")
			# subir csv
			#print ("¿Está seguro que desea subir el archivo dotacion_para_subir.csv a la tabla new_cupos_est?")
			#print ("Responda: SI o NO","\n")
			if respuesta=='SI':
				with open('dotacion_para_subir.csv', 'r') as f:
					cursor.copy_from(f, 'new_cupos_est', sep=',')
					connection.commit()
					conteo=cursor.rowcount
					print ("Se han agregado",conteo,"filas a la tabla","\n")

			else:
				print ("No se ha realizado la acción")

		except (Exception, psycopg2.Error) as error:
		    print ("Error while connecting to PostgreSQL", error)
		finally:
		    #closing database connection.
		        if(connection):
		            cursor.close()
		            connection.close()
		            print("Conexión finalizada con PostgreSQL")

class Creacion_Modificacion(wx.Frame): #Pantalla para pedir archivo para modif presup
	def __init__(self):

		import os
		"""Constructor"""
		wx.Frame.__init__(self, None, title="Ingrese datos",pos=(600,300),size=(300,200))
		panel = wx.Panel(self)

		self.currentDirectory = os.getcwd()

		my_sizer = wx.BoxSizer(wx.VERTICAL)

		openFileDlgBtn = wx.Button(panel, label="Seleccionar Archivo", pos=(30,120))
		openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
		my_sizer.Add(openFileDlgBtn, 0, wx.ALL|wx.CENTER, 5)

		panel.SetSizer(my_sizer)
		self.Show()


#----------------------------------------------------------------------
	def OnEnter2(self, event): #Aqui va el programa de creacion modificacion
		import os
		self.Destroy()

		try:
			import csv
			import pandas as pd
			import numpy as np

			print("")
			print ("leyendo base\n")


			#crear tantas copias como meses queden para llegar a diciembre (OK)
			#<inicio #

			meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

			dfmodpresup = pd.read_excel(str(path[0]))

			mes_in=list(set(dfmodpresup['mes'].tolist()))
			print (mes_in)

			ind_inicio=meses.index(mes_in[0])
			print(ind_inicio)

			dfmeses=[]
			for i in range(ind_inicio,len(meses)):
			    dfmeses.append(dfmodpresup.copy())
			print ("cantidad de df por meses",len(dfmeses))

			#</fin #


			#cambiar en las copias de acuerdo a los meses que faltan (OK)
			#<inicio #

			for i in range (1, len(dfmeses)):
			    dfmeses[i].replace(mes_in,meses[ind_inicio+i], inplace=True)

			#</fin #


			#concatenar (OK)
			#<inicio #

			df_consolidado=pd.concat(dfmeses)

			#</fin #


			#grabar (OK)
			#<inicio #

			df_consolidado.to_csv('modif_presup_para_subir_consolidada.csv', encoding='latin1',
			                  index=False, header=False)

			print ("Archivo grabado con el nombre: modif_presup_para_subir.csv")

			#</fin #
		except:
			print("u")

	def onOpenFile(self, event):#Aqui se selecciona el archivo
		#Create and show the Open FileDialog
		wildcard = "All files (*.*)|*.*"
		dlg = wx.FileDialog(self, message="Elegir el archivo",
		defaultDir=self.currentDirectory, defaultFile="",
		wildcard=wildcard, style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
		)
		if dlg.ShowModal() == wx.ID_OK:
			global path
			path = dlg.GetPaths()
		dlg.Destroy()

if __name__ == "__main__":
	app = wx.App(False)
	frame = MyFrame5(None).Show()
	app.MainLoop()
