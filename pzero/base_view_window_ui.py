# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base_view_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaseViewWindow(object):
    def setupUi(self, BaseViewWindow):
        BaseViewWindow.setObjectName("BaseViewWindow")
        BaseViewWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(BaseViewWindow.sizePolicy().hasHeightForWidth())
        BaseViewWindow.setSizePolicy(sizePolicy)
        BaseViewWindow.setMinimumSize(QtCore.QSize(1280, 800))
        BaseViewWindow.setBaseSize(QtCore.QSize(0, 30))
        BaseViewWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(BaseViewWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 726))
        self.centralwidget.setBaseSize(QtCore.QSize(1280, 726))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setBaseSize(QtCore.QSize(0, 0))
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.toolBox = QtWidgets.QToolBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBox.setBaseSize(QtCore.QSize(0, 0))
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox.setObjectName("toolBox")
        self.GeologyTreePage = QtWidgets.QWidget()
        self.GeologyTreePage.setGeometry(QtCore.QRect(0, 0, 282, 448))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.GeologyTreePage.sizePolicy().hasHeightForWidth())
        self.GeologyTreePage.setSizePolicy(sizePolicy)
        self.GeologyTreePage.setMinimumSize(QtCore.QSize(0, 0))
        self.GeologyTreePage.setBaseSize(QtCore.QSize(0, 0))
        self.GeologyTreePage.setObjectName("GeologyTreePage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.GeologyTreePage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.GeologyTreeWidget = QtWidgets.QTreeWidget(self.GeologyTreePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.GeologyTreeWidget.sizePolicy().hasHeightForWidth())
        self.GeologyTreeWidget.setSizePolicy(sizePolicy)
        self.GeologyTreeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.GeologyTreeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.GeologyTreeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.GeologyTreeWidget.setObjectName("GeologyTreeWidget")
        self.GeologyTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_7.addWidget(self.GeologyTreeWidget)
        self.toolBox.addItem(self.GeologyTreePage, "")
        self.TopologyTreePage = QtWidgets.QWidget()
        self.TopologyTreePage.setGeometry(QtCore.QRect(0, 0, 282, 448))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.TopologyTreePage.sizePolicy().hasHeightForWidth())
        self.TopologyTreePage.setSizePolicy(sizePolicy)
        self.TopologyTreePage.setMinimumSize(QtCore.QSize(0, 0))
        self.TopologyTreePage.setBaseSize(QtCore.QSize(0, 0))
        self.TopologyTreePage.setObjectName("TopologyTreePage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.TopologyTreePage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.TopologyTreeWidget = QtWidgets.QTreeWidget(self.TopologyTreePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.TopologyTreeWidget.sizePolicy().hasHeightForWidth())
        self.TopologyTreeWidget.setSizePolicy(sizePolicy)
        self.TopologyTreeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.TopologyTreeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.TopologyTreeWidget.setObjectName("TopologyTreeWidget")
        self.TopologyTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_6.addWidget(self.TopologyTreeWidget)
        self.toolBox.addItem(self.TopologyTreePage, "")
        self.XSectionListPage = QtWidgets.QWidget()
        self.XSectionListPage.setGeometry(QtCore.QRect(0, 0, 282, 448))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.XSectionListPage.sizePolicy().hasHeightForWidth())
        self.XSectionListPage.setSizePolicy(sizePolicy)
        self.XSectionListPage.setMinimumSize(QtCore.QSize(0, 0))
        self.XSectionListPage.setBaseSize(QtCore.QSize(0, 0))
        self.XSectionListPage.setObjectName("XSectionListPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.XSectionListPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.XSectionTreeWidget = QtWidgets.QTreeWidget(self.XSectionListPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.XSectionTreeWidget.sizePolicy().hasHeightForWidth())
        self.XSectionTreeWidget.setSizePolicy(sizePolicy)
        self.XSectionTreeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.XSectionTreeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.XSectionTreeWidget.setTabKeyNavigation(True)
        self.XSectionTreeWidget.setDragDropOverwriteMode(True)
        self.XSectionTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.XSectionTreeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.XSectionTreeWidget.setAutoExpandDelay(-1)
        self.XSectionTreeWidget.setObjectName("XSectionTreeWidget")
        self.XSectionTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.XSectionTreeWidget)
        self.toolBox.addItem(self.XSectionListPage, "")
        self.BoundariesPage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BoundariesPage.sizePolicy().hasHeightForWidth())
        self.BoundariesPage.setSizePolicy(sizePolicy)
        self.BoundariesPage.setObjectName("BoundariesPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.BoundariesPage)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.BoundariesTableWidget = QtWidgets.QTableWidget(self.BoundariesPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.BoundariesTableWidget.sizePolicy().hasHeightForWidth())
        self.BoundariesTableWidget.setSizePolicy(sizePolicy)
        self.BoundariesTableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.BoundariesTableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.BoundariesTableWidget.setObjectName("BoundariesTableWidget")
        self.BoundariesTableWidget.setColumnCount(0)
        self.BoundariesTableWidget.setRowCount(0)
        self.verticalLayout_8.addWidget(self.BoundariesTableWidget)
        self.toolBox.addItem(self.BoundariesPage, "")
        self.Mesh3DPage = QtWidgets.QWidget()
        self.Mesh3DPage.setGeometry(QtCore.QRect(0, 0, 282, 448))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Mesh3DPage.sizePolicy().hasHeightForWidth())
        self.Mesh3DPage.setSizePolicy(sizePolicy)
        self.Mesh3DPage.setMinimumSize(QtCore.QSize(0, 0))
        self.Mesh3DPage.setBaseSize(QtCore.QSize(0, 0))
        self.Mesh3DPage.setObjectName("Mesh3DPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Mesh3DPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Mesh3DTableWidget = QtWidgets.QTableWidget(self.Mesh3DPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Mesh3DTableWidget.sizePolicy().hasHeightForWidth())
        self.Mesh3DTableWidget.setSizePolicy(sizePolicy)
        self.Mesh3DTableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.Mesh3DTableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.Mesh3DTableWidget.setObjectName("Mesh3DTableWidget")
        self.Mesh3DTableWidget.setColumnCount(0)
        self.Mesh3DTableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.Mesh3DTableWidget)
        self.toolBox.addItem(self.Mesh3DPage, "")
        self.DOMsPage = QtWidgets.QWidget()
        self.DOMsPage.setGeometry(QtCore.QRect(0, 0, 282, 448))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DOMsPage.sizePolicy().hasHeightForWidth())
        self.DOMsPage.setSizePolicy(sizePolicy)
        self.DOMsPage.setMinimumSize(QtCore.QSize(0, 0))
        self.DOMsPage.setBaseSize(QtCore.QSize(0, 0))
        self.DOMsPage.setObjectName("DOMsPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DOMsPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DOMsTableWidget = QtWidgets.QTableWidget(self.DOMsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DOMsTableWidget.sizePolicy().hasHeightForWidth())
        self.DOMsTableWidget.setSizePolicy(sizePolicy)
        self.DOMsTableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.DOMsTableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.DOMsTableWidget.setObjectName("DOMsTableWidget")
        self.DOMsTableWidget.setColumnCount(0)
        self.DOMsTableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.DOMsTableWidget)
        self.toolBox.addItem(self.DOMsPage, "")
        self.ImagesPage = QtWidgets.QWidget()
        self.ImagesPage.setGeometry(QtCore.QRect(0, 0, 282, 448))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ImagesPage.sizePolicy().hasHeightForWidth())
        self.ImagesPage.setSizePolicy(sizePolicy)
        self.ImagesPage.setMinimumSize(QtCore.QSize(0, 0))
        self.ImagesPage.setBaseSize(QtCore.QSize(0, 0))
        self.ImagesPage.setObjectName("ImagesPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ImagesPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ImagesTableWidget = QtWidgets.QTableWidget(self.ImagesPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ImagesTableWidget.sizePolicy().hasHeightForWidth())
        self.ImagesTableWidget.setSizePolicy(sizePolicy)
        self.ImagesTableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.ImagesTableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.ImagesTableWidget.setObjectName("ImagesTableWidget")
        self.ImagesTableWidget.setColumnCount(0)
        self.ImagesTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.ImagesTableWidget)
        self.toolBox.addItem(self.ImagesPage, "")
        self.ViewFrame = QtWidgets.QFrame(self.splitter)
        self.ViewFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewFrame.sizePolicy().hasHeightForWidth())
        self.ViewFrame.setSizePolicy(sizePolicy)
        self.ViewFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.ViewFrame.setBaseSize(QtCore.QSize(0, 0))
        self.ViewFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ViewFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ViewFrame.setLineWidth(0)
        self.ViewFrame.setObjectName("ViewFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ViewFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ViewFrameLayout = QtWidgets.QVBoxLayout()
        self.ViewFrameLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ViewFrameLayout.setContentsMargins(4, 4, 4, 4)
        self.ViewFrameLayout.setSpacing(8)
        self.ViewFrameLayout.setObjectName("ViewFrameLayout")
        self.horizontalLayout.addLayout(self.ViewFrameLayout)
        self.verticalLayout_2.addWidget(self.splitter)
        BaseViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BaseViewWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QtCore.QSize(1280, 30))
        self.menubar.setBaseSize(QtCore.QSize(1280, 18))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuBaseView = QtWidgets.QMenu(self.menubar)
        self.menuBaseView.setObjectName("menuBaseView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        BaseViewWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BaseViewWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setMinimumSize(QtCore.QSize(1280, 18))
        self.statusbar.setBaseSize(QtCore.QSize(1280, 18))
        self.statusbar.setObjectName("statusbar")
        BaseViewWindow.setStatusBar(self.statusbar)
        self.toolBarBase = QtWidgets.QToolBar(BaseViewWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.toolBarBase.sizePolicy().hasHeightForWidth())
        self.toolBarBase.setSizePolicy(sizePolicy)
        self.toolBarBase.setMinimumSize(QtCore.QSize(1280, 30))
        self.toolBarBase.setBaseSize(QtCore.QSize(1280, 30))
        self.toolBarBase.setObjectName("toolBarBase")
        BaseViewWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarBase)
        self.actionClose = QtWidgets.QAction(BaseViewWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionBase_Tool = QtWidgets.QAction(BaseViewWindow)
        self.actionBase_Tool.setObjectName("actionBase_Tool")
        self.menuWindow.addAction(self.actionClose)
        self.menubar.addAction(self.menuBaseView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(BaseViewWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BaseViewWindow)

    def retranslateUi(self, BaseViewWindow):
        _translate = QtCore.QCoreApplication.translate
        BaseViewWindow.setWindowTitle(_translate("BaseViewWindow", "Base View"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.GeologyTreePage), _translate("BaseViewWindow", "Geology > Geology Tree"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.TopologyTreePage), _translate("BaseViewWindow", "Geology > Topology Tree"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.XSectionListPage), _translate("BaseViewWindow", "X Section"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.BoundariesPage), _translate("BaseViewWindow", "Boundaries"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Mesh3DPage), _translate("BaseViewWindow", "3D Meshes and Grids"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.DOMsPage), _translate("BaseViewWindow", "DEMs and DOMs"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.ImagesPage), _translate("BaseViewWindow", "Images"))
        self.menuBaseView.setTitle(_translate("BaseViewWindow", "Base View"))
        self.menuHelp.setTitle(_translate("BaseViewWindow", "Help"))
        self.menuWindow.setTitle(_translate("BaseViewWindow", "Window"))
        self.toolBarBase.setWindowTitle(_translate("BaseViewWindow", "toolBar"))
        self.actionClose.setText(_translate("BaseViewWindow", "Close Window"))
        self.actionBase_Tool.setText(_translate("BaseViewWindow", "Base Tool"))
