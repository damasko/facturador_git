# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_v005.ui'
#
# Created: Fri Jul 13 15:01:47 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui 
from completion import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_albaran(object):
    def setupUi(self, albaran):
        albaran.setObjectName(_fromUtf8("albaran"))
        albaran.setWindowModality(QtCore.Qt.NonModal)
        albaran.resize(899, 542)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(albaran.sizePolicy().hasHeightForWidth())
        albaran.setSizePolicy(sizePolicy)
        albaran.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(albaran)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.boxitems = QtGui.QComboBox(self.centralwidget)
        self.boxitems.setMinimumSize(QtCore.QSize(120, 0))
        self.boxitems.setObjectName(_fromUtf8("boxitems"))
        self.horizontalLayout_8.addWidget(self.boxitems)
        self.newti = QtGui.QLineEdit(self.centralwidget)
        self.newti.setMinimumSize(QtCore.QSize(120, 0))
        self.newti.setObjectName(_fromUtf8("newti"))
        self.horizontalLayout_8.addWidget(self.newti)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.precio_item = QtGui.QLineEdit(self.centralwidget)
        self.precio_item.setMinimumSize(QtCore.QSize(100, 0))
        self.precio_item.setObjectName(_fromUtf8("precio_item"))
        self.horizontalLayout_8.addWidget(self.precio_item)
        self.nuevoitem = QtGui.QPushButton(self.centralwidget)
        self.nuevoitem.setObjectName(_fromUtf8("nuevoitem"))
        self.horizontalLayout_8.addWidget(self.nuevoitem)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 2, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.agregait = QtGui.QPushButton(self.centralwidget)
        self.agregait.setMinimumSize(QtCore.QSize(180, 0))
        self.agregait.setObjectName(_fromUtf8("agregait"))
        self.gridLayout_6.addWidget(self.agregait, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 2, 2, 1, 1)
        self.nal = QtGui.QLabel(self.centralwidget)
        self.nal.setObjectName(_fromUtf8("nal"))
        self.gridLayout_4.addWidget(self.nal, 1, 1, 1, 1)
        self.cantidad = QtGui.QLineEdit(self.centralwidget)
        self.cantidad.setMinimumSize(QtCore.QSize(100, 0))
        self.cantidad.setReadOnly(False)
        self.cantidad.setObjectName(_fromUtf8("cantidad"))
        self.gridLayout_4.addWidget(self.cantidad, 2, 1, 1, 1)
        self.rm_item = QtGui.QPushButton(self.centralwidget)
        self.rm_item.setMinimumSize(QtCore.QSize(110, 0))
        self.rm_item.setObjectName(_fromUtf8("rm_item"))
        self.gridLayout_4.addWidget(self.rm_item, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.fel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.fel.setFont(font)
        self.fel.setObjectName(_fromUtf8("fel"))
        self.horizontalLayout_3.addWidget(self.fel)
        self.boxfacs = QtGui.QComboBox(self.centralwidget)
        self.boxfacs.setMinimumSize(QtCore.QSize(150, 0))
        self.boxfacs.setObjectName(_fromUtf8("boxfacs"))
        self.horizontalLayout_3.addWidget(self.boxfacs)
        self.nfl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.nfl.setFont(font)
        self.nfl.setObjectName(_fromUtf8("nfl"))
        self.horizontalLayout_3.addWidget(self.nfl)
        self.nf = QtGui.QLineEdit(self.centralwidget)
        self.nf.setMinimumSize(QtCore.QSize(150, 0))
        self.nf.setObjectName(_fromUtf8("nf"))
        self.horizontalLayout_3.addWidget(self.nf)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.nifl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nifl.setFont(font)
        self.nifl.setObjectName(_fromUtf8("nifl"))
        self.horizontalLayout_4.addWidget(self.nifl)
        self.nif = QtGui.QLineEdit(self.centralwidget)
        self.nif.setObjectName(_fromUtf8("nif"))
        self.horizontalLayout_4.addWidget(self.nif)
        self.poblacionl = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.poblacionl.setFont(font)
        self.poblacionl.setObjectName(_fromUtf8("poblacionl"))
        self.horizontalLayout_4.addWidget(self.poblacionl)
        self.poblacion = QtGui.QLineEdit(self.centralwidget)
        self.poblacion.setObjectName(_fromUtf8("poblacion"))
        self.horizontalLayout_4.addWidget(self.poblacion)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clil = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.clil.setFont(font)
        self.clil.setObjectName(_fromUtf8("clil"))
        self.horizontalLayout.addWidget(self.clil)
        self.boxclient = QtGui.QComboBox(self.centralwidget)
        self.boxclient.setMinimumSize(QtCore.QSize(200, 0))
        self.boxclient.setObjectName(_fromUtf8("boxclient"))
        self.horizontalLayout.addWidget(self.boxclient)
        self.namec = miQLineEdit(self.centralwidget)
        self.namec.setMinimumSize(QtCore.QSize(200, 0))
        self.namec.setObjectName(_fromUtf8("namec"))
        self.horizontalLayout.addWidget(self.namec)
        self.addclienteB = QtGui.QPushButton(self.centralwidget)
        self.addclienteB.setObjectName(_fromUtf8("addclienteB"))
        self.horizontalLayout.addWidget(self.addclienteB)
        self.rm_cliente = QtGui.QPushButton(self.centralwidget)
        self.rm_cliente.setObjectName(_fromUtf8("rm_cliente"))
        self.horizontalLayout.addWidget(self.rm_cliente)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.callel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.callel.setFont(font)
        self.callel.setObjectName(_fromUtf8("callel"))
        self.horizontalLayout_5.addWidget(self.callel)
        self.calle = QtGui.QLineEdit(self.centralwidget)
        self.calle.setObjectName(_fromUtf8("calle"))
        self.horizontalLayout_5.addWidget(self.calle)
        self.pagol = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pagol.setFont(font)
        self.pagol.setObjectName(_fromUtf8("pagol"))
        self.horizontalLayout_5.addWidget(self.pagol)
        self.pago = QtGui.QLineEdit(self.centralwidget)
        self.pago.setObjectName(_fromUtf8("pago"))
        self.horizontalLayout_5.addWidget(self.pago)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 5, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.precio_fac = QtGui.QLineEdit(self.centralwidget)
        self.precio_fac.setReadOnly(True)
        self.precio_fac.setObjectName(_fromUtf8("precio_fac"))
        self.gridLayout_7.addWidget(self.precio_fac, 1, 3, 1, 1)
        self.cantidad_ro = QtGui.QLineEdit(self.centralwidget)
        self.cantidad_ro.setReadOnly(True)
        self.cantidad_ro.setObjectName(_fromUtf8("cantidad_ro"))
        self.gridLayout_7.addWidget(self.cantidad_ro, 1, 1, 1, 1)
        self.cantidadl_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cantidadl_2.setFont(font)
        self.cantidadl_2.setObjectName(_fromUtf8("cantidadl_2"))
        self.gridLayout_7.addWidget(self.cantidadl_2, 0, 1, 1, 1)
        self.preciol_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.preciol_2.setFont(font)
        self.preciol_2.setObjectName(_fromUtf8("preciol_2"))
        self.gridLayout_7.addWidget(self.preciol_2, 0, 3, 1, 1)
        self.itemfac = QtGui.QComboBox(self.centralwidget)
        self.itemfac.setMinimumSize(QtCore.QSize(150, 0))
        self.itemfac.setObjectName(_fromUtf8("itemfac"))
        self.gridLayout_7.addWidget(self.itemfac, 1, 2, 1, 1)
        self.articulol_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.articulol_2.setFont(font)
        self.articulol_2.setObjectName(_fromUtf8("articulol_2"))
        self.gridLayout_7.addWidget(self.articulol_2, 0, 2, 1, 1)
        self.rmitemfacB = QtGui.QPushButton(self.centralwidget)
        self.rmitemfacB.setObjectName(_fromUtf8("rmitemfacB"))
        self.gridLayout_7.addWidget(self.rmitemfacB, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_8.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_8.addWidget(self.label_6, 0, 1, 1, 1)
        self.calculaImporteB = QtGui.QPushButton(self.centralwidget)
        self.calculaImporteB.setObjectName(_fromUtf8("calculaImporteB"))
        self.gridLayout_8.addWidget(self.calculaImporteB, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_8.addWidget(self.label_7, 0, 4, 1, 1)
        self.importe = QtGui.QLineEdit(self.centralwidget)
        self.importe.setReadOnly(True)
        self.importe.setObjectName(_fromUtf8("importe"))
        self.gridLayout_8.addWidget(self.importe, 1, 1, 1, 1)
        self.iva = QtGui.QLineEdit(self.centralwidget)
        self.iva.setObjectName(_fromUtf8("iva"))
        self.gridLayout_8.addWidget(self.iva, 1, 2, 1, 1)
        self.total = QtGui.QLineEdit(self.centralwidget)
        self.total.setReadOnly(True)
        self.total.setObjectName(_fromUtf8("total"))
        self.gridLayout_8.addWidget(self.total, 1, 4, 1, 1)
        self.iva_a = QtGui.QLineEdit(self.centralwidget)
        self.iva_a.setReadOnly(True)
        self.iva_a.setObjectName(_fromUtf8("iva_a"))
        self.gridLayout_8.addWidget(self.iva_a, 1, 3, 1, 1)
        self.iva_por = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.iva_por.setFont(font)
        self.iva_por.setObjectName(_fromUtf8("iva_por"))
        self.gridLayout_8.addWidget(self.iva_por, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_8, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 6, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.exitb = QtGui.QPushButton(self.centralwidget)
        self.exitb.setObjectName(_fromUtf8("exitb"))
        self.gridLayout.addWidget(self.exitb, 1, 1, 1, 1)
        self.guardartodoB = QtGui.QPushButton(self.centralwidget)
        self.guardartodoB.setMaximumSize(QtCore.QSize(200, 16777215))
        self.guardartodoB.setObjectName(_fromUtf8("guardartodoB"))
        self.gridLayout.addWidget(self.guardartodoB, 0, 1, 1, 1)
        self.rmallfac = QtGui.QPushButton(self.centralwidget)
        self.rmallfac.setMaximumSize(QtCore.QSize(200, 16777215))
        self.rmallfac.setObjectName(_fromUtf8("rmallfac"))
        self.gridLayout.addWidget(self.rmallfac, 1, 0, 1, 1)
        self.newfacB = QtGui.QPushButton(self.centralwidget)
        self.newfacB.setObjectName(_fromUtf8("newfacB"))
        self.gridLayout.addWidget(self.newfacB, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.de2l = QtGui.QLabel(self.centralwidget)
        self.de2l.setMinimumSize(QtCore.QSize(50, 0))
        self.de2l.setMaximumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.de2l.setFont(font)
        self.de2l.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.de2l.setObjectName(_fromUtf8("de2l"))
        self.horizontalLayout_2.addWidget(self.de2l)
        self.de3 = QtGui.QLineEdit(self.centralwidget)
        self.de3.setMinimumSize(QtCore.QSize(200, 0))
        self.de3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.de3.setObjectName(_fromUtf8("de3"))
        self.horizontalLayout_2.addWidget(self.de3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        albaran.setCentralWidget(self.centralwidget)

        self.retranslateUi(albaran)
        QtCore.QObject.connect(self.exitb, QtCore.SIGNAL(_fromUtf8("clicked()")), albaran.close)
        QtCore.QMetaObject.connectSlotsByName(albaran)
        albaran.setTabOrder(self.nf, self.namec)
        albaran.setTabOrder(self.namec, self.nif)
        albaran.setTabOrder(self.nif, self.poblacion)
        albaran.setTabOrder(self.poblacion, self.calle)
        albaran.setTabOrder(self.calle, self.pago)
        albaran.setTabOrder(self.pago, self.newti)
        albaran.setTabOrder(self.newti, self.precio_item)
        albaran.setTabOrder(self.precio_item, self.cantidad_ro)
        albaran.setTabOrder(self.cantidad_ro, self.precio_fac)
        albaran.setTabOrder(self.precio_fac, self.boxfacs)
        albaran.setTabOrder(self.boxfacs, self.boxclient)
        albaran.setTabOrder(self.boxclient, self.itemfac)
        albaran.setTabOrder(self.itemfac, self.addclienteB)
        albaran.setTabOrder(self.addclienteB, self.rm_cliente)
        albaran.setTabOrder(self.rm_cliente, self.nuevoitem)
        albaran.setTabOrder(self.nuevoitem, self.agregait)
        albaran.setTabOrder(self.agregait, self.rmitemfacB)
        albaran.setTabOrder(self.rmitemfacB, self.calculaImporteB)
        albaran.setTabOrder(self.calculaImporteB, self.guardartodoB)
        albaran.setTabOrder(self.guardartodoB, self.exitb)

    def retranslateUi(self, albaran):
        albaran.setWindowTitle(QtGui.QApplication.translate("albaran", "Facturador", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("albaran", "Precio:", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevoitem.setText(QtGui.QApplication.translate("albaran", "⇠ Añadir/Actualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.agregait.setText(QtGui.QApplication.translate("albaran", "⇣ Agregar a la factura ⇣", None, QtGui.QApplication.UnicodeUTF8))
        self.nal.setText(QtGui.QApplication.translate("albaran", "Tipo de articulo:", None, QtGui.QApplication.UnicodeUTF8))
        self.rm_item.setText(QtGui.QApplication.translate("albaran", "Borrar Item  ⇢", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("albaran", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("albaran", "Base de datos Items:", None, QtGui.QApplication.UnicodeUTF8))
        self.fel.setText(QtGui.QApplication.translate("albaran", "Facturas Existentes:", None, QtGui.QApplication.UnicodeUTF8))
        self.nfl.setText(QtGui.QApplication.translate("albaran", "Factura Nº", None, QtGui.QApplication.UnicodeUTF8))
        self.nifl.setText(QtGui.QApplication.translate("albaran", "N.I.F:", None, QtGui.QApplication.UnicodeUTF8))
        self.poblacionl.setText(QtGui.QApplication.translate("albaran", "Poblacion:", None, QtGui.QApplication.UnicodeUTF8))
        self.clil.setText(QtGui.QApplication.translate("albaran", "Cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.addclienteB.setText(QtGui.QApplication.translate("albaran", "⇠ Agregar a la base de datos Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.rm_cliente.setText(QtGui.QApplication.translate("albaran", "☠ Eliminar Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.callel.setText(QtGui.QApplication.translate("albaran", "Calle:", None, QtGui.QApplication.UnicodeUTF8))
        self.pagol.setText(QtGui.QApplication.translate("albaran", "Pago:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("albaran", "Datos del cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.cantidadl_2.setText(QtGui.QApplication.translate("albaran", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.preciol_2.setText(QtGui.QApplication.translate("albaran", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.articulol_2.setText(QtGui.QApplication.translate("albaran", "Tipo de Articulo", None, QtGui.QApplication.UnicodeUTF8))
        self.rmitemfacB.setText(QtGui.QApplication.translate("albaran", "Quitar Item ⇢", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("albaran", "I.V.A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("albaran", "Importe", None, QtGui.QApplication.UnicodeUTF8))
        self.calculaImporteB.setText(QtGui.QApplication.translate("albaran", "Calcular", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("albaran", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.iva_por.setText(QtGui.QApplication.translate("albaran", " Cantidad I.V.A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("albaran", "Calculo del importe:", None, QtGui.QApplication.UnicodeUTF8))
        self.exitb.setText(QtGui.QApplication.translate("albaran", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.guardartodoB.setText(QtGui.QApplication.translate("albaran", "Guardar Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.rmallfac.setText(QtGui.QApplication.translate("albaran", "☢ Eliminar Factura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.newfacB.setText(QtGui.QApplication.translate("albaran", "Nueva Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.de2l.setText(QtGui.QApplication.translate("albaran", "Fecha ", None, QtGui.QApplication.UnicodeUTF8))

