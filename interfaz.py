# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_v004.ui'
#
# Created: Wed Jul  4 23:46:53 2012
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
        albaran.resize(821, 604)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(albaran.sizePolicy().hasHeightForWidth())
        albaran.setSizePolicy(sizePolicy)
        albaran.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(albaran)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 390, 781, 146))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.precio_2 = QtGui.QLineEdit(self.gridLayoutWidget_5)
        self.precio_2.setObjectName(_fromUtf8("precio_2"))
        self.gridLayout_7.addWidget(self.precio_2, 1, 3, 1, 1)
        self.cantidad_2 = QtGui.QLineEdit(self.gridLayoutWidget_5)
        self.cantidad_2.setObjectName(_fromUtf8("cantidad_2"))
        self.gridLayout_7.addWidget(self.cantidad_2, 1, 1, 1, 1)
        self.cantidadl_2 = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cantidadl_2.setFont(font)
        self.cantidadl_2.setObjectName(_fromUtf8("cantidadl_2"))
        self.gridLayout_7.addWidget(self.cantidadl_2, 0, 1, 1, 1)
        self.preciol_2 = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.preciol_2.setFont(font)
        self.preciol_2.setObjectName(_fromUtf8("preciol_2"))
        self.gridLayout_7.addWidget(self.preciol_2, 0, 3, 1, 1)
        self.boxitems_2 = QtGui.QComboBox(self.gridLayoutWidget_5)
        self.boxitems_2.setMinimumSize(QtCore.QSize(150, 0))
        self.boxitems_2.setObjectName(_fromUtf8("boxitems_2"))
        self.gridLayout_7.addWidget(self.boxitems_2, 1, 2, 1, 1)
        self.articulol_2 = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.articulol_2.setFont(font)
        self.articulol_2.setObjectName(_fromUtf8("articulol_2"))
        self.gridLayout_7.addWidget(self.articulol_2, 0, 2, 1, 1)
        self.rmItemAct = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.rmItemAct.setObjectName(_fromUtf8("rmItemAct"))
        self.gridLayout_7.addWidget(self.rmItemAct, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_8.addWidget(self.label_5, 0, 2, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.gridLayoutWidget_5)
        self.textEdit.setMaximumSize(QtCore.QSize(100, 28))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_8.addWidget(self.textEdit, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_5)
        self.label_6.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_8.addWidget(self.label_6, 0, 1, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.gridLayoutWidget_5)
        self.textEdit_3.setMaximumSize(QtCore.QSize(100, 28))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout_8.addWidget(self.textEdit_3, 1, 3, 1, 1)
        self.calculaImporteB = QtGui.QPushButton(self.gridLayoutWidget_5)
        self.calculaImporteB.setObjectName(_fromUtf8("calculaImporteB"))
        self.gridLayout_8.addWidget(self.calculaImporteB, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_8.addWidget(self.label_7, 0, 3, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.gridLayoutWidget_5)
        self.textEdit_2.setMaximumSize(QtCore.QSize(100, 28))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_8.addWidget(self.textEdit_2, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_8, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 10, 667, 37))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.fel.setFont(font)
        self.fel.setObjectName(_fromUtf8("fel"))
        self.horizontalLayout_3.addWidget(self.fel)
        self.boxfacs = QtGui.QComboBox(self.layoutWidget)
        self.boxfacs.setMinimumSize(QtCore.QSize(150, 0))
        self.boxfacs.setObjectName(_fromUtf8("boxfacs"))
        self.horizontalLayout_3.addWidget(self.boxfacs)
        self.nfl = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.nfl.setFont(font)
        self.nfl.setObjectName(_fromUtf8("nfl"))
        self.horizontalLayout_3.addWidget(self.nfl)
        self.nf = QtGui.QLineEdit(self.layoutWidget)
        self.nf.setObjectName(_fromUtf8("nf"))
        self.horizontalLayout_3.addWidget(self.nf)
        self.addf = QtGui.QPushButton(self.layoutWidget)
        self.addf.setObjectName(_fromUtf8("addf"))
        self.horizontalLayout_3.addWidget(self.addf)
        self.layoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(140, 550, 661, 41))
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.GuardarTodoB = QtGui.QPushButton(self.layoutWidget_7)
        self.GuardarTodoB.setObjectName(_fromUtf8("GuardarTodoB"))
        self.horizontalLayout_9.addWidget(self.GuardarTodoB)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.rmclienteB = QtGui.QPushButton(self.layoutWidget_7)
        self.rmclienteB.setObjectName(_fromUtf8("rmclienteB"))
        self.horizontalLayout_9.addWidget(self.rmclienteB)
        self.rmallfac = QtGui.QPushButton(self.layoutWidget_7)
        self.rmallfac.setObjectName(_fromUtf8("rmallfac"))
        self.horizontalLayout_9.addWidget(self.rmallfac)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.exitb = QtGui.QPushButton(self.layoutWidget_7)
        self.exitb.setObjectName(_fromUtf8("exitb"))
        self.horizontalLayout_9.addWidget(self.exitb)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 90, 781, 141))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.nifl = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.nifl.setFont(font)
        self.nifl.setObjectName(_fromUtf8("nifl"))
        self.horizontalLayout_4.addWidget(self.nifl)
        self.nif = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.nif.setObjectName(_fromUtf8("nif"))
        self.horizontalLayout_4.addWidget(self.nif)
        self.poblacionl = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.poblacionl.setFont(font)
        self.poblacionl.setObjectName(_fromUtf8("poblacionl"))
        self.horizontalLayout_4.addWidget(self.poblacionl)
        self.poblacion = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.poblacion.setObjectName(_fromUtf8("poblacion"))
        self.horizontalLayout_4.addWidget(self.poblacion)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clil = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.clil.setFont(font)
        self.clil.setObjectName(_fromUtf8("clil"))
        self.horizontalLayout.addWidget(self.clil)
        self.boxclient = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.boxclient.setMinimumSize(QtCore.QSize(200, 0))
        self.boxclient.setObjectName(_fromUtf8("boxclient"))
        self.horizontalLayout.addWidget(self.boxclient)
        self.namec = miQLineEdit(self.gridLayoutWidget_2)
        self.namec.setObjectName(_fromUtf8("namec"))
        self.horizontalLayout.addWidget(self.namec)
        self.addclienteB = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.addclienteB.setObjectName(_fromUtf8("addclienteB"))
        self.horizontalLayout.addWidget(self.addclienteB)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.callel = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.callel.setFont(font)
        self.callel.setObjectName(_fromUtf8("callel"))
        self.horizontalLayout_5.addWidget(self.callel)
        self.calle = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.calle.setObjectName(_fromUtf8("calle"))
        self.horizontalLayout_5.addWidget(self.calle)
        self.pagol = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pagol.setFont(font)
        self.pagol.setObjectName(_fromUtf8("pagol"))
        self.horizontalLayout_5.addWidget(self.pagol)
        self.pago = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.pago.setObjectName(_fromUtf8("pago"))
        self.horizontalLayout_5.addWidget(self.pago)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 250, 781, 121))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        self.newci = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.newci.setObjectName(_fromUtf8("newci"))
        self.horizontalLayout_8.addWidget(self.newci)
        self.nal = QtGui.QLabel(self.gridLayoutWidget_3)
        self.nal.setObjectName(_fromUtf8("nal"))
        self.horizontalLayout_8.addWidget(self.nal)
        self.newti = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.newti.setObjectName(_fromUtf8("newti"))
        self.horizontalLayout_8.addWidget(self.newti)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.npre = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.npre.setObjectName(_fromUtf8("npre"))
        self.horizontalLayout_8.addWidget(self.npre)
        self.nuevoitem = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.nuevoitem.setObjectName(_fromUtf8("nuevoitem"))
        self.horizontalLayout_8.addWidget(self.nuevoitem)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.cantidadl = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.cantidadl.setFont(font)
        self.cantidadl.setObjectName(_fromUtf8("cantidadl"))
        self.gridLayout_6.addWidget(self.cantidadl, 0, 1, 1, 1)
        self.articulol = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.articulol.setFont(font)
        self.articulol.setObjectName(_fromUtf8("articulol"))
        self.gridLayout_6.addWidget(self.articulol, 0, 2, 1, 1)
        self.preciol = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.preciol.setFont(font)
        self.preciol.setObjectName(_fromUtf8("preciol"))
        self.gridLayout_6.addWidget(self.preciol, 0, 3, 1, 1)
        self.boxitems = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.boxitems.setMinimumSize(QtCore.QSize(150, 0))
        self.boxitems.setObjectName(_fromUtf8("boxitems"))
        self.gridLayout_6.addWidget(self.boxitems, 1, 2, 1, 1)
        self.cantidad = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.cantidad.setObjectName(_fromUtf8("cantidad"))
        self.gridLayout_6.addWidget(self.cantidad, 1, 1, 1, 1)
        self.cleari = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.cleari.setObjectName(_fromUtf8("cleari"))
        self.gridLayout_6.addWidget(self.cleari, 1, 0, 1, 1)
        self.precio = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.precio.setObjectName(_fromUtf8("precio"))
        self.gridLayout_6.addWidget(self.precio, 1, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(500, 50, 301, 29))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.de2l = QtGui.QLabel(self.layoutWidget_2)
        self.de2l.setMinimumSize(QtCore.QSize(50, 0))
        self.de2l.setMaximumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.de2l.setFont(font)
        self.de2l.setObjectName(_fromUtf8("de2l"))
        self.horizontalLayout_2.addWidget(self.de2l)
        self.de3 = QtGui.QLineEdit(self.layoutWidget_2)
        self.de3.setMinimumSize(QtCore.QSize(200, 0))
        self.de3.setObjectName(_fromUtf8("de3"))
        self.horizontalLayout_2.addWidget(self.de3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 230, 781, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 370, 781, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 530, 781, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        albaran.setCentralWidget(self.centralwidget)

        self.retranslateUi(albaran)
        QtCore.QObject.connect(self.exitb, QtCore.SIGNAL(_fromUtf8("clicked()")), albaran.close)
        QtCore.QMetaObject.connectSlotsByName(albaran)

    def retranslateUi(self, albaran):
        albaran.setWindowTitle(QtGui.QApplication.translate("albaran", "Facturador", None, QtGui.QApplication.UnicodeUTF8))
        self.cantidadl_2.setText(QtGui.QApplication.translate("albaran", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.preciol_2.setText(QtGui.QApplication.translate("albaran", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.articulol_2.setText(QtGui.QApplication.translate("albaran", "Tipo de Articulo", None, QtGui.QApplication.UnicodeUTF8))
        self.rmItemAct.setText(QtGui.QApplication.translate("albaran", "Borrar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("albaran", "I.V.A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("albaran", "Importe", None, QtGui.QApplication.UnicodeUTF8))
        self.calculaImporteB.setText(QtGui.QApplication.translate("albaran", "Calcular", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("albaran", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("albaran", "Factura ", None, QtGui.QApplication.UnicodeUTF8))
        self.fel.setText(QtGui.QApplication.translate("albaran", "Facturas Existentes:", None, QtGui.QApplication.UnicodeUTF8))
        self.nfl.setText(QtGui.QApplication.translate("albaran", "Factura Nº", None, QtGui.QApplication.UnicodeUTF8))
        self.addf.setText(QtGui.QApplication.translate("albaran", "<< Guardar/Actualizar Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.GuardarTodoB.setText(QtGui.QApplication.translate("albaran", "Guardar Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.rmclienteB.setText(QtGui.QApplication.translate("albaran", "Eliminar Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.rmallfac.setText(QtGui.QApplication.translate("albaran", "Eliminar Factura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.exitb.setText(QtGui.QApplication.translate("albaran", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.nifl.setText(QtGui.QApplication.translate("albaran", "N.I.F:", None, QtGui.QApplication.UnicodeUTF8))
        self.poblacionl.setText(QtGui.QApplication.translate("albaran", "Poblacion:", None, QtGui.QApplication.UnicodeUTF8))
        self.clil.setText(QtGui.QApplication.translate("albaran", "Cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.addclienteB.setText(QtGui.QApplication.translate("albaran", "Crear/Actualizar Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("albaran", "Datos del cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.callel.setText(QtGui.QApplication.translate("albaran", "Calle:", None, QtGui.QApplication.UnicodeUTF8))
        self.pagol.setText(QtGui.QApplication.translate("albaran", "Pago:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("albaran", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.nal.setText(QtGui.QApplication.translate("albaran", "tipo de articulo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("albaran", "Precio:", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevoitem.setText(QtGui.QApplication.translate("albaran", "<< Añadir/Actualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.cantidadl.setText(QtGui.QApplication.translate("albaran", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.articulol.setText(QtGui.QApplication.translate("albaran", "Tipo de Articulo", None, QtGui.QApplication.UnicodeUTF8))
        self.preciol.setText(QtGui.QApplication.translate("albaran", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.cleari.setText(QtGui.QApplication.translate("albaran", "Clear >>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("albaran", "Base de datos Items", None, QtGui.QApplication.UnicodeUTF8))
        self.de2l.setText(QtGui.QApplication.translate("albaran", "Fecha ", None, QtGui.QApplication.UnicodeUTF8))

