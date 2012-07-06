#!/bin/bash

rm interfaz.py ; pyuic4 interfaz_v005.ui -o interfaz.py

sed -i s/"from PyQt4 import QtCore, QtGui"/"from PyQt4 import QtCore, QtGui \nfrom completion import *"/g interfaz.py ; sed -i s/"self.namec = QtGui.QLineEdit(self.gridLayoutWidget_2)"/"self.namec = miQLineEdit(self.gridLayoutWidget_2)"/g interfaz.py
