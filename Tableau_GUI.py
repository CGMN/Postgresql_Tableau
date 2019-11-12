# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Nov  1 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sys

###########################################################################
## Class MyFrame5
###########################################################################

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


	def CreacionDotacion(self, event):
		import time
		self.new = NewWindow()
		self.new.Show()

	def SubidaDotacion(self,event):
		print ("Subida dotacion")

	def CreacionModificacion(self,event):
		print ("Creacion modificacion")

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

class NewWindow(wx.Frame):
	""""""

	#----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		wx.Frame.__init__(self, None, title="Ingrese datos",pos=(600,300),size=(300,200))
		panel = wx.Panel(self)

		my_sizer = wx.BoxSizer(wx.VERTICAL)

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
	def OnEnter(self, event):
		anio = self.txt.GetValue()
		mes = self.txt2.GetValue()
		print (anio)
		print (mes)
		self.Destroy()


if __name__ == "__main__":
	app = wx.App(False)
	frame = MyFrame5(None).Show()
	app.MainLoop()
