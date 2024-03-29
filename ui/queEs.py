# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/queEs.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QueEs(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1112, 541)
        Form.setMinimumSize(QtCore.QSize(541, 0))
        Form.setMaximumSize(QtCore.QSize(1112, 541))
        Form.setBaseSize(QtCore.QSize(1112, 541))
        Form.setStyleSheet("background-color: rgb(197, 220, 255);")
        self.btnRegresar = QtWidgets.QPushButton(Form)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(216, 216, 216);\n"
"border-radius:10px;")
        self.btnRegresar.setObjectName("btnRegresar")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(140, 10, 871, 521))
        self.textBrowser.setStyleSheet("border: none;")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnRegresar.setText(_translate("Form", "Regresar"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">El algoritmo RSA</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\',\'system-ui\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Helvetica Neue\',\'Fira Sans\',\'Ubuntu\',\'Oxygen\',\'Oxygen Sans\',\'Cantarell\',\'Droid Sans\',\'Apple Color Emoji\',\'Segoe UI Emoji\',\'Segoe UI Emoji\',\'Segoe UI Symbol\',\'Lucida Grande\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:11pt; color:rgba(0,0,0,0.894118);\">El algoritmo RSA es un algoritmo de cifrado asimétrico, y los pasos para aplicarlo son:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system\',\'system-ui\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Helvetica Neue\',\'Fira Sans\',\'Ubuntu\',\'Oxygen\',\'Oxygen Sans\',\'Cantarell\',\'Droid Sans\',\'Apple Color Emoji\',\'Segoe UI Emoji\',\'Segoe UI Emoji\',\'Segoe UI Symbol\',\'Lucida Grande\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:11pt; color:rgba(0,0,0,0.894118);\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.    Se escogen número primos muy grandes p y q distintos; actualmente se recomienda que sean de 1024 bits (equivalen a aproximadamente a 310 dígitos decimales); estos números deben ser secretos. Cada usuario debe elegir estos números.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.    Cada usuario calcula el grupo de cifra o el módulo n = p * q (n será de 2048 bits, aproximadamente 620 dígitos decimales)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.    Cada usuario calcula la función o indicador de Euler: ɸ(n)= (p-1)*(q-1)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4.    Cada usuario elige su llave pública e; en la práctica, actualmente se elige el número 65.537 (número primo de 17 bits) como llave pública, conocido como el número 4 de Fermat. La llave pública e debe ser primo relativo con ɸ(n) para que exista el inverso. Dado que el grupo de cifra es de aproximadamente 620 dígitos, el inverso de e es un número muy grande, lo que dificulta el ataque por fuerza bruta para encontrar este inverso.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5.    Cada usuario calcula la llave privada d, usando el algoritmo extendido de Euclides: d=inv(e, ɸ(n)). Debe cumplirse que d*e mod ɸ(n)=1. Como sabemos esta llave debe mantenerse en secreto.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">6.    Cada usuario publica la llave publica e y n, es decir llave pública (n,e).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Sobre el simulador:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Se ha propuesto un simulador para poder evidenciar el funcionamiento del algoritmo RSA, con una aceptación de números primos de 3 dígitos.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Por el tamaño de procesamiento de cómputo no se recomienda utilizar números grandes para la simulación.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Usted cuenta con botonoes que le puede na ayudar a generar números primos de 5 cifras a más, y también un generador del exponente &quot;</span><span style=\" font-size:10pt; font-weight:600;\">e&quot;</span><span style=\" font-size:10pt;\"> que te ayudará a hallar un número que cumpla con las condiciones del algoritmo.</span></p></body></html>"))
