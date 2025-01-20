# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crudui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_CRUD(object):
    def setupUi(self, CRUD):
        if not CRUD.objectName():
            CRUD.setObjectName(u"CRUD")
        CRUD.setEnabled(True)
        CRUD.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CRUD.sizePolicy().hasHeightForWidth())
        CRUD.setSizePolicy(sizePolicy)
        CRUD.setMinimumSize(QSize(800, 600))
        CRUD.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(CRUD)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 601))
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.produto = QWidget()
        self.produto.setObjectName(u"produto")
        self.layoutWidget = QWidget(self.produto)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(430, 20, 351, 481))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listaProduto = QListView(self.layoutWidget)
        self.listaProduto.setObjectName(u"listaProduto")

        self.verticalLayout_2.addWidget(self.listaProduto)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnListarProduto = QPushButton(self.layoutWidget)
        self.btnListarProduto.setObjectName(u"btnListarProduto")

        self.horizontalLayout_2.addWidget(self.btnListarProduto)

        self.btnExcluirProduto = QPushButton(self.layoutWidget)
        self.btnExcluirProduto.setObjectName(u"btnExcluirProduto")

        self.horizontalLayout_2.addWidget(self.btnExcluirProduto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.stackedWidget_2 = QStackedWidget(self.produto)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(19, 39, 391, 241))
        self.create_2 = QWidget()
        self.create_2.setObjectName(u"create_2")
        self.gridLayout_3 = QGridLayout(self.create_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.nameUL_3 = QLabel(self.create_2)
        self.nameUL_3.setObjectName(u"nameUL_3")
        self.nameUL_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.nameUL_3, 3, 0, 1, 1)

        self.mailUL_4 = QLabel(self.create_2)
        self.mailUL_4.setObjectName(u"mailUL_4")
        self.mailUL_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.mailUL_4, 2, 0, 1, 1)

        self.inputPrecoProduto = QLineEdit(self.create_2)
        self.inputPrecoProduto.setObjectName(u"inputPrecoProduto")
        sizePolicy1.setHeightForWidth(self.inputPrecoProduto.sizePolicy().hasHeightForWidth())
        self.inputPrecoProduto.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.inputPrecoProduto, 3, 1, 1, 1)

        self.inputDescricaoProduto = QLineEdit(self.create_2)
        self.inputDescricaoProduto.setObjectName(u"inputDescricaoProduto")

        self.gridLayout_3.addWidget(self.inputDescricaoProduto, 2, 1, 1, 1)

        self.label_3 = QLabel(self.create_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFrameShadow(QFrame.Shadow.Plain)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)

        self.btnCriarProduto = QPushButton(self.create_2)
        self.btnCriarProduto.setObjectName(u"btnCriarProduto")

        self.gridLayout_3.addWidget(self.btnCriarProduto, 4, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.create_2)
        self.update_2 = QWidget()
        self.update_2.setObjectName(u"update_2")
        self.gridLayout_4 = QGridLayout(self.update_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mailUL_5 = QLabel(self.update_2)
        self.mailUL_5.setObjectName(u"mailUL_5")
        self.mailUL_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.mailUL_5, 2, 0, 1, 1)

        self.inputPrecoProduto_2 = QLineEdit(self.update_2)
        self.inputPrecoProduto_2.setObjectName(u"inputPrecoProduto_2")
        sizePolicy1.setHeightForWidth(self.inputPrecoProduto_2.sizePolicy().hasHeightForWidth())
        self.inputPrecoProduto_2.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.inputPrecoProduto_2, 3, 1, 1, 1)

        self.mailUL_6 = QLabel(self.update_2)
        self.mailUL_6.setObjectName(u"mailUL_6")
        self.mailUL_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.mailUL_6, 1, 0, 1, 1)

        self.inputDescricaoProduto_2 = QLineEdit(self.update_2)
        self.inputDescricaoProduto_2.setObjectName(u"inputDescricaoProduto_2")

        self.gridLayout_4.addWidget(self.inputDescricaoProduto_2, 2, 1, 1, 1)

        self.nameUL_4 = QLabel(self.update_2)
        self.nameUL_4.setObjectName(u"nameUL_4")
        self.nameUL_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.nameUL_4, 3, 0, 1, 1)

        self.UPDATE_2 = QLabel(self.update_2)
        self.UPDATE_2.setObjectName(u"UPDATE_2")
        sizePolicy2.setHeightForWidth(self.UPDATE_2.sizePolicy().hasHeightForWidth())
        self.UPDATE_2.setSizePolicy(sizePolicy2)
        self.UPDATE_2.setFrameShadow(QFrame.Shadow.Plain)
        self.UPDATE_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.UPDATE_2, 0, 0, 1, 2)

        self.inputIdProduto = QLineEdit(self.update_2)
        self.inputIdProduto.setObjectName(u"inputIdProduto")
        self.inputIdProduto.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.inputIdProduto, 1, 1, 1, 1)

        self.btnAtualizarProduto = QPushButton(self.update_2)
        self.btnAtualizarProduto.setObjectName(u"btnAtualizarProduto")

        self.gridLayout_4.addWidget(self.btnAtualizarProduto, 4, 0, 1, 2)

        self.stackedWidget_2.addWidget(self.update_2)
        self.pushButton_3 = QPushButton(self.produto)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 330, 75, 24))
        self.pushButton_4 = QPushButton(self.produto)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 290, 75, 24))
        self.tabWidget.addTab(self.produto, "")
        self.cliente = QWidget()
        self.cliente.setObjectName(u"cliente")
        self.stackedWidget = QStackedWidget(self.cliente)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(19, 29, 391, 241))
        self.create = QWidget()
        self.create.setObjectName(u"create")
        self.gridLayout = QGridLayout(self.create)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameUL = QLabel(self.create)
        self.nameUL.setObjectName(u"nameUL")
        self.nameUL.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.nameUL, 3, 0, 1, 1)

        self.mailUL = QLabel(self.create)
        self.mailUL.setObjectName(u"mailUL")
        self.mailUL.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.mailUL, 2, 0, 1, 1)

        self.inputNome = QLineEdit(self.create)
        self.inputNome.setObjectName(u"inputNome")

        self.gridLayout.addWidget(self.inputNome, 3, 1, 1, 1)

        self.inputEmail = QLineEdit(self.create)
        self.inputEmail.setObjectName(u"inputEmail")

        self.gridLayout.addWidget(self.inputEmail, 2, 1, 1, 1)

        self.label_2 = QLabel(self.create)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFrameShadow(QFrame.Shadow.Plain)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.btnCriar = QPushButton(self.create)
        self.btnCriar.setObjectName(u"btnCriar")

        self.gridLayout.addWidget(self.btnCriar, 4, 0, 1, 2)

        self.stackedWidget.addWidget(self.create)
        self.update = QWidget()
        self.update.setObjectName(u"update")
        self.gridLayout_2 = QGridLayout(self.update)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mailUL_2 = QLabel(self.update)
        self.mailUL_2.setObjectName(u"mailUL_2")
        self.mailUL_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.mailUL_2, 2, 0, 1, 1)

        self.inputNome_2 = QLineEdit(self.update)
        self.inputNome_2.setObjectName(u"inputNome_2")

        self.gridLayout_2.addWidget(self.inputNome_2, 3, 1, 1, 1)

        self.mailUL_3 = QLabel(self.update)
        self.mailUL_3.setObjectName(u"mailUL_3")
        self.mailUL_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.mailUL_3, 1, 0, 1, 1)

        self.inputEmail_2 = QLineEdit(self.update)
        self.inputEmail_2.setObjectName(u"inputEmail_2")

        self.gridLayout_2.addWidget(self.inputEmail_2, 2, 1, 1, 1)

        self.nameUL_2 = QLabel(self.update)
        self.nameUL_2.setObjectName(u"nameUL_2")
        self.nameUL_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.nameUL_2, 3, 0, 1, 1)

        self.UPDATE = QLabel(self.update)
        self.UPDATE.setObjectName(u"UPDATE")
        sizePolicy2.setHeightForWidth(self.UPDATE.sizePolicy().hasHeightForWidth())
        self.UPDATE.setSizePolicy(sizePolicy2)
        self.UPDATE.setFrameShadow(QFrame.Shadow.Plain)
        self.UPDATE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.UPDATE, 0, 0, 1, 2)

        self.inputId = QLineEdit(self.update)
        self.inputId.setObjectName(u"inputId")
        self.inputId.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.inputId, 1, 1, 1, 1)

        self.btnAtualizar = QPushButton(self.update)
        self.btnAtualizar.setObjectName(u"btnAtualizar")

        self.gridLayout_2.addWidget(self.btnAtualizar, 4, 0, 1, 2)

        self.stackedWidget.addWidget(self.update)
        self.pushButton = QPushButton(self.cliente)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 280, 75, 24))
        self.pushButton_2 = QPushButton(self.cliente)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 320, 75, 24))
        self.widget = QWidget(self.cliente)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(430, 10, 351, 481))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listaC = QListView(self.widget)
        self.listaC.setObjectName(u"listaC")

        self.verticalLayout.addWidget(self.listaC)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnListar = QPushButton(self.widget)
        self.btnListar.setObjectName(u"btnListar")

        self.horizontalLayout.addWidget(self.btnListar)

        self.btnExcluir = QPushButton(self.widget)
        self.btnExcluir.setObjectName(u"btnExcluir")

        self.horizontalLayout.addWidget(self.btnExcluir)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.cliente, "")
        CRUD.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CRUD)
        self.statusbar.setObjectName(u"statusbar")
        CRUD.setStatusBar(self.statusbar)

        self.retranslateUi(CRUD)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CRUD)
    # setupUi

    def retranslateUi(self, CRUD):
        CRUD.setWindowTitle(QCoreApplication.translate("CRUD", u"MainWindow", None))
        self.btnListarProduto.setText(QCoreApplication.translate("CRUD", u"Listar", None))
        self.btnExcluirProduto.setText(QCoreApplication.translate("CRUD", u"Excluir", None))
        self.nameUL_3.setText(QCoreApplication.translate("CRUD", u"Pre\u00e7o", None))
        self.mailUL_4.setText(QCoreApplication.translate("CRUD", u"Descri\u00e7ao:", None))
        self.label_3.setText(QCoreApplication.translate("CRUD", u"CREATE", None))
        self.btnCriarProduto.setText(QCoreApplication.translate("CRUD", u"Criar", None))
        self.mailUL_5.setText(QCoreApplication.translate("CRUD", u"Descri\u00e7\u00e3o::", None))
        self.mailUL_6.setText(QCoreApplication.translate("CRUD", u"ID:", None))
        self.nameUL_4.setText(QCoreApplication.translate("CRUD", u"Pre\u00e7o:", None))
        self.UPDATE_2.setText(QCoreApplication.translate("CRUD", u"UPDATE", None))
        self.btnAtualizarProduto.setText(QCoreApplication.translate("CRUD", u"Atualizar", None))
        self.pushButton_3.setText(QCoreApplication.translate("CRUD", u"UPDATE", None))
        self.pushButton_4.setText(QCoreApplication.translate("CRUD", u"CREATE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.produto), QCoreApplication.translate("CRUD", u"produto", None))
        self.nameUL.setText(QCoreApplication.translate("CRUD", u"Nome:", None))
        self.mailUL.setText(QCoreApplication.translate("CRUD", u"E-Mail:", None))
        self.label_2.setText(QCoreApplication.translate("CRUD", u"CREATE", None))
        self.btnCriar.setText(QCoreApplication.translate("CRUD", u"Criar", None))
        self.mailUL_2.setText(QCoreApplication.translate("CRUD", u"E-Mail:", None))
        self.mailUL_3.setText(QCoreApplication.translate("CRUD", u"ID:", None))
        self.nameUL_2.setText(QCoreApplication.translate("CRUD", u"Nome:", None))
        self.UPDATE.setText(QCoreApplication.translate("CRUD", u"UPDATE", None))
        self.btnAtualizar.setText(QCoreApplication.translate("CRUD", u"Atualizar", None))
        self.pushButton.setText(QCoreApplication.translate("CRUD", u"CREATE", None))
        self.pushButton_2.setText(QCoreApplication.translate("CRUD", u"UPDATE", None))
        self.btnListar.setText(QCoreApplication.translate("CRUD", u"Listar", None))
        self.btnExcluir.setText(QCoreApplication.translate("CRUD", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cliente), QCoreApplication.translate("CRUD", u"cliente", None))
    # retranslateUi

