# -*- coding: utf-8 -*-

import wx
import wx.xrc
import sys

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Interfaz de apoyo para Tableau", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 900,-1 ), wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		log=self.m_textCtrl4 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0|wx.HSCROLL|wx.VSCROLL )
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
		d=self.Dotacion.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.Dotacion, wx.ID_ANY, u"Subida", wx.EmptyString, wx.ITEM_NORMAL )
		self.Dotacion.Append( self.m_menuItem3 )

		self.m_menu1.AppendSubMenu( self.Dotacion, u"Dotación" )

		self.ModPresupuestaria = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.ModPresupuestaria, wx.ID_ANY, u"Creación", wx.EmptyString, wx.ITEM_NORMAL )
		self.ModPresupuestaria.Append( self.m_menuItem4 )

		self.m_menuItem9 = wx.MenuItem( self.ModPresupuestaria, wx.ID_ANY, u"Subida", wx.EmptyString, wx.ITEM_NORMAL )
		self.ModPresupuestaria.Append( self.m_menuItem9 )

		self.m_menu1.AppendSubMenu( self.ModPresupuestaria, u"Mod. Presupuestaria" )

		self.Cupos = wx.Menu()
		self.m_menuItem10 = wx.MenuItem( self.Cupos, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Cupos.Append( self.m_menuItem10 )

		self.m_menuItem11 = wx.MenuItem( self.Cupos, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Cupos.Append( self.m_menuItem11 )

		self.m_menu1.AppendSubMenu( self.Cupos, u"Cupos" )

		self.Sigfe = wx.Menu()
		self.m_menuItem14 = wx.MenuItem( self.Sigfe, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Sigfe.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.Sigfe, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Sigfe.Append( self.m_menuItem15 )

		self.m_menu1.AppendSubMenu( self.Sigfe, u"Sigfe" )

		self.Respaldos = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Respaldos.Append( self.m_menuItem5 )

		self.m_menuItem6 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Respaldos.Append( self.m_menuItem6 )

		self.m_menuItem7 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Respaldos.Append( self.m_menuItem7 )

		self.m_menuItem8 = wx.MenuItem( self.Respaldos, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.Respaldos.Append( self.m_menuItem8 )

		self.m_menu1.AppendSubMenu( self.Respaldos, u"Respaldos" )

		self.ActualizacionesdeEstado = wx.Menu()
		self.m_menuItem12 = wx.MenuItem( self.ActualizacionesdeEstado, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.ActualizacionesdeEstado.Append( self.m_menuItem12 )

		self.m_menu1.AppendSubMenu( self.ActualizacionesdeEstado, u"Actualizaciones de Estado" )

		self.m_menubar1.Append( self.m_menu1, u"Menu" )

		self.SetMenuBar( self.m_menubar1 )

		self.Bind(wx.EVT_MENU,self.CreacionDotacion,d )

		self.Centre( wx.BOTH )

	def CreacionDotacion(self, event):
		print ("1")


	def __del__( self ):
		pass


if __name__ == "__main__":
	app = wx.App(False)
	frame = MyFrame5(None).Show()
	app.MainLoop()
