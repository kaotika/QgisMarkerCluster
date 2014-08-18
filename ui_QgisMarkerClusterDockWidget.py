# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_QgisMarkerClusterDockWidget.ui'
#
# Created: Fri Aug 15 16:25:18 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QgisMarkerClusterDockWidget(object):
    def setupUi(self, QgisMarkerClusterDockWidget):
        QgisMarkerClusterDockWidget.setObjectName(_fromUtf8("QgisMarkerClusterDockWidget"))
        QgisMarkerClusterDockWidget.resize(459, 314)
        QgisMarkerClusterDockWidget.setMinimumSize(QtCore.QSize(274, 293))
        QgisMarkerClusterDockWidget.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonLoadTestDataset = QtGui.QToolButton(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonLoadTestDataset.sizePolicy().hasHeightForWidth())
        self.buttonLoadTestDataset.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLoadTestDataset.setIcon(icon)
        self.buttonLoadTestDataset.setIconSize(QtCore.QSize(22, 22))
        self.buttonLoadTestDataset.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.buttonLoadTestDataset.setObjectName(_fromUtf8("buttonLoadTestDataset"))
        self.gridLayout.addWidget(self.buttonLoadTestDataset, 0, 0, 1, 1)
        self.buttonInfo = QtGui.QToolButton(self.dockWidgetContents)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/help-about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonInfo.setIcon(icon1)
        self.buttonInfo.setIconSize(QtCore.QSize(22, 22))
        self.buttonInfo.setObjectName(_fromUtf8("buttonInfo"))
        self.gridLayout.addWidget(self.buttonInfo, 0, 2, 1, 1)
        self.buttonClusterPoints = QtGui.QToolButton(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClusterPoints.sizePolicy().hasHeightForWidth())
        self.buttonClusterPoints.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonClusterPoints.setIcon(icon2)
        self.buttonClusterPoints.setIconSize(QtCore.QSize(24, 24))
        self.buttonClusterPoints.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.buttonClusterPoints.setObjectName(_fromUtf8("buttonClusterPoints"))
        self.gridLayout.addWidget(self.buttonClusterPoints, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEditClusterShapePath = QtGui.QLineEdit(self.groupBox)
        self.lineEditClusterShapePath.setReadOnly(True)
        self.lineEditClusterShapePath.setObjectName(_fromUtf8("lineEditClusterShapePath"))
        self.verticalLayout_2.addWidget(self.lineEditClusterShapePath)
        self.buttonLoadClusterDataset = QtGui.QToolButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonLoadClusterDataset.sizePolicy().hasHeightForWidth())
        self.buttonLoadClusterDataset.setSizePolicy(sizePolicy)
        self.buttonLoadClusterDataset.setIcon(icon)
        self.buttonLoadClusterDataset.setIconSize(QtCore.QSize(22, 22))
        self.buttonLoadClusterDataset.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.buttonLoadClusterDataset.setObjectName(_fromUtf8("buttonLoadClusterDataset"))
        self.verticalLayout_2.addWidget(self.buttonLoadClusterDataset)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.doubleSpinBoxClusterDistance = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBoxClusterDistance.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxClusterDistance.setDecimals(4)
        self.doubleSpinBoxClusterDistance.setMinimum(0.0)
        self.doubleSpinBoxClusterDistance.setMaximum(999999999.0)
        self.doubleSpinBoxClusterDistance.setProperty("value", 50.0)
        self.doubleSpinBoxClusterDistance.setObjectName(_fromUtf8("doubleSpinBoxClusterDistance"))
        self.verticalLayout.addWidget(self.doubleSpinBoxClusterDistance)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        QgisMarkerClusterDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(QgisMarkerClusterDockWidget)
        QtCore.QMetaObject.connectSlotsByName(QgisMarkerClusterDockWidget)

    def retranslateUi(self, QgisMarkerClusterDockWidget):
        QgisMarkerClusterDockWidget.setWindowTitle(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "Qgis Marker Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadTestDataset.setToolTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "load selected dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadTestDataset.setStatusTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "load selected dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadTestDataset.setText(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "1. Load Point Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonInfo.setToolTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "Show information", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonInfo.setStatusTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "Show information", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonInfo.setText(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "OSM", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClusterPoints.setToolTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "Show information", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClusterPoints.setStatusTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "Cluster Points", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonClusterPoints.setText(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "2. Setup First Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "Cluster Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadClusterDataset.setToolTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "load selected dataset", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadClusterDataset.setStatusTip(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "add cluster shape", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonLoadClusterDataset.setText(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "3. Add more cluster shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("QgisMarkerClusterDockWidget", "Cluster Distance", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
