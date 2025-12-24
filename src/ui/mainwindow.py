# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1274, 816)
        MainWindow.setStyleSheet(u"QMainWindow#MainWindow {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0B0F20,\n"
"        stop:0.4 #121A33,\n"
"        stop:0.7 #0C1125,\n"
"        stop:1 #0B0F20\n"
"    );\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    color: #E0E7FF;\n"
"}\n"
"QWidget#centralWidget,\n"
"QWidget#centralWidget_2,\n"
"QWidget#centralWidget_3 {\n"
"    background: rgba(255,255,255,0.04);\n"
"    backdrop-filter: blur(18px);\n"
"    border-radius: 24px;\n"
"    border: 1px solid rgba(79,139,255,0.3);\n"
"    box-shadow: 0 10px 50px rgba(0,0,64,0.7), 0 0 25px rgba(79,139,255,0.35);\n"
"    transition: transform 0.35s ease, box-shadow 0.35s ease;\n"
"}\n"
"QWidget#centralWidget:hover,\n"
"QWidget#centralWidget_2:hover,\n"
"QWidget#centralWidget_3:hover {\n"
"    transform: translateY(-6px);\n"
"    box-shadow: 0 15px 60px rgba(0,0,64,0.9), 0 0 50px rgba(79,139,255,0.55);\n"
"}\n"
"")
        self.centralWidget_2 = QWidget(MainWindow)
        self.centralWidget_2.setObjectName(u"centralWidget_2")
        self.gridLayout_5 = QGridLayout(self.centralWidget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget = QStackedWidget(self.centralWidget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    background: rgba(255,255,255,0.1);\n"
"    backdrop-filter: blur(18px);\n"
"    border-radius: 24px;\n"
"    border: 1px solid rgba(79,139,255,0.3);\n"
"    box-shadow: 0 10px 50px rgba(0,0,64,0.7), 0 0 25px rgba(79,139,255,0.35);\n"
"    transition: transform 0.35s ease, box-shadow 0.35s ease;\n"
"}\n"
"QStackedWidget:hover {\n"
"    transform: translateY(-6px);\n"
"    box-shadow: 0 15px 60px rgba(0,0,64,0.9), 0 0 50px rgba(79,139,255,0.55);\n"
"}\n"
"")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"\n"
"/* =====================================================\n"
"   CENTRAL WIDGETS (GLASS + DEEP NEON)\n"
"   ===================================================== */\n"
"/* =====================================================\n"
"   CARD CONTAINER (MONOCHROME NEON PREMIUM)\n"
"   ===================================================== */\n"
"QFrame#cardFrame {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(18,18,55,0.9),\n"
"        stop:1 rgba(38,38,95,0.9)\n"
"    );\n"
"    border-radius: 28px;\n"
"    border: 1px solid rgba(79,139,255,0.6);\n"
"    box-shadow: 0 6px 35px rgba(0,0,64,0.8), 0 0 18px rgba(79,139,255,0.45);\n"
"    transition: transform 0.35s ease, box-shadow 0.35s ease;\n"
"}\n"
"QFrame#cardFrame:hover {\n"
"    transform: translateY(-8px);\n"
"    box-shadow: 0 18px 65px rgba(0,0,64,0.95), 0 0 55px rgba(79,139,255,0.65);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   TITLES (PREMIUM MONOCHROME NEON)\n"
"   =="
                        "=================================================== */\n"
"QLabel#titleLabel {\n"
"    font-size: 34px;\n"
"    font-weight: 900;\n"
"    color: #E0E7FF;\n"
"    text-shadow: 0 0 12px #4F8BFF, 0 0 25px #6FA3FF, 0 0 40px #2563EB;\n"
"}\n"
"QLabel#subtitleLabel {\n"
"    font-size: 17px;\n"
"    color: #A0AEC0;\n"
"    text-shadow: 0 0 4px rgba(0,0,64,0.6);\n"
"    letter-spacing: 0.6px;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   INPUT FIELDS (GLASS + NEON PREMIUM)\n"
"   ===================================================== */\n"
"QTextEdit, QLineEdit {\n"
"    height: 50px;\n"
"    padding: 0 18px;\n"
"    font-size: 15px;\n"
"    color: #E0E7FF;\n"
"    background: rgba(255,255,255,0.06);\n"
"    border-radius: 18px;\n"
"    border: 1px solid rgba(79,139,255,0.45);\n"
"    backdrop-filter: blur(14px);\n"
"    box-shadow: inset 0 0 8px rgba(79,139,255,0.2);\n"
"    transition: all 0.35s ease, box-shadow 0.35s ease;\n"
"}\n"
"QTextEdit, QLineEdit:hover {\n"
"    border: 1px s"
                        "olid #4F8BFF;\n"
"    box-shadow: 0 0 16px #4F8BFF, inset 0 0 8px rgba(79,139,255,0.25);\n"
"}\n"
"QTextEdit, QLineEdit:focus {\n"
"    border: 2px solid #2563EB;\n"
"    box-shadow: 0 0 25px #2563EB, inset 0 0 12px rgba(79,139,255,0.3);\n"
"}\n"
"/* =====================================================\n"
"   BUTTON COMMON STYLE (ALL THREE)\n"
"   ===================================================== */\n"
"/* =====================================================\n"
"   BUTTON COMMON STYLE (ALL THREE)\n"
"   ===================================================== */\n"
"\n"
"/* =====================================================\n"
"   BROWSE BUTTON - GLASS STYLE + UNIFIED BORDER\n"
"   ===================================================== */\n"
"QPushButton#browseButton {\n"
"    background: rgba(255,255,255,0.05);\n"
"height: 64px;\n"
"    min-width: 180px;\n"
"    font-size: 20px;\n"
"    font-weight: 700;\n"
"    color: #ffffff;\n"
"    border-radius: 32px; /* fully rounded corners */\n"
"    border: 2px "
                        "solid rgba(139,92,246,0.5); /* unified border */\n"
"    transition: all 0.3s cubic-bezier(0.4,0,0.2,1);\n"
"    box-shadow: 0 12px 50px rgba(139,92,246,0.6), 0 0 70px rgba(99,102,241,0.4);\n"
"}\n"
"\n"
"QPushButton#browseButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #c084fc,\n"
"        stop:0.2 #a78bfa,\n"
"        stop:0.5 #818cf8,\n"
"        stop:0.8 #60a5fa,\n"
"        stop:1 #3b82f6\n"
"    );\n"
"    transform: translateY(-3px) scale(1.05);\n"
"    box-shadow: 0 25px 90px rgba(139,92,246,1), 0 0 120px rgba(99,102,241,0.8);\n"
"    border: 2px solid rgba(168,85,247,0.8);\n"
"}\n"
"\n"
"QPushButton#browseButton:pressed {\n"
"    transform: translateY(-1px) scale(0.98);\n"
"    box-shadow: 0 12px 50px rgba(139,92,246,0.7), 0 0 70px rgba(99,102,241,0.5);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   IMPORT BUTTON - PREMIUM GRADIENT STYLE\n"
"   ===================================================== */\n"
"QPushBu"
                        "tton#importButton {\n"
"   height: 54px;\n"
"    min-width: 150px;\n"
"    font-size: 20px;\n"
"    font-weight: 700;\n"
"    color: #E0E7FF;\n"
"    border-radius: 20px;\n"
"    border: none;\n"
"      background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #c084fc,\n"
"        stop:0.2 #a78bfa,\n"
"        stop:0.5 #818cf8,\n"
"        stop:0.8 #60a5fa,\n"
"        stop:1 #3b82f6\n"
"    );\n"
"    transform: translateY(-3px) scale(1.05);\n"
"    box-shadow: 0 25px 90px rgba(139,92,246,1), 0 0 120px rgba(99,102,241,0.8);\n"
"    border: 2px solid rgba(168,85,247,0.8);\n"
"}\n"
"\n"
"QPushButton#importButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #a855f7,\n"
"        stop:0.2 #8b5cf6,\n"
"        stop:0.5 #6366f1,\n"
"        stop:0.8 #3b82f6,\n"
"        stop:1 #2563eb\n"
"    );\n"
"    transform: translateY(-3px) scale(1.05);\n"
"    box-shadow: 0 25px 90px rgba(139,92,246,1), 0 0 120px rgba(99,102,241,0.8);\n"
"    bo"
                        "rder: 2px solid rgba(168,85,247,0.8);\n"
"}\n"
"\n"
"QPushButton#importButton:pressed {\n"
"    transform: translateY(-1px) scale(0.98);\n"
"    box-shadow: 0 12px 50px rgba(139,92,246,0.7), 0 0 70px rgba(99,102,241,0.5);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   CLEAR BUTTON - SAME AS IMPORT\n"
"   ===================================================== */\n"
"QPushButton#clearButton {\n"
"   height: 54px;\n"
"    min-width: 150px;\n"
"    font-size: 20px;\n"
"    font-weight: 700;\n"
"    color: #E0E7FF;\n"
"    border-radius: 20px;\n"
"    border: none;\n"
"   background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #c084fc,\n"
"        stop:0.2 #a78bfa,\n"
"        stop:0.5 #818cf8,\n"
"        stop:0.8 #60a5fa,\n"
"        stop:1 #3b82f6\n"
"    );\n"
"    transform: translateY(-3px) scale(1.05);\n"
"    box-shadow: 0 25px 90px rgba(139,92,246,1), 0 0 120px rgba(99,102,241,0.8);\n"
"    border: 2px solid rgba(168,85,247,0.8);\n"
"}\n"
"\n"
"QPu"
                        "shButton#clearButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #a855f7,\n"
"        stop:0.2 #8b5cf6,\n"
"        stop:0.5 #6366f1,\n"
"        stop:0.8 #3b82f6,\n"
"        stop:1 #2563eb\n"
"    );\n"
"    transform: translateY(-3px) scale(1.05);\n"
"    box-shadow: 0 25px 90px rgba(139,92,246,1), 0 0 120px rgba(99,102,241,0.8);\n"
"    border: 2px solid rgba(168,85,247,0.8);\n"
"}\n"
"\n"
"QPushButton#clearButton:pressed {\n"
"    transform: translateY(-1px) scale(0.98);\n"
"    box-shadow: 0 12px 50px rgba(139,92,246,0.7), 0 0 70px rgba(99,102,241,0.5);\n"
"}\n"
"\n"
"\n"
"/* =====================================================\n"
"   MENU BAR - PREMIUM STYLE WITH ROUNDED CORNERS\n"
"   ===================================================== */\n"
"QMenuBar {\n"
"    background: rgba(18,18,55,0.8);\n"
"    color: #E0E7FF;\n"
"    border-bottom: 1px solid rgba(79,139,255,0.3);\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    border-radius: 8px;\n"
""
                        "}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 8px 16px;\n"
"    border-radius: 12px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: rgba(79,139,255,0.2);\n"
"    border: 1px solid rgba(79,139,255,0.4);\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: rgba(79,139,255,0.3);\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   MENU DROPDOWN - PREMIUM STYLE WITH ROUNDED CORNERS\n"
"   ===================================================== */\n"
"QMenu {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(18,18,55,0.95),\n"
"        stop:1 rgba(28,28,75,0.95)\n"
"    );\n"
"    color: #E0E7FF;\n"
"    border: 1px solid rgba(79,139,255,0.5);\n"
"    border-radius: 16px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 10px 30px 10px 20px;\n"
"    border-radius: 10px;\n"
"    margin: 2px;\n"
"}\n"
""
                        "\n"
"QMenu::item:selected {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(139,92,246,0.3),\n"
"        stop:1 rgba(99,102,241,0.3)\n"
"    );\n"
"    border: 1px solid rgba(139,92,246,0.5);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: rgba(79,139,255,0.3);\n"
"    margin: 5px 10px;\n"
"    border-radius: 1px;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.centralWidget = QWidget(self.page_3)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setObjectName(u"rootLayout")
        self.cardFrame = QFrame(self.centralWidget)
        self.cardFrame.setObjectName(u"cardFrame")
        self.cardFrame.setMinimumSize(QSize(0, 0))
        self.cardFrame.setStyleSheet(u"")
        self.cardFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cardFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.cardFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleLabel = QLabel(self.cardFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.titleLabel)

        self.fileInputContainer = QWidget(self.cardFrame)
        self.fileInputContainer.setObjectName(u"fileInputContainer")
        self.fileInputContainer.setMinimumSize(QSize(300, 150))
        self.fileInputContainer.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.fileInputContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.filePathInput = QLineEdit(self.fileInputContainer)
        self.filePathInput.setObjectName(u"filePathInput")
        self.filePathInput.setMinimumSize(QSize(0, 42))
        self.filePathInput.setStyleSheet(u"")

        self.gridLayout.addWidget(self.filePathInput, 2, 0, 1, 1)

        self.browseButton = QPushButton(self.fileInputContainer)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setMinimumSize(QSize(184, 0))
        font = QFont()
        font.setBold(True)
        self.browseButton.setFont(font)

        self.gridLayout.addWidget(self.browseButton, 2, 1, 1, 1)

        self.xmlInput = QTextEdit(self.fileInputContainer)
        self.xmlInput.setObjectName(u"xmlInput")

        self.gridLayout.addWidget(self.xmlInput, 3, 0, 1, 2)

        self.subtitleLabel = QLabel(self.fileInputContainer)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setEnabled(True)
        self.subtitleLabel.setMinimumSize(QSize(0, 0))
        self.subtitleLabel.setStyleSheet(u"")

        self.gridLayout.addWidget(self.subtitleLabel, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.fileInputContainer)

        self.actionButtonContainer = QWidget(self.cardFrame)
        self.actionButtonContainer.setObjectName(u"actionButtonContainer")
        self.actionButtonContainer.setEnabled(True)
        self.actionButtonContainer.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.actionButtonContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clearButton = QPushButton(self.actionButtonContainer)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(154, 0))
        self.clearButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.clearButton)

        self.importButton = QPushButton(self.actionButtonContainer)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setMinimumSize(QSize(154, 0))
        self.importButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.importButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.importButton)


        self.verticalLayout_2.addWidget(self.actionButtonContainer)


        self.rootLayout.addWidget(self.cardFrame)


        self.verticalLayout.addLayout(self.rootLayout)


        self.gridLayout_3.addWidget(self.centralWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMaximumSize(QSize(16777215, 767))
        self.page_4.setStyleSheet(u"/* =====================================================\n"
"   ENHANCED LAYOUT STYLES\n"
"   ===================================================== */\n"
"/* =====================================================\n"
"   PAGE 2 - COMPLETE STYLESHEET\n"
"   ===================================================== */\n"
"\n"
"/* Page Container */\n"
"QWidget#page_4 {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Main Card Container */\n"
"QFrame#cardFrame_3 {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(18,18,55,0.95),\n"
"        stop:1 rgba(28,28,65,0.95)\n"
"    );\n"
"    border-radius: 32px;\n"
"    border: 2px solid rgba(139,92,246,0.4);\n"
"    box-shadow: 0 20px 60px rgba(0,0,0,0.6), \n"
"                0 0 40px rgba(79,139,255,0.3),\n"
"                inset 0 1px 0 rgba(255,255,255,0.1);\n"
"}\n"
"\n"
"/* Main Title */\n"
"QLabel#functionLabel {\n"
"    font-size: 42px;\n"
"    font-weight: 900;\n"
"    background-clip: text;\n"
""
                        "    color: white;\n"
"\n"
"    text-shadow: 0 0 30px rgba(139,92,246,0.5);\n"
"  qproperty-alignment: 'AlignCenter';\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   SECTION LABELS\n"
"   ===================================================== */\n"
"QLabel#sectionLabel1,\n"
"QLabel#sectionLabel2,\n"
"QLabel#sectionLabel3,\n"
"QLabel#sectionLabel4 {\n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"    color: #A0AEC0;\n"
"    padding: 0px 0 5px 0;\n"
"    border-bottom: 1px solid rgba(79,139,255,0.2);\n"
"    margin: 0px 0 10px 0;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   PROCESSING FUNCTION BUTTONS\n"
"   ===================================================== */\n"
"QPushButton#XMLconsistency_2,\n"
"QPushButton#Minifying_2,\n"
"QPushButton#Prettifying_2,\n"
"QPushButton#XMLtoJSON_2,\n"
"QPushButton#Compression_2,\n"
"QPushButton#Decompresssion_2 {\n"
"    background: rgba(255,255,255,0.08);\n"
"    h"
                        "eight: 45px;\n"
"    min-width: 160px;\n"
"    padding: 0 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #E0E7FF;\n"
"    border-radius: 22px;\n"
"    border: 1.5px solid rgba(139,92,246,0.5);\n"
"    transition: all 0.3s cubic-bezier(0.4,0,0.2,1);\n"
"    box-shadow: 0 4px 15px rgba(0,0,0,0.2);\n"
"}\n"
"\n"
"QPushButton#XMLconsistency_2:hover,\n"
"QPushButton#Minifying_2:hover,\n"
"QPushButton#Prettifying_2:hover,\n"
"QPushButton#XMLtoJSON_2:hover,\n"
"QPushButton#Compression_2:hover,\n"
"QPushButton#Decompresssion_2:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #8B5CF6,\n"
"        stop:1 #3B82F6\n"
"    );\n"
"    border: 1.5px solid rgba(255,255,255,0.3);\n"
"    transform: translateY(-3px);\n"
"    box-shadow: 0 10px 25px rgba(139,92,246,0.4);\n"
"}\n"
"\n"
"QPushButton#XMLconsistency_2:pressed,\n"
"QPushButton#Minifying_2:pressed,\n"
"QPushButton#Prettifying_2:pressed,\n"
"QPushButton#XMLtoJSON_2:pressed,\n"
"QPushButton#Comp"
                        "ression_2:pressed,\n"
"QPushButton#Decompresssion_2:pressed {\n"
"    transform: translateY(-1px);\n"
"    box-shadow: 0 4px 15px rgba(139,92,246,0.3);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   NETWORK ANALYSIS BUTTONS\n"
"   ===================================================== */\n"
"QPushButton#mostActiveButton,\n"
"QPushButton#mostInfluencerButton,\n"
"QPushButton#user1suggestButton {\n"
"     background: rgba(255,255,255,0.08);\n"
"    height: 45px;\n"
"    min-width: 160px;\n"
"    padding: 0 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #E0E7FF;\n"
"    border-radius: 22px;\n"
"    border: 1.5px solid rgba(139,92,246,0.5);\n"
"    transition: all 0.3s cubic-bezier(0.4,0,0.2,1);\n"
"    box-shadow: 0 4px 15px rgba(0,0,0,0.2);\n"
"}\n"
"\n"
"QPushButton#mostActiveButton:hover,\n"
"QPushButton#mostInfluencerButton:hover,\n"
"QPushButton#user1suggestButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"     "
                        "   stop:0 #8B5CF6,\n"
"        stop:1 #3B82F6\n"
"    );\n"
"    border: 1.5px solid rgba(255,255,255,0.3);\n"
"    transform: translateY(-3px);\n"
"    box-shadow: 0 10px 25px rgba(139,92,246,0.4);\n"
"}\n"
"\n"
"QPushButton#mostActiveButton:pressed,\n"
"QPushButton#mostInfluencerButton:pressed,\n"
"QPushButton#user1suggestButton:pressed {\n"
"    transform: translateY(-1px);\n"
"    box-shadow: 0 4px 15px rgba(139,92,246,0.3);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   UTILITY BUTTONS\n"
"   ===================================================== */\n"
"QPushButton#graph_2,\n"
"QPushButton#backButton,\n"
"QPushButton#save_2 {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #8B5CF6,\n"
"        stop:1 #3B82F6\n"
"    );\n"
"    height: 45px;\n"
"    min-width: 160px;\n"
"    padding: 0 25px;\n"
"    font-size: 15px;\n"
"    font-weight: 700;\n"
"    color: white;\n"
"    border-radius: 22px;\n"
"    border: none;\n"
"    box-shadow:"
                        " 0 8px 30px rgba(139,92,246,0.4);\n"
"    transition: all 0.3s cubic-bezier(0.4,0,0.2,1);\n"
"}\n"
"\n"
"QPushButton#graph_2:hover,\n"
"QPushButton#backButton:hover,\n"
"QPushButton#save_2:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #7C3AED,\n"
"        stop:1 #2563EB\n"
"    );\n"
"    transform: translateY(-2px);\n"
"    box-shadow: 0 12px 35px rgba(139,92,246,0.6);\n"
"}\n"
"\n"
"QPushButton#graph_2:pressed,\n"
"QPushButton#backButton:pressed,\n"
"QPushButton#save_2:pressed {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #6D28D9,\n"
"        stop:1 #1D4ED8\n"
"    );\n"
"    transform: translateY(0);\n"
"    box-shadow: 0 4px 15px rgba(139,92,246,0.4);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   RESULTS TEXT AREA\n"
"   ===================================================== */\n"
"QTextEdit#textEdit_2 {\n"
"    padding: 20px;\n"
"    font-size: 15px;\n"
"    font-family: \""
                        "Consolas\", \"Monaco\", monospace;\n"
"    color: #E0E7FF;\n"
"    background: rgba(0,0,0,0.3);\n"
"    border-radius: 20px;\n"
"    border: 1px solid rgba(139,92,246,0.3);\n"
"    selection-background-color: rgba(139,92,246,0.5);\n"
"    box-shadow: inset 0 2px 10px rgba(0,0,0,0.3);\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QTextEdit#textEdit_2:focus {\n"
"    border: 2px solid rgba(139,92,246,0.6);\n"
"    box-shadow: inset 0 2px 15px rgba(0,0,0,0.4),\n"
"                0 0 20px rgba(139,92,246,0.2);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   SEARCH & ANALYSIS SECTION\n"
"   ===================================================== */\n"
"QGroupBox#searchGroupBox {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(255,255,255,0.05),\n"
"        stop:1 rgba(255,255,255,0.03)\n"
"    );\n"
"    border: 1.5px solid rgba(139,92,246,0.4);\n"
"    border-radius: 22px;\n"
"    margin-top: 15px;\n"
"    padding-top: 20px;\n"
"   "
                        " color: #CBD5E0;\n"
"    font-size: 16px;\n"
"    font-weight: 700;\n"
"    backdrop-filter: blur(10px);\n"
"    box-shadow: 0 8px 32px rgba(0,0,0,0.2),\n"
"                inset 0 1px 0 rgba(255,255,255,0.1);\n"
"}\n"
"\n"
"QGroupBox#searchGroupBox::title {\n"
"    \n"
"    font-style: italic;\n"
"    font-size: 17px;\n"
"    padding: 10px; color: #E0E7FF;\n"
"    border-radius: 10px;\n"
"    margin-top: 0px;\n"
"    subcontrol-origin: margin;\n"
"    left: 0px;\n"
"  \n"
"    \n"
"}\n"
"\n"
"/* Search Section Labels */\n"
"QLabel#mutualLabel,\n"
"QLabel#searchLabel {\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #A0AEC0;\n"
"    padding: 5px 0;\n"
"    min-width: 120px;\n"
"    text-shadow: 0 1px 2px rgba(0,0,0,0.3);\n"
"}\n"
"\n"
"/* Search Input Fields */\n"
"QLineEdit#lineEdit,\n"
"QLineEdit#lineEdit_2 {\n"
"    height: 40px;\n"
"    padding: 0 18px;\n"
"    font-size: 14px;\n"
"    color: #E0E7FF;\n"
"    background: rgba(255,255,255,0.07);\n"
"    border-radius: 20px;\n"
"    border:"
                        " 1.5px solid rgba(139,92,246,0.3);\n"
"    selection-background-color: rgba(139,92,246,0.5);\n"
"    selection-color: #FFFFFF;\n"
"    transition: all 0.3s ease;\n"
"    box-shadow: inset 0 2px 8px rgba(0,0,0,0.2);\n"
"}\n"
"\n"
"QLineEdit#lineEdit:hover,\n"
"QLineEdit#lineEdit_2:hover {\n"
"    border: 1.5px solid rgba(139,92,246,0.6);\n"
"    background: rgba(255,255,255,0.09);\n"
"    box-shadow: inset 0 2px 12px rgba(0,0,0,0.3),\n"
"                0 0 0 2px rgba(139,92,246,0.1);\n"
"}\n"
"\n"
"QLineEdit#lineEdit:focus,\n"
"QLineEdit#lineEdit_2:focus {\n"
"    border: 2px solid rgba(139,92,246,0.8);\n"
"    background: rgba(255,255,255,0.1);\n"
"    box-shadow: inset 0 2px 15px rgba(0,0,0,0.4),\n"
"                0 0 0 3px rgba(139,92,246,0.15);\n"
"}\n"
"\n"
"/* Search Buttons */\n"
"QPushButton#mutualButton,\n"
"QPushButton#searchButton {\n"
"    height: 40px;\n"
"    min-width: 100px;\n"
"    padding: 0 25px;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"    color: #FFFFFF;\n"
"    border-radi"
                        "us: 20px;\n"
"    border: none;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(139,92,246,0.9),\n"
"        stop:1 rgba(99,102,241,0.9)\n"
"    );\n"
"    transition: all 0.3s cubic-bezier(0.4,0,0.2,1);\n"
"    box-shadow: 0 6px 20px rgba(139,92,246,0.4);\n"
"}\n"
"\n"
"QPushButton#mutualButton:hover,\n"
"QPushButton#searchButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(168,85,247,0.9),\n"
"        stop:1 rgba(124,58,237,0.9)\n"
"    );\n"
"    transform: translateY(-2px);\n"
"    box-shadow: 0 10px 30px rgba(139,92,246,0.6),\n"
"                0 0 20px rgba(139,92,246,0.3);\n"
"}\n"
"\n"
"QPushButton#mutualButton:pressed,\n"
"QPushButton#searchButton:pressed {\n"
"    transform: translateY(0);\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(124,58,237,0.9),\n"
"        stop:1 rgba(109,40,217,0.9)\n"
"    );\n"
"    box-shadow: 0 4px 15px rgba(139,9"
                        "2,246,0.4);\n"
"}\n"
"\n"
"QGridLayout {\n"
"    margin: 5px;\n"
"    spacing: 15px;\n"
"}\n"
"\n"
"QHBoxLayout, QVBoxLayout {\n"
"    spacing: 6px;\n"
"}\n"
"\n"
"QVBoxLayout#groupBoxVerticalLayout {\n"
"    spacing: 15px;\n"
"    margin: 15px;\n"
"}\n"
"\n"
"QHBoxLayout#mutualHorizontalLayout,\n"
"QHBoxLayout#searchHorizontalLayout {\n"
"    spacing: 12px;\n"
"    margin: 8px 0;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   PLACEHOLDER TEXT\n"
"   ===================================================== */\n"
"QLineEdit#lineEdit::placeholder,\n"
"QLineEdit#lineEdit_2::placeholder {\n"
"    color: rgba(160,174,192,0.6);\n"
"    font-style: italic;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QTextEdit#textEdit_2::placeholder {\n"
"    color: rgba(160,174,192,0.5);\n"
"    font-style: italic;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   SCROLL BARS (Optional Enhancement)\n"
"   =================================================="
                        "=== */\n"
"QScrollBar:vertical {\n"
"    background: rgba(255,255,255,0.05);\n"
"    width: 12px;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(139,92,246,0.5);\n"
"    border-radius: 6px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(139,92,246,0.7);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: rgba(255,255,255,0.05);\n"
"    height: 12px;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(139,92,246,0.5);\n"
"    border-radius: 6px;\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(139,92,246,0.7);\n"
"}\n"
"give me the name of every thing so i can edit it in qt\n"
"/* Main Card Layout Improvements */\n"
"QWidget#page_4 {\n"
"    background: qlin"
                        "eargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0F0F23,\n"
"        stop:1 #1A1A2E\n"
"    );\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame#cardFrame_3 {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(25,25,60,0.97),\n"
"        stop:1 rgba(35,35,80,0.97)\n"
"    );\n"
"    border-radius: 32px;\n"
"    border: 2px solid rgba(139,92,246,0.4);\n"
"    box-shadow: \n"
"        0 25px 70px rgba(0,0,0,0.7),\n"
"        0 0 50px rgba(79,139,255,0.4),\n"
"        inset 0 1px 0 rgba(255,255,255,0.15),\n"
"        inset 0 0 30px rgba(139,92,246,0.1);\n"
"    padding: 25px;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   SEARCH & MUTUAL SECTION ONLY\n"
"   ===================================================== */\n"
"\n"
"/* Group Box Container */\n"
"QGroupBox#searchGroupBox {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 rgba(255,255,255,0.05),\n"
"        stop:1 rgba(255,255"
                        ",255,0.03)\n"
"    );\n"
"    border: 1.5px solid rgba(139,92,246,0.4);\n"
"    border-radius: 22px;\n"
"    margin-top: 15px;\n"
"    padding: 15px;\n"
"    color: #CBD5E0;\n"
"    font-size: 16px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Labels - ALIGNMENT FIXED */\n"
"QLabel#mutualLabel {\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #A0AEC0;\n"
"    qproperty-alignment: 'AlignRight|AlignVCenter';\n"
"    min-width: 120px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLabel#searchLabel {\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #A0AEC0;\n"
"    qproperty-alignment: 'AlignRight|AlignVCenter';\n"
"    min-width: 120px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"/* Mutual Followers Input */\n"
"QLineEdit#lineEdit {\n"
"    height: 40px;\n"
"    padding: 0 15px;\n"
"    font-size: 14px;\n"
"    color: #E0E7FF;\n"
"    background: rgba(255,255,255,0.07);\n"
"    border-radius: 20px;\n"
"    border: 1.5px solid rgba(139,92,246,0.3);\n"
"    min-width: 200p"
                        "x;\n"
"}\n"
"\n"
"/* Search Text Input */\n"
"QLineEdit#lineEdit_2 {\n"
"    height: 40px;\n"
"    padding: 0 15px;\n"
"    font-size: 14px;\n"
"    color: #E0E7FF;\n"
"    background: rgba(255,255,255,0.07);\n"
"    border-radius: 20px;\n"
"    border: 1.5px solid rgba(139,92,246,0.3);\n"
"    min-width: 180px;\n"
"}\n"
"\n"
"/* Mutual Button */\n"
"QPushButton#mutualButton {\n"
"    height: 40px;\n"
"    min-width: 110px;\n"
"    padding: 0 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"    color: #FFFFFF;\n"
"    border-radius: 20px;\n"
"    border: none;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(139,92,246,0.9),\n"
"        stop:1 rgba(99,102,241,0.9)\n"
"    );\n"
"}\n"
"\n"
"/* Search Button */\n"
"QPushButton#searchButton {\n"
"    height: 40px;\n"
"    min-width: 80px;\n"
"    padding: 0 15px;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"    color: #FFFFFF;\n"
"    border-radius: 20px;\n"
"    border: none;\n"
"    backgroun"
                        "d: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(139,92,246,0.9),\n"
"        stop:1 rgba(99,102,241,0.9)\n"
"    );\n"
"}\n"
"\n"
"/* Common Button Hover */\n"
"QPushButton#mutualButton:hover,\n"
"QPushButton#searchButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(168,85,247,0.9),\n"
"        stop:1 rgba(124,58,237,0.9)\n"
"    );\n"
"    transform: translateY(-2px);\n"
"}\n"
"\n"
"/* Common Button Pressed */\n"
"QPushButton#mutualButton:pressed,\n"
"QPushButton#searchButton:pressed {\n"
"    transform: translateY(0);\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(124,58,237,0.9),\n"
"        stop:1 rgba(109,40,217,0.9)\n"
"    );\n"
"}\n"
"\n"
"/* Hover & Focus States */\n"
"QLineEdit#lineEdit:hover, QLineEdit#lineEdit:focus,\n"
"QLineEdit#lineEdit_2:hover, QLineEdit#lineEdit_2:focus {\n"
"    border: 2px solid rgba(139,92,246,0.6);\n"
"    background: rgba(255,255,25"
                        "5,0.1);\n"
"}\n"
"QComboBox#searchModeCombo:hover, QComboBox#searchModeCombo:focus {\n"
"    border: 2px solid rgba(139,92,246,0.6);\n"
"    background: rgba(255,255,255,0.1);\n"
"}\n"
"/* Placeholder Text */\n"
"QLineEdit#lineEdit::placeholder,\n"
"QLineEdit#lineEdit_2::placeholder {\n"
"    color: rgba(160,174,192,0.6);\n"
"    font-style: italic;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* Horizontal Line Separator */\n"
"QFrame#line {\n"
"    background: rgba(139,92,246,0.3);\n"
"    border: none;\n"
"    height: 1px;\n"
"    margin: 10px 0;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   ENHANCED COMBOBOX\n"
"   ===================================================== */\n"
"\n"
"QComboBox#searchModeCombo {\n"
"    background: rgba(255,255,255,0.08);\n"
"    height: 45px;\n"
"    min-width: 160px;\n"
"    padding: 0 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #E0E7FF;\n"
"    border-radius: 22px;\n"
"    border: 1.5px solid rgba(139,92,246,0.5);\n"
" "
                        "   transition: all 0.3s cubic-bezier(0.4,0,0.2,1);\n"
"    box-shadow: 0 4px 15px rgba(0,0,0,0.2);\n"
"\n"
"}\n"
"\n"
"QComboBox#searchModeCombo:hover {\n"
"\n"
"    border: 1.5px solid rgba(139,92,246,0.6);\n"
"    background: rgba(255,255,255,0.09);\n"
"    box-shadow: inset 0 2px 12px rgba(0,0,0,0.3),\n"
"                0 0 0 2px rgba(139,92,246,0.1);\n"
"\n"
"}\n"
"\n"
"/* =====================================================\n"
"   ENHANCED STATUS LABEL\n"
"   ===================================================== */\n"
"\n"
"QLabel#statusLabel {\n"
"    color: #A0AEC0;\n"
"    font-style: italic;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    padding: 15px;\n"
"    background: rgba(30,30,70,0.6);\n"
"    border-radius: 15px;\n"
"    border-left: 4px solid #8B5CF6;\n"
"    border-top: 1px solid rgba(139,92,246,0.3);\n"
"    border-bottom: 1px solid rgba(139,92,246,0.3);\n"
"    margin-top: 20px;\n"
"    text-shadow: 0 1px 2px rgba(0,0,0,0.3);\n"
"    box-shadow: \n"
"        inset 0 1px 0 rgba"
                        "(255,255,255,0.1),\n"
"        0 4px 15px rgba(0,0,0,0.2);\n"
"}\n"
"\n"
"/* =====================================================\n"
"   LAYOUT SPACING IMPROVEMENTS\n"
"   ===================================================== */\n"
"\n"
"QVBoxLayout#groupBoxVerticalLayout {\n"
"    spacing: 18px;\n"
"    margin: 20px 15px;\n"
"}\n"
"\n"
"QHBoxLayout#mutualHorizontalLayout,\n"
"QHBoxLayout#searchHorizontalLayout {\n"
"    spacing: 15px;\n"
"    margin: 10px 0;\n"
"}\n"
"\n"
"/* Form rows spacing */\n"
"QWidget {\n"
"    spacing: 12px;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   PLACEHOLDER ENHANCEMENTS\n"
"   ===================================================== */\n"
"\n"
"QLineEdit#lineEdit::placeholder,\n"
"QLineEdit#lineEdit_2::placeholder,\n"
"QSpinBox::placeholder {\n"
"    color: rgba(203,213,224,0.6);\n"
"    font-style: italic;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   SECTION SEP"
                        "ARATORS (Visual organization)\n"
"   ===================================================== */\n"
"\n"
"/* Optional: Add visual separators between sections */\n"
"QFrame[frameShape=\"4\"] { /* HLine */\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 transparent,\n"
"        stop:0.5 rgba(139,92,246,0.3),\n"
"        stop:1 transparent\n"
"    );\n"
"    max-height: 1px;\n"
"    margin: 20px 0;\n"
"}\n"
"\n"
"QSpinBox {\n"
"     background: rgba(255,255,255,0.08);\n"
"    height: 45px;\n"
"    min-width: 160px;\n"
"    padding: 0 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #E0E7FF;\n"
"    border-radius: 22px;\n"
"    border: 1.5px solid rgba(139,92,246,0.5);\n"
"    transition: all 0.3s cubic-bezier(0.4,0,0.2,1);\n"
"    box-shadow: 0 4px 15px rgba(0,0,0,0.2);\n"
"}\n"
"/* =====================================================\n"
"   SPINBOX \u2013 SMALLER ARROWS (SIDE, MINIMAL)\n"
"   ===================================================== */"
                        "\n"
"/* =====================================================\n"
"   SPINBOX \u2013 CLEAR, VISIBLE ARROWS (COMPACT)\n"
"   ===================================================== */\n"
"\n"
"/* =====================================================\n"
"   SPINBOX \u2013 ARROWS (SLIGHTLY BIGGER + HOVER)\n"
"   ===================================================== */\n"
"\n"
"\n"
"/* Hover background */\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover {\n"
"    background: rgba(139,92,246,0.45);\n"
"}\n"
"\n"
"/* Pressed */\n"
"QSpinBox::up-button:pressed,\n"
"QSpinBox::down-button:pressed {\n"
"    background: rgba(124,58,237,0.75);\n"
"}\n"
"\n"
"/* =====================\n"
"   ARROW SHAPES\n"
"   ===================== */\n"
"\n"
"QSpinBox::up-arrow,\n"
"QSpinBox::down-arrow {\n"
"    margin: auto;\n"
"    transition: all 0.2s ease;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Arrow hover glow */\n"
"QSpinBox::up-button:hover QSpinBox::up-arrow,\n"
"QSpinBox::down-button:hover QSpinBox::down-arrow {\n"
"    border-b"
                        "ottom-color: #FFFFFF;\n"
"    border-top-color: #FFFFFF;\n"
"}\n"
"\n"
"/* =====================================================\n"
"   COMBOBOX DROPDOWN LIST ENHANCEMENT\n"
"   ===================================================== */\n"
"QComboBox#searchModeCombo QAbstractItemView {\n"
"    background: rgba(25, 25, 50, 0.95);\n"
"    border: 1px solid rgba(139, 92, 246, 0.4);\n"
"    border-radius: 12px;\n"
"    padding: 8px;\n"
"    outline: none;\n"
"    selection-background-color: rgba(139, 92, 246, 0.5);\n"
"    selection-color: white;\n"
"    color: #E0E7FF;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"/* List item hover effect */\n"
"QComboBox#searchModeCombo QAbstractItemView::item {\n"
"    height: 36px;\n"
"    padding: 0 15px;\n"
"    border-radius: 8px;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QComboBox#searchModeCombo QAbstractItemView::item:hover {\n"
"    background: rgba(139, 92, 246, 0.3);\n"
"    color: white;\n"
"    font-"
                        "weight: 600;\n"
"}\n"
"\n"
"QComboBox#searchModeCombo QAbstractItemView::item:selected {\n"
"    background: rgba(139, 92, 246, 0.6);\n"
"    color: white;\n"
"    font-weight: 600;\n"
"    border-left: 3px solid #FFFFFF;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.page_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.centralWidget_3 = QWidget(self.page_4)
        self.centralWidget_3.setObjectName(u"centralWidget_3")
        self.centralWidget_3.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.centralWidget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.cardFrame_3 = QFrame(self.centralWidget_3)
        self.cardFrame_3.setObjectName(u"cardFrame_3")
        self.cardFrame_3.setMinimumSize(QSize(0, 0))
        self.cardFrame_3.setStyleSheet(u"")
        self.cardFrame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_4 = QGridLayout(self.cardFrame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_2 = QWidget(self.cardFrame_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit_2 = QTextEdit(self.widget_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"    padding: 18px;\n"
"    font-size: 15px;\n"
"    color: #E0E7FF;\n"
"    background: rgba(255,255,255,0.06);\n"
"    border-radius: 18px;\n"
"    border: 2px solid rgba(79,139,255,0.45);\n"
"}\n"
"\n"
"QTextEditt:hover {\n"
"    border: 2px solid #4F8BFF;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 2px solid #2563EB;\n"
"}")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setAcceptRichText(False)

        self.verticalLayout_6.addWidget(self.textEdit_2)

        self.searchGroupBox = QGroupBox(self.widget_2)
        self.searchGroupBox.setObjectName(u"searchGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.searchGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBoxVerticalLayout = QVBoxLayout()
        self.groupBoxVerticalLayout.setObjectName(u"groupBoxVerticalLayout")
        self.mutualHorizontalLayout = QWidget(self.searchGroupBox)
        self.mutualHorizontalLayout.setObjectName(u"mutualHorizontalLayout")
        self.horizontalLayout_11 = QHBoxLayout(self.mutualHorizontalLayout)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 10, 10, 10)
        self.mutualLabel = QLabel(self.mutualHorizontalLayout)
        self.mutualLabel.setObjectName(u"mutualLabel")

        self.horizontalLayout_11.addWidget(self.mutualLabel)

        self.lineEdit = QLineEdit(self.mutualHorizontalLayout)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        self.lineEdit.setFont(font1)

        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.mutualButton = QPushButton(self.mutualHorizontalLayout)
        self.mutualButton.setObjectName(u"mutualButton")

        self.horizontalLayout_11.addWidget(self.mutualButton)


        self.groupBoxVerticalLayout.addWidget(self.mutualHorizontalLayout)

        self.searchHorizontalLayout = QHBoxLayout()
        self.searchHorizontalLayout.setObjectName(u"searchHorizontalLayout")
        self.searchLabel = QLabel(self.searchGroupBox)
        self.searchLabel.setObjectName(u"searchLabel")

        self.searchHorizontalLayout.addWidget(self.searchLabel)

        self.searchModeCombo = QComboBox(self.searchGroupBox)
        self.searchModeCombo.addItem("")
        self.searchModeCombo.addItem("")
        self.searchModeCombo.setObjectName(u"searchModeCombo")
        self.searchModeCombo.setAcceptDrops(True)

        self.searchHorizontalLayout.addWidget(self.searchModeCombo)

        self.lineEdit_2 = QLineEdit(self.searchGroupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.searchHorizontalLayout.addWidget(self.lineEdit_2)

        self.searchButton = QPushButton(self.searchGroupBox)
        self.searchButton.setObjectName(u"searchButton")

        self.searchHorizontalLayout.addWidget(self.searchButton)


        self.groupBoxVerticalLayout.addLayout(self.searchHorizontalLayout)


        self.horizontalLayout_6.addLayout(self.groupBoxVerticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.searchGroupBox)


        self.gridLayout_4.addWidget(self.widget_2, 1, 1, 1, 1)

        self.widget = QWidget(self.cardFrame_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAcceptDrops(True)
        self.spinBox.setValue(1)

        self.gridLayout_6.addWidget(self.spinBox, 12, 0, 1, 1)

        self.Prettifying_2 = QPushButton(self.widget)
        self.Prettifying_2.setObjectName(u"Prettifying_2")
        self.Prettifying_2.setMinimumSize(QSize(204, 0))

        self.gridLayout_6.addWidget(self.Prettifying_2, 3, 0, 1, 1)

        self.sectionLabel1 = QLabel(self.widget)
        self.sectionLabel1.setObjectName(u"sectionLabel1")

        self.gridLayout_6.addWidget(self.sectionLabel1, 0, 0, 1, 1)

        self.Decompresssion_2 = QPushButton(self.widget)
        self.Decompresssion_2.setObjectName(u"Decompresssion_2")

        self.gridLayout_6.addWidget(self.Decompresssion_2, 5, 1, 1, 1)

        self.XMLconsistency_2 = QPushButton(self.widget)
        self.XMLconsistency_2.setObjectName(u"XMLconsistency_2")
        self.XMLconsistency_2.setMinimumSize(QSize(204, 0))

        self.gridLayout_6.addWidget(self.XMLconsistency_2, 1, 0, 1, 1)

        self.Minifying_2 = QPushButton(self.widget)
        self.Minifying_2.setObjectName(u"Minifying_2")

        self.gridLayout_6.addWidget(self.Minifying_2, 1, 1, 1, 1)

        self.mostActiveButton = QPushButton(self.widget)
        self.mostActiveButton.setObjectName(u"mostActiveButton")

        self.gridLayout_6.addWidget(self.mostActiveButton, 8, 0, 1, 1)

        self.mostInfluencerButton = QPushButton(self.widget)
        self.mostInfluencerButton.setObjectName(u"mostInfluencerButton")

        self.gridLayout_6.addWidget(self.mostInfluencerButton, 8, 1, 1, 1)

        self.graph_2 = QPushButton(self.widget)
        self.graph_2.setObjectName(u"graph_2")

        self.gridLayout_6.addWidget(self.graph_2, 14, 0, 1, 1)

        self.sectionLabel4 = QLabel(self.widget)
        self.sectionLabel4.setObjectName(u"sectionLabel4")

        self.gridLayout_6.addWidget(self.sectionLabel4, 13, 0, 1, 1)

        self.sectionLabel2 = QLabel(self.widget)
        self.sectionLabel2.setObjectName(u"sectionLabel2")

        self.gridLayout_6.addWidget(self.sectionLabel2, 7, 0, 1, 1)

        self.save_2 = QPushButton(self.widget)
        self.save_2.setObjectName(u"save_2")

        self.gridLayout_6.addWidget(self.save_2, 14, 1, 1, 1)

        self.XMLtoJSON_2 = QPushButton(self.widget)
        self.XMLtoJSON_2.setObjectName(u"XMLtoJSON_2")

        self.gridLayout_6.addWidget(self.XMLtoJSON_2, 3, 1, 1, 1)

        self.user1suggestButton = QPushButton(self.widget)
        self.user1suggestButton.setObjectName(u"user1suggestButton")

        self.gridLayout_6.addWidget(self.user1suggestButton, 12, 1, 1, 1)

        self.sectionLabel3 = QLabel(self.widget)
        self.sectionLabel3.setObjectName(u"sectionLabel3")

        self.gridLayout_6.addWidget(self.sectionLabel3, 11, 0, 1, 2)

        self.Compression_2 = QPushButton(self.widget)
        self.Compression_2.setObjectName(u"Compression_2")
        self.Compression_2.setMinimumSize(QSize(204, 0))

        self.gridLayout_6.addWidget(self.Compression_2, 5, 0, 1, 1)

        self.backButton = QPushButton(self.widget)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout_6.addWidget(self.backButton, 15, 0, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout_6)


        self.gridLayout_4.addWidget(self.widget, 1, 0, 1, 1)

        self.functionLabel = QLabel(self.cardFrame_3)
        self.functionLabel.setObjectName(u"functionLabel")

        self.gridLayout_4.addWidget(self.functionLabel, 0, 0, 1, 2)


        self.gridLayout_8.addWidget(self.cardFrame_3, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.centralWidget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget_2)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1274, 25))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Import your XML file", None))
        self.filePathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter file path...", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.xmlInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your XML content here...", None))
        self.subtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Upload an XML file from your computer or paste a URL", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Processing results will be displayed here\"", None))
        self.searchGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search and Mutuals", None))
        self.mutualLabel.setText(QCoreApplication.translate("MainWindow", u"Mutual Followers: ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter user IDs separated by commas for ex:  1, 2", None))
        self.mutualButton.setText(QCoreApplication.translate("MainWindow", u"Find Mutuals", None))
        self.searchLabel.setText(QCoreApplication.translate("MainWindow", u"Search: ", None))
        self.searchModeCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Topic", None))
        self.searchModeCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Word", None))

        self.searchModeCombo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text to search", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter user ID</p><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.spinBox.setSpecialValueText(QCoreApplication.translate("MainWindow", u"Enter ID", None))
        self.Prettifying_2.setText(QCoreApplication.translate("MainWindow", u"Prettify XML", None))
        self.sectionLabel1.setText(QCoreApplication.translate("MainWindow", u"Processing Functions", None))
        self.Decompresssion_2.setText(QCoreApplication.translate("MainWindow", u"Decompress", None))
        self.XMLconsistency_2.setText(QCoreApplication.translate("MainWindow", u"Validate XML", None))
        self.Minifying_2.setText(QCoreApplication.translate("MainWindow", u"Minify XML", None))
        self.mostActiveButton.setText(QCoreApplication.translate("MainWindow", u"Most Active User ", None))
        self.mostInfluencerButton.setText(QCoreApplication.translate("MainWindow", u"Most Influencer User", None))
        self.graph_2.setText(QCoreApplication.translate("MainWindow", u"graph", None))
        self.sectionLabel4.setText(QCoreApplication.translate("MainWindow", u"Action Panel", None))
        self.sectionLabel2.setText(QCoreApplication.translate("MainWindow", u"Network Analysis", None))
        self.save_2.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.XMLtoJSON_2.setText(QCoreApplication.translate("MainWindow", u"XMLtoJSON", None))
        self.user1suggestButton.setText(QCoreApplication.translate("MainWindow", u"Suggest Users ", None))
        self.sectionLabel3.setText(QCoreApplication.translate("MainWindow", u"Suggest Users for a specific User using his ID", None))
        self.Compression_2.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Go back to Import", None))
        self.functionLabel.setText(QCoreApplication.translate("MainWindow", u"XML Parsing Functions", None))
    # retranslateUi

