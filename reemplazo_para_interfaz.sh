#!/bin/bash

rm interfaz.py ; pyuic4 interfaz_v005.ui -o interfaz.py

sed -i s/"from PyQt4 import QtCore, QtGui"/"from PyQt4 import QtCore, QtGui \nfrom completion import *"/g interfaz.py ; sed -i s/"self.namec = QtGui.QLineEdit(self.centralwidget)"/"self.namec = miQLineEdit(self.centralwidget)"/g interfaz.py
